# Coverage report — CS50x knowledge base

Built: 2026-10-18T06:00:54+03:30 (Asia/Tehran). Crawl: 2026-10-18 (Asia/Tehran), 1 request/second, User-Agent `CS50xAnzali-KB-builder/2.0`, no login, no paid services.

## 1. Summary
- **Documents (Markdown with front matter):** 332  ·  **Transcript files:** 65  ·  **Glossary entries:** 179  ·  **search.jsonl records:** 7577
- **KB size (excluding `_build/`):** 17.3 MB
- **Docs by type:** concept 51, concept-index 1, course 1, course-page 18, final-project 1, glossary 1, lecture 12, practice 22, project 3, pset 35, pset-index 10, reference 76, reference-index 2, section 9, short 44, source-code 11, tool 22, tool-index 1, week 12
- **Docs by source_type:** generated 7, mixed 56, official 269
- **Docs by review_status:** partially-verified 61, unverified 6, verified-against-source 265
- **Manifest URLs:** 7603 total — fetched 562, failed 2, skipped 7039 (every discovered URL is logged in `_build/manifest.json`).

## 2. Sources reviewed (fetched)
| Category | Fetched |
|---|---:|
| harvard | 162 |
| cdn-listing-file | 115 |
| manual | 75 |
| cdn-transcript | 65 |
| cdn-listing | 54 |
| cdn-zip | 50 |
| readthedocs | 21 |
| harvard-archive-2025 | 12 |
| cdn-file | 6 |
| cs50.ai | 1 |
| cs50.dev | 1 |

Category meanings: `harvard` = cs50.harvard.edu/x pages (home, 12 week pages, 12 lecture notes, 9 sections, 44 shorts, 10 pset indexes, 35 problem specs, 22 practice problems, practice/psets/weeks/sections indexes, project, syllabus, FAQs, honesty, certificate, license, communities, staff, seminars, gallery, puzzles, zoom, courses); `harvard-archive-2025` = 12 CS50x 2025 pset pages kept only for the year-over-year comparison; `cdn-transcript` = English .txt transcripts (12 lectures, 9 sections, 44 shorts); `cdn-zip` = lecture source, section source, problem-set and practice distribution ZIPs; `cdn-listing`/`cdn-listing-file` = directory listing + small text files of lecture 9 source (fallback, ZIP too large); `readthedocs` = cs50.readthedocs.io pages (check50, submit50, style50, help50, CS50 library C/Python, codespace, cs50.dev, CS50.ai, manual, video player, certificates, terminal, C style guide); `manual` = manual.cs50.io index + 74 function pages; `cs50.ai`, `cs50.dev` = public home pages.

## 3. Sources not reviewed

### 3a. Failed (2)
- https://cs50.harvard.edu/x/sections/psets/7/songs — HTTP 404 (broken relative link on the official Section page; not a KB error)
- https://cs50.readthedocs.io/libraries/cs50/c/cli50/ — HTTP 404 (linked from the CS50 docs; page does not exist)

