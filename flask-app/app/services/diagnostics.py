"""سرویس عیب‌یابی و شناسنامه تشخیصی یادگیری دانش‌آموز (Diagnostic & Knowledge Tracing Engine).

این سرویس وظیفه ثبت خطاها (Mistake Vault)، دسته‌بندی موضوعی بر اساس تگ‌های مفاهیم،
تشخیص نقاط ضعف بحرانی (Weak Spots)، محاسبه نرخ رفع اشتباهات و ارائه آمار کلاسی به منتورها را بر عهده دارد.
"""
from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from sqlalchemy import func, case

from app import db
from app.models import User, StudentMistake, LearningEvent


def _stringify_value(val: Any) -> str:
    """تبدیل مقادیر مختلف به رشته خوانا برای ذخیره در دیتابیس."""
    if val is None:
        return ""
    if isinstance(val, (list, tuple)):
        return ", ".join(str(x) for x in val)
    if isinstance(val, dict):
        return json.dumps(val, ensure_ascii=False)
    return str(val).strip()


def record_mistake(
    user_id: int,
    week: int,
    source: str,
    item_id: str,
    item_title: str | None,
    concept_tag: str,
    user_answer: Any,
    expected_answer: Any,
    explanation: str | None = None,
) -> StudentMistake:
    """ثبت یا به‌روزرسانی خطای دانش‌آموز در جعبه اشتباهات (Mistake Vault)."""
    clean_user = _stringify_value(user_answer)
    clean_exp = _stringify_value(expected_answer)
    clean_title = (item_title or item_id)[:200]
    clean_tag = (concept_tag or "مفاهیم پایه")[:100]

    mistake = StudentMistake.query.filter_by(user_id=user_id, item_id=item_id).first()
    now = datetime.utcnow()

    if mistake:
        mistake.error_count = (mistake.error_count or 1) + 1
        mistake.user_answer = clean_user
        mistake.expected_answer = clean_exp
        mistake.is_resolved = False
        mistake.resolved_at = None
        mistake.created_at = now
        if explanation:
            mistake.explanation = explanation
        if item_title:
            mistake.item_title = clean_title
        if concept_tag:
            mistake.concept_tag = clean_tag
    else:
        mistake = StudentMistake(
            user_id=user_id,
            week=week,
            source=source,
            item_id=item_id,
            item_title=clean_title,
            concept_tag=clean_tag,
            user_answer=clean_user,
            expected_answer=clean_exp,
            explanation=explanation,
            error_count=1,
            is_resolved=False,
            created_at=now,
        )
        db.session.add(mistake)

    db.session.commit()
    return mistake


def resolve_mistake(user_id: int, item_id: str) -> bool:
    """علامت‌گذاری یک خطا به عنوان حل‌شده پس از پاسخ صحیح بعدی دانش‌آموز."""
    mistake = StudentMistake.query.filter_by(
        user_id=user_id, item_id=item_id, is_resolved=False
    ).first()
    if mistake:
        mistake.is_resolved = True
        mistake.resolved_at = datetime.utcnow()
        db.session.commit()
        return True
    return False


