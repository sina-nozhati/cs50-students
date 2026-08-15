"""منطق منابع (فایلهای قابل‌دانلود) — لیست، شمارش، ایجاد، دریافت."""
from flask import abort

from app import db
from app.models import Resource


def list_for_week(week: int) -> list[Resource]:
    """فایلهای منتشرشده‌ی یک هفته را مرتب بر اساس دسته برمیگرداند."""
    return (
        Resource.query.filter_by(week=week, is_published=True)
        .order_by(Resource.category, Resource.id)
        .all()
    )


def count_for_week(week: int) -> int:
    """تعداد فایلهای منتشرشده‌ی یک هفته — برای badge روی کارت هفته."""
    return Resource.query.filter_by(week=week, is_published=True).count()


def get(resource_id: int):
    """یک Resource بر اساس id برمیگرداند یا None."""
    return db.session.get(Resource, resource_id)


def get_or_404(resource_id: int) -> Resource:
    res = get(resource_id)
    if res is None:
        abort(404)
    return res


def create_resource(
    week: int, filename: str, display_name: str, category: str, uploaded_by: int
) -> Resource:
    """یک منبع جدید در DB ثبت میکند.

    فرض بر این است که فایل فیزیکی از قبل در static/downloads/weekN/ ذخیره شده.
    """
    res = Resource(
        week=week,
        filename=filename,
        display_name=display_name,
        category=category,
        uploaded_by=uploaded_by,
        is_published=True,
    )
    db.session.add(res)
    db.session.commit()
    return res
