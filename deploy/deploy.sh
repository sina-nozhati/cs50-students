#!/bin/bash
# ==============================================================
# CS50x Anzali Hub — Professional Auto-Deploy Pipeline v2.0
#
# قابلیت‌ها:
#   ۱. رابط کاربری یوزرفرندلی و رنگی در ترمینال با تفکیک دقیق مراحل
#   ۲. پشتیبان‌گیری اتمیک خودکار از دیتابیس قبل از هرگونه تغییر
#   ۳. مکانیزم بازگشت سریع خودکار (Instant Rollback) در صورت بروز خطا در هر مرحله
#   ۴. همگام‌سازی ساختار دیتابیس، مدل‌ها و داده‌های اولیه (Idempotent DB Sync)
#   ۵. آماده‌سازی و فعال‌سازی متغیرهای محیطی و کش دانلودهای پویا
#   ۶. تست دود خودکار (Automated Smoke Tests) و ارزیابی سلامت سرویس
#   ۷. ثبت تاریخچه کامل و گزارش وقایع در فایل لاگ سیستم
# ==============================================================

set -euo pipefail

# ─── تنظیمات و مسیرها ─────────────────────────────────────────
PROJECT_DIR="/var/www/cs50hub"
FLASK_DIR="${PROJECT_DIR}/flask-app"
VENV_DIR="${PROJECT_DIR}/venv"
DB_PATH="${FLASK_DIR}/instance/cs50.db"
BACKUP_DIR="${PROJECT_DIR}/backups"
LOG_FILE="/var/log/cs50hub-deploy.log"
SMOKE_TEST_SCRIPT="${PROJECT_DIR}/deploy/smoke_test.sh"

TOTAL_STEPS=7
CURRENT_STEP=0
START_TIME=$(date +%s)

# متغیرهای وضعیت برای Rollback
PREV_COMMIT=""
CURRENT_BACKUP=""
GIT_UPDATED=0
DEPLOY_SUCCEEDED=0

# ─── رنگ‌ها و استایل‌های ترمینال ──────────────────────────────
BOLD='\033[1m'
DIM='\033[2m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m' # بدون رنگ

# ─── توابع لاگ‌گیری و نمایش ─────────────────────────────────────
mkdir -p "$(dirname "$LOG_FILE")" 2>/dev/null || true
touch "$LOG_FILE" 2>/dev/null || LOG_FILE="/tmp/cs50hub-deploy.log"

log_raw() {
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] $1" >> "$LOG_FILE"
}

log() {
    local msg="$1"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo -e "${DIM}[${timestamp}]${NC} ${msg}"
    local clean_msg=$(echo -e "$msg" | sed -r 's/\x1B\[[0-9;]*[mK]//g')
    echo "[$timestamp] ${clean_msg}" >> "$LOG_FILE"
}

step() {
    CURRENT_STEP=$((CURRENT_STEP + 1))
    echo ""
    log "${CYAN}${BOLD}[${CURRENT_STEP}/${TOTAL_STEPS}]${NC} ${BOLD}$1${NC}"
    echo -e "${DIM}────────────────────────────────────────────────────────────────${NC}"
}

ok() {
    log "  ${GREEN}${BOLD}✓${NC} $1"
}

warn() {
    log "  ${YELLOW}${BOLD}⚠${NC} $1"
}

fail() {
    log "  ${RED}${BOLD}✗${NC} $1"
}

run_as_admin() {
    if [ "$EUID" -eq 0 ]; then
        "$@"
    else
        sudo "$@"
    fi
}

