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

    # Upload settings (stored under static/ so Nginx can serve them directly)
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "static", "downloads")
    MAX_CONTENT_LENGTH = 30 * 1024 * 1024  # 30 MB max upload size
    ALLOWED_EXTENSIONS = {"pdf", "zip"}


class TestingConfig(Config):
    """Testing config — in-memory DB, CSRF disabled for convenience."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    SECRET_KEY = "testing-secret"
