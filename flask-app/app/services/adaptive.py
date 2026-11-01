"""سرویس و موتور تمرین تطبیقی ۵ دقیقه‌ای CS50x Anzali (Adaptive Engine).

پیاده‌سازی کامل مدل ردیابی دانش بیزی (BKT)، فاصله‌گذاری جعبه‌های لایتنر (Leitner)،
تشخیص و جبران بدفهمی‌ها (Misconceptions & Follow-ups)، و توزیع استاندارد نشست:
  - ۶۰٪ مفاهیم ضعیف (P(L) < threshold)
  - ۲۵٪ مفاهیم نیازمند مرور (سررسید Leitner)
  - ۱۵٪ مفاهیم جدید و تازه (Fresh / Unseen)
  - ۸ تا ۱۰ پرسش در ۳۰۰ ثانیه
"""
from __future__ import annotations

import copy
import hashlib
import json
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from app import db
from app.content import kb_repo
from app.models import AdaptiveState, StudentMistake, User
from app.services import streak as streak_service
from app.services import xp as xp_service

TEHRAN_TZ = timezone(timedelta(hours=3, minutes=30))

DEFAULT_CONFIG: dict[str, Any] = {
    "version": "1.0.0",
    "bkt": {
        "prior": 0.10,      # P(L0)
        "learn": 0.15,      # P(T)
        "guess": 0.25,      # P(G)
        "slip": 0.10,       # P(S)
        "threshold": 0.85,  # آستانه تسلط مفهوم
    },
    "leitner": {
        "intervals": [1, 2, 4, 7, 14],  # فاصله‌های مرور جعبه‌های ۱ تا ۵ بر حسب روز
    },
    "session": {
        "target_questions": 8,
        "max_questions": 10,
        "time_limit_sec": 300,
        "weak_ratio": 0.60,
        "review_ratio": 0.25,
        "fresh_ratio": 0.15,
        "max_misconception_followups": 2,
    },
    "xp": {
        "per_answer_xp": 0,
        "concept_mastered_xp": 3,
        "week_mastered_xp": 15,
    },
}


def get_tehran_date_str() -> str:
    """تاریخ جاری به وقت تهران به فرمت YYYY-MM-DD."""
    return datetime.now(TEHRAN_TZ).strftime("%Y-%m-%d")


def load_adaptive_config() -> dict[str, Any]:
    """بارگذاری تنظیمات موتور تطبیقی از پایگاه دانش یا استفاده از پیش‌فرض‌ها."""
    kb_root = kb_repo.kb_root()
    cfg_path = kb_root / "anzali-fa" / "adaptive" / "config.json"
    if not cfg_path.is_file():
        # بررسی مسیرهای احتمالی دیگر در ساختار بسته
        cfg_path = kb_root / "adaptive" / "config.json"
    if cfg_path.is_file():
        try:
            with open(cfg_path, encoding="utf-8") as f:
                data = json.load(f)
                res = copy.deepcopy(DEFAULT_CONFIG)
                res.update(data)
                return res
        except Exception:
            pass
    return copy.deepcopy(DEFAULT_CONFIG)


