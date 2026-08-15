#!/usr/bin/env python3
"""
GitHub Webhook Listener for CS50x Anzali Auto-Deploy.

When you push to GitHub, GitHub sends a POST request to this service,
which then runs deploy.sh to update the live site.

GitHub setup:
  1. Repo Settings > Webhooks > Add webhook
  2. Payload URL: http://YOUR_SERVER_IP:9000/webhook
  3. Content type: application/json
  4. Secret: (same value as WEBHOOK_SECRET env var)
  5. Events: Just the push event
"""

import hashlib
import hmac
import os
import subprocess
import logging
from flask import Flask, request, abort

app = Flask(__name__)

WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "cs50-anzali-webhook-secret")
DEPLOY_SCRIPT = "/var/www/cs50hub/deploy/deploy.sh"

logging.basicConfig(
    filename="/var/log/cs50hub-webhook.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def verify_signature(payload, signature):
    """Verify the GitHub webhook signature."""
    if not signature:
        return False
    sha_name, signature_hash = signature.split("=")
    mac = hmac.new(
        WEBHOOK_SECRET.encode("utf-8"),
        msg=payload,
        digestmod=hashlib.sha256
    )
    return hmac.compare_digest(mac.hexdigest(), signature_hash)


@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers.get("X-Hub-Signature-256")

    if not verify_signature(request.data, signature):
        logging.warning("Invalid signature received")
        abort(403)

    event = request.headers.get("X-GitHub-Event", "ping")

    if event == "ping":
        logging.info("Ping received from GitHub")
        return "pong", 200

    if event == "push":
        payload = request.get_json()
        ref = payload.get("ref", "")

        if ref == "refs/heads/main":
            logging.info("Push to main detected — deploying...")
            result = subprocess.run(
                ["bash", DEPLOY_SCRIPT],
                capture_output=True,
                text=True,
                timeout=120
            )
            if result.returncode == 0:
                logging.info("Deploy successful")
                return "Deployed", 200
            else:
                logging.error(f"Deploy failed: {result.stderr}")
                return "Deploy failed", 500

    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
