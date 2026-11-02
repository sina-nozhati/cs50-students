# CS50x Anzali week exports — generator (prototype 0.1.0)

Builds downloadable files for one week **only from the KB package** (`knowledge-base/weeks/<slug>/`): notes, overview, summary, glossary, problem-set guides, sources.json, fenced code, flashcards. No hand-written content beyond the templates.

```
python generate.py KB_DIR WEEK_SLUG OUT_DIR [--no-pdf] [--pdf-engine=weasy]
python verify.py OUT_DIR [--offline]      # PDF Persian text fidelity, links, code syntax
```

Outputs per week: `01-*-jozve` (overview + all notes + TOC), `02-*-kholase-vazhename` (summary + glossary), `03-*-rahnamaye-tamrin` (guides, refuses if a solution is marked provided), `04-*-source-code.zip` (runnable fenced code + README.fa.md + official src link), `05-*-slides.html` (link card only), `06-*-flashcards` (printable), `index.html`, `build-report.json`.

- HTML: one self-contained file (inline CSS, base64 fonts, inline images from the official notes with credit, tiny copy-code script). Works offline in any browser; print stylesheet included.
- PDF: printed from the same HTML by headless Chromium (`CHROME` env var, default `google-chrome`), then metadata/ID/structure ids fixed with PyMuPDF so the bytes are reproducible. `--pdf-engine=weasy` is a no-browser fallback.
- Deterministic: timestamps come from the package (`max(verified_at, sources.generated_at)`), ZIP entries use a fixed date; images are cached in `cache/` by URL hash.
- Deps (see requirements.txt): jinja2, markdown, pygments, pymupdf, (weasyprint optional), Chromium for PDF; poppler-utils for verify.

Porting to Flask: call `generate.main` per week at package-build time (or on KB version change), store outputs under `static/downloads/<kb_version>/<week>/`, serve with long cache headers + ETag = sha256. Do not render on request.
