"""نقطه‌ی ورود برای توسعه.

اجرا (dev):
    python run.py

در production از Gunicorn استفاده کنید:
    gunicorn --workers 2 --bind 127.0.0.1:5000 "run:app"
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug=True فقط برای dev؛ هرگز در production
    app.run(host="127.0.0.1", port=5000, debug=True)