def get_student_diagnostic_profile(user_id: int) -> dict[str, Any]:
    """تهیه پروفایل جامع تشخیصی، نقاط ضعف و جعبه اشتباهات یک دانش‌آموز."""
    all_mistakes = (
        StudentMistake.query.filter_by(user_id=user_id)
        .order_by(StudentMistake.created_at.desc())
        .all()
    )

    total_mistakes = len(all_mistakes)
    unresolved = [m for m in all_mistakes if not m.is_resolved]
    resolved = [m for m in all_mistakes if m.is_resolved]

    resolution_rate = (
        round((len(resolved) / total_mistakes) * 100, 1) if total_mistakes > 0 else 100.0
    )

    # تحلیل مفهومی و خوشه‌بندی نقاط ضعف بر اساس تگ‌ها
    concepts_map: dict[str, dict[str, Any]] = {}
    for m in all_mistakes:
        tag = m.concept_tag or "عمومی"
        if tag not in concepts_map:
            concepts_map[tag] = {
                "tag": tag,
                "unresolved_count": 0,
                "resolved_count": 0,
                "total_mistakes": 0,
                "error_count_sum": 0,
                "weeks": set(),
            }
        item = concepts_map[tag]
        item["total_mistakes"] += 1
        item["error_count_sum"] += (m.error_count or 1)
        item["weeks"].add(m.week)
        if m.is_resolved:
            item["resolved_count"] += 1
        else:
            item["unresolved_count"] += 1

    concepts_list = []
    for tag, data in concepts_map.items():
        unres = data["unresolved_count"]
        err_sum = data["error_count_sum"]
        if unres >= 2 or err_sum >= 3:
            severity = "critical"
            severity_label = "نقطه ضعف بحرانی"
            severity_badge = "bg-red-100 text-red-800 border-red-200"
        elif unres == 1:
            severity = "warning"
            severity_label = "نیازمند تمرین و تثبیت"
            severity_badge = "bg-amber-100 text-amber-800 border-amber-200"
        else:
            severity = "mastered"
            severity_label = "تثبیت‌شده و رفع‌شده"
            severity_badge = "bg-green-100 text-green-800 border-green-200"

        concepts_list.append({
            "tag": tag,
            "unresolved_count": unres,
            "resolved_count": data["resolved_count"],
            "total_mistakes": data["total_mistakes"],
            "error_count_sum": err_sum,
            "weeks": sorted(list(data["weeks"])),
            "severity": severity,
            "severity_label": severity_label,
            "severity_badge": severity_badge,
        })

    # مرتب‌سازی: بحرانی‌ها بالاتر
    severity_order = {"critical": 0, "warning": 1, "mastered": 2}
    concepts_list.sort(key=lambda x: (severity_order.get(x["severity"], 3), -x["error_count_sum"]))

    # جعبه اشتباهات فعال
    mistake_vault = []
    for m in unresolved:
        practice_url = (
            f"/kb/week/{m.week}/practice" if m.source == "practice" else f"/kb/week/{m.week}"
        )
        mistake_vault.append({
            "id": m.id,
            "item_id": m.item_id,
            "week": m.week,
            "source": m.source,
            "title": m.item_title or m.item_id,
            "concept_tag": m.concept_tag,
            "user_answer": m.user_answer,
            "expected_answer": m.expected_answer,
            "explanation": m.explanation,
            "error_count": m.error_count,
            "created_at": m.created_at,
            "practice_url": practice_url,
        })

    # موارد اخیراً حل‌شده
    resolved_vault = []
    for m in resolved[:5]:
        resolved_vault.append({
            "id": m.id,
            "item_id": m.item_id,
            "week": m.week,
            "title": m.item_title or m.item_id,
            "concept_tag": m.concept_tag,
            "error_count": m.error_count,
            "resolved_at": m.resolved_at,
        })

    # تولید توصیه‌های هوشمند شخصی‌سازی‌شده
    recommendations = []
    critical_tags = [c["tag"] for c in concepts_list if c["severity"] == "critical"]
    warning_tags = [c["tag"] for c in concepts_list if c["severity"] == "warning"]

    for tag in critical_tags + warning_tags:
        lower_tag = tag.lower()
        if "loop" in lower_tag or "حلقه" in lower_tag:
            recommendations.append("مرور ساختار حلقه‌ها: به شرط پایان و گام افزایش شمارنده (i++) و تفاوت for با do-while بیشتر توجه کنید.")
        elif "syntax" in lower_tag or "سمی‌کالن" in lower_tag or "نحو" in lower_tag:
            recommendations.append("دقت در بیانیه‌های C: در پایان دستورات حتماً از سمی‌کالن (;) استفاده کنید و ساختار آکولادها را چک نمایید.")
        elif "binary" in lower_tag or "دودویی" in lower_tag or "باینری" in lower_tag:
            recommendations.append("تقویت محاسبات باینری: ارزش هر بیت از راست به چپ (۱، ۲، ۴، ۸، ۱۶، ...) را روی کاغذ رسم و تمرین نمایید.")
        elif "pointer" in lower_tag or "اشاره‌گر" in lower_tag or "حافظه" in lower_tag:
            recommendations.append("تجسم حافظه: برای اشاره‌گرها دیاگرام خانه‌های رم را با آدرس و مقدار رسم کنید.")

    if not recommendations:
        if unresolved:
            recommendations.append("با کلیک روی «تمرین مجدد»، سوالات جعبه اشتباهات را یک‌بار دیگر مرور و حل کنید.")
        elif total_mistakes > 0:
            recommendations.append("عملکرد فوق‌العاده! تمام خطاهای پیشین خود را اصلاح و یادگیری را تثبیت کرده‌اید.")
        else:
            recommendations.append("هنوز خطایی ثبت نشده است. با ورود به بخش تمرین‌های تعاملی هر هفته، مهارت‌های خود را بسنجید.")

    # شاخص کلی تسلط (Mastery Score از ۰ تا ۱۰۰)
    if total_mistakes == 0:
        mastery_score = 100
    else:
        mastery_score = max(20, min(100, int(resolution_rate - (len(unresolved) * 4))))

    return {
        "total_mistakes": total_mistakes,
        "unresolved_count": len(unresolved),
        "resolved_count": len(resolved),
        "resolution_rate": resolution_rate,
        "mastery_score": mastery_score,
        "concepts": concepts_list,
        "mistake_vault": mistake_vault,
        "resolved_vault": resolved_vault,
        "recommendations": list(dict.fromkeys(recommendations)),  # یکتا
    }