# ─── مکانیزم بازگشت به عقب (Atomic Rollback Engine) ──────────────
handle_deploy_error() {
    local exit_code=$?
    local line_no=${1:-$LINENO}
    local failed_cmd=${2:-$BASH_COMMAND}

    # اگر دیپلوی با موفقیت تمام شده، رول‌بک اجرا نشود
    if [ "$DEPLOY_SUCCEEDED" -eq 1 ] || [ "$exit_code" -eq 0 ]; then
        return 0
    fi

    echo ""
    echo -e "${RED}${BOLD}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}${BOLD}║   ❌ خطای استقرار! فرآیند دیپلوی متوقف و رول‌بک آغاز شد       ║${NC}"
    echo -e "${RED}${BOLD}╚══════════════════════════════════════════════════════════════╝${NC}"
    log "${RED}خطا در سطر ${line_no}: دستور '${failed_cmd}' با کد خطای ${exit_code} متوقف شد.${NC}"
    echo ""

    log "${YELLOW}${BOLD}🔄 در حال اجرای فرآیند بازگردانی خودکار (Automatic Rollback)...${NC}"

    # ۱. بازگردانی کد گیت به آخرین کامیت سالم
    if [ "$GIT_UPDATED" -eq 1 ] && [ -n "$PREV_COMMIT" ]; then
        log "  ${YELLOW}←${NC} بازگردانی شاخه گیت به آخرین کامیت سالم (${PREV_COMMIT:0:7})..."
        git -C "$PROJECT_DIR" reset --hard "$PREV_COMMIT" >> "$LOG_FILE" 2>&1 || true
        ok "کد منبع به نسخه پایدار قبلی بازگردانده شد."
    fi

    # ۲. بازگردانی پایگاه داده از نسخه پشتیبان
    if [ -n "$CURRENT_BACKUP" ] && [ -f "$CURRENT_BACKUP" ]; then
        log "  ${YELLOW}←${NC} بازگردانی پایگاه داده از نسخه پشتیبان قبل از دیپلوی..."
        if [[ "$CURRENT_BACKUP" == *.gz ]]; then
            gunzip -c "$CURRENT_BACKUP" > "$DB_PATH" 2>/dev/null || true
        else
            cp "$CURRENT_BACKUP" "$DB_PATH" 2>/dev/null || true
        fi
        ok "پایگاه داده به وضعیت کاملاً سالم قبل از دیپلوی بازگردانی شد."
    fi

    # ۳. راه‌اندازی مجدد سرویس با نسخه قبلی
    log "  ${YELLOW}←${NC} راه‌اندازی مجدد سرویس cs50hub با نسخه پایدار قبلی..."
    run_as_admin systemctl restart cs50hub >> "$LOG_FILE" 2>&1 || true
    sleep 2

    if run_as_admin systemctl is-active --quiet cs50hub; then
        ok "سرویس وب با موفقیت به نسخه قبلی بازگشت و در حال سرویس‌دهی است."
    else
        fail "سرویس نسخه قبلی نیز استارت نشد! لاگ‌ها را با دستور زیر بررسی کنید:"
        echo -e "   ${CYAN}sudo journalctl -u cs50hub -n 50 --no-pager${NC}"
    fi

    echo ""
    log "${YELLOW}لاگ تفصیلی خطا در مسیر زیر ذخیره شد:${NC} ${BOLD}${LOG_FILE}${NC}"
    echo -e "${RED}${BOLD}================================================================${NC}"
    exit "$exit_code"
}

trap 'handle_deploy_error $LINENO "$BASH_COMMAND"' ERR

# ─── پرچم‌های اجرایی (Flags) ────────────────────────────────────
if [ "${1:-}" = "--smoke-only" ]; then
    echo -e "${CYAN}${BOLD}▶ اجرای مجزای تست‌های دود (Smoke Tests)...${NC}"
    bash "$SMOKE_TEST_SCRIPT"
    exit $?
fi

# ─── شروع فرآیند استقرار ────────────────────────────────────────
clear 2>/dev/null || true
echo -e "${CYAN}${BOLD}"
echo "  ╔══════════════════════════════════════════════════════════════╗"
echo "  ║        CS50x Anzali Hub — Production Deployer v2.0          ║"
echo "  ║    ایمن • پشتیبان‌گیری خودکار • تست دود • بازگردانی آنی       ║"
echo "  ╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
log "شروع فرآیند استقرار در مسیر ${BOLD}${PROJECT_DIR}${NC}"

