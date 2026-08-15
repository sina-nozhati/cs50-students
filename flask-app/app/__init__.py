"""Application Factory پلتفرم Anzali-CS50-Hub.

این الگو (Application Factory) به ما اجازه می‌دهد instanceهای مختلف بسازیم
(dev, test, production) با کانفیگ متفاوت — بدون متغیر سراسری app.
این یکی از مهم‌ترین الگوهایی است که به بچه‌ها آموزش می‌دهیم.
"""
import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


from flask_wtf.csrf import CSRFProtect

# extensionها در سطح ماژول ساخته می‌شوند اما به هیچ appی متصل نیستند تا create_app صدا زده شود
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "برای ادامه لطفاً وارد شوید."
login_manager.login_message_category = "info"


def create_app(config_object: str = "app.config.Config") -> Flask:
    """ساخت و پیکربندی یک instance از اپلیکیشن.

    Args:
        config_object: مسیر کلاس کانفیگ (پیش‌فرض برای production/dev).
                       برای تست: "app.config.TestingConfig"

    Returns:
        یک Flask app آماده‌ی اجرا.
    """
    # مسیر ریشه‌ی پروژه: یکی بالاتر از پکیج app/ (یعنی flask-app/).
    # templateها و فایلهای static در ریشه‌ی پروژه نگهداری می‌شوند، نه داخل پکیج.
    # این با config.UPLOAD_FOLDER (که به ../static/downloads اشاره میکند) هماهنگ است.
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder=os.path.join(project_root, "templates"),
        static_folder=os.path.join(project_root, "static"),
    )
    app.config.from_object(config_object)

    # اطمینان از وجود پوشه‌ی instance برای فایل SQLite
    os.makedirs(app.instance_path, exist_ok=True)

    # متصل‌کردن extensionها به این app
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    # ثبت blueprintهای هر ماژول
    from app.routes import main, kb, assignments, gamification, auth, resources, admin
    app.register_blueprint(main.bp)
    app.register_blueprint(kb.bp)
    app.register_blueprint(assignments.bp)
    app.register_blueprint(gamification.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(resources.bp)
    app.register_blueprint(admin.bp)

    # ساخت جداول در صورت نبودن (مناسب SQLite dev)
    # در production ترجیحاً از init_db.py استفاده کنید
    with app.app_context():
        from app import models  # noqa: F401 — ثبت مدلها با SQLAlchemy
        db.create_all()

    # logging سبک به stdout (systemd journal آن را جمع می‌کند)
    logging.basicConfig(
        level=app.config.get("LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    # ثبت صفحه‌ی خطای سفارشی (404 — صفحه یافت نشد)
    from flask import render_template
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404

    return app
