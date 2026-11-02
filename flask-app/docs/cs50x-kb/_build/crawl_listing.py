#!/usr/bin/env python3
"""Fallback for source-code zips that exceed the size cap (e.g. lecture 9 src9.zip, 140 MB):
walk the cdn.cs50.net directory listing (Index link on the week page) and fetch only small text files."""
import os, re, sys, urllib.parse as up
from bs4 import BeautifulSoup
import crawl
TEXT = re.compile(r"\.(c|h|py|sql|html|css|js|txt|md|json|csv|toml|cfg|ini|jinja|j2)$|(^|/)(Makefile|requirements\.txt)$", re.I)
MAXF = 100 * 1024
ROOTS = sys.argv[1:] or ["https://cdn.cs50.net/2025/fall/lectures/9/src9/"]
inv = []
def walk(url, root):
    e = crawl.get(url, "cdn-listing", root)
    if e.get("status") != "fetched": return
    s = BeautifulSoup(open(os.path.join(crawl.HERE, e["file"]), "rb").read(), "lxml")
    for tr in s.find_all("tr"):
        a = tr.find("a", href=True)
        if not a or a["href"].startswith("..") or a["href"].startswith("/"): continue
        u = up.urldefrag(up.urljoin(url, a["href"]))[0]
        if "?" in u or not u.startswith(url) or u == url: continue
        if u.endswith("/"): walk(u, root); continue
        tds = [td.get_text(strip=True) for td in tr.find_all("td")]
        size = None
        for td in tr.find_all("td"):
            for k, v in td.attrs.items():
                if k.lower() == "data-size":
                    try: size = int(v)
                    except: pass
        rel = u[len(root):]
        if TEXT.search(rel) and (size is None or size <= MAXF):
            crawl.get(u, "cdn-listing-file", url)
        else:
            crawl.record(u, status="skipped", reason=f"inventory only (binary or > {MAXF} bytes)", bytes=size, category="cdn-listing-file", discovered_from=url)
for r in ROOTS: walk(r, r)
crawl.save()
