#!/usr/bin/env python3
"""CS50x KB crawler (free, polite, no login).

Fetches official CS50 sources into _build/raw/ and _build/downloads/ and logs
EVERY discovered URL into _build/manifest.json with status
fetched / failed (+reason) / skipped (+reason).

Usage:  python3 crawl.py            # seed from ../../cs50x-2026-kb/raw + crawl the rest
        python3 crawl.py --no-cdn   # do not fetch anything from cdn.cs50.net (robots.txt: Disallow /)
"""
import hashlib, json, os, re, shutil, sys, time, urllib.parse as up
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import requests
from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
DL = os.path.join(HERE, "downloads")
MANIFEST = os.path.join(HERE, "manifest.json")
SEED_DIR = "/workspace/cs50x-2026-kb"
TZ = ZoneInfo("Asia/Tehran")
UA = "CS50xAnzali-KB-builder/2.0 (non-commercial educational knowledge base; 1 req/s; contact: github.com/sina-nozhati)"
DELAY = 1.0
MAX_ZIP = 60 * 1024 * 1024
NO_CDN = "--no-cdn" in sys.argv

S = requests.Session(); S.headers["User-Agent"] = UA
_last = [0.0]
manifest = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}

def now(): return datetime.now(TZ).isoformat(timespec="seconds")
def save(): json.dump(manifest, open(MANIFEST, "w"), indent=1, sort_keys=True, ensure_ascii=False)
def sha(b): return hashlib.sha256(b).hexdigest()

def local_path(url, base=RAW):
    p = up.urlparse(url)
    path = p.path
    if path.endswith("/") or path == "": path += "index.html"
    return os.path.join(base, p.netloc, path.lstrip("/"))

def record(url, **kw):
    e = manifest.get(url, {})
    if e.get("status") == "fetched" and kw.get("status") != "fetched":
        # keep fetched record; only add discovery info
        for k in ("discovered_from",):
            if k in kw and kw[k] not in e.setdefault("discovered_from_all", []):
                e["discovered_from_all"].append(kw[k])
        return e
    e.update(kw); manifest[url] = e; return e

def polite():
    d = time.time() - _last[0]
    if d < DELAY: time.sleep(DELAY - d)
    _last[0] = time.time()

def get(url, category, discovered_from=None, base=RAW, head_first=False):
    if manifest.get(url, {}).get("status") == "fetched" and os.path.exists(os.path.join(HERE, manifest[url]["file"])):
        return manifest[url]
    try:
        if head_first:
            polite(); h = S.head(url, allow_redirects=True, timeout=30)
            size = int(h.headers.get("content-length", 0) or 0)
            if h.status_code != 200:
                return record(url, status="failed", reason=f"HTTP {h.status_code} on HEAD", category=category, discovered_from=discovered_from, checked_at=now())
            if size > MAX_ZIP:
                return record(url, status="skipped", reason=f"too large ({size} bytes > {MAX_ZIP})", bytes=size, category=category, discovered_from=discovered_from, checked_at=now())
        polite(); r = S.get(url, timeout=120, allow_redirects=True)
    except Exception as ex:
        return record(url, status="failed", reason=f"network error: {ex.__class__.__name__}: {ex}", category=category, discovered_from=discovered_from, checked_at=now())
    if r.status_code != 200:
        return record(url, status="failed", reason=f"HTTP {r.status_code}", http_status=r.status_code, final_url=r.url, category=category, discovered_from=discovered_from, checked_at=now())
    lp = local_path(url, base)
    os.makedirs(os.path.dirname(lp), exist_ok=True)
    open(lp, "wb").write(r.content)
    e = record(url, status="fetched", http_status=200, final_url=r.url, file=os.path.relpath(lp, HERE),
               fetched_at=now(), sha256=sha(r.content), bytes=len(r.content),
               content_type=r.headers.get("content-type", ""), category=category, discovered_from=discovered_from)
    print("GET", r.status_code, url, flush=True)
    return e

# ---------------------------------------------------------------- seeding
def seed():
    old = os.path.join(SEED_DIR, "manifest.json")
    if not os.path.exists(old): return
    om = json.load(open(old))
    for url, e in om.items():
        src = os.path.join(SEED_DIR, e.get("file") or "")
        if e.get("status") != 200 or not os.path.isfile(src) or url in manifest: continue
        lp = local_path(url); os.makedirs(os.path.dirname(lp), exist_ok=True)
        shutil.copyfile(src, lp); b = open(lp, "rb").read()
        fa = datetime.fromisoformat(e["fetched_at"]).astimezone(TZ).isoformat(timespec="seconds")
        manifest[url] = dict(status="fetched", http_status=200, final_url=e.get("final_url", url), file=os.path.relpath(lp, HERE),
                             fetched_at=fa, sha256=sha(b), bytes=len(b), content_type="text/html",
                             category="harvard-archive-2025" if "/x/2025/" in url else "harvard",
                             discovered_from="seeded from /workspace/cs50x-2026-kb (crawl of 2026-10-18)")
    # the 2026 entry URL redirect
    if "https://cs50.harvard.edu/x/2026/" in om:
        manifest.setdefault("https://cs50.harvard.edu/x/2026/", dict(status="skipped", reason="HTTP 302 redirect to canonical https://cs50.harvard.edu/x/ (fetched there)", category="harvard"))
    save()