### 3b. Skipped (grouped; full list in `_build/manifest.json`)
| Category | Reason | Count | Example |
|---|---|---:|---|
| video | video page; URL recorded only (no video download, no YouTube crawling) | 5710 | https://video.cs50.io/ |
| cdn-media | video/audio file; URL recorded only | 468 | https://cdn.cs50.net/2017/fall/shorts/ajax/ajax-1080p.mp4.download |
| external | non-official or out-of-scope domain; URL recorded only | 355 | http://astyle.sourceforge.net/ |
| cdn-other | individual lecture/section source file; covered by the source ZIP (or listing fallback) | 122 | https://cdn.cs50.net/2025/fall/lectures/4/src4/addresses0.c?download |
| cdn-pdf | PDF (slides/source printout); content covered by notes/source zip; not downloaded | 96 | https://cdn.cs50.net/2016/x/events/puzzles/packet.pdf |
| cdn-subtitles | subtitle file (.srt) duplicates the .txt transcript; URL recorded only | 89 | https://cdn.cs50.net/2017/fall/shorts/ajax/lang/en/ajax.srt |
| cs50-app | CS50 web application / redirector (login or app); URL recorded only | 38 | https://certificates.cs50.io/ |
| cdn-transcript-other-lang | non-English transcript; English transcript fetched instead | 24 | https://cdn.cs50.net/2025/fall/lectures/0/lang/es/clase0.txt |
| harvard-other | outside CS50x (/x/) scope | 24 | https://cs50.harvard.edu/ai |
| rtd-other | readthedocs page outside selected course-relevant scope | 22 | https://cs50.readthedocs.io/cli50/ |
| slides | Google Slides (external app); URL recorded only | 22 | https://docs.google.com/presentation/d/1-DqiLRbks97oBXeYKZUbZpc0yFcTWwKNpMwsHFfap28/edit?usp=sharing |
| cdn-index | directory listing; the corresponding .zip is downloaded instead | 17 | https://cdn.cs50.net/2025/fall/lectures/0/src0/ |
| cdn-listing-file | inventory only (binary or > 102400 bytes) | 15 | https://cdn.cs50.net/2025/fall/lectures/9/src9/froshims3/static/cat.jpg |
| rtd-asset | Sphinx source/static asset | 15 | https://cs50.readthedocs.io/_sources/certificates.cs50.io.md.txt |
| cs50.dev | application page | 9 | https://cs50.dev/.devcontainer.json |
| rtd-other | Harvard dining/map API docs; not course-relevant | 3 | https://cs50.readthedocs.io/api/dining/ |
| cdn-other | cdn file type .ipynb not needed | 2 | https://cdn.cs50.net/2022/fall/seminars/python_for_data_science/datascience.ipynb |
| cdn-other | cdn file type .db not needed | 2 | https://cdn.cs50.net/2025/fall/lectures/7/src7/imdb/shows.db?download |
| cdn-zip | too large (140278028 bytes > 62914560) | 1 | https://cdn.cs50.net/2025/fall/lectures/9/src9.zip |
| cdn-other | cdn file type .jpg not needed | 1 | https://cdn.cs50.net/2025/fall/lectures/9/src9/froshims4/static/cat.jpg |
| cdn-zip | too large (77017284 bytes > 62914560) | 1 | https://cdn.cs50.net/2026/x/psets/7/movies.zip |
| harvard | HTTP 302 redirect to canonical https://cs50.harvard.edu/x/ (fetched there); duplicate | 1 | https://cs50.harvard.edu/x/2026/ |
| manual | manual page linked; only cs50.h + curated function pages are fetched (see manual category) | 1 | https://manual.cs50.io |
| manual | not listed in manual.cs50.io index | 1 | https://manual.cs50.io/3/sizeof |

## 4. Content coverage per week
| Week | Lecture notes | Lecture transcript | Section (+transcript) | Shorts (with transcript) | PSet problems | Practice | Source code (stored / inventoried files) |
|---|---|---|---|---|---|---|---|
| Week 0 — Scratch | ✓ verified-against-source | ✓ | — (no section page linked) | 0 (0) | 1 | 0 | 0 / 21 |
| Week 1 — C | ✓ verified-against-source | ✓ | ✓ (+transcript) | 6 (6) | 6 | 3 | 41 / 41 |
| Week 2 — Arrays | ✓ verified-against-source | ✓ | ✓ (+transcript) | 6 (6) | 4 | 3 | 35 / 35 |
| Week 3 — Algorithms | ✓ verified-against-source | ✓ | ✓ (+transcript) | 7 (7) | 4 | 4 | 6 / 6 |
| Week 4 — Memory | ✓ verified-against-source | ✓ | ✓ (+transcript) | 5 (5) | 4 | 2 | 34 / 34 |
| Week 5 — Data Structures | ✓ verified-against-source | ✓ | ✓ (+transcript) | 8 (8) | 2 | 1 | 10 / 10 |
| Week 6 — Python | ✓ verified-against-source | ✓ | ✓ (+transcript) | 1 (1) | 7 | 5 | 70 / 98 |
| Week 7 — SQL | ✓ verified-against-source | ✓ | ✓ (+transcript) | 1 (1) | 3 | 2 | 12 / 14 |
| Artificial Intelligence — Artificial Intelligence | ✓ verified-against-source | ✓ | — (no section page linked) | 0 (0) | 0 | 0 | 34 / 63 |
| Week 8 — HTML, CSS, JavaScript | ✓ verified-against-source | ✓ | ✓ (+transcript) | 8 (8) | 2 | 1 | 43 / 47 |
| Week 9 — Flask | ✓ verified-against-source | ✓ | ✓ (+transcript) | 2 (2) | 2 | 1 | 115 / 130 |
| Week 10 | ✓ verified-against-source | ✓ | — (no section page linked) | 0 (0) | 0 | 0 | — |

