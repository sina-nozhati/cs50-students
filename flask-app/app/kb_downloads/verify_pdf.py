"""Persian text-fidelity check: share of Persian words of the HTML that pdftotext/pymupdf recovers from the PDF."""
from __future__ import annotations

import html as H
import json
import re
import shutil
import subprocess
import sys


def words(t: str) -> list[str]:
    """Extract Persian words of length >= 2."""
    return re.findall(r"[\u0621-\u065F\u0670-\u06D3\u200c]{2,}", t)


def extract_pdf_text(pdf_path: str) -> str:
    """Extract text from PDF using pdftotext if available, then pymupdf, then pure fallback."""
    if shutil.which("pdftotext"):
        try:
            r = subprocess.run(["pdftotext", "-layout", pdf_path, "-"], capture_output=True, text=True, timeout=30)
            if r.returncode == 0:
                return r.stdout
        except Exception:
            pass

    try:
        import pymupdf
        d = pymupdf.open(pdf_path)
        txt = "\n".join(page.get_text() for page in d)
        d.close()
        return txt
    except ImportError:
        pass

    # Basic binary stream text extraction fallback
    try:
        with open(pdf_path, "rb") as f:
            data = f.read().decode("latin1", errors="ignore")
        # Extract plain text stream chunks
        stream_chunks = re.findall(r"stream[\r\n]+(.*?)[\r\n]+endstream", data, flags=re.S)
        return " ".join(stream_chunks)
    except Exception:
        return ""


def check(html_path: str, pdf_path: str) -> dict[str, Any]:
    src = H.unescape(
        re.sub(r"<script.*?</script>|<style.*?</style>|<[^>]+>", " ", open(html_path, encoding="utf-8").read(), flags=re.S)
    )
    out = extract_pdf_text(pdf_path)
    sw = words(src)
    pw = set(words(out))
    pw_nz = {w.replace("\u200c", "") for w in pw}

    if not sw:
        return {"words": 0, "exact": 1.0, "ignoring_zwnj": 1.0, "lam_alef_words": 0, "lam_alef_lost": 0}

    exact = sum(w in pw for w in sw) / len(sw)
    nozw = sum(w.replace("\u200c", "") in pw_nz for w in sw) / len(sw)
    lamalef = sum(1 for w in sw if "لا" in w)
    broken = sum(1 for w in sw if "لا" in w and w.replace("\u200c", "") not in pw_nz)
    return {
        "words": len(sw),
        "exact": round(exact, 4),
        "ignoring_zwnj": round(nozw, 4),
        "lam_alef_words": lamalef,
        "lam_alef_lost": broken,
    }


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: verify_pdf.py HTML_FILE PDF_FILE")
        sys.exit(1)
    print(json.dumps(check(sys.argv[1], sys.argv[2]), ensure_ascii=False, indent=2))