# ---------------------------------------------------------------- classification
OFFICIAL = {"cs50.harvard.edu", "cdn.cs50.net", "cs50.readthedocs.io", "manual.cs50.io", "cs50.ai", "cs50.dev"}
RTD_PREFIXES = ["/", "/libraries/cs50/", "/style50/", "/submit50/", "/help50/", "/cs50/codespace/", "/style/c/",
                "/cs50.ai/", "/cs50.dev/", "/manual.cs50.io/", "/video.cs50.io/", "/certificates.cs50.io/",
                "/projects/check50/", "/debug50/", "/terminal/"]

def norm(url):
    url, _ = up.urldefrag(url)
    p = up.urlparse(url)
    path = p.path or "/"
    return up.urlunparse((p.scheme, p.netloc.lower(), path, p.params, p.query, ""))

def classify(url):
    """-> (action, category, reason)"""
    p = up.urlparse(url); host = p.netloc.lower(); path = p.path
    if p.scheme not in ("http", "https"): return ("skip", "other", f"non-http scheme ({p.scheme})")
    ext = os.path.splitext(path)[1].lower()
    if host in ("youtu.be", "www.youtube.com", "youtube.com", "video.cs50.io"):
        return ("skip", "video", "video page; URL recorded only (no video download, no YouTube crawling)")
    if host == "cs50.harvard.edu":
        if not path.startswith("/x/"): return ("skip", "harvard-other", "outside CS50x (/x/) scope")
        if re.match(r"^/x/\d{4}/", path): return ("skip", "harvard-archive", "archived prior-year page; out of scope for 2026 KB")
        if ext and ext not in (".html",): return ("skip", "harvard-file", f"file type {ext}")
        return ("fetch", "harvard", None)
    if host == "cdn.cs50.net":
        if NO_CDN: return ("skip", "cdn", "--no-cdn: cdn.cs50.net robots.txt disallows /")
        if ext in (".mp4", ".mp3", ".download", ".mov", ".webm", ".m4a") or path.endswith(".mp4.download"):
            return ("skip", "cdn-media", "video/audio file; URL recorded only")
        if ext == ".pdf": return ("skip", "cdn-pdf", "PDF (slides/source printout); content covered by notes/source zip; not downloaded")
        if ext == ".srt": return ("skip", "cdn-subtitles", "subtitle file (.srt) duplicates the .txt transcript; URL recorded only")
        if ext == ".txt":
            if "/lang/en/" in path: return ("fetch", "cdn-transcript", None)
            return ("skip", "cdn-transcript-other-lang", "non-English transcript; English transcript fetched instead")
        if ext == ".zip": return ("zip", "cdn-zip", None)
        if path.endswith("/"): return ("skip", "cdn-index", "directory listing; the corresponding .zip is downloaded instead")
        if re.search(r"\.(c|h|py|sql|html|css|js|csv|txt)$", path):
            if "/lectures/" in path or "/sections/" in path:
                return ("skip", "cdn-other", "individual lecture/section source file; covered by the source ZIP (or listing fallback)")
            return ("fetch", "cdn-file", None)
        return ("skip", "cdn-other", f"cdn file type {ext or 'unknown'} not needed")
    if host == "cs50.readthedocs.io":
        if ext in (".txt",) or "/_sources/" in path or "/_static/" in path or "/_downloads/" in path:
            return ("skip", "rtd-asset", "Sphinx source/static asset")
        if "/api/" in path: return ("skip", "rtd-other", "Harvard dining/map API docs; not course-relevant")
        if any(path.startswith(px) for px in RTD_PREFIXES[1:]) or path == "/":
            # check50 project: only en/latest
            if path.startswith("/projects/check50/") and not (path.startswith("/projects/check50/en/latest/") or path == "/projects/check50/"):
                return ("skip", "rtd-other", "non-latest check50 doc version")
            return ("fetch", "readthedocs", None)
        return ("skip", "rtd-other", "readthedocs page outside selected course-relevant scope")
    if host == "manual.cs50.io":
        return ("manual", "manual", None)
    if host == "cs50.ai":
        return ("fetch" if path in ("", "/") else "skip", "cs50.ai", None if path in ("", "/") else "login-only application page")
    if host == "cs50.dev":
        return ("fetch" if path in ("", "/") else "skip", "cs50.dev", None if path in ("", "/") else "application page")
    if host == "docs.google.com": return ("skip", "slides", "Google Slides (external app); URL recorded only")
    if host.endswith("cs50.me") or host.endswith("cs50.io") or host.endswith("cs50.edx.org") or host.endswith("cs50.ly"):
        return ("skip", "cs50-app", "CS50 web application / redirector (login or app); URL recorded only")
    return ("skip", "external", "non-official or out-of-scope domain; URL recorded only")