Course-level: home, syllabus, FAQs, academic honesty, certificate, license, communities, staff, seminars, puzzles, zoom, courses, index pages, gallery (intro + counts only), compiled deadlines & grading, changes vs 2025 (generated), final project.
Tools: 22 tool docs (+ index). Reference: C style guide, Python style pointer, 74 manual pages. Concepts: 51. Glossary: 179 entries.

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
- `course-gallery`: The gallery lists thousands of student final-project videos; per-project entries were deliberately NOT extracted (size; they are student works, not course content). Only intro text and counts are recorded.
- `course-deadlines-and-grading`: Passages were selected automatically by keyword; read the full pages (course/certificate.md, course/syllabus.md, course/faqs.md) for complete context.
- `week-9-source-code`: ZIP not downloaded (zip skipped: too large (140278028 bytes > 62914560)); inventory built from the cdn.cs50.net directory listing https://cdn.cs50.net/2025/fall/lectures/9/src9/ instead (small text files stored; binaries listed only).
- `pset-7-movies`: https://cdn.cs50.net/2026/x/psets/7/movies.zip: zip skipped: too large (77017284 bytes > 62914560)
- `tool-debug50`: No dedicated official documentation page for this tool was fetched; passages were auto-selected from course pages by keyword.
- `tool-valgrind`: No dedicated official documentation page for this tool was fetched; passages were auto-selected from course pages by keyword.
- `tool-duck-in-course-policy`: No dedicated official documentation page for this tool was fetched; passages were auto-selected from course pages by keyword.
- `reference-style-guide-python`: PEP 8 (peps.python.org) is outside the official CS50 domains in scope and was not extracted.
- `reference-manual`: Only a curated subset of manual.cs50.io (about 1,700 pages listed) was fetched; see manifest category `manual` for names that were requested but not listed in the index.
- `concept-binary`: Passages were matched automatically with the regex `\bbinary\b|\bbits?\b|\bbytes?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-algorithms-and-pseudocode`: Passages were matched automatically with the regex `\balgorithms?\b|\bpseudocode\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-abstraction`: Passages were matched automatically with the regex `\babstraction\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-functions`: Passages were matched automatically with the regex `\bfunctions?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-variables`: Passages were matched automatically with the regex `\bvariables?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-conditionals`: Passages were matched automatically with the regex `\bconditionals?\b|\bboolean\b|\bif\b statement`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-loops`: Passages were matched automatically with the regex `\bloops?\b|\bwhile\b|\bfor\b loop|do while`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-data-types`: Passages were matched automatically with the regex `\btypes?\b.*\b(int|float|char|long|double|bool|string)\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-operators`: Passages were matched automatically with the regex `\boperators?\b|\bmodulo\b|\bremainder\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-compiling`: Passages were matched automatically with the regex `\bcompil(e|er|ing|ed)\b|\bclang\b|\bmake\b|\blinking\b|\bassembl`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-integer-overflow-and-floating-point-imprecision`: Passages were matched automatically with the regex `\boverflow\b|\bimprecision\b|\btruncat`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-correctness-design-style`: Passages were matched automatically with the regex `\bcorrectness\b|\bdesign\b|\bstyle\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-command-line`: Passages were matched automatically with the regex `\bcommand[- ]line\b|\bterminal\b|\bcd\b|\bls\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-command-line-arguments`: Passages were matched automatically with the regex `\bargc\b|\bargv\b|command-line argument`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-arrays`: Passages were matched automatically with the regex `\barrays?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-strings`: Passages were matched automatically with the regex `\bstrings?\b|\bNUL\b|\\0`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-debugging`: Passages were matched automatically with the regex `\bdebug|\bbugs?\b|\brubber duck\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-scope`: Passages were matched automatically with the regex `\bscope\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-linear-search`: Passages were matched automatically with the regex `\blinear search\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-binary-search`: Passages were matched automatically with the regex `\bbinary search\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-running-time-big-o`: Passages were matched automatically with the regex `\bbig o\b|\brunning time\b|\bomega\b|\btheta\b|O\(n|O\(log|O\(1\)`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-selection-and-bubble-sort`: Passages were matched automatically with the regex `\bselection sort\b|\bbubble sort\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-merge-sort`: Passages were matched automatically with the regex `\bmerge sort\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-recursion`: Passages were matched automatically with the regex `\brecursi(on|ve|vely)\b|\bbase case\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-structs`: Passages were matched automatically with the regex `\bstruct\b|\btypedef\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-hexadecimal-and-memory-addresses`: Passages were matched automatically with the regex `\bhexadecimal\b|\baddress(es)?\b|\b0x`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-pointers`: Passages were matched automatically with the regex `\bpointers?\b|\bdereferenc`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-dynamic-memory-allocation`: Passages were matched automatically with the regex `\bmalloc\b|\bfree\b|\brealloc\b|\bheap\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-memory-errors-and-valgrind`: Passages were matched automatically with the regex `\bvalgrind\b|\bleak|\bgarbage values?\b|\bsegmentation fault\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-stack-and-heap`: Passages were matched automatically with the regex `\bstack\b|\bheap\b|\bstack overflow\b|\bbuffer overflow\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-file-io`: Passages were matched automatically with the regex `\bfopen\b|\bfclose\b|\bfread\b|\bfwrite\b|\bfprintf\b|\bFILE\b|\bfiles?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-linked-lists`: Passages were matched automatically with the regex `\blinked lists?\b|\bnodes?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-trees`: Passages were matched automatically with the regex `\btrees?\b|\bbinary search tree\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-hash-tables`: Passages were matched automatically with the regex `\bhash(ing)? tables?\b|\bhash functions?\b|\bhashing\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-tries`: Passages were matched automatically with the regex `\btries\b|\btrie\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-stacks-and-queues`: Passages were matched automatically with the regex `\bqueues?\b|\bstacks?\b|\bLIFO\b|\bFIFO\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-python-basics`: Passages were matched automatically with the regex `\bpython\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-dictionaries`: Passages were matched automatically with the regex `\bdict(ionary|ionaries)?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-exceptions`: Passages were matched automatically with the regex `\bexceptions?\b|\btry\b|\bexcept\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-sql-basics`: Passages were matched automatically with the regex `\bSQL\b|\bSELECT\b|\bdatabases?\b|\btables?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-sql-joins-and-keys`: Passages were matched automatically with the regex `\bJOIN\b|\bprimary key\b|\bforeign key\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-sql-injection-and-race-conditions`: Passages were matched automatically with the regex `\binjection\b|\brace conditions?\b|\btransactions?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-internet-and-http`: Passages were matched automatically with the regex `\bTCP\b|\bIP\b|\bDNS\b|\bHTTPS?\b|\brouters?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-html-and-css`: Passages were matched automatically with the regex `\bHTML\b|\bCSS\b|\btags?\b|\bselectors?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-javascript-and-dom`: Passages were matched automatically with the regex `\bJavaScript\b|\bDOM\b|\bevents?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-flask-and-routes`: Passages were matched automatically with the regex `\bFlask\b|\broutes?\b|\bJinja\b|\btemplates?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-forms-get-post`: Passages were matched automatically with the regex `\bGET\b|\bPOST\b|\bforms?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-sessions-and-cookies`: Passages were matched automatically with the regex `\bsessions?\b|\bcookies?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-mvc`: Passages were matched automatically with the regex `\bMVC\b|\bmodel\b.*\bview\b|\bcontroller\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-ajax-and-apis`: Passages were matched automatically with the regex `\bAJAX\b|\bAPIs?\b|\bJSON\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `concept-artificial-intelligence`: Passages were matched automatically with the regex `\bartificial intelligence\b|\bAI\b|\blarge language models?\b|\bLLMs?\b|\bmachine learning\b|\bneural networks?\b`; they are verbatim, but the selection may miss the best definition or include incidental mentions.
- `glossary`: Automatic term extraction: some entries are emphasis rather than definitions; defined terms that are not italicised are missing.

