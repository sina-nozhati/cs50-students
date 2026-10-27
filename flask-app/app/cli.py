import click
from flask import current_app
from app import db
from app.services import engagement as engagement_service
from app.services import notifications as notif_service
from app.models import User


def register_cli_commands(app):
    """ثبت دستورات CLI برای زمان‌بندی و نگهداری دوره‌ای."""

    @app.cli.command("engagement-tick")
    def engagement_tick():
        """محاسبه دوره‌ای امتیاز ریسک و بررسی وضعیت یادگیری دانش‌آموزان."""
        click.echo("🔄 در حال ارزیابی وضعیت یادگیری و تعامل دانش‌آموزان...")
        students = User.query.filter_by(is_admin=False, is_active=True).all()
        high_risk_count = 0
        for s in students:
            res = engagement_service.compute_user_engagement(s.id)
            if res["risk_level"] == "high":
                high_risk_count += 1

        click.echo(f"✅ محاسبه تکمیل شد. {len(students)} دانش‌آموز بررسی شدند. ({high_risk_count} نفر نیازمند توجه ویژه)")

    @app.cli.command("events-cleanup")
    @click.option("--days", default=180, help="تعداد روزهای نگهداری رویدادها")
    def events_cleanup(days):
        """حذف یا آرشیو رویدادهای قدیمی‌تر از ۱۸۰ روز جهت حفظ حریم خصوصی."""
        click.echo(f"🧹 در حال پاکسازی رویدادهای قدیمی‌تر از {days} روز...")
        from datetime import datetime, timedelta
        from app.models import LearningEvent

        cutoff = datetime.utcnow() - timedelta(days=days)
        deleted = LearningEvent.query.filter(LearningEvent.created_at < cutoff).delete()
        db.session.commit()
        click.echo(f"✅ {deleted} رویداد قدیمی با موفقیت پاکسازی شد.")
