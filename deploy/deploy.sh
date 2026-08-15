#!/bin/bash
# ==============================================================
# CS50x Anzali Hub — Auto-Deploy Script
# Called by the webhook listener on each git push to main
# ==============================================================

set -e

PROJECT_DIR="/var/www/cs50hub"
LOG_FILE="/var/log/cs50hub-deploy.log"

echo "$(date '+%Y-%m-%d %H:%M:%S') [START] Deploy triggered" >> $LOG_FILE

cd $PROJECT_DIR

# 1. Pull latest changes (hard reset = no conflicts ever)
git fetch origin main
git reset --hard origin/main
echo "$(date '+%Y-%m-%d %H:%M:%S') [OK] Code updated from GitHub" >> $LOG_FILE

# 2. Update dependencies if requirements.txt changed
source $PROJECT_DIR/venv/bin/activate
pip install --quiet -r flask-app/requirements.txt

# 3. Restart the app server
sudo systemctl restart cs50hub

echo "$(date '+%Y-%m-%d %H:%M:%S') [DONE] Deploy successful" >> $LOG_FILE