def get_cohort_diagnostic_overview() -> dict[str, Any]:
    """آمار کلی کلاسی از خطاهای پرتکرار و نقاط ضعف رایج برای اساتید و منتورها."""
    total_mistakes = db.session.query(func.count(StudentMistake.id)).scalar() or 0
    total_unresolved = (
        db.session.query(func.count(StudentMistake.id))
        .filter(StudentMistake.is_resolved == False)
        .scalar()
        or 0
    )

    # ۵ چالش سخت‌تر دوره (با بیشترین تعداد دانش‌آموزان گیرکرده)
    hardest_items_rows = (
        db.session.query(
            StudentMistake.item_id,
            StudentMistake.item_title,
            StudentMistake.concept_tag,
            StudentMistake.week,
            func.count(StudentMistake.id).label("student_count"),
            func.sum(StudentMistake.error_count).label("total_errors"),
            func.sum(case((StudentMistake.is_resolved == False, 1), else_=0)).label("unresolved_count"),
        )
        .group_by(
            StudentMistake.item_id,
            StudentMistake.item_title,
            StudentMistake.concept_tag,
            StudentMistake.week,
        )
        .order_by(func.count(StudentMistake.id).desc())
        .limit(6)
        .all()
    )

    hardest_items = []
    for row in hardest_items_rows:
        hardest_items.append({
            "item_id": row.item_id,
            "title": row.item_title or row.item_id,
            "concept_tag": row.concept_tag,
            "week": row.week,
            "student_count": row.student_count,
            "total_errors": int(row.total_errors or 0),
            "unresolved_count": int(row.unresolved_count or 0),
        })

    # پرتکرارترین تگ‌های ضعف مفهومی در کل کلاس
    concept_heatmap_rows = (
        db.session.query(
            StudentMistake.concept_tag,
            func.count(StudentMistake.id).label("total_occurrences"),
            func.sum(case((StudentMistake.is_resolved == False, 1), else_=0)).label("open_occurrences"),
        )
        .group_by(StudentMistake.concept_tag)
        .order_by(func.count(StudentMistake.id).desc())
        .limit(8)
        .all()
    )

    concept_heatmap = []
    for row in concept_heatmap_rows:
        concept_heatmap.append({
            "concept_tag": row.concept_tag,
            "total_occurrences": row.total_occurrences,
            "open_occurrences": int(row.open_occurrences or 0),
        })

    # دانش‌آموزان نیازمند بیشترین راهنمایی و توجه منتور (بر اساس خطاهای حل‌نشده)
    struggling_students_rows = (
        db.session.query(
            User.id,
            User.username,
            User.streak,
            func.count(StudentMistake.id).label("unresolved_count"),
            func.sum(StudentMistake.error_count).label("total_errors"),
        )
        .join(StudentMistake, User.id == StudentMistake.user_id)
        .filter(StudentMistake.is_resolved == False)
        .group_by(User.id, User.username, User.streak)
        .order_by(func.count(StudentMistake.id).desc())
        .limit(6)
        .all()
    )

    struggling_students = []
    for row in struggling_students_rows:
        struggling_students.append({
            "user_id": row.id,
            "username": row.username,
            "streak": row.streak or 0,
            "unresolved_count": row.unresolved_count,
            "total_errors": int(row.total_errors or 0),
        })

    return {
        "total_mistakes": total_mistakes,
        "total_unresolved": total_unresolved,
        "hardest_items": hardest_items,
        "concept_heatmap": concept_heatmap,
        "struggling_students": struggling_students,
    }
