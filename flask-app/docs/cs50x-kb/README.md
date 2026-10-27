# CS50x 2026 — Hierarchical Knowledge Base (for CS50x Anzali)

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
concepts/                    51 concept docs (verbatim definitions from notes + Persian explanation)
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

Counts at build 2026-10-18T06:00:54+03:30: 332 documents, 65 transcript files, 7577 search records.