class AdaptiveEngine:
    """موتور مرجع تطبیقی (سازگار ۱۰۰٪ با reference_engine)."""

    def __init__(self, config: dict[str, Any] | None = None) -> None:
        self.config = config or load_adaptive_config()
        self.bkt_cfg = self.config.get("bkt", DEFAULT_CONFIG["bkt"])
        self.leitner_cfg = self.config.get("leitner", DEFAULT_CONFIG["leitner"])
        self.session_cfg = self.config.get("session", DEFAULT_CONFIG["session"])
        self.xp_cfg = self.config.get("xp", DEFAULT_CONFIG["xp"])

    def new_state(self) -> dict[str, Any]:
        """ایجاد وضعیت تازه برای دانش‌آموز جدید."""
        return {
            "version": "1.0.0",
            "cold_start": True,
            "concepts": {},      # concept_id -> {"p_l": float, "box": int, "next_review": str, "attempts": int}
            "sessions": [],
            "current_session": None,
        }

    def update_bkt(self, p_l: float, is_correct: bool, params: dict[str, float] | None = None) -> float:
        """به‌روزرسانی BKT: احتمال شرطی پسین و انتقال یادگیری."""
        p_cfg = params or self.bkt_cfg
        p_g = float(p_cfg.get("guess", 0.25))
        p_s = float(p_cfg.get("slip", 0.10))
        p_t = float(p_cfg.get("learn", 0.15))

        p_l = max(0.0001, min(0.9999, float(p_l)))

        if is_correct:
            p_obs = (p_l * (1.0 - p_s)) / (p_l * (1.0 - p_s) + (1.0 - p_l) * p_g)
        else:
            p_obs = (p_l * p_s) / (p_l * p_s + (1.0 - p_l) * (1.0 - p_g))

        new_p_l = p_obs + (1.0 - p_obs) * p_t
        return round(max(0.0, min(1.0, new_p_l)), 4)

    def update_leitner(self, current_box: int, is_correct: bool, today_str: str) -> tuple[int, str]:
        """محاسبه شماره جعبه جدید و تاریخ سررسید بعدی مرور بر اساس لایتنر."""
        intervals = self.leitner_cfg.get("intervals", [1, 2, 4, 7, 14])
        try:
            today_dt = datetime.strptime(today_str, "%Y-%m-%d")
        except Exception:
            today_dt = datetime.now(TEHRAN_TZ)

        if is_correct:
            new_box = min(current_box + 1, len(intervals))
        else:
            new_box = 1

        delta_days = intervals[new_box - 1]
        next_dt = today_dt + timedelta(days=delta_days)
        return new_box, next_dt.strftime("%Y-%m-%d")

    def build_session(
        self,
        state: dict[str, Any],
        bank: list[dict[str, Any]],
        today_str: str | None = None,
        seed: int | None = None,
    ) -> dict[str, Any]:
        """طراحی یک نشست ۵ دقیقه‌ای استاندارد شامل ۸ تا ۱۰ پرسش متعادل."""
        if seed is not None:
            rng = random.Random(seed)
        else:
            rng = random.Random()

        today = today_str or get_tehran_date_str()
        target_count = int(self.session_cfg.get("target_questions", 8))
        threshold = float(self.bkt_cfg.get("threshold", 0.85))

        # دسته‌بندی مفاهیم دانش‌آموز
        concepts_state = state.setdefault("concepts", {})

        # مپ سوالات به مفاهیم
        all_concepts_in_bank = set()
        item_concept_map: dict[str, list[str]] = {}
        for item in bank:
            c_ids = item.get("concept_ids") or []
            if not c_ids and item.get("lesson_id"):
                c_ids = [item["lesson_id"]]
            item_concept_map[item["id"]] = c_ids
            for cid in c_ids:
                all_concepts_in_bank.add(cid)

        weak_concepts = []
        review_concepts = []
        mastered_concepts = []
        unseen_concepts = []

        for cid in sorted(all_concepts_in_bank):
            if cid not in concepts_state:
                unseen_concepts.append(cid)
            else:
                c_data = concepts_state[cid]
                p_l = c_data.get("p_l", self.bkt_cfg.get("prior", 0.10))
                next_rev = c_data.get("next_review", today)
                if p_l < threshold:
                    weak_concepts.append(cid)
                elif next_rev <= today:
                    review_concepts.append(cid)
                else:
                    mastered_concepts.append(cid)

        # محاسبه سهمیه‌ها: ۶۰٪ ضعیف، ۲۵٪ مرور، ۱۵٪ تازه
        weak_quota = max(1, int(round(target_count * self.session_cfg.get("weak_ratio", 0.60))))
        review_quota = max(1, int(round(target_count * self.session_cfg.get("review_ratio", 0.25))))
        fresh_quota = max(1, target_count - weak_quota - review_quota)

        selected_items: list[dict[str, Any]] = []
        selected_ids: set[str] = set()

        def _pick_for_concepts(c_list: list[str], max_needed: int) -> list[dict[str, Any]]:
            picked = []
            shuffled_c = list(c_list)
            rng.shuffle(shuffled_c)
            for c in shuffled_c:
                if len(picked) >= max_needed:
                    break
                matching = [
                    it for it in bank
                    if it["id"] not in selected_ids
                    and c in item_concept_map.get(it["id"], [])
                ]
                if matching:
                    choice = rng.choice(matching)
                    picked.append(choice)
                    selected_ids.add(choice["id"])
            return picked

        # انتخاب به تفکیک سهمیه‌ها
        selected_items.extend(_pick_for_concepts(weak_concepts, weak_quota))
        selected_items.extend(_pick_for_concepts(review_concepts, review_quota))
        selected_items.extend(_pick_for_concepts(unseen_concepts, fresh_quota))

        # در صورت باقی‌ماندن ظرفیت، از کل بانک سوال تکمیل می‌شود
        remaining_needed = target_count - len(selected_items)
        if remaining_needed > 0:
            pool = [it for it in bank if it["id"] not in selected_ids]
            rng.shuffle(pool)
            for it in pool[:remaining_needed]:
                selected_items.append(it)
                selected_ids.add(it["id"])

        # اگر بانک کم باشد، سوالات باقیمانده بازگردانده می‌شوند
        rng.shuffle(selected_items)

        session_id = f"sess_{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}_{rng.randint(1000, 9999)}"
        plan_summary = {
            "weak_count": min(len(weak_concepts), weak_quota),
            "review_count": min(len(review_concepts), review_quota),
            "fresh_count": min(len(unseen_concepts), fresh_quota),
            "total": len(selected_items),
        }

        session_obj = {
            "session_id": session_id,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "today_tehran": today,
            "target_count": len(selected_items),
            "item_ids": [it["id"] for it in selected_items],
            "plan": plan_summary,
            "answers": {},
            "misconception_followups_used": 0,
            "completed": False,
        }

        state["current_session"] = session_obj
        return session_obj

    def record_answer(
        self,
        state: dict[str, Any],
        session_id: str,
        question_id: str,
        answer_value: Any,
        bank: list[dict[str, Any]],
        today_str: str | None = None,
    ) -> dict[str, Any]:
        """ثبت پاسخ یک پرسش در نشست تطبیقی جاری و به‌روزرسانی وضعیت دانش‌آموز."""
        today = today_str or get_tehran_date_str()
        current_sess = state.get("current_session")
        if not current_sess or current_sess.get("session_id") != session_id:
            return {"success": False, "error": "نشست تطبیقی معتبر یا فعال نیست."}

        # یافتن سوال در بانک
        target = next((it for it in bank if it.get("id") == question_id), None)
        if not target:
            return {"success": False, "error": f"پرسش {question_id} در بانک سوالات یافت نشد."}

        # بررسی درستی پاسخ
        clean_ans = str(answer_value or "").replace("\r\n", "\n").replace("\r", "\n").strip()
        q_type = target.get("type", "mcq")
        ans_obj = target.get("answer") or {}

        is_correct = False
        selected_option = None
        if q_type == "mcq":
            correct_ids = [str(x).strip().lower() for x in ans_obj.get("correct_option_ids", [])]
            is_correct = clean_ans.lower() in correct_ids
            for opt in target.get("options", []):
                if str(opt.get("id")).lower() == clean_ans.lower():
                    selected_option = opt
                    break
        elif q_type == "true_false":
            val = bool(ans_obj.get("value"))
            user_val = clean_ans.lower() in ("true", "1", "درست")
            is_correct = (user_val == val)
        elif q_type in ("predict_output", "fill_blank", "fill_blank_code", "short_answer"):
            accept_list = ans_obj.get("accept", [])
            if isinstance(accept_list, str):
                accept_list = [accept_list]
            normalized = [str(x).strip().lower() for x in accept_list]
            if ans_obj.get("value") is not None:
                normalized.append(str(ans_obj.get("value")).strip().lower())
            is_correct = clean_ans.lower() in normalized
        elif q_type in ("parsons", "ordering"):
            expected_order = ans_obj.get("order") or ans_obj.get("correct_order", [])
            user_order = []
            if isinstance(answer_value, list):
                user_order = [str(x).strip() for x in answer_value]
            elif isinstance(answer_value, str) and answer_value.startswith("["):
                try:
                    user_order = [str(x).strip() for x in json.loads(answer_value)]
                except Exception:
                    user_order = [x.strip() for x in answer_value.strip("[]").split(",") if x.strip()]
            else:
                user_order = [clean_ans]
            is_correct = ([str(x).strip() for x in expected_order] == user_order)

        # استخراج بازخورد و توضیح
        feedback_text = ""
        if selected_option:
            feedback_text = selected_option.get("feedback_fa", "")
        else:
            q_fb = target.get("feedback") or {}
            if is_correct:
                feedback_text = q_fb.get("correct_fa") or target.get("feedback_fa", "")
            else:
                feedback_text = q_fb.get("incorrect_fa") or target.get("feedback_fa", "")

        explanation_text = target.get("explanation_fa", "")

        # بررسی بدفهمی (Misconception)
        misconception_name = None
        remediation_text = None
        anchor_link = None
        follow_up_item_id = None

        if not is_correct and selected_option and selected_option.get("misconception"):
            misconception_name = selected_option.get("misconception")
            remediation_text = selected_option.get("remediation_fa") or target.get("remediation_fa")
            anchor_link = selected_option.get("anchor") or target.get("anchor")

            # ایجاد سوال پیگیری (حداکثر ۲ سوال پیگیری در هر نشست)
            used_fu = current_sess.get("misconception_followups_used", 0)
            max_fu = int(self.session_cfg.get("max_misconception_followups", 2))
            if used_fu < max_fu:
                # جستجو برای سوال مرتبط با همین بدفهمی یا مفهوم
                c_ids = target.get("concept_ids") or []
                c_tag = c_ids[0] if c_ids else None
                candidates = [
                    it for it in bank
                    if it["id"] != question_id
                    and it["id"] not in current_sess.get("item_ids", [])
                    and (c_tag in (it.get("concept_ids") or []))
                ]
                if candidates:
                    fu_item = candidates[0]
                    follow_up_item_id = fu_item["id"]
                    current_sess["item_ids"].append(follow_up_item_id)
                    current_sess["misconception_followups_used"] = used_fu + 1

        # به‌روزرسانی BKT و Leitner برای تک‌تک مفاهیم سوال
        concept_ids = target.get("concept_ids") or []
        if not concept_ids and target.get("lesson_id"):
            concept_ids = [target["lesson_id"]]

        concepts_state = state.setdefault("concepts", {})
        mastery_threshold = float(self.bkt_cfg.get("threshold", 0.85))
        just_mastered_concepts: list[str] = []

        for cid in concept_ids:
            c_entry = concepts_state.setdefault(
                cid,
                {
                    "p_l": float(self.bkt_cfg.get("prior", 0.10)),
                    "box": 1,
                    "next_review": today,
                    "attempts": 0,
                    "correct": 0,
                },
            )
            old_p_l = c_entry["p_l"]
            new_p_l = self.update_bkt(old_p_l, is_correct)
            new_box, next_rev = self.update_leitner(c_entry.get("box", 1), is_correct, today)

            c_entry["p_l"] = new_p_l
            c_entry["box"] = new_box
            c_entry["next_review"] = next_rev
            c_entry["attempts"] = c_entry.get("attempts", 0) + 1
            if is_correct:
                c_entry["correct"] = c_entry.get("correct", 0) + 1

            if old_p_l < mastery_threshold and new_p_l >= mastery_threshold:
                just_mastered_concepts.append(cid)

        # ثبت پاسخ در نشست
        current_sess.setdefault("answers", {})[question_id] = {
            "answer": clean_ans,
            "is_correct": is_correct,
            "submitted_at": datetime.now(timezone.utc).isoformat(),
        }

        state["cold_start"] = False

        return {
            "success": True,
            "question_id": question_id,
            "is_correct": is_correct,
            "feedback_fa": feedback_text,
            "explanation_fa": explanation_text,
            "misconception": misconception_name,
            "remediation_fa": remediation_text,
            "anchor": anchor_link,
            "follow_up_item_id": follow_up_item_id,
            "just_mastered_concepts": just_mastered_concepts,
            "session_progress": {
                "answered": len(current_sess["answers"]),
                "total": len(current_sess["item_ids"]),
            },
        }

    def finish_session(self, state: dict[str, Any], session_id: str) -> dict[str, Any]:
        """پایان نشست تطبیقی، محاسبه آمار و بررسی واجد شرایط بودن استریک."""
        current_sess = state.get("current_session")
        if not current_sess or current_sess.get("session_id") != session_id:
            return {"success": False, "error": "نشست جاری معتبر نیست."}

        answers = current_sess.get("answers", {})
        total_answered = len(answers)
        correct_count = sum(1 for a in answers.values() if a.get("is_correct"))

        current_sess["completed"] = True
        current_sess["completed_at"] = datetime.now(timezone.utc).isoformat()
        current_sess["final_score"] = correct_count
        current_sess["total_answered"] = total_answered

        # آرشیو نشست در تاریخچه
        state.setdefault("sessions", []).append(copy.deepcopy(current_sess))
        state["current_session"] = None

        qualifies_for_streak = total_answered >= 8
        return {
            "success": True,
            "session_id": session_id,
            "total_answered": total_answered,
            "correct_count": correct_count,
            "accuracy": round(correct_count / total_answered, 2) if total_answered > 0 else 0.0,
            "qualifies_for_streak": qualifies_for_streak,
            "today_tehran": current_sess.get("today_tehran", get_tehran_date_str()),
        }


