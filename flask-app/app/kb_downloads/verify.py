"""Verify one week's exports: Persian text fidelity of each PDF, internal links/anchors, external links (HTTP), source-code ZIP."""
from __future__ import annotations

import concurrent.futures as cf
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from typing import Any

from .verify_pdf import check as check_pdf


def verify_week_exports(out_dir: str, online: bool = False) -> dict[str, Any]:
    """Verify generated files for one week."""
    out = os.path.abspath(out_dir)
    res: dict[str, Any] = {
        "pdf_text": {},
        "internal_links": {},
        "external": {},
        "code": {},
    }

    if not os.path.isdir(out):
        res["error"] = f"Directory not found: {out}"
        return res

    htmls = sorted(f for f in os.listdir(out) if f.endswith(".html"))
    ids: dict[str, set[str]] = {
        f: set(re.findall(r'\sid="([^"]+)"', open(os.path.join(out, f), encoding="utf-8").read()))
        for f in htmls
    }

    ext: set[str] = set()
    bad: list[tuple[str, str]] = []

    for f in htmls:
        t = open(os.path.join(out, f), encoding="utf-8").read()
        t = re.sub(r"<pre.*?</pre>|<code.*?</code>", "", t, flags=re.S)
        for h in re.findall(r'href="([^"]+)"', t):
            if h.startswith(("http://", "https://")):
                ext.add(h.replace("&amp;", "&"))
                continue
            fn, _, frag = h.partition("#")
            fn = fn or f
            if not os.path.exists(os.path.join(out, fn)):
                bad.append((f, h))
                continue
            if frag and fn.endswith(".html") and frag not in ids.get(fn, set()):
                bad.append((f, h))

        if re.search(r'(src|href)="(?!data:|#|https?:|mailto:)[^"]*\.(css|js|woff2?|png|jpe?g)"', t):
            bad.append((f, "non-inline asset"))

    res["internal_links"] = {"checked_files": len(htmls), "broken": bad}

    for f in sorted(os.listdir(out)):
        if f.endswith(".pdf"):
            html_sibling = f[:-4] + ".html"
            html_p = os.path.join(out, html_sibling)
            pdf_p = os.path.join(out, f)
            if os.path.exists(html_p):
                res["pdf_text"][f] = check_pdf(html_p, pdf_p)

    def head(u: str) -> int | str:
        try:
            r = urllib.request.urlopen(
                urllib.request.Request(u, method="GET", headers={"User-Agent": "Mozilla/5.0 cs50x-anzali-linkcheck"}),
                timeout=10,
            )
            return r.status
        except urllib.error.HTTPError as e:
            return e.code
        except Exception as e:
            return type(e).__name__

    if online and ext:
        with cf.ThreadPoolExecutor(8) as ex:
            st = dict(zip(sorted(ext), ex.map(head, sorted(ext))))
        res["external"] = {
            "total": len(st),
            "ok": sum(1 for v in st.values() if v == 200),
            "not_ok": {k: v for k, v in st.items() if v != 200},
        }

    z = [f for f in os.listdir(out) if f.endswith("source-code.zip")]
    if z:
        with tempfile.TemporaryDirectory() as d:
            zipfile.ZipFile(os.path.join(out, z[0])).extractall(d)
            for root, _, fs in os.walk(d):
                for fn in sorted(fs):
                    p = os.path.join(root, fn)
                    if fn.endswith(".c"):
                        cc = "clang" if shutil.which("clang") else "gcc" if shutil.which("gcc") else None
                        if cc:
                            r = subprocess.run([cc, "-fsyntax-only", "-Wall", p], capture_output=True, text=True)
                            res["code"][fn] = "ok" if r.returncode == 0 else ("needs cs50.h" if "cs50.h" in r.stderr else r.stderr.strip()[:200])
                        else:
                            res["code"][fn] = "compiler not found (skipped)"
                    elif fn.endswith(".py"):
                        r = subprocess.run([sys.executable, "-m", "py_compile", p], capture_output=True, text=True)
                        res["code"][fn] = "ok (syntax)" if r.returncode == 0 else r.stderr.strip()[:200]

    return res


def main():
    if len(sys.argv) < 2:
        print("Usage: verify.py OUT_DIR [--offline]")
        sys.exit(1)
    out = sys.argv[1]
    online = "--offline" not in sys.argv
    res = verify_week_exports(out, online=online)
    print(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
