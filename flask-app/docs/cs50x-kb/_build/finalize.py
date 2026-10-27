#!/usr/bin/env python3
"""Write README.md, LICENSE-NOTICE.md, _templates/document-template.md, coverage-report.md and _build/README.md."""
import collections, json, os, re
import yaml
B = os.path.dirname(os.path.abspath(__file__)); KB = os.path.dirname(B)
M = json.load(open(os.path.join(B, "manifest.json")))
S = json.load(open(os.path.join(B, "build_stats.json")))
V = json.load(open(os.path.join(B, "validation.json"))) if os.path.exists(os.path.join(B, "validation.json")) else {}
SC = json.load(open(os.path.join(B, "spotcheck.json"))) if os.path.exists(os.path.join(B, "spotcheck.json")) else []
IDX = json.load(open(os.path.join(KB, "index.json")))
def W(p, t):
    os.makedirs(os.path.dirname(os.path.join(KB, p)), exist_ok=True); open(os.path.join(KB, p), "w", encoding="utf-8").write(t)
docs = [n for n in IDX["nodes"] if not n["id"].startswith("file:")]
files = [n for n in IDX["nodes"] if n["id"].startswith("file:")]
bytype = collections.Counter(n["type"] for n in docs)
bystatus = collections.Counter(n["status"] for n in docs)
bysrc = collections.Counter(n["source_type"] for n in docs)
st = collections.Counter(e["status"] for e in M.values())
cat_f = collections.Counter(e.get("category") for e in M.values() if e["status"] == "fetched")
skipped = collections.defaultdict(list)
for u, e in M.items():
    if e["status"] == "skipped": skipped[(e.get("category"), e.get("reason"))].append(u)
failed = [(u, e.get("reason")) for u, e in M.items() if e["status"] == "failed"]
def kbsize():
    t = 0
    for r, d, f in os.walk(KB):
        if r.startswith(os.path.join(KB, "_build")): continue
        t += sum(os.path.getsize(os.path.join(r, x)) for x in f)
    return t

# ---------------- LICENSE-NOTICE
W("LICENSE-NOTICE.md", """# LICENSE / NOTICE

## Extracted content — CC BY-NC-SA 4.0 (non-commercial)
All content in this knowledge base that is marked **OFFICIAL** (section 2 of every document, every file under `transcripts/`, and every file
under `*/files/` folders: lecture source code, section code and problem-set distribution code) is extracted from **CS50x 2026**
(CS50’s Introduction to Computer Science) by **David J. Malan, Harvard University**, and its official sites
(cs50.harvard.edu, cdn.cs50.net, cs50.readthedocs.io, manual.cs50.io, cs50.ai, cs50.dev).

- License: **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** — https://creativecommons.org/licenses/by-nc-sa/4.0/
- CS50’s license page: https://cs50.harvard.edu/x/license/ (local copy: [course/license.md](course/license.md))
- Each document’s front matter carries `license`, `attribution`, `source_urls`, `retrieved_at` and a `checksum` of the raw source page.

**Conditions you must keep when reusing this KB or showing its content on the CS50x Anzali site:**
1. **Attribution** — credit “CS50x, David J. Malan, Harvard University”, link the source page and the license.
2. **NonCommercial** — no commercial use (no paid courses, ads-for-profit reuse, or sale of this content).
3. **ShareAlike** — translations, summaries and other adaptations must be released under CC BY-NC-SA 4.0 too.
4. **Indicate changes** — say that content was converted to Markdown, reorganised, and (where applicable) translated or summarised.

Manual pages on manual.cs50.io include Linux man-page text from the Linux man-pages project; where a page carries its own copyright/license section, that section is preserved verbatim inside the document.

## Generated content
Sections marked **GENERATED** (sections 3b and 5 of every document, all of `project/`, index pages, and the Persian hints) were written by the
CS50x Anzali KB builder. They are not CS50 text. Because they adapt CS50 material, they are distributed under the same CC BY-NC-SA 4.0 license.

## Not included
No videos, audio, slide PDFs, or student works were downloaded. No content behind a login was accessed.
""")

