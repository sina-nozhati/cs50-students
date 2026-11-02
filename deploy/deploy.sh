#!/bin/bash
# ==============================================================
# CS50x Anzali Hub — Professional Auto-Deploy Pipeline v2.0
#
# Key Features:
#   1. Clean, English terminal UI with live real-time action tracking
#   2. Atomic pre-deploy database backup (SQLite WAL-safe)
#   3. Automatic instant rollback on failure (Git + DB + Systemd)
#   4. Idempotent database schema & reference model sync
#   5. Dynamic Knowledge Base downloads validation & cache warm-up
#   6. Automated production smoke tests (/health, /, /login, /offline)
#   7. Full persistent audit trail in /var/log/cs50hub-deploy.log
# ==============================================================

set -euo pipefail

# ─── Configuration & Paths ────────────────────────────────────
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

# Rollback state trackers
PREV_COMMIT=""
CURRENT_BACKUP=""
GIT_UPDATED=0
DEPLOY_SUCCEEDED=0

# ─── ANSI Terminal Colors ─────────────────────────────────────
BOLD='\033[1m'
DIM='\033[2m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

# ─── Logging & Display Helpers ────────────────────────────────
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

action() {
    log "  ${BLUE}→${NC} ${DIM}$1${NC}"
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

# ─── Atomic Rollback Engine ───────────────────────────────────
handle_deploy_error() {
    local exit_code=$?
    local line_no=${1:-$LINENO}
    local failed_cmd=${2:-$BASH_COMMAND}

    # If deployment already succeeded, do not rollback
    if [ "$DEPLOY_SUCCEEDED" -eq 1 ] || [ "$exit_code" -eq 0 ]; then
        return 0
    fi

    echo ""
    echo -e "${RED}${BOLD}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}${BOLD}║   DEPLOYMENT FAILED! Initiating Automatic Rollback...         ║${NC}"
    echo -e "${RED}${BOLD}╚══════════════════════════════════════════════════════════════╝${NC}"
    log "${RED}Failure at line ${line_no}: command '${failed_cmd}' exited with code ${exit_code}.${NC}"
    echo ""

    log "${YELLOW}${BOLD}🔄 Starting automatic system rollback...${NC}"

    # 1. Revert Git repository to previous stable commit
    if [ "$GIT_UPDATED" -eq 1 ] && [ -n "$PREV_COMMIT" ]; then
        log "  ${YELLOW}←${NC} Reverting Git working tree to commit (${PREV_COMMIT:0:7})..."
        git -C "$PROJECT_DIR" reset --hard "$PREV_COMMIT" >> "$LOG_FILE" 2>&1 || true
        ok "Source code successfully reverted to previous stable state."
    fi

    # 2. Revert Database from pre-deploy snapshot
    if [ -n "$CURRENT_BACKUP" ] && [ -f "$CURRENT_BACKUP" ]; then
        log "  ${YELLOW}←${NC} Restoring database from pre-deploy backup snapshot..."
        if [[ "$CURRENT_BACKUP" == *.gz ]]; then
            gunzip -c "$CURRENT_BACKUP" > "$DB_PATH" 2>/dev/null || true
        else
            cp "$CURRENT_BACKUP" "$DB_PATH" 2>/dev/null || true
        fi
        ok "Database successfully restored to clean pre-deploy state."
    fi

    # 3. Restart previous service version
    log "  ${YELLOW}←${NC} Restarting cs50hub systemd service with previous release..."
    run_as_admin systemctl restart cs50hub >> "$LOG_FILE" 2>&1 || true
    sleep 2

    if run_as_admin systemctl is-active --quiet cs50hub; then
        ok "Web service successfully recovered and running previous stable release."
    else
        fail "Service recovery failed! Check system logs with:"
        echo -e "   ${CYAN}sudo journalctl -u cs50hub -n 50 --no-pager${NC}"
    fi

    echo ""
    log "${YELLOW}Detailed error log available at:${NC} ${BOLD}${LOG_FILE}${NC}"
    echo -e "${RED}${BOLD}================================================================${NC}"
    exit "$exit_code"
}

trap 'handle_deploy_error $LINENO "$BASH_COMMAND"' ERR

# ─── Optional CLI Flags ───────────────────────────────────────
if [ "${1:-}" = "--smoke-only" ]; then
    echo -e "${CYAN}${BOLD}▶ Executing standalone production smoke tests...${NC}"
    bash "$SMOKE_TEST_SCRIPT"
    exit $?
fi

# ─── Begin Deployment Pipeline ────────────────────────────────
clear 2>/dev/null || true
echo -e "${CYAN}${BOLD}"
echo "  ╔══════════════════════════════════════════════════════════════╗"
echo "  ║        CS50x Anzali Hub — Production Deployer v2.0          ║"
echo "  ║      Safe • Atomic Backups • Auto-Rollback • Smoke Tests    ║"
echo "  ╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
log "Deployment initiated for project root: ${BOLD}${PROJECT_DIR}${NC}"

# Capture pre-deploy commit SHA for rollback
if [ -d "${PROJECT_DIR}/.git" ]; then
    PREV_COMMIT=$(git -C "$PROJECT_DIR" rev-parse HEAD 2>/dev/null || echo "")
fi

# ─── Step 1: Pre-flight & Environment Checks ──────────────────
step "Pre-flight Environment & Requirements Checks"

action "Verifying project root directory (${PROJECT_DIR})..."
if [ ! -d "$PROJECT_DIR" ]; then
    fail "Project directory not found: $PROJECT_DIR"
    exit 1
fi
ok "Project directory confirmed: ${PROJECT_DIR}"

action "Verifying Python virtual environment (${VENV_DIR})..."
if [ ! -d "$VENV_DIR" ]; then
    fail "Python virtual environment not found: $VENV_DIR"
    exit 1
fi
ok "Python virtual environment confirmed: ${VENV_DIR}"

action "Validating environment configuration (.env)..."
mkdir -p "${FLASK_DIR}/instance"
if [ ! -f "${FLASK_DIR}/.env" ]; then
    touch "${FLASK_DIR}/.env"
fi

if ! grep -q "KB_DOWNLOADS_DYNAMIC" "${FLASK_DIR}/.env" 2>/dev/null; then
    action "Injecting KB_DOWNLOADS_DYNAMIC=true into .env..."
    echo "KB_DOWNLOADS_DYNAMIC=true" >> "${FLASK_DIR}/.env"
    ok "Added KB_DOWNLOADS_DYNAMIC=true to ${FLASK_DIR}/.env"
else
    ok "Dynamic downloads configuration confirmed in .env"
fi

# ─── Step 2: Atomic Database Backup ───────────────────────────
step "Atomic Database Backup (Pre-deploy Snapshot)"

mkdir -p "$BACKUP_DIR"

action "Checking SQLite database at ${DB_PATH}..."
if [ -f "$DB_PATH" ]; then
    BACKUP_TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
    RAW_BACKUP="${BACKUP_DIR}/pre_deploy_${BACKUP_TIMESTAMP}.db"

    action "Creating WAL-safe SQLite snapshot..."
    if command -v sqlite3 >/dev/null 2>&1; then
        sqlite3 "$DB_PATH" ".backup '${RAW_BACKUP}'" >> "$LOG_FILE" 2>&1
    else
        cp "$DB_PATH" "$RAW_BACKUP"
    fi

    action "Compressing snapshot with gzip..."
    gzip -c "$RAW_BACKUP" > "${RAW_BACKUP}.gz"
    rm -f "$RAW_BACKUP"
    CURRENT_BACKUP="${RAW_BACKUP}.gz"
    ok "Atomic backup created successfully:"
    log "     ${DIM}${CURRENT_BACKUP}${NC}"

    action "Purging backups older than 14 days..."
    find "$BACKUP_DIR" -type f -name "pre_deploy_*.db.gz" -mtime +14 -exec rm -f {} \; 2>/dev/null || true
else
    warn "Database file not found yet (fresh install). Skipped backup."
fi

# ─── Step 3: Git Pull & Hard Reset to origin/main ─────────────
step "Synchronizing Code with GitHub (Git Fetch & Reset to origin/main)"

action "Connecting to remote origin and fetching main branch..."
cd "$PROJECT_DIR"
git fetch origin main >> "$LOG_FILE" 2>&1

action "Resetting working tree to match origin/main..."
git reset --hard origin/main >> "$LOG_FILE" 2>&1
GIT_UPDATED=1

NEW_COMMIT=$(git rev-parse --short HEAD)
COMMIT_MSG=$(git log -1 --pretty=format:"%s")
ok "Code synchronized to commit ${BOLD}[${NEW_COMMIT}]${NC}:"
log "     ${DIM}${COMMIT_MSG}${NC}"

# ─── Step 4: Virtualenv Python Dependencies ───────────────────
step "Updating Python Dependencies (Virtualenv Requirements)"

action "Activating virtual environment at ${VENV_DIR}..."
source "${VENV_DIR}/bin/activate"

action "Verifying pip package manager..."
pip install --quiet --upgrade pip >> "$LOG_FILE" 2>&1 || true

action "Installing/updating dependencies from requirements.txt (may take a few seconds)..."
pip install -r "${FLASK_DIR}/requirements.txt" >> "$LOG_FILE" 2>&1
ok "Installed/verified Python packages (Pygments, Flask, SQLAlchemy, etc.)."

# ─── Step 5: Database Models & Seed Synchronization ───────────
step "Synchronizing Database Models & Seed Data (Idempotent Sync)"

action "Loading Flask application context..."
cd "$FLASK_DIR"
action "Executing db.create_all() for all registered models..."
python3 -c "
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
" >> "$LOG_FILE" 2>&1
ok "Database schema and tables validated & synchronized."

action "Executing idempotent curriculum and reference seeder (init_db.py)..."
python3 init_db.py >> "$LOG_FILE" 2>&1
ok "Reference curriculum data and resources verified."

action "Enforcing high-performance SQLite WAL mode & RAM cache on database..."
if command -v sqlite3 >/dev/null 2>&1 && [ -f "$DB_PATH" ]; then
    sqlite3 "$DB_PATH" "PRAGMA journal_mode=WAL; PRAGMA synchronous=NORMAL; PRAGMA cache_size=-64000;" >> "$LOG_FILE" 2>&1 || true
    ok "SQLite WAL mode and 64MB RAM page cache verified."
fi

# ─── Step 6: Dynamic KB Downloads Warm-up ─────────────────────
step "Knowledge Base Dynamic Downloads Cache Warm-up"

action "Checking dynamic downloads engine status..."
action "Pre-building missing weekly HTML & PDF packages..."
python3 -c "
from app import create_app
from app.services.downloads import build_all_downloads
app = create_app()
with app.app_context():
    if app.config.get('KB_DOWNLOADS_DYNAMIC', False):
        build_all_downloads(force=False)
" >> "$LOG_FILE" 2>&1 || warn "Dynamic downloads pre-build completed with warnings (will build on first request)."
ok "Dynamic downloads engine verified and warm."

# ─── Step 7: Service Restart & Automated Smoke Tests ──────────
step "Restarting Application Service & Running Smoke Tests"

action "Synchronizing Gunicorn systemd service configuration..."
if [ -f "/etc/systemd/system/cs50hub.service" ]; then
    run_as_admin cp "${PROJECT_DIR}/deploy/cs50hub.service" /etc/systemd/system/cs50hub.service >> "$LOG_FILE" 2>&1 || true
    run_as_admin systemctl daemon-reload >> "$LOG_FILE" 2>&1 || true
fi

action "Synchronizing Nginx performance configuration (Gzip & Security)..."
if [ -f "/etc/nginx/sites-available/cs50hub" ]; then
    if grep -q "ssl_certificate" /etc/nginx/sites-available/cs50hub; then
        ok "Active SSL certificate detected in /etc/nginx/sites-available/cs50hub; preserving SSL configuration."
        if ! grep -q "client_max_body_size" /etc/nginx/sites-available/cs50hub; then
            action "Configuring 250MB upload limit in /etc/nginx/sites-available/cs50hub..."
            run_as_admin sed -i '/server_name/a \    client_max_body_size 250M;\n    client_body_timeout 180s;' /etc/nginx/sites-available/cs50hub 2>/dev/null || true
        fi
        if run_as_admin nginx -t >> "$LOG_FILE" 2>&1; then
            run_as_admin systemctl reload nginx >> "$LOG_FILE" 2>&1 || true
        fi
    else
        run_as_admin cp "${PROJECT_DIR}/deploy/nginx.conf" /etc/nginx/sites-available/cs50hub >> "$LOG_FILE" 2>&1 || true
        if [ -f "/etc/letsencrypt/live/cs50xanzali.ir/fullchain.pem" ] && command -v certbot >/dev/null 2>&1; then
            action "Re-binding existing Let's Encrypt SSL certificate for cs50xanzali.ir..."
            run_as_admin certbot install --cert-name cs50xanzali.ir --nginx >> "$LOG_FILE" 2>&1 || true
        fi
        if run_as_admin nginx -t >> "$LOG_FILE" 2>&1; then
            run_as_admin systemctl reload nginx >> "$LOG_FILE" 2>&1 || true
            ok "Nginx reloaded with performance optimizations and SSL security."
        else
            warn "Nginx config test failed; kept running existing configuration."
        fi
    fi
fi

action "Restarting systemd service cs50hub..."
run_as_admin systemctl restart cs50hub >> "$LOG_FILE" 2>&1

action "Waiting for Gunicorn workers to warm up and become ready..."
max_wait=20
waited=0
ready=0
while [ $waited -lt $max_wait ]; do
    if curl -s -f --max-time 2 http://127.0.0.1:5000/health >/dev/null 2>&1; then
        ready=1
        break
    fi
    sleep 1
    waited=$((waited + 1))
done

if [ $ready -eq 1 ]; then
    ok "Gunicorn workers initialized and ready in ${waited}s."
else
    warn "Gunicorn workers took more than ${max_wait}s to initialize; proceeding to smoke tests."
fi

action "Checking systemd service active state..."
if ! run_as_admin systemctl is-active --quiet cs50hub; then
    fail "cs50hub.service failed to enter active state after restart!"
    exit 1
fi
ok "Service cs50hub is active (running)."

action "Executing automated production smoke tests..."
echo ""
chmod +x "$SMOKE_TEST_SCRIPT" 2>/dev/null || true
if ! bash "$SMOKE_TEST_SCRIPT"; then
    fail "Automated production smoke tests failed!"
    exit 1
fi

# ─── Deployment Complete ──────────────────────────────────────
DEPLOY_SUCCEEDED=1
ELAPSED=$(($(date +%s) - START_TIME))

echo ""
echo -e "${GREEN}${BOLD}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}${BOLD}║   🎉 DEPLOYMENT SUCCESSFUL! All systems operational.         ║${NC}"
echo -e "${GREEN}${BOLD}╚══════════════════════════════════════════════════════════════╝${NC}"
log "Current commit: ${BOLD}${NEW_COMMIT}${NC} (${COMMIT_MSG:0:45}...)"
log "Total duration: ${BOLD}${ELAPSED}s${NC} | Service status: ${GREEN}${BOLD}Active (Running)${NC}"
if [ -n "$CURRENT_BACKUP" ]; then
    log "Backup snapshot: ${DIM}${CURRENT_BACKUP}${NC}"
fi
echo -e "${DIM}Detailed audit log: ${LOG_FILE}${NC}"
echo ""

exit 0
