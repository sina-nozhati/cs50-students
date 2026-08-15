#!/bin/bash
# Daily SQLite database backup script
# Add to crontab: 0 3 * * * /var/www/cs50hub/deploy/backup_db.sh

DB_PATH="/var/www/cs50hub/flask-app/instance/cs50.db"
BACKUP_DIR="/var/www/cs50hub/backups"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="${BACKUP_DIR}/cs50_${DATE}.db"

mkdir -p "$BACKUP_DIR"

# Safe backup using sqlite3 (supports WAL mode)
sqlite3 "$DB_PATH" ".backup '${BACKUP_FILE}'"

# Compress to save disk space
gzip "$BACKUP_FILE"

# Keep only last 7 days of backups
find "$BACKUP_DIR" -type f -name "*.db.gz" -mtime +7 -exec rm {} \;

echo "[OK] Backup saved: ${BACKUP_FILE}.gz"
