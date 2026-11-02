"""HTML -> Markdown conversion that keeps CS50's structure (headings, lists, code blocks, tables)."""
import re, urllib.parse as up
from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter

class Conv(MarkdownConverter):
    def convert_iframe(self, el, text, *args, **kw):
        src = el.get("src", "")
        return f"\n\n[Embedded video: {src.split('?')[0]}]({src.split('?')[0]})\n\n" if src else ""
    def convert_details(self, el, text, *args, **kw):
        summ = el.find("summary")
        st = summ.get_text(" ", strip=True) if summ else "Details"
        body = text
        lines = "\n".join("> " + l if l.strip() else ">" for l in body.strip().splitlines())
        return f"\n\n> **{st}** *(collapsible block on the source page)*\n>\n{lines}\n\n"
    def convert_summary(self, el, text, *args, **kw):
        return ""

def code_lang(el):
    node = el
    for _ in range(4):
        if node is None: break
        for c in node.get("class", []) or []:
            if c.startswith("language-") and c != "language-plaintext":
                return c[len("language-"):]
        node = node.parent
    return ""

def to_md(main, base_url, drop_toc=True):
    main = BeautifulSoup(str(main), "lxml")
    if drop_toc:
        for t in main.select("#markdown-toc"): t.decompose()
    for t in main.select("script[src*='asciinema']"):
        a = main.new_tag("p"); a.string = f"[Terminal demo recording (asciinema): {t['src'].replace('.js','')}]"
        t.replace_with(a)
    for t in main.select("script, style, button.btn-clipboard, nav, a.headerlink"): t.decompose()
    for sec in main.find_all("section", id=True):   # Sphinx puts anchors on <section id=...>
        h = sec.find(["h1", "h2", "h3", "h4", "h5", "h6"])
        if h is not None and not h.get("id"): h["id"] = sec["id"]
    # absolutise links and images
    for a in main.find_all("a", href=True):
        h = a["href"]
        if not h.startswith("#") and not h.startswith("mailto:"):
            a["href"] = up.urljoin(base_url, h)
        elif h.startswith("#"):
            a["href"] = base_url + h
    for im in main.find_all("img", src=True):
        im["src"] = up.urljoin(base_url, im["src"])
    # heading anchors: keep id as explicit anchor marker
    for h in main.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        if h.get("id"):
            anchor = main.new_tag("a"); anchor["id"] = h["id"]
            h.insert_before(NavigableString(f"\n\n<a id=\"{h['id']}\"></a>\n\n"))
    md = Conv(heading_style="ATX", bullets="*", code_language_callback=code_lang, escape_underscores=False,
              escape_asterisks=False, strip=["span"]).convert_soup(main)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    return md

def demote(md, levels=1):
    """Demote headings so official content nests under '## 2. OFFICIAL CONTENT'."""
    out = []
    infence = False
    for line in md.splitlines():
        if line.startswith("```"): infence = not infence
        if not infence and re.match(r"^#{1,5} ", line):
            line = "#" * levels + line
        out.append(line)
    return "\n".join(out)
