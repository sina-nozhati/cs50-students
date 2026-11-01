#!/usr/bin/env python3
"""CS50x Anzali week exports generator module.
Reads only the KB package; writes self-contained offline HTML,
PDF (via Chromium headless or WeasyPrint), a source-code ZIP, and a slides link card.
Usage:
    from app.kb_downloads.generate import build_week
    manifest = build_week(kb_dir, week_slug, out_dir, pdf=True, engine="chrome")
Deterministic: fixed timestamps come from the package data; ZIP entries use a fixed date.
"""
from __future__ import annotations

import base64
import hashlib
import html
import io
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path
from typing import Any

import jinja2
import markdown
try:
    from pygments.formatters import HtmlFormatter
    PYGMENTS_CSS = HtmlFormatter(style="friendly").get_style_defs(".hl")
except Exception:
    HtmlFormatter = None
    PYGMENTS_CSS = """

GEN_VERSION = "0.2.0"
HERE = os.path.dirname(os.path.abspath(__file__))
FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
CODE_EXT = {
    "c": "c",
    "py": "py",
    "python": "py",
    "sql": "sql",
    "html": "html",
    "css": "css",
    "js": "js",
    "javascript": "js",
    "bash": "sh",
    "sh": "sh",
}


def fa(s: Any) -> str:
    return str(s).translate(FA_DIGITS)


FA_ALPHA = "آاأإبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیيكةۀ"
FA_MONTHS = [
    "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
    "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند",
]


def jalali(iso: str) -> str:
    """ISO date -> '۱۰ آبان ۱۴۰۵' (Persian calendar, words for month: no digit-order ambiguity in RTL)."""
    gy, gm, gd = (int(x) for x in iso[:10].split("-"))
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    gy2 = gy + 1 if gm > 2 else gy
    days = 355666 + 365 * gy + (gy2 + 3) // 4 - (gy2 + 99) // 100 + (gy2 + 399) // 400 + gd + g_d_m[gm - 1]
    jy = -1595 + 33 * (days // 12053)
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461
    if days > 365:
        jy += (days - 1) // 365
        days = (days - 1) % 365
    jm, jd = (1 + days // 31, 1 + days % 31) if days < 186 else (7 + (days - 186) // 30, 1 + (days - 186) % 30)
    return fa(f"{jd} {FA_MONTHS[jm - 1]} {jy}")


def fa_key(s: str) -> list[int]:
    """Persian alphabetical order (پ چ ژ گ in place), ZWNJ/space ignored for comparison."""
    t = s.replace("\u200c", "").replace(" ", "")
    return [FA_ALPHA.find(ch) if ch in FA_ALPHA else 100 + ord(ch) for ch in t]


def front(path: str) -> tuple[dict[str, str], str]:
    t = open(path, encoding="utf-8").read()
    meta, body = {}, t
    if t.startswith("---\n"):
        end = t.index("\n---\n", 4)
        head, body = t[4:end], t[end + 5:]
        for line in head.splitlines():
            m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
            if m:
                meta[m.group(1)] = m.group(2).strip().strip("'\"")
    return meta, body


class Week:
    def __init__(self, kb: str, slug: str):
        self.kb, self.slug, self.dir = kb, slug, os.path.join(kb, "weeks", slug)
        self.overview_meta, self.overview = front(os.path.join(self.dir, "overview.fa.md"))
        self.num = self.overview_meta.get("week", "")
        h1 = re.search(r"^# (.+)$", self.overview, re.M)
        self.title = h1.group(1).strip() if h1 else slug
        self.title_short = re.split(r"\s+[—-]\s+", self.title)[0]
        self.official_url = self.overview_meta.get("source_url", "https://cs50.harvard.edu/x/")
        self.sources = json.load(open(os.path.join(self.dir, "sources.json"), encoding="utf-8"))
        nd = os.path.join(self.dir, "notes")
        self.notes = [(front(os.path.join(nd, f)), f) for f in sorted(os.listdir(nd)) if f.endswith(".fa.md")]
        self.notes.sort(key=lambda x: int(x[0][0].get("order", 999)))
        sp = os.path.join(self.dir, "summary.fa.md")
        self.summary = front(sp) if os.path.exists(sp) else None
        pd = os.path.join(self.dir, "problem-sets")
        self.psets = []
        if os.path.isdir(pd):
            for f in sorted(os.listdir(pd)):
                if f.endswith(".fa.md"):
                    j = os.path.join(pd, f[:-6] + ".json")
                    self.psets.append((front(os.path.join(pd, f)), json.load(open(j, encoding="utf-8")) if os.path.exists(j) else {}))
        fcp = os.path.join(self.dir, "flashcards.json")
        self.flashcards = json.load(open(fcp, encoding="utf-8"))["cards"] if os.path.exists(fcp) else []
        stamps = [self.sources.get("generated_at", "")] + [m.get("verified_at", "") for (m, _), _f in self.notes]
        self.built = max(s for s in stamps if s) or "2026-01-01T00:00:00+03:30"

    def src(self, sid: str) -> dict[str, Any] | None:
        return next((s for s in self.sources.get("sources", []) if s["id"] == sid), None)

    def src_by_type(self, t: str) -> list[dict[str, Any]]:
        return [s for s in self.sources.get("sources", []) if s.get("source_type") == t]


LATIN_RUN = re.compile(r"(?<![\w`])([A-Za-z][A-Za-z0-9 .,'’:/+\-–!?&]*[A-Za-z0-9.!?)]?)")


def bidi(h: str) -> str:
    """Isolate Latin runs in Persian prose (<bdi>) so mixed RTL/LTR lines keep their order when they wrap. Skips pre/code/attributes."""
    parts = re.split(r"(<pre.*?</pre>|<code.*?</code>|<[^>]+>)", h, flags=re.S)
    for i in range(0, len(parts), 2):
        t = parts[i]
        if re.search(r"[\u0600-\u06FF]", t) or (i and parts[i - 1].startswith("<td")):
            parts[i] = re.sub(
                r"\(([A-Za-z][^()\u0600-\u06FF]*)\)",
                lambda m: f'(<bdi{" class=nw" if len(m.group(1)) <= 32 else ""}>{m.group(1)}</bdi>)',
                t,
            )
    return "".join(parts)


def inline(t: str) -> str:
    """Flashcard / glossary text: escape, then `code`."""
    return bidi(re.sub(r"`([^`]+)`", r'<code dir="ltr">\1</code>', html.escape(t)))


class Renderer:
    def __init__(self, week: Week, cache: str):
        self.w, self.cache = week, cache
        self.doc_targets: dict[str, str] = {}
        self.warnings: list[str] = []
        self.md = markdown.Markdown(
            extensions=["tables", "fenced_code", "codehilite", "sane_lists"],
            extension_configs={"codehilite": {"guess_lang": False, "css_class": "hl"}},
        )

    def image(self, url: str, alt: str) -> str:
        try:
            os.makedirs(self.cache, exist_ok=True)
            ext = os.path.splitext(url)[1] or ".png"
            p = os.path.join(self.cache, hashlib.sha256(url.encode()).hexdigest()[:16] + ext)
            if not os.path.exists(p):
                req = urllib.request.Request(url, headers={"User-Agent": "cs50x-anzali-exports"})
                open(p, "wb").write(urllib.request.urlopen(req, timeout=15).read())
            mime = "image/png" if p.endswith(".png") else "image/jpeg" if p.endswith((".jpg", ".jpeg")) else "image/gif"
            data = base64.b64encode(open(p, "rb").read()).decode()
            return f'<figure><img src="data:{mime};base64,{data}" alt="{html.escape(alt)}"><figcaption>تصویر از <a href="{html.escape(url)}">درس‌نامهٔ رسمی CS50x</a> (CC BY-NC-SA 4.0)</figcaption></figure>'
        except Exception as e:
            # Fallback when offline or download fails: link to official image
            self.warnings.append(f"Image download failed for {url}: {e}")
            return f'<figure><p class="meta"><a href="{html.escape(url)}" target="_blank" rel="noopener">{html.escape(alt or "تصویر درس‌نامهٔ رسمی CS50x")}</a></p><figcaption>تصویر از <a href="{html.escape(url)}">درس‌نامهٔ رسمی CS50x</a> (CC BY-NC-SA 4.0)</figcaption></figure>'

    def render(self, body: str, anchor_prefix: str) -> str:
        body = re.sub(r"^# .+\n", "", body.lstrip("\n"), count=1)

        def link(m: re.Match) -> str:
            text, target = m.group(1), m.group(2)
            if target.startswith("/kb/d/"):
                doc = target[6:].split("#")[0]
                href = self.doc_targets.get(doc)
                return f"[{text}]({href})" if href else text
            return m.group(0)

        body = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)", link, body)
        imgs: list[str] = []

        def img(m: re.Match) -> str:
            imgs.append(self.image(m.group(2), m.group(1)))
            return f"\n\nIMGPLACEHOLDER{len(imgs) - 1}\n\n"

        body = re.sub(r'!\[([^\]]*)\]\((\S+?)(?:\s+"[^"]*")?\)', img, body)
        self.md.reset()
        out = self.md.convert(body)
        for i, tag in enumerate(imgs):
            out = out.replace(f"<p>IMGPLACEHOLDER{i}</p>", tag)
        n = [0]

        def hid(m: re.Match) -> str:
            n[0] += 1
            return f'<{m.group(1)} id="{anchor_prefix}-s{n[0]}">'

        out = re.sub(r"<(h[23])>", hid, out)

        def block(m: re.Match) -> str:
            cls = m.group(1)
            lang = re.search(r"language-(\w+)", cls)
            lab = lang.group(1) if lang else ""
            return f'<div class="codeblock">{"<span class=lang>" + lab + "</span>" if lab and lab != "text" else ""}<div class="{cls}"><pre dir="ltr"'

        out = re.sub(r'<div class="(hl[^"]*)"><pre', block, out)
        out = out.replace("</pre></div>", "</pre></div></div>")
        out = re.sub(r"<code>", '<code dir="ltr">', out)
        return bidi(out)

    def headings(self, html_: str) -> list[tuple[str, str]]:
        return re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html_)


def find_chrome() -> str | None:
    """Find Chromium / Google Chrome binary on system."""
    env_c = os.environ.get("CHROME")
    if env_c and (os.path.isfile(env_c) or shutil.which(env_c)):
        return env_c
    for cmd in ["google-chrome", "chromium", "chromium-browser", "chrome"]:
        p = shutil.which(cmd)
        if p:
            return p
    # Standard Windows paths
    for win_path in [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]:
        if os.path.isfile(win_path):
            return win_path
    return None


def count_pdf_pages(pdf_path: str) -> int:
    """Reliably count PDF pages without hard external C library dependencies."""
    try:
        import pymupdf
        d = pymupdf.open(pdf_path)
        cnt = d.page_count
        d.close()
        return cnt
    except ImportError:
        pass
    try:
        with open(pdf_path, "rb") as f:
            data = f.read()
        matches = re.findall(rb"/Type\s*/Page\b", data)
        return max(1, len(matches))
    except Exception:
        return 1


def write_pdf(page: str, html_path: str, pdf_path: str, built: str, title: str, engine: str = "chrome") -> dict[str, Any] | None:
    """Generate PDF from HTML.
    Supports Chromium print (default) with optional PyMuPDF post-processing, or WeasyPrint fallback.
    Returns dict with bytes, pages, engine, or None if skipped/unavailable.
    """
    chrome_bin = find_chrome()
    if engine == "weasy":
        try:
            from weasyprint import HTML
            doc = HTML(string=page, base_url=os.path.dirname(html_path)).render()
            doc.write_pdf(pdf_path, pdf_identifier=hashlib.md5(page.encode()).hexdigest().encode())
            n = count_pdf_pages(pdf_path)
            return {"bytes": os.path.getsize(pdf_path), "pages": n, "engine": "weasy"}
        except Exception:
            return None
    elif chrome_bin:
        abs_pdf = os.path.abspath(pdf_path)
        abs_tmp = abs_pdf + ".tmp"
        abs_html = os.path.abspath(html_path).replace("\\", "/")
        file_url = "file:///" + abs_html.lstrip("/")
        try:
            if os.path.exists(abs_tmp):
                try: os.remove(abs_tmp)
                except Exception: pass

            subprocess.run([
                chrome_bin, "--headless=new", "--no-sandbox", "--disable-gpu",
                "--no-pdf-header-footer", "--disable-extensions",
                f"--print-to-pdf={abs_tmp}", file_url
            ], check=True, capture_output=True, timeout=180)

            try:
                import pymupdf
                d = pymupdf.open(abs_tmp)
                base = "file:///" + os.path.abspath(os.path.dirname(html_path)).replace("\\", "/").lstrip("/") + "/"
                for pg in d:
                    for ln in pg.get_links():
                        u = ln.get("uri") or ln.get("file") or ""
                        if u.startswith("file://") or u.startswith("/"):
                            u = u if u.startswith("file://") else "file://" + u
                            tgt = u[len(base):].split("#")[0] if u.startswith(base) else ""
                            pg.delete_link(ln)
                            if tgt.endswith(".html") and tgt != os.path.basename(html_path):
                                pg.insert_link({"kind": pymupdf.LINK_GOTOR, "from": ln["from"], "file": tgt[:-5] + ".pdf", "page": 0})
                stamp = "D:" + re.sub(r"[-:T]", "", built[:19]) + "+03'30'"
                d.set_metadata({
                    "title": title, "author": "CS50x Anzali (unofficial)",
                    "subject": "CS50x 2026, CC BY-NC-SA 4.0", "creator": "cs50x-anzali-exports " + GEN_VERSION,
                    "producer": "Chromium/Skia + PyMuPDF", "creationDate": stamp, "modDate": stamp,
                    "keywords": "", "trapped": ""
                })
                d.save(abs_pdf, garbage=4, deflate=True, no_new_id=True)
                d.close()
                if os.path.exists(abs_tmp):
                    os.remove(abs_tmp)
                raw = open(abs_pdf, "rb").read()
                fid = hashlib.md5(page.encode()).hexdigest().upper().encode()
                raw = re.sub(rb"/ID\s*\[\s*<[0-9A-Fa-f]+>\s*<[0-9A-Fa-f]+>\s*\]", b"/ID [<" + fid + b"> <" + fid + b">]", raw)
                ids: dict[bytes, int] = {}
                raw = re.sub(rb"\(node(\d{8})\)", lambda m: b"(node%08d)" % ids.setdefault(m.group(1), len(ids) + 1), raw)
                open(abs_pdf, "wb").write(raw)
                n = count_pdf_pages(abs_pdf)
            except Exception:
                # If pymupdf is not available or post-processing fails, keep Chromium's output directly
                if os.path.exists(abs_pdf):
                    os.remove(abs_pdf)
                os.rename(abs_tmp, abs_pdf)
                n = count_pdf_pages(abs_pdf)

            return {"bytes": os.path.getsize(abs_pdf), "pages": n, "engine": "chrome"}
        except Exception:
            if os.path.exists(abs_tmp):
                try: os.remove(abs_tmp)
                except Exception: pass
            return None
    return None


def zipdet(path: str, files: dict[str, str | bytes]) -> None:
    """Create a deterministic ZIP archive with fixed modification timestamps."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in sorted(files.items()):
            zi = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, data if isinstance(data, bytes) else data.encode("utf-8"))
    open(path, "wb").write(buf.getvalue())


