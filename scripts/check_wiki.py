#!/usr/bin/env python3
"""Chequeo de calidad de la wiki de hematología.

Verifica en las páginas clínicas (docs/benigna, docs/hemato-onco, docs/transversal):
  1. Que tengan "Última revisión".
  2. Que toda cita [n] exista en docs/referencias.md.
  3. Que los enlaces internos (.md) apunten a archivos existentes.
  4. Informa cuántos ítems [PV] (pendientes de verificación) quedan por página.

Uso (desde la raíz del proyecto):  python3 scripts/check_wiki.py
Sale con código 1 si hay errores (citas inexistentes, enlaces rotos, falta de fecha).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CLINICAL_DIRS = ["benigna", "hemato-onco", "transversal"]

ref_text = (DOCS / "referencias.md").read_text(encoding="utf-8")
valid_refs = {int(m) for m in re.findall(r"^\|\s*(\d+)\s*\|", ref_text, flags=re.M)}

link_re = re.compile(r"\[[^\]]*\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")
cite_re = re.compile(r"\[(\d{1,3})\]")
# Cuenta solo la marca en negrita [PV]; se ignoran las explicaciones de la propia marca.
pv_re = re.compile(r"\*\*\[PV\]\*\*")

errors = 0
print(f"Referencias válidas en la lista: {sorted(valid_refs)}\n")

for d in CLINICAL_DIRS:
    for md in sorted((DOCS / d).glob("*.md")):
        text = md.read_text(encoding="utf-8")
        rel = md.relative_to(DOCS)
        is_index = md.name == "index.md"
        problems = []

        if not is_index and "Última revisión" not in text:
            problems.append("falta 'Última revisión'")

        # Citas [n] (se ignoran los enlaces tipo [texto](url) y las casillas [ ] / [x])
        body = re.sub(r"\]\([^)]*\)", "]", text)
        cited = {int(n) for n in cite_re.findall(body)}
        missing = sorted(n for n in cited if n not in valid_refs)
        if missing:
            problems.append(f"citas sin referencia: {missing}")

        for target in link_re.findall(text):
            if target.startswith("http"):
                continue
            if not (md.parent / target).resolve().exists():
                problems.append(f"enlace roto: {target}")

        pv = len(pv_re.findall(text))
        status = "OK " if not problems else "ERR"
        print(f"[{status}] {rel}  | citas: {len(cited)} | [PV] pendientes: {pv}")
        for p in problems:
            errors += 1
            print(f"       - {p}")

print()
if errors:
    print(f"{errors} problema(s) encontrados.")
    sys.exit(1)
print("Sin errores.")