## 6. Unverified / generated items
- All **section 3b and section 5** content (Persian teaching use, hints, AI-tutor guidance, feature ideas) is GENERATED and has not been reviewed by CS50 or by a human teacher.
- `generated_difficulty` values are the builder’s estimates (CS50 states only comfort levels such as “less comfortable”).
- `language` per problem and `key_concepts`/English summaries come from the earlier KB (`/workspace/cs50x-2026-kb`), marked as paraphrase.
- **Concept docs, glossary, deadlines-and-grading, debug50/valgrind/duck docs** quote official text verbatim, but the *selection* of passages was automatic (keyword regex) → `review_status: partially-verified`.
- Prerequisite links (week → previous week, problem → week lecture) are generated.
- `project/` documents are generated and refer to the repo audit; they were not checked against the current repo code (the repo was not touched).

## 7. Validation results
- Errors: **0**; warnings: 1
- Documents with complete front matter and all 6 sections: 332
- Relative links checked: 2886; broken: 0
- index.json nodes: 397; edges.json edges: 967; search.jsonl records: 7577
- Counts vs manifest: pset 35/35, practice 22/22, week 12/12, pset-index 10/10, short 44/44, section 9/9, lecture 12/12, reference(manual pages) 74/74
- Fetched sources not used by any document: 0
- warning: link inside verbatim distribution/source file points to a file not stored in KB: weeks/week-03-algorithms/practice/snackbar-distribution/files/snackbar/README.md: beach-g1e2b206d7_1280.jpg