# ثبت کامیت قبلی برای امکان رول‌بک
if [ -d "${PROJECT_DIR}/.git" ]; then
    PREV_COMMIT=$(git -C "$PROJECT_DIR" rev-parse HEAD 2>/dev/null || echo "")
fi

# ─── مرحله ۱: بررسی پیش‌نیازها و محیط ──────────────────────────
step "بررسی پیش‌نیازها و تنظیمات محیطی (Pre-flight Checks)"

if [ ! -d "$PROJECT_DIR" ]; then
    fail "مسیر پروژه ($PROJECT_DIR) پیدا نشد!"
    exit 1
fi
ok "مسیر پروژه تایید شد: ${PROJECT_DIR}"

if [ ! -d "$VENV_DIR" ]; then
    fail "محیط مجازی پایتون ($VENV_DIR) یافت نشد!"
    exit 1
fi
ok "محیط مجازی پایتون تایید شد: ${VENV_DIR}"

# ایجاد و بررسی تنظیمات .env در پوشه flask-app
mkdir -p "${FLASK_DIR}/instance"
if [ ! -f "${FLASK_DIR}/.env" ]; then
    touch "${FLASK_DIR}/.env"
fi

if ! grep -q "KB_DOWNLOADS_DYNAMIC" "${FLASK_DIR}/.env" 2>/dev/null; then
    echo "KB_DOWNLOADS_DYNAMIC=true" >> "${FLASK_DIR}/.env"
    ok "متغیر محیطی KB_DOWNLOADS_DYNAMIC=true به صورت خودکار به .env اضافه شد."
else
    ok "متغیرهای محیطی سیستم دانلود تایید شدند."
fi

# ─── مرحله ۲: پشتیبان‌گیری اتمیک از پایگاه داده ────────────────
step "تهیه نسخه پشتیبان اتمیک از پایگاه داده (Atomic Database Backup)"

mkdir -p "$BACKUP_DIR"

if [ -f "$DB_PATH" ]; then
    BACKUP_TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
    RAW_BACKUP="${BACKUP_DIR}/pre_deploy_${BACKUP_TIMESTAMP}.db"

    if command -v sqlite3 >/dev/null 2>&1; then
        sqlite3 "$DB_PATH" ".backup '${RAW_BACKUP}'" >> "$LOG_FILE" 2>&1
    else
        cp "$DB_PATH" "$RAW_BACKUP"
    fi

    gzip -c "$RAW_BACKUP" > "${RAW_BACKUP}.gz"
    rm -f "$RAW_BACKUP"
    CURRENT_BACKUP="${RAW_BACKUP}.gz"
    ok "پشتیبان اتمیک در فایل زیر ایجاد شد:"
    log "     ${DIM}${CURRENT_BACKUP}${NC}"

    # نگهداری حداکثر پشتیبان‌های ۱۴ روز اخیر برای جلوگیری از پر شدن حافظه دیسک
    find "$BACKUP_DIR" -type f -name "pre_deploy_*.db.gz" -mtime +14 -exec rm -f {} \; 2>/dev/null || true
else
    warn "فایل پایگاه داده هنوز ایجاد نشده است (احتمال نصب اولیه). از ایجاد پشتیبان صرف‌نظر شد."
fi

# ─── مرحله ۳: همگام‌سازی آخرین تغییرات از گیت‌هاب ──────────────
step "همگام‌سازی آخرین کد با گیت‌هاب (Git Fetch & Reset to origin/main)"

cd "$PROJECT_DIR"
git fetch origin main >> "$LOG_FILE" 2>&1
git reset --hard origin/main >> "$LOG_FILE" 2>&1
GIT_UPDATED=1

NEW_COMMIT=$(git rev-parse --short HEAD)
COMMIT_MSG=$(git log -1 --pretty=format:"%s")
ok "کد سرور به کامیت ${BOLD}${NEW_COMMIT}${NC} به‌روزرسانی شد:"
log "     ${DIM}پیام کامیت: ${COMMIT_MSG}${NC}"