# ---------------- template
W("_templates/document-template.md", """---
id: <stable-kebab-id>            # e.g. pset-3-tideman, week-4-lecture, concept-pointers
type: <project|course|course-page|week|lecture|section|short|source-code|pset-index|pset|practice|final-project|tool|tool-index|reference|reference-index|concept|concept-index|glossary>
title: <title as on source>
week: <0-10 | ai | null>
parent: <id of parent node>
children: [<ids>]
prerequisites: [<ids>]           # GENERATED unless the source states them
related: [<ids>]
source_urls: [<exact official URLs>]
source_type: <official|mixed|generated>
license: <CC BY-NC-SA 4.0 ... | generated notice>
attribution: <CS50x 2026 © David J. Malan, Harvard University — CC BY-NC-SA 4.0 ...>
retrieved_at: <ISO 8601, Asia/Tehran, e.g. 2026-10-18T05:11:27+03:30>
review_status: <verified-against-source|partially-verified|unverified|unavailable>
difficulty: <only if stated by source (e.g. "less comfortable"), else null>
generated_difficulty: {value: <1-5>, scale: "1 (easy) – 5 (hard)", note: "GENERATED estimate"}   # or null
languages: [<C|Python|SQL|HTML/CSS/JavaScript|...>]
tags: [<kebab tags>]
checksum: sha256:<hash of the raw fetched source page>
generated_language: fa
built_at: <ISO timestamp of build>
---

# <title>

## 1. Source metadata
- Title, type, source type, official link(s), review status, retrieved time, license.

## 2. OFFICIAL CONTENT
> Source: <url> · attribution
(verbatim/faithful content converted from the official page; headings, lists, code blocks and tables preserved; links absolute)

## 3. Learning objectives, prerequisites, order, difficulty
### 3a. Stated by source
### 3b. GENERATED (fa)

## 4. Relationships
- Parent / Children / Prerequisites (generated) / Related / Backlinks (auto-generated) — relative links + ids

## 5. GENERATED — application (fa)
> ⚠️ generated notice
### کاربرد آموزشی
### راهنمایی مرحله‌ای مفهومی (بدون راه‌حل)   ← psets/practice only; never solutions
### راهنمای پاسخ‌گویی دستیار هوش مصنوعی
### ایده‌های پیاده‌سازی در سایت

## 6. References, review, gaps
- each source URL with retrieval time and sha256 prefix; review date; gaps / unverified items
""")

# ---------------- coverage report
weeks = [n for n in docs if n["type"] == "week"]
weeks.sort(key=lambda n: n["order"])
def kids(i, t): return [n for n in docs if n["parent"] == i and n["type"] == t]
rows = ["| Week | Lecture notes | Lecture transcript | Section (+transcript) | Shorts (with transcript) | PSet problems | Practice | Source code (stored / inventoried files) |", "|---|---|---|---|---|---|---|---|"]
def count_files(path_prefix):
    tot = sto = 0
    p = os.path.join(KB, path_prefix)
    readme = os.path.join(p, "README.md")
    if os.path.exists(readme):
        t = open(readme, encoding="utf-8").read()
        tot = len(re.findall(r"^\| `", t, re.M)); sto = len(re.findall(r"\| \[yes\]\(", t))
    return sto, tot
for w in weeks:
    i = w["id"]; folder = os.path.dirname(w["path"])
    lec = [n for n in docs if n["id"] == f"{i}-lecture"]
    tr = [f for f in files if f["parent"] == f"{i}-lecture"]
    sec = [n for n in docs if n["id"] == f"{i}-section"]
    sect = [f for f in files if f["parent"] == f"{i}-section"]
    shorts = kids(i, "short"); shorts_t = [s for s in shorts if any(f["parent"] == s["id"] for f in files)]
    ps = [n for n in docs if n["type"] == "pset" and n["week"] == w["week"]]
    pr = [n for n in docs if n["type"] == "practice" and n["week"] == w["week"]]
    sto, tot = count_files(f"{folder}/source-code")
    rows.append(f"| {w['title']} | {'✓ ' + lec[0]['status'] if lec else '—'} | {'✓' if tr else '—'} | {('✓' + (' (+transcript)' if sect else '')) if sec else '— (no section page linked)'} | {len(shorts)} ({len(shorts_t)}) | {len(ps)} | {len(pr)} | {f'{sto} / {tot}' if tot else '—'} |")
gap_lines = []
for n in docs:
    t = open(os.path.join(KB, n["path"]), encoding="utf-8").read()
    g = t.split("- **Gaps / unverified items:**", 1)
    if len(g) == 2:
        for line in g[1].strip().splitlines():
            if line.startswith("- ") and "None recorded" not in line:
                gap_lines.append(f"- `{n['id']}`: {line[2:]}")