### Spot-check against live pages
| Doc | Live URL | HTTP | Raw vs live main text | Sampled sentences found live |
|---|---|---|---|---|
| `weeks/week-03-algorithms/psets/tideman.md` | https://cs50.harvard.edu/x/psets/3/tideman/ | 200 | identical | 7/8 |
| `weeks/week-04-memory/lecture.md` | https://cs50.harvard.edu/x/notes/4/ | 200 | identical | 8/8 |
| `weeks/week-04-memory/shorts/pointers.md` | https://cs50.harvard.edu/x/shorts/pointers/ | 200 | identical | 8/8 |
| `course/honesty.md` | https://cs50.harvard.edu/x/honesty/ | 200 | identical | 8/8 |
| `final-project/README.md` | https://cs50.harvard.edu/x/project/ | 200 | identical | 8/8 |
| `reference/manual/get_string.md` | https://manual.cs50.io/3/get_string | 200 | identical | 6/7 |
| `tools/submit50.md` | https://cs50.readthedocs.io/submit50/ | 200 | identical | 8/8 |
| `weeks/week-07-sql/psets/fiftyville.md` | https://cs50.harvard.edu/x/psets/7/fiftyville/ | 200 | identical | 8/8 |

“Raw vs live” compares the main text of the stored raw page with a fresh fetch. “Sampled sentences” are random sentences from section 2 of the KB doc looked up in the live page (for shorts: in the live transcript); misses were inspected and are Markdown/markup artifacts of the checker (e.g. code blocks, image alt text), not content differences.