# ──────────────────────────────────────────────────────────────────────────────
# توابع لایه پایگاه‌داده و سرویس وب (Database & Flask Service Layer)
# ──────────────────────────────────────────────────────────────────────────────

def get_or_create_adaptive_state(user_id: int) -> dict[str, Any]:
    """واکشی وضعیت تطبیقی کاربر از جدول adaptive_states."""
    row = AdaptiveState.query.filter_by(user_id=user_id).first()
    engine = AdaptiveEngine()
    if not row or not row.state_json:
        init_state = engine.new_state()
        if not row:
            row = AdaptiveState(user_id=user_id, state_json=init_state)
            db.session.add(row)
            db.session.commit()
        return init_state
    return dict(row.state_json)


def save_adaptive_state(user_id: int, state: dict[str, Any]) -> None:
    """ذخیره وضعیت تطبیقی کاربر در دیتابیس."""
    row = AdaptiveState.query.filter_by(user_id=user_id).first()
    if not row:
        row = AdaptiveState(user_id=user_id, state_json=state)
        db.session.add(row)
    else:
        row.state_json = state
        row.updated_at = datetime.utcnow()
    db.session.commit()


def load_question_bank_for_practice() -> list[dict[str, Any]]:
    """گردآوری بانک جامع سوالات مفهومی دوره CS50x جهت تمرین تطبیقی."""
    bank = []
    seen_ids = set()

    # پیمایش تمام هفته‌های موجود در پایگاه دانش
    kb_root = kb_repo.kb_root()
    weeks_dir = kb_root / "anzali-fa" / "weeks"
    if not weeks_dir.is_dir():
        weeks_dir = kb_root / "weeks"

    if weeks_dir.is_dir():
        for w_folder in sorted(weeks_dir.iterdir()):
            if not w_folder.is_dir():
                continue
            qz_path = w_folder / "quizzes.json"
            if qz_path.is_file():
                try:
                    with open(qz_path, encoding="utf-8") as f:
                        data = json.load(f)
                    for item in data.get("items", []):
                        iid = item.get("id")
                        if iid and iid not in seen_ids:
                            bank.append(item)
                            seen_ids.add(iid)
                except Exception:
                    pass

    return bank


