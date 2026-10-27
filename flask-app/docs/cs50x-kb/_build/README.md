# _build — reproducible pipeline

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