## 8. Final KB tree
```
cs50x-kb/
  LICENSE-NOTICE.md
  _build/  (crawler, builder, validator, manifest, raw sources)
  _templates/
    document-template.md
  concepts/
    README.md
    abstraction.md
    ajax-and-apis.md
    algorithms-and-pseudocode.md
    arrays.md
    artificial-intelligence.md
    binary-search.md
    binary.md
    command-line-arguments.md
    command-line.md
    compiling.md
    conditionals.md
    correctness-design-style.md
    data-types.md
    debugging.md
    dictionaries.md
    dynamic-memory-allocation.md
    exceptions.md
    file-io.md
    flask-and-routes.md
    forms-get-post.md
    functions.md
    hash-tables.md
    hexadecimal-and-memory-addresses.md
    html-and-css.md
    integer-overflow-and-floating-point-imprecision.md
    internet-and-http.md
    javascript-and-dom.md
    linear-search.md
    linked-lists.md
    loops.md
    memory-errors-and-valgrind.md
    merge-sort.md
    mvc.md
    operators.md
    pointers.md
    python-basics.md
    recursion.md
    running-time-big-o.md
    scope.md
    selection-and-bubble-sort.md
    sessions-and-cookies.md
    sql-basics.md
    sql-injection-and-race-conditions.md
    sql-joins-and-keys.md
    stack-and-heap.md
    stacks-and-queues.md
    strings.md
    structs.md
    trees.md
    tries.md
    variables.md
  course/
    README.md
    certificate.md
    changes-vs-2025.md
    communities.md
    courses.md
    deadlines-and-grading.md
    faqs.md
    gallery.md
    honesty.md
    license.md
    practice-index.md
    psets-index.md
    puzzles.md
    sections-index.md
    seminars.md
    staff.md
    syllabus.md
    weeks-index.md
    zoom.md
  edges.json
  final-project/
    README.md
  glossary.md
  index.json
  project/
    README.md
    ai-tutor-policy.md
    site-model-mapping.md
  reference/
    README.md
    manual/
      README.md
      abs.md
      assert.md
      atof.md
      atoi.md
      atol.md
      calloc.md
      ceil.md
      drand48.md
      exit.md
      fabs.md
      fclose.md
      feof.md
      ferror.md
      fgetc.md
      fgets.md
      floor.md
      fopen.md
      fprintf.md
      fputc.md
      fputs.md
      fread.md
      free.md
      fscanf.md
      fwrite.md
      get_char.md
      get_double.md
      get_float.md
      get_int.md
      get_long.md
      get_long_long.md
      get_string.md
      getchar.md
      isalnum.md
      isalpha.md
      isblank.md
      isdigit.md
      islower.md
      ispunct.md
      isspace.md
      isupper.md
      malloc.md
      memcpy.md
      memset.md
      pow.md
      printf.md
      putchar.md
      puts.md
      qsort.md
      rand.md
      realloc.md
      round.md
      roundf.md
      scanf.md
      sleep.md
      snprintf.md
      sprintf.md
      sqrt.md
      srand.md
      srand48.md
      strcasecmp.md
      strcat.md
      strchr.md
      strcmp.md
      strcpy.md
      strdup.md
      strlen.md
      strncpy.md
      strstr.md
      strtok.md
      strtol.md
      time.md
      tolower.md
      toupper.md
      usleep.md
    style-guide-c.md
    style-guide-python.md
  search.jsonl
  tools/
    README.md
    certificates.md
    check50/
      README.md
      check-writer.md
      check50-user.md
      extension-writer.md
      json-specification.md
    codespace.md
    cs50-ai-duck.md
    cs50-dev.md
    cs50-docs-index.md
    cs50-library/
      README.md
      c.md
      python.md
    debug50.md
    duck-in-course-policy.md
    help50.md
    manual-pages.md
    style50.md
    submit50.md
    terminal.md
    valgrind.md
    video-player.md
  weeks/
    week-00-scratch/
      lecture.md
      psets/  (2 files)
      source-code/  (1 files)
      transcripts/  (1 files)
      week.md
    week-01-c/
      lecture.md
      practice/  (6 files)
      psets/  (7 files)
      section-code/  (3 files)
      sections.md
      shorts/  (6 files)
      source-code/  (42 files)
      transcripts/  (8 files)
      week.md
    week-02-arrays/
      lecture.md
      practice/  (6 files)
      psets/  (5 files)
      section-code/  (4 files)
      sections.md
      shorts/  (6 files)
      source-code/  (36 files)
      transcripts/  (8 files)
      week.md
    week-03-algorithms/
      lecture.md
      practice/  (9 files)
      psets/  (15 files)
      section-code/  (3 files)
      sections.md
      shorts/  (7 files)
      source-code/  (7 files)
      transcripts/  (9 files)
      week.md
    week-04-memory/
      lecture.md
      practice/  (6 files)
      psets/  (17 files)
      section-code/  (3 files)
      sections.md
      shorts/  (5 files)
      source-code/  (35 files)
      transcripts/  (7 files)
      week.md
    week-05-data-structures/
      lecture.md
      practice/  (3 files)
      psets/  (37 files)
      section-code/  (2 files)
      sections.md
      shorts/  (8 files)
      source-code/  (11 files)
      transcripts/  (10 files)
      week.md
    week-06-python/
      lecture.md
      practice/  (10 files)
      psets/  (31 files)
      section-code/  (3 files)
      sections.md
      shorts/  (1 files)
      source-code/  (71 files)
      transcripts/  (3 files)
      week.md
    week-07-sql/
      lecture.md
      practice/  (5 files)
      psets/  (15 files)
      sections.md
      shorts/  (1 files)
      source-code/  (13 files)
      transcripts/  (3 files)
      week.md
    week-08-html-css-javascript/
      lecture.md
      practice/  (4 files)
      psets/  (7 files)
      section-code/  (1 files)
      sections.md
      shorts/  (8 files)
      source-code/  (44 files)
      transcripts/  (10 files)
      week.md
    week-09-flask/
      lecture.md
      practice/  (1 files)
      psets/  (13 files)
      section-code/  (3 files)
      sections.md
      shorts/  (2 files)
      source-code/  (116 files)
      transcripts/  (4 files)
      week.md
    week-10/
      lecture.md
      transcripts/  (1 files)
      week.md
    week-ai-artificial-intelligence/
      lecture.md
      source-code/  (35 files)
      transcripts/  (1 files)
      week.md
```
