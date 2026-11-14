#!/usr/bin/env python3
"""Genera docs/novedades.md con artículos recientes de PubMed por tema.

Lee scripts/vigilancia.json (temas, consultas, ventana en días) y consulta la API
pública de PubMed (E-utilities). Solo usa la biblioteca estándar de Python.
No modifica ninguna página clínica: la lista es un insumo para revisión humana.

Uso (desde la raíz del proyecto):  python3 scripts/novedades_pubmed.py
Si PubMed no responde, termina con código 1 y deja novedades.md como estaba.
"""
import datetime
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "scripts" / "vigilancia.json"
SALIDA = ROOT / "docs" / "novedades.md"
API = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
PAUSA = 0.4  # PubMed admite 3 solicitudes por segundo sin clave


def pedir(endpoint, **params):
    params.update(retmode="json", tool="wiki-hematologia")
    url = API + endpoint + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as r:
        datos = json.load(r)
    time.sleep(PAUSA)
    return datos


def buscar(consulta, dias, maximo):
    r = pedir("esearch.fcgi", db="pubmed", term=consulta, datetype="edat",
              reldate=dias, retmax=maximo, sort="date")
    return r["esearchresult"].get("idlist", [])


def resumenes(pmids):
    if not pmids:
        return []
    r = pedir("esummary.fcgi", db="pubmed", id=",".join(pmids))["result"]
    return [r[p] for p in pmids if p in r]


def linea(art):
    autores = art.get("authors") or []
    primero = autores[0]["name"] if autores else "Sin autor"
    if len(autores) > 1:
        primero += " et al."
    titulo = " ".join(art.get("title", "").split()).rstrip(".")
    titulo = titulo.replace("[", "(").replace("]", ")").replace("|", "/")
    tipos = ", ".join(t for t in art.get("pubtype", []) if t != "Journal Article")
    pmid = art["uid"]
    txt = (f"- {primero} **{titulo}.** *{art.get('source', '')}* "
           f"{art.get('pubdate', '')}. PMID [{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)")
    return txt + (f" — {tipos}" if tipos else "")


def main():
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    dias, maximo, filtro = cfg["dias"], cfg["max_por_tema"], cfg["filtro"]
    hoy = datetime.date.today().isoformat()
    out = [
        "# Novedades de la literatura",
        "",
        '!!! warning "Lista automática, sin revisar"',
        f"    Generada automáticamente el **{hoy}** desde PubMed: guías, consensos, ensayos "
        f"aleatorizados y metaanálisis ingresados en los últimos **{dias} días** "
        f"(máximo {maximo} por tema). **No forma parte del contenido verificado de la wiki**: "
        "es una lista de candidatos para revisar e incorporar a cada página. "
        "Los temas y consultas se definen en `scripts/vigilancia.json`.",
        "",
    ]
    total = 0
    for tema in cfg["temas"]:
        arts = resumenes(buscar(f"({tema['consulta']}) AND {filtro}", dias, maximo))
        total += len(arts)
        out += [f"## {tema['titulo']}", "", f"Página de la wiki: [{tema['titulo']}]({tema['pagina']})", ""]
        out += [linea(a) for a in arts] or ["*Sin artículos nuevos en este período.*"]
        out.append("")
    SALIDA.write_text("\n".join(out), encoding="utf-8")
    print(f"novedades.md actualizado: {total} artículos en {len(cfg['temas'])} temas.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # red caída, API sin respuesta, etc.
        print(f"No se pudo actualizar novedades: {e}", file=sys.stderr)
        sys.exit(1)