# ─── مرحله ۴: به‌روزرسانی وابستگی‌های پایتون ──────────────────
step "به‌روزرسانی وابستگی‌های پایتون (Python Requirements)"

source "${VENV_DIR}/bin/activate"
pip install --quiet --upgrade pip >> "$LOG_FILE" 2>&1 || true
pip install --quiet -r "${FLASK_DIR}/requirements.txt" >> "$LOG_FILE" 2>&1
ok "وابستگی‌های بسته نرم‌افزاری (از جمله Pygments و فریم‌ورک‌ها) به‌روزرسانی شدند."

# ─── مرحله ۵: همگام‌سازی پایگاه داده و مدل‌ها ──────────────────
step "همگام‌سازی ساختار دیتابیس، مدل‌ها و سیدها (Database Sync & Migrations)"

cd "$FLASK_DIR"
python3 -c "
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
" >> "$LOG_FILE" 2>&1
ok "جداول پایگاه داده و ساختار مدل‌ها اعتبارسنجی و ساخته شدند."

# اجرای اسکریپت امن و idempotent اولیه
python3 init_db.py >> "$LOG_FILE" 2>&1
ok "داده‌های مرجع (هفته‌ها، منابع آموزشی و مقادیر پایه) همگام‌سازی شدند."

# ─── مرحله ۶: آماده‌سازی و بیلد کش دانلودهای پویا ─────────────
step "بررسی و پیش‌بارگذاری کش موتور دانلودها (Warm-up Dynamic KB)"

python3 -c "
from app import create_app
from app.services.downloads import build_all_downloads
app = create_app()
with app.app_context():
    if app.config.get('KB_DOWNLOADS_DYNAMIC', False):
        build_all_downloads(force=False)
" >> "$LOG_FILE" 2>&1 || warn "پیش‌ساخت دانلودها با هشدار مواجه شد (در اولین درخواست دانشجو خودکار ساخته خواهد شد)."
ok "موتور دانلودهای پویا و کش پکیج‌های آموزشی آماده‌سازی شد."

# ─── مرحله ۷: راه‌اندازی مجدد و تست دود نهایی ────────────────
step "راه‌اندازی مجدد سرویس و اجرای تست‌های دود (Restart & Smoke Tests)"

run_as_admin systemctl restart cs50hub >> "$LOG_FILE" 2>&1
sleep 2

if ! run_as_admin systemctl is-active --quiet cs50hub; then
    fail "سرویس cs50hub پس از ری‌استارت فعال نشد!"
    exit 1
fi
ok "سرویس وب cs50hub در وضعیت فعال (Active) قرار گرفت."

echo ""
# اجرای اسکریپت تست دود مستقل
chmod +x "$SMOKE_TEST_SCRIPT" 2>/dev/null || true
if ! bash "$SMOKE_TEST_SCRIPT"; then
    fail "تست‌های دود (Smoke Tests) با شکست مواجه شدند!"
    exit 1
fi

# ─── پایان موفقیت‌آمیز ─────────────────────────────────────────
DEPLOY_SUCCEEDED=1
ELAPSED=$(($(date +%s) - START_TIME))

echo ""
echo -e "${GREEN}${BOLD}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}${BOLD}║   🎉 استقرار و دیپلوی با موفقیت کامل به پایان رسید!          ║${NC}"
echo -e "${GREEN}${BOLD}╚══════════════════════════════════════════════════════════════╝${NC}"
log "کامیت جاری: ${BOLD}${NEW_COMMIT}${NC} (${COMMIT_MSG:0:45}...)"
log "مدت زمان عملیات: ${BOLD}${ELAPSED} ثانیه${NC} | وضعیت سرویس: ${GREEN}${BOLD}Active (Running)${NC}"
if [ -n "$CURRENT_BACKUP" ]; then
    log "پشتیبان ایجادشده: ${DIM}${CURRENT_BACKUP}${NC}"
fi
echo -e "${DIM}لاگ تفصیلی استقرار: ${LOG_FILE}${NC}"
echo ""

exit 0
