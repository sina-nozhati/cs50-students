#!/usr/bin/env python3
"""Validate the KB: front matter, links, sources, counts, indexes. Writes _build/validation.json."""
import json, os, re, sys, urllib.parse as up
import yaml
B = os.path.dirname(os.path.abspath(__file__)); KB = os.path.dirname(B)
REQ = ["id", "type", "title", "week", "parent", "children", "prerequisites", "related", "source_urls", "source_type", "license",
       "retrieved_at", "review_status", "difficulty", "generated_difficulty", "languages", "tags", "checksum"]
NON_DOCS = {"README.md", "LICENSE-NOTICE.md", "coverage-report.md"}
res = dict(errors=[], warnings=[], checks={})
def err(m): res["errors"].append(m)
def warn(m): res["warnings"].append(m)

mds = []
for root, dirs, files in os.walk(KB):
    if "/_build" in root + "/" and root.startswith(os.path.join(KB, "_build")): continue
    for f in files:
        if f.endswith(".md"): mds.append(os.path.relpath(os.path.join(root, f), KB))
docs = {}
for p in mds:
    t = open(os.path.join(KB, p), encoding="utf-8").read()
    if p in NON_DOCS or p.startswith("_templates/"): continue
    if "-distribution/files/" in p or "/source-code/files/" in p or "/section-code/files/" in p: continue
    if not t.startswith("---\n"): err(f"no front matter: {p}"); continue
    fm = yaml.safe_load(t.split("\n---\n", 1)[0][4:])
    miss = [k for k in REQ if k not in fm]
    if miss: err(f"missing keys {miss}: {p}")
    if fm.get("source_type") in ("official", "mixed"):
        if not fm.get("source_urls"): err(f"official/mixed doc without source_urls: {p}")
        body = t.split("## 2. OFFICIAL CONTENT", 1)
        if len(body) < 2 or "> Source:" not in body[1][:2000]: err(f"official section lacks Source line: {p}")
    for s in ["## 1. Source metadata", "## 2. OFFICIAL CONTENT", "## 3. Learning objectives", "## 4. Relationships", "## 5. GENERATED", "## 6. References"]:
        if s not in t: err(f"missing section '{s}': {p}")
    docs[fm["id"]] = (p, fm)
res["checks"]["docs_with_front_matter"] = len(docs)

# links
anchors_cache = {}
def anchors(path):
    if path not in anchors_cache:
        t = open(os.path.join(KB, path), encoding="utf-8").read()
        a = set(re.findall(r'<a id="([^"]+)"></a>', t))
        for h in re.findall(r"^#+ (.+)$", t, re.M):
            a.add(re.sub(r"[^\w\- ]", "", h.lower()).strip().replace(" ", "-"))
        anchors_cache[path] = a
    return anchors_cache[path]
nlinks = nbad = 0
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
for p in mds:
    t = open(os.path.join(KB, p), encoding="utf-8").read()
    t = re.sub(r"```.*?```", "", t, flags=re.S)
    for m in LINK.finditer(t):
        u = m.group(1)
        if re.match(r"^[a-z]+:", u) or u.startswith("#") or u.startswith("<"): continue
        nlinks += 1
        path, _, frag = u.partition("#")
        tgt = os.path.normpath(os.path.join(os.path.dirname(p), up.unquote(path)))
        verbatim_file = "/files/" in p
        if not os.path.exists(os.path.join(KB, tgt)):
            if verbatim_file: warn(f"link inside verbatim distribution/source file points to a file not stored in KB: {p}: {u}"); continue
            nbad += 1; err(f"broken link in {p}: {u}"); continue
        if frag and tgt.endswith(".md") and frag not in anchors(tgt):
            nbad += 1; err(f"broken anchor in {p}: {u}")
res["checks"]["relative_links_checked"] = nlinks; res["checks"]["relative_links_broken"] = nbad

# indexes
idx = json.load(open(os.path.join(KB, "index.json")))
ids = {n["id"] for n in idx["nodes"]}
for i in docs:
    if i not in ids: err(f"doc not in index.json: {i}")
for n in idx["nodes"]:
    if not os.path.exists(os.path.join(KB, n["path"])): err(f"index path missing: {n['path']}")
    if n["parent"] and n["parent"] not in ids: err(f"index parent missing: {n['id']} -> {n['parent']}")
    for c in n["children"]:
        if c not in ids: err(f"index child missing: {n['id']} -> {c}")
edges = json.load(open(os.path.join(KB, "edges.json")))
for e in edges:
    if e["source"] not in ids or e["target"] not in ids: err(f"dangling edge {e}")
res["checks"]["index_nodes"] = len(idx["nodes"]); res["checks"]["edges"] = len(edges)
nsearch = 0
for line in open(os.path.join(KB, "search.jsonl"), encoding="utf-8"):
    r = json.loads(line); nsearch += 1
    if r.get("source_type") not in ("official", "generated", "metadata", "mixed"): err(f"bad source_type in search record {r['id']}")
    if r["doc_id"] not in ids: err(f"search record with unknown doc {r['id']}")
res["checks"]["search_records"] = nsearch

# counts vs manifest / old KB
M = json.load(open(os.path.join(B, "manifest.json")))
old = json.load(open("/workspace/cs50x-2026-kb/kb.json"))
bytype = {}
for i, (p, fm) in docs.items(): bytype[fm["type"]] = bytype.get(fm["type"], 0) + 1
expect = {
 "pset": sum(1 for p in old["problems"] if p["kind"] == "problem_set"),
 "practice": sum(1 for p in old["problems"] if p["kind"] != "problem_set"),
 "week": len(old["weeks"]), "pset-index": len(old["problem_sets"]),
 "short": sum(1 for u, e in M.items() if "/x/shorts/" in u and e["status"] == "fetched"),
 "section": sum(1 for u, e in M.items() if re.search(r"/x/sections/\d+/$", u) and e["status"] == "fetched"),
 "lecture": sum(1 for u, e in M.items() if re.search(r"/x/notes/[^/]+/$", u) and e["status"] == "fetched"),
}
man_fetched = sum(1 for u, e in M.items() if e.get("category") == "manual" and e["status"] == "fetched" and u.rstrip("/") != "https://manual.cs50.io")
expect["reference(manual pages)"] = man_fetched
got = dict(bytype); got["reference(manual pages)"] = sum(1 for i in docs if i.startswith("manual-"))
for k, v in expect.items():
    g = got.get(k, 0)
    res["checks"][f"count_{k}"] = f"{g}/{v}"
    if g != v: err(f"count mismatch {k}: docs={g} expected={v}")
stats = json.load(open(os.path.join(B, "build_stats.json")))
mapped = set(stats["mapped_urls"])
unmapped = [u for u, e in M.items() if e["status"] == "fetched" and e.get("category") in ("harvard", "readthedocs", "cdn-transcript", "cdn-zip", "cdn-file", "manual", "cs50.ai", "cs50.dev", "harvard-archive-2025") and u not in mapped]
res["checks"]["fetched_sources_not_mapped_to_a_doc"] = unmapped
for u in unmapped: warn(f"fetched but not used in any doc: {u}")
res["checks"]["manifest_status_counts"] = {s: sum(1 for e in M.values() if e["status"] == s) for s in ("fetched", "failed", "skipped")}
res["ok"] = not res["errors"]
json.dump(res, open(os.path.join(B, "validation.json"), "w"), indent=1)
print(json.dumps(res["checks"], indent=1)[:3000]); print("errors:", len(res["errors"]), res["errors"][:30]); print("warnings:", len(res["warnings"]), res["warnings"][:20])
