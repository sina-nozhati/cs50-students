"""Standalone Reference Engine for CS50x Anzali Adaptive Practice v1.0.0.

Pure Python implementation of Bayesian Knowledge Tracing (BKT),
Leitner box scheduling, and 5-minute practice session composition.
"""
from __future__ import annotations

import copy
import json
import random
from datetime import datetime, timedelta, timezone
from typing import Any

TEHRAN_TZ = timezone(timedelta(hours=3, minutes=30))

DEFAULT_CONFIG: dict[str, Any] = {
    "version": "1.0.0",
    "bkt": {
        "prior": 0.10,
        "learn": 0.15,
        "guess": 0.25,
        "slip": 0.10,
        "threshold": 0.85,
    },
    "leitner": {
        "intervals": [1, 2, 4, 7, 14],
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


class ReferenceEngine:
    """Pure standalone reference implementation of the Adaptive Engine."""

    def __init__(self, config: dict[str, Any] | None = None) -> None:
        self.config = config or copy.deepcopy(DEFAULT_CONFIG)
        self.bkt_cfg = self.config.get("bkt", DEFAULT_CONFIG["bkt"])
        self.leitner_cfg = self.config.get("leitner", DEFAULT_CONFIG["leitner"])
        self.session_cfg = self.config.get("session", DEFAULT_CONFIG["session"])
        self.xp_cfg = self.config.get("xp", DEFAULT_CONFIG["xp"])

    def new_state(self) -> dict[str, Any]:
        return {
            "version": "1.0.0",
            "cold_start": True,
            "concepts": {},
            "sessions": [],
            "current_session": None,
        }

    def update_bkt(self, p_l: float, is_correct: bool, params: dict[str, float] | None = None) -> float:
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
        if seed is not None:
            rng = random.Random(seed)
        else:
            rng = random.Random()

        today = today_str or datetime.now(TEHRAN_TZ).strftime("%Y-%m-%d")
        target_count = int(self.session_cfg.get("target_questions", 8))
        threshold = float(self.bkt_cfg.get("threshold", 0.85))

        concepts_state = state.setdefault("concepts", {})

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

        selected_items.extend(_pick_for_concepts(weak_concepts, weak_quota))
        selected_items.extend(_pick_for_concepts(review_concepts, review_quota))
        selected_items.extend(_pick_for_concepts(unseen_concepts, fresh_quota))

        remaining_needed = target_count - len(selected_items)
        if remaining_needed > 0:
            pool = [it for it in bank if it["id"] not in selected_ids]
            rng.shuffle(pool)
            for it in pool[:remaining_needed]:
                selected_items.append(it)
                selected_ids.add(it["id"])

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
