# Wiki de Hematología

Wiki docente y de estudio (hematología benigna y hemato-oncología), escrita en Markdown y generada con **Zensical** (compatible con `mkdocs.yml`).

## Uso rápido

```bash
pip install zensical
zensical serve            # vista local en http://localhost:8000
zensical build            # genera el sitio estático en ./site
python3 scripts/check_wiki.py   # control de citas, enlaces y pendientes
```

También puedes abrir la carpeta `docs/` como bóveda en **Obsidian** para leer y editar sin instalar nada más.

## Estructura

```
docs/
  index.md                 inicio y leyenda de verificación
  benigna/                 hematología benigna (piloto: PTI del adulto)
  hemato-onco/             hemato-oncología (piloto: LLC)
  transversal/             laboratorio, transfusión, trasplante, urgencias, scores, fármacos
  metodologia.md           cómo se construye y actualiza
  plantilla-pagina.md      plantilla para páginas nuevas
  referencias.md           referencias verificadas (PMID/DOI)
  alojamiento.md           dónde publicarla y cómo protegerla
  changelog.md             registro de cambios
scripts/check_wiki.py      control de calidad
mkdocs.yml                 configuración y navegación
```

## Marcas de verificación

**[V-TF]** texto completo revisado · **[V-RS]** solo resumen/metadatos · **[PV]** pendiente de verificación.

Lee `docs/alojamiento.md` para publicarla (GitHub Pages) y para la actualización automática (`.github/workflows/publicar.yml`, `scripts/novedades_pubmed.py`).

## Nota sobre los diagramas

Los diagramas de flujo (Mermaid) se dibujan en el navegador cargando una librería desde internet (unpkg.com). Sin conexión verás el código del diagrama en lugar del gráfico.