def build_week(
    kb_dir: str | Path,
    week_slug: str,
    out_dir: str | Path,
    pdf: bool = True,
    engine: str = "chrome",
    cache_dir: str | Path | None = None,
) -> dict[str, Any]:
    """Build all export downloads for a single week from the KB package.
    Args:
        kb_dir: Root directory of KB containing manifest.json, weeks/, etc.
        week_slug: Slug of the week, e.g. 'week-00', 'week-06', 'week-09'.
        out_dir: Target output directory where files and downloads.json are saved.
        pdf: Whether to generate PDF format files.
        engine: 'chrome' (default) or 'weasy'.
        cache_dir: Directory for caching official images.
    Returns:
        Manifest dictionary loaded from downloads.json.
    Raises:
        ValueError: If solution is provided in problem-set JSON (solution leakage prevention).
    """
    kb = str(kb_dir)
    slug = str(week_slug)
    out = str(out_dir)
    os.makedirs(out, exist_ok=True)

    cache = str(cache_dir or os.path.join(HERE, "cache"))
    w = Week(kb, slug)
    R = Renderer(w, cache)

    manifest_path = os.path.join(kb, "manifest.json")
    kb_version = ""
    if os.path.exists(manifest_path):
        try:
            kb_version = json.load(open(manifest_path, encoding="utf-8")).get("version", "")
        except Exception:
            kb_version = "1.0.0"

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(HERE, "templates")), autoescape=False)
    fonts = {
        k: base64.b64encode(open(os.path.join(HERE, "fonts", f), "rb").read()).decode()
        for k, f in [
            ("vaz_r", "Vazirmatn-Regular.woff2"),
            ("vaz_b", "Vazirmatn-Bold.woff2"),
            ("naskh", "NotoNaskhArabic.woff2"),
            ("mono", "IBMPlexMono.woff2"),
        ]
    }
    css = env.get_template("theme.css").render(
        fonts=fonts,
        pygments_css=PYGMENTS_CSS,
    )
    built_fa = jalali(w.built)
    prefix = re.sub(r"[^a-z0-9]+", "", slug.replace("week-", "week"))
    names: dict[str, str] = {
        "handout": f"01-{prefix}-jozve",
        "summary": f"02-{prefix}-kholase-vazhename",
        "code": f"04-{prefix}-source-code.zip",
        "slides": f"05-{prefix}-slides",
        "flash": f"06-{prefix}-flashcards",
    }

    for (m, _b), f in w.notes:
        R.doc_targets[m["id"]] = f"{names['handout']}.html#{m['id']}"
    if w.summary:
        R.doc_targets[w.summary[0].get("id", "")] = f"{names['summary']}.html"

    pset_keys = []
    for (m, _b), j in w.psets:
        # STRICT SECURITY CHECK: Never leak solutions!
        if j.get("solution", {}).get("provided"):
            raise ValueError(f"refusing: solution provided in {m.get('id')}")

        ps = re.sub(
            r"[^a-z0-9-]+",
            "-",
            (j.get("guide_file") or m.get("id", "pset"))[:-6].lower() if j.get("guide_file") else m.get("id", "pset").lower(),
        ).strip("-")
        k = "pset:" + ps
        names[k] = f"03-{prefix}-pset-{ps}"
        pset_keys.append((k, ps, m, _b, j))
        R.doc_targets[m.get("id", "")] = f"{names[k]}.html"

    R.doc_targets[w.overview_meta.get("id", "")] = f"{names['handout']}.html#overview"
    report: dict[str, Any] = {"week": slug, "files": {}, "warnings": []}
    items: list[dict[str, Any]] = []

    def sha(p: str) -> str:
        return hashlib.sha256(open(p, "rb").read()).hexdigest()

    def add_item(key: str, kind: str, title: str, fmts: list[str], meta: dict[str, Any] | None = None) -> None:
        it: dict[str, Any] = {
            "id": f"{slug}:{key}",
            "kind": kind,
            "title_fa": title,
            "week": slug,
            "kb_version": kb_version,
            "formats": [],
        }
        it.update(meta or {})
        for ext in fmts:
            fn = names[key] + ext if not names[key].endswith(ext) else names[key]
            fp = os.path.join(out, fn)
            if os.path.exists(fp):
                f_entry: dict[str, Any] = {
                    "format": ext.lstrip("."),
                    "path": fn,
                    "size": os.path.getsize(fp),
                    "sha256": sha(fp),
                    "mime": {
                        ".html": "text/html; charset=utf-8",
                        ".pdf": "application/pdf",
                        ".zip": "application/zip",
                    }[ext],
                }
                if ext == ".pdf":
                    pdf_info = report["files"].get(fn)
                    if isinstance(pdf_info, dict) and "pages" in pdf_info:
                        f_entry["pages"] = pdf_info["pages"]
                    else:
                        f_entry["pages"] = count_pdf_pages(fp)
                it["formats"].append(f_entry)
        items.append(it)

    KIND = {"handout": "handout", "summary": "summary-glossary", "slides": "slides-link", "flash": "flashcards"}

    def emit(key: str, title: str, body: str, subtitle: str = "", js: bool = True, meta: dict[str, Any] | None = None) -> None:
        page = env.get_template("base.html.j2").render(
            title=title,
            subtitle=subtitle,
            week=w,
            body=body,
            css=css,
            built=w.built,
            built_fa=built_fa,
            kb_version=fa(kb_version),
            gen_version=GEN_VERSION,
            copy_js=js,
        )
        hp = os.path.join(out, names[key] + ".html")
        open(hp, "w", encoding="utf-8").write(page)
        report["files"][names[key] + ".html"] = os.path.getsize(hp)

        pdf_fmts = [".html"]
        if pdf and key != "slides":
            pp = os.path.join(out, names[key] + ".pdf")
            pdf_res = write_pdf(page, hp, pp, w.built, title, engine)
            if pdf_res:
                report["files"][names[key] + ".pdf"] = pdf_res
                pdf_fmts.append(".pdf")
            else:
                report["warnings"].append(f"PDF generation skipped for {names[key]}")

        if key != "index":
            add_item(key, KIND.get(key, "pset-guide"), title, pdf_fmts, meta)

    def doc_h1(id_: str, text: str, first: bool = False) -> str:
        return f'<h1 class="doc{" first" if first else ""}" id="{id_}">{html.escape(text)}</h1>'

    # 1) Handout: overview + all notes + TOC
    parts, toc = [], []
    ov = R.render(w.overview, "overview")
    parts.append(doc_h1("overview", "نمای کلی هفته", True) + ov)
    toc.append(("overview", "نمای کلی هفته", []))
    for (m, b), f in w.notes:
        t = m.get("title_fa") or m.get("title", f)
        body = R.render(b, m["id"])
        meta = f'<p class="meta"><span class="badge">{fa(m.get("order", ""))}</span>منبع رسمی: <a href="{m.get("source_url", "")}">{html.escape(m.get("title_en", ""))}</a></p>'
        parts.append(doc_h1(m["id"], t) + meta + body)
        toc.append((m["id"], t, R.headings(body)))

    def toc_html(items_list: list[tuple[str, str, Any]]) -> str:
        li = "".join(
            f'<li><a href="#{i}">{html.escape(t)}</a>'
            + (("<ol>" + "".join(f'<li><a href="#{a}">{h}</a></li>' for a, h in sub) + "</ol>") if sub else "")
            + "</li>"
            for i, t, sub in items_list
        )
        return f'<nav class="toc" aria-label="فهرست"><h2>فهرست</h2><ol>{li}</ol></nav>'

    emit("handout", "جزوهٔ هفته", toc_html([(i, t, []) for i, t, _ in toc]) + "".join(parts), f"نمای کلی و {fa(len(w.notes))} یادداشت")

    # 2) Summary + Glossary
    gl_rows = []
    wg = os.path.join(w.dir, "curriculum", "glossary.fa.json")
    if os.path.exists(wg):
        for k, v in sorted(json.load(open(wg, encoding="utf-8")).items(), key=lambda x: fa_key(x[1]["fa"])):
            gl_rows.append((v["fa"], v["en"], v.get("definition", "")))
    else:
        glo_path = os.path.join(kb, "curriculum", "glossary.fa.json")
        lm_path = os.path.join(kb, "curriculum", "learning-map.json")
        G = json.load(open(glo_path, encoding="utf-8"))["terms"] if os.path.exists(glo_path) else []
        L = {c["id"]: c for c in json.load(open(lm_path, encoding="utf-8"))["concepts"]} if os.path.exists(lm_path) else {}
        wp = f"w{int(w.num):02d}-" if str(w.num).isdigit() else None
        for t in sorted((t for t in G if wp and (t.get("concept_id") or "").startswith(wp)), key=lambda t: fa_key(t["fa"])):
            nid = L.get(t["concept_id"], {}).get("note_id")
            href = R.doc_targets.get(nid)
            nn = next((fa(int(m.get("order", 0))) for (m, _b), _f in w.notes if m["id"] == nid), "")
            gl_rows.append((t["fa"], t["en"], f'<a href="{href}">یادداشت {nn}</a>' if href else ""))

    sb = ""
    if w.summary:
        sm, sbody = w.summary
        sb = doc_h1("summary", sm.get("title_fa", "جمع‌بندی"), True) + R.render(sbody, "summary")
    rows = "".join(
        f"<tr><td>{html.escape(a)}</td><td class=\"en\" dir=\"ltr\">{html.escape(b)}</td><td class=\"{'nw' if c.startswith('<a') else ''}\">{c if c.startswith('<a') else html.escape(c)}</td></tr>"
        for a, b, c in gl_rows
    )
    sb += doc_h1("glossary", "واژه‌نامهٔ هفته") + f'<p class="meta">{fa(len(gl_rows))} واژه، به ترتیب الفبای فارسی.</p><table><thead><tr><th>فارسی</th><th>انگلیسی</th><th>{"تعریف" if os.path.exists(wg) else "کجا"}</th></tr></thead><tbody>{rows}</tbody></table>'
    emit("summary", "خلاصهٔ هفته و واژه‌نامه", sb, f"جمع‌بندی و {fa(len(gl_rows))} واژه")

    # 3) PSET guides (strictly without solutions)
    for k, ps, m, b, j in pset_keys:
        pid = m.get("id", ps)
        t = m.get("title_fa") or m.get("title", pid)
        body = R.render(b, pid)
        off = j.get("official", {}).get("url") or m.get("source_url", "")
        emit(
            k,
            "راهنمای تمرین: " + t,
            doc_h1(pid, t, True) + f'<p class="meta">صورت رسمی تمرین: <a dir="ltr" href="{off}">{html.escape(off)}</a> · راه‌حل در این فایل نیست (سیاست صداقت علمی CS50).</p>' + body,
            (j.get("title_en") or "") + " · راهنما، بدون راه‌حل",
            meta={"pset_slug": ps, "pset_id": pid, "title_en": j.get("title_en", ""), "official_url": off},
        )

    # 4) Source code ZIP from fenced code in notes
    files, used, listing = {}, set(), []
    for (m, b), f in w.notes:
        for mt in re.finditer(r"^```(\w+)\n(.*?)^```", b, re.M | re.S):
            ext = CODE_EXT.get(mt.group(1).lower())
            if not ext:
                continue
            before = b[:mt.start()]
            names_seen = re.findall(r"`([A-Za-z0-9_\-]+\." + ext + r")`", before)
            base = names_seen[-1] if names_seen else f"{f.split('.')[0]}.{ext}"
            stem, e = os.path.splitext(base)
            name, k = base, 1
            while name in used:
                k += 1
                name = f"{stem}-{k}{e}"
            if name != base and base in used and k == 2 and base in files:
                files[f"{stem}-1{e}"] = files.pop(base)
                used.add(f"{stem}-1{e}")
                listing = [(f"{stem}-1{e}" if n == base else n, nid, tt) for n, nid, tt in listing]
            used.add(name)
            files[name] = mt.group(2)
            listing.append((name, m["id"], m.get("title_fa", "")))

    zsrc = w.src_by_type("source-code") or [s for s in w.sources.get("sources", []) if s["id"].endswith("-zip")]
    readme = [
        f"# کد منبع {w.title}",
        "",
        "این بسته کدهای قابل اجرای درون یادداشت‌های فارسی همین هفته است، عیناً همان که در درس‌نامهٔ رسمی آمده.",
        "بلوک‌های شبه‌کد و بلوک‌های Scratch (متنی) در این بسته نیستند.",
        "",
        "| فایل | یادداشت |",
        "|---|---|",
    ]
    readme += [f"| `{n}` | {tt} (`{nid}`) |" for n, nid, tt in listing]
    readme += [
        "",
        "## کد رسمی CS50",
        "",
    ] + [f"- [{s['title']}]({s['url']})" for s in zsrc] + [
        "",
        "## مجوز",
        "",
        "بر پایهٔ CS50x 2026، © David J. Malan، دانشگاه هاروارد، با مجوز CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/).",
        "ترجمه و بازآرایی فارسی CS50x انزلی — غیررسمی؛ محصول رسمی هاروارد یا CS50 نیست.",
        "",
    ]
    files["README.fa.md"] = "\n".join(readme)
    zp = os.path.join(out, names["code"])
    zipdet(zp, {f"{prefix}-src/{k}": v for k, v in files.items()})
    report["files"][names["code"]] = os.path.getsize(zp)
    report["code_files"] = [n for n, _, _ in listing]
    if listing:
        add_item("code", "source-code", "کد منبع هفته (ZIP)", [".zip"], {"code_files": [n for n, _, _ in listing]})
    else:
        if os.path.exists(zp):
            os.remove(zp)
        if names["code"] in report["files"]:
            del report["files"][names["code"]]

    # 5) Slides link card (no rehosting)
    sl = w.src_by_type("slides")
    vid = [s for s in w.sources.get("sources", []) if s["id"] == "src-video" or s.get("source_type") == "video"]
    li = "".join(
        f'<li><a href="{s["url"]}">{html.escape(s["title"])}</a> <span class="meta" dir="ltr">{html.escape(s["url"])}</span></li>'
        for s in sl + vid[:1]
    )
    emit(
        "slides",
        "اسلایدهای سخنرانی",
        f'<div class="card"><h2>اسلایدهای رسمی</h2><p>اسلایدها متعلق به CS50 هستند و اینجا بازنشر نمی‌شوند. نسخهٔ رسمی را از پیوندهای زیر باز کن یا بارگیری کن.</p><ul class="dl">{li or "<li>برای این هفته پیوند اسلاید رسمی در بسته ثبت نشده است.</li>"}</ul></div>',
        "فقط پیوند به نسخهٔ رسمی",
    )

    # 6) Printable flashcards
    if w.flashcards:
        cards = "".join(
            f'<div class="c"><div class="q">{inline(c["front_fa"])}</div><div class="a">{inline(c["back_fa"])}</div></div>'
            for c in w.flashcards
        )
        emit(
            "flash",
            "فلش‌کارت‌های چاپی",
            f'<p class="meta noprint">برای چاپ: هر کارت را از خط‌چین ببر و از وسط تا کن؛ پرسش رو، پاسخ پشت.</p><div class="fc">{cards}</div>',
            f"{fa(len(w.flashcards))} کارت",
        )

    # 7) Index page
    raw_list = [("handout", "جزوهٔ هفته"), ("summary", "خلاصهٔ هفته و واژه‌نامه")] + [
        (k, "راهنمای تمرین: " + (m.get("title_fa") or ps)) for k, ps, m, _b, _j in pset_keys
    ] + [("slides", "اسلایدها (پیوند رسمی)"), ("flash", "فلش‌کارت‌های چاپی")]
    lst = "".join(
        f'<li><a href="{names[k]}.html">{t}</a>{f" · <a href={chr(34)}{names[k]}.pdf{chr(34)}>PDF</a>" if pdf and k != "slides" and os.path.exists(os.path.join(out, names[k] + ".pdf")) else ""}</li>'
        for k, t in raw_list
        if os.path.exists(os.path.join(out, names[k] + ".html"))
    )
    lst += f'<li><a href="{names["code"]}">کد منبع (ZIP)</a></li>' if listing else ""
    names["index"] = "index"

    page = env.get_template("base.html.j2").render(
        title="بارگیری‌های هفته",
        subtitle="",
        week=w,
        css=css,
        built=w.built,
        built_fa=built_fa,
        kb_version=fa(kb_version),
        gen_version=GEN_VERSION,
        copy_js=False,
        body=f'<div class="card"><h2>فایل‌ها</h2><ul class="dl">{lst}</ul><p class="meta">فایل‌های HTML بدون اینترنت در هر مرورگری باز می‌شوند. PDF برای چاپ است.</p></div>',
    )
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page)

    manifest_data = {
        "schema": "cs50x-anzali-downloads/1",
        "week": slug,
        "week_title_fa": w.title,
        "kb_version": kb_version,
        "generator": GEN_VERSION,
        "built": w.built,
        "items": items,
    }
    json.dump(
        manifest_data,
        open(os.path.join(out, "downloads.json"), "w", encoding="utf-8"),
        ensure_ascii=False,
        indent=1,
        sort_keys=True,
    )
    json.dump(
        report,
        open(os.path.join(out, "build-report.json"), "w", encoding="utf-8"),
        ensure_ascii=False,
        indent=1,
        sort_keys=True,
    )
    return manifest_data


def main():
    if len(sys.argv) < 4:
        print("Usage: generate.py KB_DIR WEEK_SLUG OUT_DIR [--no-pdf] [--pdf-engine=weasy]")
        sys.exit(1)
    kb, slug, out = sys.argv[1], sys.argv[2], sys.argv[3]
    pdf = "--no-pdf" not in sys.argv
    engine = "weasy" if "--pdf-engine=weasy" in sys.argv else "chrome"
    res = build_week(kb, slug, out, pdf=pdf, engine=engine)
    print(json.dumps({"week": slug, "items_count": len(res.get("items", []))}, ensure_ascii=False))


if __name__ == "__main__":
    main()
