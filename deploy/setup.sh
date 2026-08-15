#!/bin/bash
# ==============================================================
# CS50x Anzali Hub — First-time Server Setup
# Target: Ubuntu 24.04 LTS
# Run as root: bash setup.sh
# ==============================================================

set -euo pipefail

# ── Config ────────────────────────────────────────────────────
PROJECT_DIR="/var/www/cs50hub"
REPO_URL="https://github.com/sina-nozhati/cs50-students.git"
DOMAIN="cs50anzali.ir"

# ── Helpers ───────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

ok()   { echo -e "${GREEN}[OK]${NC} $1"; }
warn() { echo -e "${YELLOW}[!!]${NC} $1"; }
fail() { echo -e "${RED}[FAIL]${NC} $1"; exit 1; }

step() {
    echo ""
    echo -e "${GREEN}[$1/$TOTAL_STEPS]${NC} $2"
    echo "────────────────────────────────────────"
}

TOTAL_STEPS=9

# ── Pre-flight checks ────────────────────────────────────────
if [ "$EUID" -ne 0 ]; then
    fail "This script must be run as root. Try: sudo bash setup.sh"
fi

echo ""
echo "=========================================="
echo "  CS50x Anzali Hub — Server Setup"
echo "  Target: Ubuntu 24.04"
echo "=========================================="

# ── Step 1: System packages ──────────────────────────────────
step 1 "Installing system packages..."
apt-get update -qq || fail "apt update failed"
apt-get install -y -qq python3 python3-pip python3-venv nginx git sqlite3 > /dev/null 2>&1 || fail "apt install failed"
ok "System packages installed."

# ── Step 2: Clone repository ─────────────────────────────────
step 2 "Cloning repository..."
if [ -d "$PROJECT_DIR/.git" ]; then
    warn "Directory $PROJECT_DIR already exists. Pulling latest..."
    cd "$PROJECT_DIR"
    git fetch origin main
    git reset --hard origin/main
else
    mkdir -p "$(dirname $PROJECT_DIR)"
    git clone "$REPO_URL" "$PROJECT_DIR" || fail "git clone failed"
fi
ok "Repository ready at $PROJECT_DIR"

# ── Step 3: Python virtual environment ───────────────────────
step 3 "Creating virtual environment and installing dependencies..."
cd "$PROJECT_DIR/flask-app"
python3 -m venv "$PROJECT_DIR/venv" || fail "Failed to create venv"
source "$PROJECT_DIR/venv/bin/activate"
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt || fail "pip install failed"
pip install --quiet gunicorn
ok "Python environment ready. $(python3 --version)"

# ── Step 4: Generate secrets & .env ──────────────────────────
step 4 "Generating secret key and .env file..."
SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")

if [ -f "$PROJECT_DIR/flask-app/.env" ]; then
    warn ".env already exists. Keeping existing file."
else
    cat > "$PROJECT_DIR/flask-app/.env" << EOF
SECRET_KEY=$SECRET_KEY
FLASK_ENV=production
EOF
    ok ".env created with a random SECRET_KEY."
fi

# ── Step 5: Initialize database ──────────────────────────────
step 5 "Initializing database..."
cd "$PROJECT_DIR/flask-app"
python3 init_db.py || fail "Database initialization failed"
echo ""
ok "Database initialized. If this is a fresh install, admin credentials were printed above."

# ── Step 6: Systemd service (Gunicorn) ───────────────────────
step 6 "Configuring Gunicorn systemd service..."
cp "$PROJECT_DIR/deploy/cs50hub.service" /etc/systemd/system/cs50hub.service
systemctl daemon-reload
systemctl enable cs50hub --quiet
systemctl restart cs50hub || fail "Failed to start cs50hub service"
sleep 2

if systemctl is-active --quiet cs50hub; then
    ok "cs50hub.service is running."
else
    fail "cs50hub.service failed to start. Check: journalctl -u cs50hub -n 20"
fi

# ── Step 7: Nginx ────────────────────────────────────────────
step 7 "Configuring Nginx..."
cp "$PROJECT_DIR/deploy/nginx.conf" /etc/nginx/sites-available/cs50hub
sed -i "s|cs50anzali.ir www.cs50anzali.ir|$DOMAIN www.$DOMAIN|g" /etc/nginx/sites-available/cs50hub
ln -sf /etc/nginx/sites-available/cs50hub /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default

nginx -t 2>/dev/null || fail "Nginx config test failed. Check: nginx -t"
systemctl restart nginx || fail "Failed to restart Nginx"
ok "Nginx configured and running."

# ── Step 8: Webhook auto-deploy listener ─────────────────────
step 8 "Setting up GitHub webhook listener..."
cp "$PROJECT_DIR/deploy/cs50hub-webhook.service" /etc/systemd/system/
systemctl daemon-reload
systemctl enable cs50hub-webhook --quiet
systemctl restart cs50hub-webhook || warn "Webhook service failed to start (non-critical)"

if systemctl is-active --quiet cs50hub-webhook; then
    ok "Webhook listener running on port 9000."
else
    warn "Webhook listener not running. Check: journalctl -u cs50hub-webhook -n 20"
fi

# ── Step 9: Daily database backup ────────────────────────────
step 9 "Setting up daily database backup..."
chmod +x "$PROJECT_DIR/deploy/backup_db.sh"
CRON_LINE="0 3 * * * $PROJECT_DIR/deploy/backup_db.sh"
(crontab -l 2>/dev/null | grep -v "backup_db.sh"; echo "$CRON_LINE") | crontab -
ok "Daily backup scheduled at 03:00 AM."

# ── Summary ──────────────────────────────────────────────────
echo ""
echo "=========================================="
echo "  SETUP COMPLETE"
echo ""
echo "  Site:    http://$DOMAIN"
echo "  Webhook: http://$DOMAIN:9000/webhook"
echo ""
echo "  Useful commands:"
echo "    Status:   systemctl status cs50hub"
echo "    Logs:     journalctl -u cs50hub -f"
echo "    Restart:  systemctl restart cs50hub"
echo ""
echo "  Next steps:"
echo "    1. Point your domain A-record to this server IP"
echo "    2. Add webhook in GitHub repo Settings > Webhooks:"
echo "       URL: http://$(hostname -I | awk '{print $1}'):9000/webhook"
echo "       Content type: application/json"
echo "       Secret: cs50-anzali-webhook-secret"
echo "    3. (Optional) Enable HTTPS:"
echo "       apt install certbot python3-certbot-nginx"
echo "       certbot --nginx -d $DOMAIN -d www.$DOMAIN"
echo "=========================================="
echo ""
