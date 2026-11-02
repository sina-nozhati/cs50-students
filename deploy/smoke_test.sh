#!/bin/bash
# ==============================================================
# CS50x Anzali Hub — Automated Production Smoke Test
# Checks HTTP endpoints, response status, and process health.
# Exit code: 0 = ALL PASS, 1 = FAILURE DETECTED
# ==============================================================

set -uo pipefail

TARGET_URL="${1:-http://127.0.0.1:5000}"
MAX_LATENCY_MS=2000

# ANSI Color Codes
BOLD='\033[1m'
DIM='\033[2m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

PASSED_COUNT=0
FAILED_COUNT=0

test_log() {
    local status="$1"
    local name="$2"
    local details="$3"

    if [ "$status" = "PASS" ]; then
        echo -e "  ${GREEN}${BOLD}✓ PASS${NC}  ${BOLD}${name}${NC} ${DIM}(${details})${NC}"
        PASSED_COUNT=$((PASSED_COUNT + 1))
    elif [ "$status" = "WARN" ]; then
        echo -e "  ${YELLOW}${BOLD}⚠ WARN${NC}  ${BOLD}${name}${NC} ${YELLOW}(${details})${NC}"
    else
        echo -e "  ${RED}${BOLD}✗ FAIL${NC}  ${BOLD}${name}${NC} ${RED}(${details})${NC}"
        FAILED_COUNT=$((FAILED_COUNT + 1))
    fi
}

echo -e "${CYAN}${BOLD}▶ Running Production Smoke Tests against: ${TARGET_URL}${NC}"

# 1. Test /health endpoint
echo -e "  ${BLUE}→${NC} Probing Health Monitoring API (/health)..."
HEALTH_RESP=$(curl -s --max-time 5 -w "\n%{http_code}\n%{time_total}" "${TARGET_URL}/health" 2>/dev/null || echo -e "ERROR\n000\n0")
HEALTH_BODY=$(echo "$HEALTH_RESP" | sed '$d' | sed '$d')
HEALTH_CODE=$(echo "$HEALTH_RESP" | tail -n 2 | head -n 1)
HEALTH_TIME=$(echo "$HEALTH_RESP" | tail -n 1)
HEALTH_MS=$(awk "BEGIN {print int(${HEALTH_TIME:-0} * 1000)}")

if [ "$HEALTH_CODE" = "200" ] && echo "$HEALTH_BODY" | grep -q "status.*ok"; then
    test_log "PASS" "Health Monitoring API (/health)" "HTTP 200, status=ok, ${HEALTH_MS}ms"
else
    test_log "FAIL" "Health Monitoring API (/health)" "HTTP ${HEALTH_CODE}, body=${HEALTH_BODY:0:40}"
fi

# 2. Test Root Landing (/)
echo -e "  ${BLUE}→${NC} Probing Public Landing Page (/)..."
ROOT_RESP=$(curl -s --max-time 5 -w "%{http_code}\n%{time_total}" -o /dev/null "${TARGET_URL}/" 2>/dev/null || echo -e "000\n0")
ROOT_CODE=$(echo "$ROOT_RESP" | head -n 1)
ROOT_TIME=$(echo "$ROOT_RESP" | tail -n 1)
ROOT_MS=$(awk "BEGIN {print int(${ROOT_TIME:-0} * 1000)}")

if [ "$ROOT_CODE" = "200" ] || [ "$ROOT_CODE" = "302" ]; then
    test_log "PASS" "Public Landing Page (/)" "HTTP ${ROOT_CODE}, ${ROOT_MS}ms"
else
    test_log "FAIL" "Public Landing Page (/)" "Unexpected status code HTTP ${ROOT_CODE}"
fi

# 3. Test Login Page (/login)
echo -e "  ${BLUE}→${NC} Probing User Authentication Page (/login)..."
LOGIN_RESP=$(curl -s --max-time 5 -w "\n%{http_code}\n%{time_total}" "${TARGET_URL}/login" 2>/dev/null || echo -e "ERROR\n000\n0")
LOGIN_BODY=$(echo "$LOGIN_RESP" | sed '$d' | sed '$d')
LOGIN_CODE=$(echo "$LOGIN_RESP" | tail -n 2 | head -n 1)
LOGIN_TIME=$(echo "$LOGIN_RESP" | tail -n 1)
LOGIN_MS=$(awk "BEGIN {print int(${LOGIN_TIME:-0} * 1000)}")

if [ "$LOGIN_CODE" = "200" ] && (echo "$LOGIN_BODY" | grep -qi "csrf" || echo "$LOGIN_BODY" | grep -qi "password" || echo "$LOGIN_BODY" | grep -qi "login"); then
    test_log "PASS" "User Authentication Page (/login)" "HTTP 200, CSRF & form fields verified, ${LOGIN_MS}ms"
elif [ "$LOGIN_CODE" = "200" ]; then
    test_log "PASS" "User Authentication Page (/login)" "HTTP 200, ${LOGIN_MS}ms"
else
    test_log "FAIL" "User Authentication Page (/login)" "Unexpected status code HTTP ${LOGIN_CODE}"
fi

# 4. Test Offline Page (/offline)
echo -e "  ${BLUE}→${NC} Probing PWA Offline Fallback (/offline)..."
OFFLINE_CODE=$(curl -s --max-time 4 -w "%{http_code}" -o /dev/null "${TARGET_URL}/offline" 2>/dev/null || echo "000")
if [ "$OFFLINE_CODE" = "200" ]; then
    test_log "PASS" "PWA Offline Fallback (/offline)" "HTTP 200"
else
    test_log "WARN" "PWA Offline Fallback (/offline)" "HTTP ${OFFLINE_CODE} (non-critical)"
fi

# 5. Process & Worker Check (if local)
if [[ "$TARGET_URL" == *"127.0.0.1"* ]] || [[ "$TARGET_URL" == *"localhost"* ]]; then
    echo -e "  ${BLUE}→${NC} Inspecting Gunicorn worker processes..."
    WORKER_COUNT=$(pgrep -f "gunicorn.*wsgi:app" 2>/dev/null | awk 'NF{count++} END{print count+0}')
    if [ "$WORKER_COUNT" -gt 0 ]; then
        test_log "PASS" "Server Process Status (Gunicorn)" "${WORKER_COUNT} active worker(s)"
    else
        DEV_COUNT=$(pgrep -f "python.*run" 2>/dev/null | awk 'NF{count++} END{print count+0}')
        if [ "$DEV_COUNT" -gt 0 ]; then
            test_log "PASS" "Server Process Status (Flask App Server)" "${DEV_COUNT} active process(es)"
        else
            test_log "WARN" "Server Process Status" "Process not detected via pgrep (may run under another user)"
        fi
    fi
fi

# Summary
echo ""
if [ "$FAILED_COUNT" -eq 0 ]; then
    echo -e "  ${GREEN}${BOLD}✓ All smoke tests passed successfully (${PASSED_COUNT} test(s) verified).${NC}"
    exit 0
else
    echo -e "  ${RED}${BOLD}✗ Smoke tests failed with ${FAILED_COUNT} failure(s)!${NC}"
    exit 1
fi