def tree(root, depth=0, maxd=3):
    out = []
    for name in sorted(os.listdir(root)):
        if name in ("_build",) and depth == 0:
            out.append("  " * depth + "_build/  (crawler, builder, validator, manifest, raw sources)"); continue
        p = os.path.join(root, name)
        if os.path.isdir(p):
            nfiles = sum(len(f) for _, _, f in os.walk(p))
            if name == "files" or name.endswith("-distribution") or name in ("section-code",):
                out.append("  " * depth + f"{name}/  ({nfiles} files)"); continue
            out.append("  " * depth + f"{name}/" + (f"  ({nfiles} files)" if depth >= maxd - 1 else ""))
            if depth < maxd - 1: out += tree(p, depth + 1, maxd)
        elif depth <= 1 or name.endswith(".md") and depth <= 2:
            out.append("  " * depth + name)
    return out
skipped_tbl = ["| Category | Reason | Count | Example |", "|---|---|---:|---|"]
for (c, r), us in sorted(skipped.items(), key=lambda x: -len(x[1])):
    skipped_tbl.append(f"| {c} | {r} | {len(us)} | {us[0]} |")
spot = ["| Doc | Live URL | HTTP | Raw vs live main text | Sampled sentences found live |", "|---|---|---|---|---|"]
for s in SC:
    spot.append(f"| `{s['doc']}` | {s['url']} | {s['http']} | {'identical' if s['identical_main_text'] else s['raw_vs_live_word_similarity']} | {s['sampled_sentences_found_live']}/{s['sampled_sentences']} |")
