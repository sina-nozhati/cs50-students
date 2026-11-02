"""سازگاری با importهای قدیمی — منبع حقیقت: kb_repo."""
from app.content import kb_repo
from app.content.certificate import CERTIFICATE
from app.services import kb_content as kb_service


def list_weeks() -> list[dict]:
    return kb_service.catalog()


def week_numbers() -> list[int]:
    return [w["number"] for w in list_weeks()]


def get_week(number: int) -> dict | None:
    return kb_service.week_payload(number)


def has_content(number: int) -> bool:
    return kb_repo.week_node_by_site_number(number) is not None


def get_certificate_meta() -> dict:
    return CERTIFICATE
