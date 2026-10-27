#!/usr/bin/env python3
"""Merge integration/index.fragment.json into a COPY of the loader index.json.

Usage:
  python _tools/merge_index_fragment.py --index flask-app/docs/cs50x-kb/index.json --fragment flask-app/docs/cs50x-kb/anzali-fa/integration/index.fragment.json [--out flask-app/docs/cs50x-kb/index.json] [--mount anzali-fa/]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description="Merge KB index fragment into index.json")
    ap.add_argument("--index", required=True, help="Path to input index.json")
    ap.add_argument("--fragment", required=True, help="Path to index.fragment.json")
    ap.add_argument("--out", default=None, help="Output path (default: in-place overwrite if specified, or out/index.merged.json)")
    ap.add_argument("--mount", default="anzali-fa/", help="Prefix mount in KB tree (default: anzali-fa/)")
    ap.add_argument("--force", action="store_true", help="Allow overwrite of input index")
    a = ap.parse_args()

    idx_path = Path(a.index).resolve()
    frag_path = Path(a.fragment).resolve()
    out_path = Path(a.out).resolve() if a.out else (idx_path if a.force else Path("_tools/out/index.merged.json").resolve())

    if not idx_path.exists():
        sys.exit(f"Error: index file not found at {idx_path}")
    if not frag_path.exists():
        sys.exit(f"Error: fragment file not found at {frag_path}")

    with open(idx_path, encoding="utf-8") as f:
        idx = json.load(f)
    with open(frag_path, encoding="utf-8") as f:
        frag = json.load(f)

    byid = {n["id"]: n for n in idx["nodes"]}
    clash = [n["id"] for n in frag["nodes"] if n["id"] in byid]
    if clash:
        print(f"Warning: {len(clash)} node IDs already present in index (will be updated): {clash}")
        # به‌روزرسانی نودهای موجود
        for n in frag["nodes"]:
            nid = n["id"]
            if nid in byid:
                byid[nid].update(n)

    # افزودن نودهای جدید
    new_nodes = [dict(n) for n in frag["nodes"] if n["id"] not in byid]
    orig_mount = frag.get("mount_prefix", "")
    if a.mount and a.mount != orig_mount:
        for n in new_nodes:
            if orig_mount and n.get("path", "").startswith(orig_mount):
                n["path"] = a.mount + n["path"][len(orig_mount):]
            elif not n.get("path", "").startswith(a.mount):
                n["path"] = a.mount + n.get("path", "")

    for att in frag.get("attach_to", []):
        pid = att.get("parent_id")
        cid = att.get("append_child")
        p = byid.get(pid)
        if p is None:
            sys.exit(f"Error: missing parent node {pid}")
        p.setdefault("children", [])
        if cid not in p["children"]:
            p["children"].append(cid)

    idx["nodes"].extend(new_nodes)

    # صحت‌سنجی نبود آیدی تکراری
    ids = [n["id"] for n in idx["nodes"]]
    if len(ids) != len(set(ids)):
        sys.exit("Error: duplicate IDs detected in merged nodes")

    allid = set(ids)
    for n in idx["nodes"]:
        for c in n.get("children") or []:
            if c not in allid:
                sys.exit(f"Error: dangling child {c} in {n['id']}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=2)

    print(f"Successfully merged {len(frag['nodes'])} nodes into {out_path} (total: {len(idx['nodes'])} nodes)")


if __name__ == "__main__":
    main()
