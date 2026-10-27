#!/usr/bin/env python3
"""Spot-check KB docs against the LIVE pages (polite: 1 req/s). Writes _build/spotcheck.json."""
import difflib, json, os, random, re, sys, time
from datetime import datetime
from zoneinfo import ZoneInfo
import requests, yaml
from bs4 import BeautifulSoup
B = os.path.dirname(os.path.abspath(__file__)); KB = os.path.dirname(B)
UA = "CS50xAnzali-KB-builder/2.0 (spot-check; non-commercial educational KB)"
M = json.load(open(os.path.join(B, "manifest.json")))
DOCS = sys.argv[1:] or ["weeks/week-03-algorithms/psets/tideman.md", "weeks/week-04-memory/lecture.md", "weeks/week-04-memory/shorts/pointers.md",
        "course/honesty.md", "final-project/README.md", "reference/manual/get_string.md", "tools/submit50.md", "weeks/week-07-sql/psets/fiftyville.md"]
def norm(t): return re.sub(r"\s+", " ", t).strip()
def main_text(html, url):
    s = BeautifulSoup(html, "lxml")
    m = s.select_one("main") or s.select_one("div[role=main]") or s.body
    for x in m.select("script, style"): x.decompose()
    return norm(m.get_text(" "))
out = []
random.seed(50)
for p in DOCS:
    t = open(os.path.join(KB, p), encoding="utf-8").read()
    fm = yaml.safe_load(t.split("\n---\n", 1)[0][4:])
    url = fm["source_urls"][0]
    time.sleep(1.0)
    r = requests.get(url, headers={"User-Agent": UA}, timeout=60)
    live = main_text(r.content, url) if "text/html" in r.headers.get("content-type", "") else norm(r.text)
    rawf = os.path.join(B, M[url]["file"])
    rb = open(rawf, "rb").read()
    raw = main_text(rb, url) if rb.lstrip()[:1] == b"<" else norm(rb.decode("utf-8", "replace"))
    ratio = difflib.SequenceMatcher(None, raw.split(), live.split(), autojunk=False).ratio() if len(raw) < 400000 else None
    off = t.split("## 2. OFFICIAL CONTENT", 1)[1].split("## 3. Learning", 1)[0]
    sents = [norm(re.sub(r"[*_`>\[\]]|\(http[^)]*\)|<a id=[^>]*></a>", " ", x)) for x in re.split(r"(?<=[.!?])\s+", off)]
    sents = [x for x in sents if 60 < len(x) < 300 and "Source:" not in x and "CS50x 2026 ©" not in x and "Extracted for non-commercial" not in x]
    sample = random.sample(sents, min(8, len(sents)))
    hay = live
    if fm.get("type") == "short" and len(fm["source_urls"]) > 1:   # shorts: official text = transcript on cdn.cs50.net
        time.sleep(1.0); hay = norm(requests.get(fm["source_urls"][1], headers={"User-Agent": UA}, timeout=60).text)
    found = sum(1 for x in sample if norm(x)[:50] in hay or norm(x)[-50:] in hay)
    out.append(dict(doc=p, url=url, http=r.status_code, raw_vs_live_word_similarity=round(ratio, 4) if ratio is not None else None,
                    identical_main_text=(raw == live), sampled_sentences=len(sample), sampled_sentences_found_live=found,
                    checked_at=datetime.now(ZoneInfo("Asia/Tehran")).isoformat(timespec="seconds")))
    print(out[-1], flush=True)
json.dump(out, open(os.path.join(B, "spotcheck.json"), "w"), indent=1)
