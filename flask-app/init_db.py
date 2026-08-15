"""Initialize database tables and seed default data.

Usage:
    python init_db.py

This script:
    1. Creates all database tables.
    2. Creates a default admin user (prints credentials clearly).
    3. Seeds Resource records for all weekly download files.
    4. Seeds Week records for all 11 weeks (0-10), all unpublished.

Safe to run multiple times (idempotent — skips existing records).
"""
import secrets
import string

from werkzeug.security import generate_password_hash

from app import create_app, db
from app.models import User, Resource, Week


WEEK_TITLES = [
    "Week 0 — Scratch",
    "Week 1 — C (Basics)",
    "Week 2 — Arrays",
    "Week 3 — Algorithms",
    "Week 4 — Memory",
    "Week 5 — Data Structures",
    "Week 6 — Python",
    "Week 7 — SQL",
    "Week 8 — HTML/CSS/JS",
    "Week 9 — Flask",
    "Week 10 — Final Project",
]


SEED_RESOURCES = [
    # Week 0 — Scratch
    (0, "slides.pdf", "Slides", "slides"),
    (0, "notes.pdf", "Notes", "notes"),
    (0, "exercise.pdf", "Scratch Exercise", "pset"),
    (0, "first-submit.pdf", "First Submission Guide", "extra"),
    (0, "src.zip", "Source Code", "src"),
    # Week 1 — C Basics
    (1, "slides.pdf", "Slides", "slides"),
    (1, "notes.pdf", "Week 1 Notes", "notes"),
    (1, "pset-guide.pdf", "Problem Set 1 Guide", "pset"),
    (1, "src.zip", "Source Code", "src"),
    # Week 2 — Arrays
    (2, "slides.pdf", "Slides", "slides"),
    (2, "notes.pdf", "Week 2 Notes", "notes"),
    (2, "pset-guide.pdf", "Problem Set 2 Guide", "pset"),
    (2, "src.zip", "Source Code", "src"),
    # Week 3 — Algorithms
    (3, "slides.pdf", "Slides", "slides"),
    (3, "notes.pdf", "Algorithms Notes", "notes"),
    (3, "pset-guide.pdf", "Problem Set 3 Guide", "pset"),
    (3, "src.zip", "Source Code", "src"),
    # Week 4 — Memory
    (4, "slides.pdf", "Slides (Lecture 4)", "slides"),
    (4, "notes.pdf", "Week 4 Notes", "notes"),
    (4, "pset-guide.pdf", "Problem Set 4 Guide", "pset"),
    (4, "src.zip", "Source Code", "src"),
    # Week 5 — Data Structures
    (5, "slides.pdf", "Slides", "slides"),
    (5, "notes.pdf", "Lecture 5 Notes", "notes"),
    (5, "pset-1-speller.pdf", "PS5 - Speller", "pset"),
    (5, "pset-2-inheritance.pdf", "PS5 - Inheritance", "pset"),
    (5, "week5-summary.pdf", "Week 5 Summary", "notes"),
    (5, "src.zip", "Source Code", "src"),
    # Week 6 — Python
    (6, "slides.pdf", "Slides (Lecture 6)", "slides"),
    (6, "notes.pdf", "Week 6 Notes", "notes"),
    (6, "pset-guide.pdf", "Problem Set 6 Guide", "pset"),
    (6, "src.zip", "Source Code", "src"),
    # Week 7 — SQL
    (7, "slides.pdf", "Slides (Lecture 7)", "slides"),
    (7, "notes-1.pdf", "Week 7 Notes (Part 1)", "notes"),
    (7, "notes-2.pdf", "Week 7 Notes (Part 2)", "notes"),
    (7, "pset-1.pdf", "Problem Set 7-1", "pset"),
    (7, "pset-2.pdf", "Problem Set 7-2", "pset"),
    (7, "pset-3.pdf", "Problem Set 7-3", "pset"),
    (7, "exam-answer.pdf", "Exam Answer Key", "extra"),
    (7, "src.zip", "Source Code", "src"),
    # Week 8 — HTML/CSS/JS
    (8, "src.zip", "Source Code", "src"),
]


def generate_password(length=12):
    """Generate a random secure password."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def main() -> None:
    app = create_app()
    with app.app_context():
        db.create_all()
        print("[OK] All database tables created.")

        # 1. Default admin user
        admin = User.query.filter_by(username="admin").first()
        if not admin:
            password = generate_password()
            db.session.add(
                User(
                    username="admin",
                    password_hash=generate_password_hash(password),
                    is_admin=True,
                )
            )
            db.session.commit()
            print("")
            print("=" * 50)
            print("  ADMIN ACCOUNT CREATED")
            print(f"  Username: admin")
            print(f"  Password: {password}")
            print("=" * 50)
            print("  SAVE THIS PASSWORD NOW! It will not be shown again.")
            print("=" * 50)
            print("")
        else:
            print("[--] Admin user already exists, skipping.")

        # 2. Seed resources
        added = 0
        for week, filename, display_name, category in SEED_RESOURCES:
            exists = Resource.query.filter_by(week=week, filename=filename).first()
            if not exists:
                db.session.add(
                    Resource(
                        week=week,
                        filename=filename,
                        display_name=display_name,
                        category=category,
                    )
                )
                added += 1
        db.session.commit()
        print(f"[OK] Resources: {added} new / {len(SEED_RESOURCES)} total.")

        # 3. Seed weeks (0-10), all unpublished
        weeks_added = 0
        for number, title in enumerate(WEEK_TITLES):
            if not Week.query.filter_by(number=number).first():
                db.session.add(Week(number=number, title=title))
                weeks_added += 1
        db.session.commit()
        print(f"[OK] Weeks: {weeks_added} new / {len(WEEK_TITLES)} total.")

        print("[OK] Database initialization complete.")


if __name__ == "__main__":
    main()