chk = V.get("checks", {})
cov = f"""# Coverage report — CS50x knowledge base

Built: {S['built_at']} (Asia/Tehran). Crawl: 2026-10-18 (Asia/Tehran), 1 request/second, User-Agent `CS50xAnzali-KB-builder/2.0`, no login, no paid services.

## 1. Summary
- **Documents (Markdown with front matter):** {len(docs)}  ·  **Transcript files:** {len(files)}  ·  **Glossary entries:** {S['glossary_terms']}  ·  **search.jsonl records:** {S['search_chunks']}
- **KB size (excluding `_build/`):** {kbsize()/1e6:.1f} MB
- **Docs by type:** {', '.join(f'{k} {v}' for k, v in sorted(bytype.items()))}
- **Docs by source_type:** {', '.join(f'{k} {v}' for k, v in sorted(bysrc.items()))}
- **Docs by review_status:** {', '.join(f'{k} {v}' for k, v in sorted(bystatus.items()))}
- **Manifest URLs:** {len(M)} total — fetched {st['fetched']}, failed {st['failed']}, skipped {st['skipped']} (every discovered URL is logged in `_build/manifest.json`).

## 2. Sources reviewed (fetched)
| Category | Fetched |
|---|---:|
""" + "\n".join(f"| {k} | {v} |" for k, v in sorted(cat_f.items(), key=lambda x: -x[1])) + f"""

Category meanings: `harvard` = cs50.harvard.edu/x pages (home, 12 week pages, 12 lecture notes, 9 sections, 44 shorts, 10 pset indexes, 35 problem specs, 22 practice problems, practice/psets/weeks/sections indexes, project, syllabus, FAQs, honesty, certificate, license, communities, staff, seminars, gallery, puzzles, zoom, courses); `harvard-archive-2025` = 12 CS50x 2025 pset pages kept only for the year-over-year comparison; `cdn-transcript` = English .txt transcripts (12 lectures, 9 sections, 44 shorts); `cdn-zip` = lecture source, section source, problem-set and practice distribution ZIPs; `cdn-listing`/`cdn-listing-file` = directory listing + small text files of lecture 9 source (fallback, ZIP too large); `readthedocs` = cs50.readthedocs.io pages (check50, submit50, style50, help50, CS50 library C/Python, codespace, cs50.dev, CS50.ai, manual, video player, certificates, terminal, C style guide); `manual` = manual.cs50.io index + {sum(1 for n in docs if n['id'].startswith('manual-'))} function pages; `cs50.ai`, `cs50.dev` = public home pages.

## 3. Sources not reviewed

### 3a. Failed ({len(failed)})
""" + "\n".join(f"- {u} — {r}" + (" (broken relative link on the official Section page; not a KB error)" if "sections/psets" in u else " (linked from the CS50 docs; page does not exist)" if "cli50" in u else "") for u, r in failed) + f"""

### 3b. Skipped (grouped; full list in `_build/manifest.json`)
{chr(10).join(skipped_tbl)}

## 4. Content coverage per week
{chr(10).join(rows)}

Course-level: home, syllabus, FAQs, academic honesty, certificate, license, communities, staff, seminars, puzzles, zoom, courses, index pages, gallery (intro + counts only), compiled deadlines & grading, changes vs 2025 (generated), final project.
Tools: {bytype.get('tool', 0)} tool docs (+ index). Reference: C style guide, Python style pointer, {sum(1 for n in docs if n['id'].startswith('manual-'))} manual pages. Concepts: {bytype.get('concept', 0)}. Glossary: {S['glossary_terms']} entries.

## 5. Information gaps (global)
- **Videos, audio, slide PDFs, source-code PDFs**: URLs recorded only (by design). Slide content is therefore not in the KB except where the notes reproduce slide images (image URLs kept).
- **Non-English transcripts and .srt subtitle files**: skipped; English .txt transcripts stored instead.
- **cdn.cs50.net robots.txt is `Disallow: /`**: the task explicitly authorised downloading transcripts and ZIPs; the crawler fetched only individually linked files (no directory crawling except the one listing fallback below), at 1 req/s. Re-run with `python3 crawl.py --no-cdn` to respect robots.txt strictly (transcripts, ZIPs and source files would then be missing).
- **Lecture 9 source ZIP (140 MB)** exceeded the 60 MB cap → inventory built from the cdn directory listing; small text files stored, binaries listed.
- **Movies distribution ZIP (77 MB, `movies.db`)** exceeded the cap → not downloaded or inventoried (spec page fully extracted).
- **Gallery of Final Projects**: individual student projects not extracted.
- **manual.cs50.io**: curated subset (cs50.h + functions used in the course), not the ~1,700 pages.
- **cs50.ai / CS50 Duck**: the app is login-only; only its public home page and the CS50 Docs page were used. No duck behaviour beyond what official pages state is documented.
- **Python style guide**: CS50 points to PEP 8 (external, not extracted).
- **Week 0, AI week, Week 10**: no Section page is linked from these week pages; Week 10 has no title on the week page (folder `week-10`).
- **Seminars**: only the seminars index page (titles/links) — seminar videos not transcribed.
- **Edx, YouTube, Discord, Ed, Gradebook (cs50.me), submit.cs50.io**: out of scope (apps/logins); URLs recorded only.

### Per-document gaps (from section 6 of each document)
{chr(10).join(gap_lines[:400])}

## 6. Unverified / generated items
- All **section 3b and section 5** content (Persian teaching use, hints, AI-tutor guidance, feature ideas) is GENERATED and has not been reviewed by CS50 or by a human teacher.
- `generated_difficulty` values are the builder’s estimates (CS50 states only comfort levels such as “less comfortable”).
- `language` per problem and `key_concepts`/English summaries come from the earlier KB (`/workspace/cs50x-2026-kb`), marked as paraphrase.
- **Concept docs, glossary, deadlines-and-grading, debug50/valgrind/duck docs** quote official text verbatim, but the *selection* of passages was automatic (keyword regex) → `review_status: partially-verified`.
- Prerequisite links (week → previous week, problem → week lecture) are generated.
- `project/` documents are generated and refer to the repo audit; they were not checked against the current repo code (the repo was not touched).

## 7. Validation results
- Errors: **{len(V.get('errors', []))}**; warnings: {len(V.get('warnings', []))}
- Documents with complete front matter and all 6 sections: {chk.get('docs_with_front_matter')}
- Relative links checked: {chk.get('relative_links_checked')}; broken: {chk.get('relative_links_broken')}
- index.json nodes: {chk.get('index_nodes')}; edges.json edges: {chk.get('edges')}; search.jsonl records: {chk.get('search_records')}
- Counts vs manifest: """ + ", ".join(f"{k[6:]} {v}" for k, v in chk.items() if k.startswith("count_")) + f"""
- Fetched sources not used by any document: {len(chk.get('fetched_sources_not_mapped_to_a_doc', []))}
""" + ("".join(f"- warning: {w}\n" for w in V.get("warnings", [])[:20])) + f"""
### Spot-check against live pages
{chr(10).join(spot)}

“Raw vs live” compares the main text of the stored raw page with a fresh fetch. “Sampled sentences” are random sentences from section 2 of the KB doc looked up in the live page (for shorts: in the live transcript); misses were inspected and are Markdown/markup artifacts of the checker (e.g. code blocks, image alt text), not content differences.

## 8. Final KB tree
```
cs50x-kb/
{chr(10).join('  ' + l for l in tree(KB))}
```
"""
W("coverage-report.md", cov)