def start_user_practice_session(user_id: int, seed: int | None = None) -> dict[str, Any]:
    """شروع یا ادامه یک نشست تمرین تطبیقی ۵ دقیقه‌ای برای دانش‌آموز."""
    state = get_or_create_adaptive_state(user_id)
    engine = AdaptiveEngine()

    # اگر نشست باز قبلی وجود دارد و تکمیل نشده، همان ادامه می‌یابد
    current = state.get("current_session")
    if current and not current.get("completed"):
        # بررسی زمان سپری شده (اگر بیش از ۱ ساعت گذشته، نشست جدید ساخته شود)
        created_at_str = current.get("created_at")
        try:
            c_dt = datetime.fromisoformat(created_at_str)
            if datetime.now(timezone.utc) - c_dt < timedelta(hours=1):
                return current
        except Exception:
            pass

    bank = load_question_bank_for_practice()
    sess = engine.build_session(state, bank, today_str=get_tehran_date_str(), seed=seed)
    save_adaptive_state(user_id, state)
    return sess


def submit_user_practice_answer(
    user_id: int, session_id: str, question_id: str, answer_value: Any
) -> dict[str, Any]:
    """ثبت پاسخ در نشست تطبیقی، اعمال BKT، و اعطای XP در صورت تسلط بر مفهوم."""
    state = get_or_create_adaptive_state(user_id)
    engine = AdaptiveEngine()
    bank = load_question_bank_for_practice()

    res = engine.record_answer(state, session_id, question_id, answer_value, bank)
    if not res.get("success"):
        return res

    # بررسی تسلط مفهوم جدید و اعطای ۳ XP
    just_mastered = res.get("just_mastered_concepts", [])
    total_xp_awarded = 0
    for cid in just_mastered:
        reason = f"kb:adaptive:concept:{cid}:mastered"
        if xp_service.award(user_id, 3, reason):
            total_xp_awarded += 3

    res["xp_awarded"] = total_xp_awarded
    save_adaptive_state(user_id, state)

    # ثبت در پایگاه اشتباهات (StudentMistake) در صورت نادرست بودن
    if not res.get("is_correct"):
        target = next((it for it in bank if it.get("id") == question_id), {})
        c_ids = target.get("concept_ids") or []
        tag = c_ids[0] if c_ids else "adaptive_practice"
        mistake = StudentMistake.query.filter_by(user_id=user_id, item_id=question_id).first()
        if not mistake:
            mistake = StudentMistake(
                user_id=user_id,
                week=target.get("week", 0),
                source="adaptive",
                item_id=question_id,
                item_title=target.get("prompt_fa", f"پرسش تطبیقی {question_id}"),
                concept_tag=tag,
                user_answer=str(answer_value),
                expected_answer=str(target.get("answer")),
                explanation=res.get("explanation_fa"),
                error_count=1,
                is_resolved=False,
            )
            db.session.add(mistake)
        else:
            mistake.error_count += 1
            mistake.is_resolved = False
        db.session.commit()

    return res


def complete_user_practice_session(user_id: int, session_id: str) -> dict[str, Any]:
    """نهایی‌سازی نشست تمرین، ثبت استریک در صورت ۸ پاسخ و ذخیره تاریخچه."""
    state = get_or_create_adaptive_state(user_id)
    engine = AdaptiveEngine()

    res = engine.finish_session(state, session_id)
    if not res.get("success"):
        return res

    save_adaptive_state(user_id, state)

    # ثبت استریک در صورتی که دست‌کم ۸ سوال پاسخ داده شده باشد
    streak_updated = False
    if res.get("qualifies_for_streak"):
        streak_reason = f"adaptive:session:{res.get('today_tehran')}"
        # ثبت فعالیت روزانه در لاگ و به‌روزرسانی استریک
        xp_service.award(user_id, 0, streak_reason)
        streak_service.update_streak(user_id)
        streak_updated = True

    res["streak_updated"] = streak_updated
    return res
