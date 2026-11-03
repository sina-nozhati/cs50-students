"""Application configuration — reads from environment variables.

Never hardcode sensitive values (SECRET_KEY, passwords) in this file.
For development, safe fallback defaults are provided.
"""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Main config — used in both production and development."""

    # SECRET_KEY must be set via env var in production
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        if os.environ.get("FLASK_ENV") == "production":
            raise ValueError("SECRET_KEY environment variable is missing in production!")
        SECRET_KEY = "dev-secret-change-me-in-production"

    # SQLite in instance folder (gitignored). Change to PostgreSQL URL if needed.
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "..", "instance", "cs50.db"),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

    # آپلودها روی دیسک زیر static/downloads — اما Nginx این مسیر را مسدود می‌کند.
    # دانلود فقط از روت /resources/file/<id>/download با لاگین انجام می‌شود.
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "static", "downloads")
    DATA_DIR = os.environ.get("DATA_DIR", os.path.abspath(os.path.join(BASE_DIR, "..", "data")))
    KB_DOWNLOADS_DYNAMIC = os.environ.get("KB_DOWNLOADS_DYNAMIC", "False").lower() in ("true", "1", "yes")
    MAX_CONTENT_LENGTH = int(os.environ.get("MAX_CONTENT_LENGTH", 250 * 1024 * 1024))  # 250 MB max upload size
    ALLOWED_EXTENSIONS = {"pdf", "zip", "tar", "gz", "tgz"}
    WTF_CSRF_TIME_LIMIT = 86400  # 24 hours (prevents premature CSRF token expiration)
    # محدودیت نرخ ورود: حداکثر تلاش در پنجرهٔ زمانی (ثانیه)
    LOGIN_RATE_LIMIT = 10
    LOGIN_RATE_WINDOW_SECONDS = 300


class TestingConfig(Config):
    """Testing config — in-memory DB, CSRF disabled for convenience."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    SECRET_KEY = "testing-secret"
    KB_DOWNLOADS_DYNAMIC = True