# ---------------- README
W("README.md", f"""# CS50x 2026 — Hierarchical Knowledge Base (for CS50x Anzali)

> پایگاه دانش درختی و قابل توسعه از منابع رسمی CS50x 2026 برای پلتفرم آموزشی فارسی CS50x Anzali.
> محتوای رسمی به زبان اصلی (انگلیسی) و بخش‌های تولیدشده به فارسی هستند و همیشه جدا و برچسب‌دار.

**License:** extracted content is CC BY-NC-SA 4.0 (non-commercial, share-alike) — read [LICENSE-NOTICE.md](LICENSE-NOTICE.md) before reusing anything.
**Coverage, gaps, validation:** [coverage-report.md](coverage-report.md).

## Hierarchy
```
project/                     CS50x Anzali context (GENERATED): purpose, site-model mapping, AI-tutor policy
course/                      course home + syllabus, FAQs, honesty, certificate, license, communities, staff, seminars, puzzles, ...
weeks/week-NN-<slug>/        12 weeks (0–10 + week-ai-artificial-intelligence between 7 and 8)
  week.md                    week page
  lecture.md                 full lecture notes (verbatim) + links to video/slides/transcript
  sections.md                section page (+ section code inventory)
  shorts/<slug>.md           shorts with full transcripts
  transcripts/*.txt          lecture / section / short transcripts (verbatim, English)
  source-code/README.md      lecture source inventory; small text files under source-code/files/
  psets/README.md            problem-set index page
  psets/<slug>.md            full problem spec (verbatim) + distribution-code inventory (<slug>-distribution/files/)
  practice/<slug>.md         optional practice problems (same format)
final-project/README.md      final project spec
tools/                       check50 (+ sub-docs), submit50, style50, help50, CS50 library (C, Python), codespace, cs50.dev, CS50.ai/duck, debug50, valgrind, ...
reference/                   C style guide, Python style pointer, manual pages (manual.cs50.io) for cs50.h + functions used in the course
concepts/                    {bytype.get('concept', 0)} concept docs (verbatim definitions from notes + Persian explanation)
glossary.md                  term → definition source → linked docs
index.json                   machine-readable tree (id, type, title, path, parent, children, source_url, status, order, tags)
edges.json                   relation graph (parent-of, prerequisite-of, related, has-file)
search.jsonl                 one record per doc section chunk (≤2000 chars) and transcript chunk — for search / RAG
_templates/document-template.md
_build/                      reproducible crawl + build + validation scripts, manifest of every URL, raw sources
```

## Document conventions
- **Every document** has YAML front matter (keys in English) and the same six sections:
  1. Source metadata · 2. **OFFICIAL CONTENT** · 3. Objectives/prerequisites/order/difficulty (3a stated by source, 3b GENERATED) · 4. Relationships (parent, children, prerequisites, related, auto-backlinks) · 5. **GENERATED** application (teaching use, conceptual hints, AI-tutor guidance, site-feature ideas — Persian) · 6. References, review date, gaps.
- **`source_type`**: `official` (section 2 is extracted verbatim from one official page), `mixed` (verbatim official passages selected automatically + generated text, e.g. concepts), `generated` (no official text).
- **`review_status`**: `verified-against-source` (mechanically extracted from the fetched page; spot-checked docs re-compared with the live page), `partially-verified` (verbatim quotes but automatic selection or fallback inventory), `unverified` (generated), `unavailable` (source could not be fetched).
- **`difficulty`** is only what CS50 states (e.g. “less comfortable”); `generated_difficulty` is our estimate and labelled as such.
- **IDs** are stable kebab-case: `week-4`, `week-4-lecture`, `week-4-section`, `week-4-source-code`, `short-pointers`, `pset-4`, `pset-4-filter-less`, `practice-4-license`, `concept-pointers`, `manual-get_string`, `tool-check50`, `course-honesty`.
- Official content keeps CS50’s headings, lists, tables and code blocks; links/images are absolute URLs to the official site; heading anchors are preserved as `<a id="...">` so KB links like `lecture.md#pointers` match the official `#pointers` anchors.
- Times are ISO 8601 in Asia/Tehran (+03:30). Deadlines are shown as stated (UTC) and converted.

## Using it
- **Humans:** start at [project/README.md](project/README.md) → [course/README.md](course/README.md) → a week’s `week.md`.
- **AI agents / RAG:** load `search.jsonl`; filter or weight by `source_type` (cite only `official` chunks as CS50’s words), `doc_type`, `week`, `tags`. Resolve context with `index.json` and `edges.json`. Follow [project/ai-tutor-policy.md](project/ai-tutor-policy.md).
- **Site import:** see [project/site-model-mapping.md](project/site-model-mapping.md) (Week / Assignment / Resource / Submission / XP).

## Academic honesty
No solutions to any problem set or practice problem are included. Hints in section 5 are conceptual only. Distribution code stored under `*-distribution/files/` is CS50’s official starter code, not solutions.

## Rebuild
See [_build/README.md](_build/README.md): `python3 crawl.py && python3 crawl_listing.py && python3 build.py && python3 validate.py && python3 spotcheck.py && python3 finalize.py`.

Counts at build {S['built_at']}: {len(docs)} documents, {len(files)} transcript files, {S['search_chunks']} search records.
""")