def links_of(entry, url):
    path = os.path.join(HERE, entry["file"])
    s = BeautifulSoup(open(path, "rb").read(), "lxml")
    base = entry.get("final_url") or url
    out = []
    root = s
    # URLs that appear only as text (e.g. `wget https://cdn.cs50.net/...zip` in code blocks)
    for t in re.findall(r"https?://cdn\.cs50\.net/[^\s\"'<>`)]+", s.get_text(" ")):
        out.append(norm(t.rstrip(".,;")))
    for a in root.find_all(["a", "iframe", "source"], href=True) + root.find_all(["iframe", "source"], src=True):
        h = a.get("href") or a.get("src")
        if not h or h.startswith("mailto:") or h.startswith("#") or h.startswith("javascript:"): continue
        out.append(norm(up.urljoin(base, h)))
    return out

MANUAL_EXTRA = """printf strlen strcmp strcasecmp strcpy strncpy strcat strdup toupper tolower isalpha isdigit isalnum isupper islower
isspace ispunct isblank atoi atof atol strtol round roundf pow sqrt fabs floor ceil abs rand srand drand48 srand48 time exit malloc calloc
realloc free fopen fclose fread fwrite fprintf fscanf fgetc fputc fgets fputs feof ferror sprintf snprintf scanf getchar putchar puts
memcpy memset strtok strchr strstr qsort sizeof assert sleep usleep""".split()

def crawl_manual(disc):
    idx = get("https://manual.cs50.io/", "manual", disc)
    names = []
    if idx.get("status") == "fetched":
        s = BeautifulSoup(open(os.path.join(HERE, idx["file"]), "rb").read(), "lxml")
        h = s.find(id="cs50.h")
        ul = h.find_next("ul") if h else None
        if ul: names = [a["href"] for a in ul.find_all("a", href=True)]
        allhref = {a["href"].split("/")[-1]: a["href"] for a in s.find_all("a", href=True) if re.match(r"^\d/", a["href"])}
        for n in MANUAL_EXTRA:
            if n in allhref: names.append(allhref[n])
            else: record(f"https://manual.cs50.io/3/{n}", status="skipped", reason="not listed in manual.cs50.io index", category="manual", discovered_from="KB curated function list")
    seen = set()
    for h in names:
        u = "https://manual.cs50.io/" + h.lstrip("/")
        if u in seen: continue
        seen.add(u); get(u, "manual", "https://manual.cs50.io/ (cs50.h section or curated list of functions used in CS50x)")

def main():
    seed()
    queue = ["https://cs50.harvard.edu/x/"] + [u for u, e in manifest.items() if e.get("status") == "fetched" and e.get("category") == "harvard"]
    queue += ["https://cs50.readthedocs.io/", "https://cs50.readthedocs.io/libraries/cs50/c/", "https://cs50.readthedocs.io/libraries/cs50/python/",
              "https://cs50.readthedocs.io/projects/check50/en/latest/", "https://cs50.readthedocs.io/style/c/", "https://cs50.readthedocs.io/cs50.ai/",
              "https://cs50.readthedocs.io/cs50.dev/", "https://cs50.ai/"]
    seen = set()
    zips = []
    while queue:
        url = norm(queue.pop(0))
        if url in seen: continue
        seen.add(url)
        action, cat, reason = classify(url)
        if action != "fetch":
            if action == "zip": zips.append(url)
            continue
        e = get(url, cat, manifest.get(url, {}).get("discovered_from"))
        if e.get("status") != "fetched" or "html" not in (e.get("content_type") or "text/html"): continue
        if cat in ("harvard", "readthedocs") and "html" in (e.get("content_type") or "text/html"):
            for l in links_of(e, url):
                if l in seen: continue
                a2, c2, r2 = classify(l)
                if a2 == "skip":
                    record(l, status="skipped", reason=r2, category=c2, discovered_from=url)
                elif a2 == "manual":
                    record(l, status=manifest.get(l, {}).get("status", "skipped"), reason=manifest.get(l, {}).get("reason", "manual page linked; only cs50.h + curated function pages are fetched (see manual category)"), category="manual", discovered_from=url)
                else:
                    manifest.setdefault(l, {}).setdefault("discovered_from", url)
                    if a2 == "fetch" and c2 == "cdn-transcript": queue.insert(0, l)
                    else: queue.append(l)
        if len(seen) % 25 == 0: save()
    save()
    for z in sorted(set(zips)):
        get(z, "cdn-zip", manifest.get(z, {}).get("discovered_from"), base=DL, head_first=True)
    save()
    crawl_manual("https://cs50.harvard.edu/x/ (nav: Manual Pages)")
    save()
    c = {}
    for e in manifest.values(): c[e.get("status")] = c.get(e.get("status"), 0) + 1
    print("DONE", c)

if __name__ == "__main__":
    main()