W("_build/README.md", """# _build — reproducible pipeline

| Script | What it does |
|---|---|
| `crawl.py` | Seeds from `/workspace/cs50x-2026-kb/raw` (earlier crawl, same day), then BFS over `cs50.harvard.edu/x/` (excluding prior-year archives), English transcripts and ZIPs on `cdn.cs50.net` linked from those pages (also URLs that appear only as text, e.g. `wget` lines), selected `cs50.readthedocs.io` sections, `cs50.ai`/`cs50.dev` home pages and `manual.cs50.io` (cs50.h + curated function list). 1 request/second, descriptive User-Agent, no login. Every discovered URL is logged in `manifest.json` as fetched / failed (+reason) / skipped (+reason). `--no-cdn` skips cdn.cs50.net entirely (its robots.txt disallows `/`). ZIPs over 60 MB are skipped (HEAD check). |
| `crawl_listing.py` | Fallback for oversized source ZIPs: walks a cdn.cs50.net directory listing (default lecture 9 `src9/`) and fetches only small text files. |
| `build.py` | Generates every KB document from `raw/`, `downloads/` and `manifest.json` (+ structured fields from `/workspace/cs50x-2026-kb/kb.json`) and the generated Persian content in `curated/`. Writes `index.json`, `edges.json`, `search.jsonl`, `build_stats.json`. Deletes and regenerates everything outside `_build/`. |
| `htmlmd.py` | HTML → Markdown conversion preserving headings (with `<a id>` anchors), lists, tables, code blocks (with language), collapsible blocks, asciinema demos, embedded videos. |
| `validate.py` | Front matter keys, six sections, Source line in every official section, all relative links + anchors, index/edges/search integrity, counts vs manifest, fetched-but-unused sources → `validation.json`. |
| `spotcheck.py` | Re-fetches ≥5 live pages and compares with stored raw + KB text → `spotcheck.json`. |
| `finalize.py` | Writes README.md, LICENSE-NOTICE.md, `_templates/`, coverage-report.md. |
| `curated/fa_problems.py` | GENERATED Persian teaching notes, conceptual hints (no solutions), pitfalls and difficulty estimates per problem; per-week teaching notes. |
| `curated/concepts.py` | Concept catalogue: primary weeks, regex used to select verbatim passages from notes, related shorts, Persian explanation (GENERATED). |

Order: `python3 crawl.py && python3 crawl_listing.py && python3 build.py && python3 validate.py && python3 spotcheck.py && python3 finalize.py && python3 validate.py`

Requirements: Python 3.11+, `requests`, `beautifulsoup4`, `lxml`, `markdownify`, `pyyaml`.
`raw/` = fetched pages and transcripts (provenance; sha256 in manifest). `downloads/` = ZIPs (not included in the tarball because of size; re-run `crawl.py` to restore).
""")
print("finalized")
