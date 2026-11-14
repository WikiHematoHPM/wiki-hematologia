# Registro de cambios

| Fecha | Cambio | Fuentes |
|---|---|---|
| 2026-11-11 | **Creación de la wiki.** Esqueleto de tres bloques, plantilla, metodología y guía de alojamiento. | — |
| 2026-11-11 | Página piloto **PTI del adulto** basada en la guía ASH 2026 (texto completo). | [1]–[5] |
| 2026-11-11 | Página piloto **LLC** (borrador): iwCLL 2018, ESMO 2020/2024, AMPLIFY, CLL14. Texto completo de guías pendiente. | [6]–[16] |

## 2026-11-14 (18) — Novedades de noviembre 2026: PTI (rilzabrutinib) y LMA (evidencia emergente aza-ven en pacientes aptos)
- **PTI del adulto:** la fila de **inhibidor de BTK** en la tabla de fármacos y dosis, antes **[PV]** por falta de fármaco y dosis específicos, se completa con **rilzabrutinib 400 mg c/12 h VO**, según los resultados del período abierto del ensayo de fase 3 **LUNA3** (Kuter et al. 2026, *Lancet Haematol*).
- **LMA:** se agrega una nota de "evidencia emergente" (sin modificar el algoritmo ni la dosis estándar de 7+3) sobre el ensayo fase 2 **PARADIGM** (Fathi et al. 2026, *N Engl J Med*): azacitidina-venetoclax mostró supervivencia libre de eventos superior al 7+3 en pacientes **aptos** (14,5 vs 6,2 meses; HR 0,57), en una población mayoritariamente de riesgo adverso ELN 2022. Se deja marcada explícitamente **[PV]** por tratarse de un solo ensayo fase 2 aún no incorporado a las guías ELN/NCCN.
- Referencias **[138]**–**[139]** añadidas.

## 2026-11-14 (17) — Competencias docentes y guía de alojamiento más desarrollada
- Nueva página **Competencias docentes (mapeo CanMEDS)** (`competencias-docentes.md`, grupo Metodología): mapa de los 7 roles CanMEDS 2015 [137] contra cada página clínica de la wiki, con momento docente sugerido por página y guía de uso en supervisión (anclada a la retroalimentación C3 y las EPA del programa, pendientes de completar con la taxonomía exacta).
- **Linfomas** confirmado como parte integral de la wiki general (ya estaba en `mkdocs.yml` e `hemato-onco/index.md`; se aclara en el `docs/index.md` general, que antes no lo mencionaba explícitamente).
- `docs/index.md`: tabla de estructura actualizada para reflejar el estado real de cada bloque (9 páginas en benigna, 7 en hemato-oncología incluyendo linfomas, 3 en transversal) en vez de solo los pilotos originales.
- **Alojamiento y publicación** reorganizada y ampliada:
    - Nueva sección 2, "¿Dónde viven los archivos?": aclara que tras el primer `git push` la wiki deja de depender del Mac de Pablo, con tabla de opciones (GitHub, GitLab, nubes de archivos) y formas de editar sin ese computador (editor web, GitHub Codespaces/github.dev, GitHub Mobile, Claude conectado al repositorio).
    - Sección "Subir la wiki" (antes 3, ahora 4) con pasos más granulares por pantalla y un **Camino B** alternativo: subir todo por el navegador sin instalar GitHub Desktop.
    - Sección "Actualización automática" (antes 5, ahora 6) reescrita en 4 niveles explícitos: publicación automática, vigilancia semanal de PubMed (explicada paso a paso, con cómo ajustar temas/ventana/horario), y dos niveles opcionales nuevos con tarea programada de Claude que propone cambios como Pull Request para aprobación de Pablo.
- Referencia [137] añadida (CanMEDS 2015 Physician Competency Framework).

## 2026-11-14 (16) — Alojamiento: opciones adicionales con acceso restringido
- **Alojamiento y publicación** ampliada con dos opciones más para que solo Pablo edite y otras personas solo lean, ambas con actualización automática:
    - **Gratis:** Render (sitio estático) + PageCrypt (una contraseña compartida, cifrado del HTML en el build).
    - **Pago pequeño (~US$5-6/mes):** servidor propio (VPS) con Caddy y usuario/clave individual por persona, con control total de altas y bajas de acceso.
- Tabla comparativa y recuadro de orientación ("¿cuál elegir?") actualizados con las 4 opciones de acceso restringido (Cloudflare Access, Render+PageCrypt, VPS+Caddy, Netlify Pro).
- Fuentes [g]-[i] añadidas (Netlify password protection, límite nativo de Render, PageCrypt).

## 2026-11-14 (15) — Publicación y actualización automática
- **Alojamiento y publicación** reescrita como guía paso a paso (Mac): GitHub + GitHub Pages (solo el dueño edita, lectura pública), edición posterior por web/GitHub Desktop, y alternativa de lectura restringida con Cloudflare Pages + Access.
- Nuevo flujo `.github/workflows/publicar.yml`: control de calidad, construcción con Zensical y publicación en cada cambio.
- **Vigilancia semanal de PubMed:** `scripts/novedades_pubmed.py` + `scripts/vigilancia.json` regeneran la nueva página **Novedades de la literatura** (lista automática, sin revisar; no modifica páginas clínicas).
- Linfomas: corregido un residuo de formato en la sección 2 y el enlace a urgencias hematológicas.

## 2026-11-14 (14) — Linfomas: nueva página de diagnóstico y etapificación
- Nueva página **Linfomas** (`hemato-onco/linfomas.md`), cubriendo exclusivamente **diagnóstico y etapificación** (sin tratamiento, por instrucción explícita): linfoma de Hodgkin (clásico y NLPHL), DLBCL, linfoma folicular, linfoma de células del manto, linfomas de zona marginal (MALT/esplénico/nodal) y linfoma de Burkitt.
- **Clasificación OMS-HEMA5 (2022) e ICC 2022** como marco general de las neoplasias linfoides maduras.
- **Linfoma de Hodgkin:** tabla comparativa cHL vs. NLPHL (subtipos, IHC: CD30/CD15/CD20/CD45/PAX5).
- **DLBCL:** algoritmo de Hans (célula de origen GCB/no-GCB), linfoma de células B grandes de alto grado doble/triple hit (FISH MYC/BCL2/BCL6) y concepto de "doble expresor" (IHC).
- **Linfoma folicular:** t(14;18) *IGH::BCL2*, grading OMS (1/2/3A/3B).
- **Linfoma de células del manto:** t(11;14) *CCND1::IGH*, ciclina D1, SOX11, variantes blastoide/pleomórfica, forma leucémica no nodal indolente.
- **Linfomas de zona marginal:** tabla de los 3 subtipos (MALT con *H. pylori*, esplénico, nodal).
- **Linfoma de Burkitt:** t(8;14) *MYC::IGH* y variantes, 3 formas clínico-epidemiológicas (endémica/esporádica/asociada a inmunodeficiencia), riesgo de lisis tumoral.
- **Etapificación:** clasificación de Lugano 2014 (estadios I-IV, enfermedad limitada vs. extensa, PET-CT/Deauville, rol reducido de la biopsia de médula ósea).
- **Índices pronósticos de la etapificación:** IPI (Shipp 1993), NCCN-IPI (Zhou 2014), R-IPI, FLIPI/FLIPI2 (folicular), MIPI/MIPI-b (manto), IPS/score de Hasenclever (Hodgkin avanzado).
- Algoritmo Mermaid de aproximación diagnóstica general por inmunofenotipo.
- Nav (`mkdocs.yml`) y fila "Linfomas" de `hemato-onco/index.md` actualizadas; tratamiento queda explícitamente pendiente para una página aparte.
- Referencias [129]–[136] añadidas.

## 2026-11-14 (13) — Mieloma múltiple: actualización 2026 y gammapatías monoclonales
- Página **mieloma múltiple** reescrita y ampliada a "Mieloma múltiple (MM) y gammapatías monoclonales": incorpora MGUS, mieloma múltiple quiescente (SMM) y una sección ampliada de plasmocitoma solitario, además de actualizar el manejo de MM activo con evidencia 2022–2025.
- **Espectro de gammapatías monoclonales:** tabla de clasificación general (MGUS no-IgM/cadena liviana/IgM, SMM, MM, plasmocitoma) por carga tumoral y daño de órgano.
- **MGUS:** subtipos y criterios IMWG 2014 (Rajkumar et al.), consenso IMWG 2010 de riesgo (Kyle et al.), modelo de riesgo de Mayo Clinic (M-proteína, isotipo, razón de FLC).
- **SMM:** definición IMWG 2014, modelos de riesgo Mayo "20/2/20" e IMWG 2020 (Mateos et al., marcado [PV]), y el ensayo **AQUILA** (daratumumab monoterapia vs. observación en SMM de alto riesgo — SLP a 5 años 63,1 % vs 40,8 %, primer tratamiento con beneficio demostrado en SMM).
- **Criterios diagnósticos de MM (SLiM-CRAB)** desarrollados en detalle por primera vez en esta wiki, con tabla de biomarcadores SLiM y criterios CRAB.
- **Estadificación:** ISS, R-ISS y **R2-ISS** (D'Agostino et al., JCO 2022) con las 4 categorías de riesgo y SG por grupo.
- **Primera línea actualizada:** cuádruplos con anti-CD38 como nuevo estándar — **PERSEUS** (Dara-VRd, trasplantables) y **IMROZ** (Isa-VRd, no trasplantables), con nuevo algoritmo Mermaid; referencia a NCCN v1.2025/v2.2026.
- **Recaída/refractariedad actualizada:** **CARTITUDE-4** (cilta-cel en 2.ª línea) y anticuerpos biespecíficos BCMA×CD3 (teclistamab/MajesTEC-1, elranatamab/MagnetisMM-3) y GPRC5D×CD3 (talquetamab/MonumenTAL-1, cita pendiente de verificación), con nuevo algoritmo Mermaid.
- **Plasmocitoma solitario** ampliado: diferenciación óseo (SBP) vs. extramedular (EMP), criterios diagnósticos, riesgo de progresión a MM (mayor en SBP), tratamiento con radioterapia local.
- Se conserva sin cambios de fondo la sección de tromboprofilaxis en IMiDs (IMWG/Palumbo 2008) y leucemia de células plasmáticas primaria.
- Referencias [117]–[128] añadidas.

## 2026-11-11 (2)
- LLC: dosis y escalada de venetoclax, SLT, interacciones (ficha técnica UE); sección GES Chile (parcial, con pendientes marcados).
- PTI: dosis de eltrombopag, romiplostim y avatrombopag desde fichas técnicas.
- Referencias 17–22 añadidas.
- Nueva página: anemia ferropénica (BSG 2021, texto completo) y referencia [23].
- Nuevas páginas: TEV y anticoagulación (ASH 2020 por resumen + fichas de apixabán/rivaroxabán) y mieloma múltiple (EHA-ESMO 2021, texto completo). Referencias [24]–[30].

## 2026-11-11 (3)
- **Mieloma múltiple:** nueva sección 7 de tromboprofilaxis con IMiDs (IMWG 2008, Palumbo et al.), algoritmo Mermaid, dosis de aspirina/enoxaparina/warfarina, manejo de TEV durante tratamiento.
- Nueva página: **leucemia mieloide aguda (LMA)** — clasificación ELN 2022, inducción 7+3, midostaurina (RATIFY), quizartinib (QuANTUM-First), CPX-351 (Vyxeos), inhibidores IDH, GO, HiDAC, venetoclax + HMA para no aptos, alo-TPH, criterios de respuesta, EMR, LPA. Dos algoritmos Mermaid (aptos y no aptos).
- Referencias [31]–[35] añadidas (IMWG tromboprofilaxis, ELN 2022, RATIFY, QuANTUM-First, CPX-351).

## 2026-11-11 (4) — Protocolos ANACAN/MINSAL Chile 2025
- **PTI del adulto:** actualizado con guías ASH 2026 (Blood Advances 2026). Secciones de primera y segunda línea reescritas.
- **LLC:** nueva sección 8c «Manejo en Chile» — protocolo ANACAN 2025 con Venetoclax-R 1ª línea (24 meses, finito) e Ibrutinib 2ª línea (indefinido). Incluye esquemas completos con escalada, SLT, ajustes de dosis, criterios de exclusión, canasta GES 2025.
- **LMA:** nueva sección 10b «Manejo en Chile» — (A) LMA CBF con GO para pacientes aptos en 1ª línea (inducción 7+3+GO, consolidación HiDAC+GO); (B) LMA ≥60/frágil con AZA-VEN × 12 ciclos. Canasta GES 2025.
- **LLA-B >60 y frágiles:** nueva página completa — protocolo ANACAN 2025 basado en Oxford, 16 escenarios (8 OLD + 8 FRAIL) según CD20/Ph, esquemas LAL-07 con detalle farmacológico, dasatinib vía DAC, rituximab para CD20+, profilaxis SNC.
- Referencias [36]–[39] añadidas (protocolos ANACAN 2025: LLC, LMA CBF GO, LMA >60/frágil, LLA-B >60/frágiles).

## 2026-11-12 (6) — Anemias hemolíticas
- Nueva página: **anemias hemolíticas** — cobertura integral: AHAI (wAIHA, CAD, mixta, HCF, DAT-negativa), HPN, esferocitosis hereditaria, déficit de G6PD, hemoglobinopatías (resumen).
- AHAI: consenso internacional Jäger 2020, Barcellini Blood 2021, Berentsen Front Immunol 2023, BSH Hill 2017. Algoritmos Mermaid de clasificación y tratamiento wAIHA. Tablas de fármacos y dosis (prednisona, rituximab, esplenectomía, azatioprina, MMF, ciclosporina). CAD: rituximab ± bendamustina, sutimlimab (CARDINAL).
- HPN: Hillmen NEJM 2006, Peffault de Latour NEJM 2024. Algoritmo Mermaid de tratamiento. Tabla completa de inhibidores del complemento (eculizumab, ravulizumab, pegcetacoplan, iptacopan, danicopan).
- Esferocitosis hereditaria: BSH 2011 (Bolton-Maggs). Clasificación por gravedad, test EMA, indicaciones de esplenectomía.
- G6PD: desencadenantes, diagnóstico (precaución con falsos negativos), contraindicación de rasburicasa.
- Hemoglobinopatías: resumen orientativo de drepanocitosis y talasemias.
- Índice de hematología benigna y navegación actualizados.
- Referencias [45]–[52] añadidas.

## 2026-11-12 (7) — Aplasia medular adquirida
- Nueva página: **aplasia medular adquirida** — cobertura completa: fisiopatología (destrucción inmune CMH, hematopoyesis clonal), diagnóstico (Camitta modificada, exclusión SMD hipoplásico y SFMH), estudio con test de fragilidad cromosómica, longitud telomérica por flow-FISH, NGS mieloide y clon HPN.
- Tratamiento primera línea: alo-TPH con MSD (sin corte de edad fijo, ASTCT 2024), triple terapia hATG + CsA + eltrombopag (ensayo RACE, NEJM 2022; Townsley NEJM 2017; consenso Blood Adv 2024). Algoritmo Mermaid estratificado por edad y donante.
- Segunda línea: 2.º ciclo ATG, alo-TPH MUD/haplo, CsA + eltrombopag, andrógenos.
- Evolución clonal: vigilancia molecular con NGS seriado, mutaciones de alto/bajo riesgo, señales de alarma.
- Soporte: profilaxis antimicrobiana (antifúngica anti-moho, PJP, antiviral), transfusiones irradiadas, quelación.
- Situaciones especiales: NSAA, embarazo, hepatitis seronegativa.
- Referencias [53]–[58] añadidas (BSH 2024, RACE NEJM 2022, Blood Adv 2024, Townsley NEJM 2017, ASTCT 2024, Piekarska Front Immunol 2024).

## 2026-11-12 (8) — SMD y LMMC
- Nueva página: **síndrome mielodisplásico (SMD)** — clasificación OMS 2022 (neoplasias mielodisplásicas: MDS-del5q, MDS-SF3B1, MDS-biTP53) e ICC 2022. Estratificación IPSS-R e IPSS-M (31 genes, 6 categorías, calculadora online, validación GenoMed4All C-index 0,81). Algoritmos Mermaid: LR-MDS (del5q → lenalidomida, RS+/SF3B1 → luspatercept primera línea COMMANDS, post-AEE → imetelstat IMerge FDA 2024) y HR-MDS (azacitidina estándar, VERONA venetoclax+aza no alcanzó SG). Decisión alo-TPH por IPSS-M (EBMT 2025, DSS Tentori JCO 2024). TP53 bialélico como entidad aparte. Quelación de hierro. GES Chile.
- Nueva página: **leucemia mielomonocítica crónica (LMMC)** — criterios OMS 2022 (monocitosis ≥ 0,5 × 10⁹/L reducido, ≥ 10 %, ≥ 3 meses), subclasificación LMMC-0/1/2, MD-LMMC vs. MP-LMMC. Paisaje mutacional (TET2 60 %, SRSF2 50 %, ASXL1 40-62 %, RAS 30 %). CPSS-Mol (4 genes + variables clínicas, 4 grupos). iCPSS (JCO 2026, 43 genes, 9 clases moleculares). Algoritmo Mermaid de tratamiento (HU citorreducción, HMA, alo-TPH). GES Chile.
- Índice de hemato-oncología y navegación actualizados.
- Referencias [59]–[72] añadidas.

## 2026-11-12 (9) — Hemostasia y trombosis
- Nueva página: **hemostasia y trombosis** — cobertura integral de hemostasia, coagulopatías y trombofilias.
- **Fisiología:** modelo celular de la hemostasia (Hoffman & Monroe 2001, Smith 2009): iniciación, amplificación, propagación, fibrinólisis. Anticoagulantes naturales.
- **Enfermedad de von Willebrand:** guías ASH/ISTH/NHF/WFH 2021 (diagnóstico y manejo). Clasificación tipos 1, 2A, 2B, 2M, 2N, 3. BATs, desmopresina, concentrados de VWF.
- **Hemofilia congénita:** guía ISTH 2024 (Rezende et al.). Profilaxis FVIII/FIX (fuerte), emicizumab (condicional).
- **Hemofilia adquirida A:** consenso Tiede 2020, revisión JTH 2024. Diagnóstico (estudio de mezcla → FVIII:C → Bethesda). Tratamiento hemostático (rFVIIa, CCPa, emicizumab) + inmunosupresión.
- **CID:** actualización ISTH 2025 (Iba et al.). Score revisado con umbrales de D-dímero > 3×/7× LSN. Clasificación por fases (pre-CID, temprana, abierta). Score SIC para sepsis. Algoritmo Mermaid por fenotipo.
- **PTT:** guías ISTH 2020/2025 (Zheng et al.). Score PLASMIC (Bendapudi 2017, validación Li 2018). Caplacizumab (HERCULES). ADAMTS13 recombinante en PTTc (fuerte, ISTH 2025). Algoritmo Mermaid de manejo urgente.
- **SHUa/TMA mediada por complemento:** KDIGO, eculizumab/ravulizumab, criterios de suspensión.
- **TIH:** guía ASH 2018 (Cuker et al., 33 recomendaciones). Score 4Ts obligatorio (VPN 99,8 % si ≤ 3). Anticoagulantes no heparínicos (argatrobán, fondaparinux, DOACs, bivalirudina). Algoritmo Mermaid.
- **Trombofilias:** guía ASH 2023 (Middeldorp et al., 23 recomendaciones). No testear población general pre-ACO (fuerte). Indicaciones selectivas de testeo.
- **SAF:** criterios ACR/EULAR 2023 (Barbhaiya et al.). Dominios ponderados aditivos. Especificidad 99 %, sensibilidad 84 %.
- Índice de hematología benigna y navegación actualizados.
- Referencias [73]–[86] añadidas.

## 2026-11-12 (12) — Medicina transfusional y urgencias hematológicas
- Nueva página transversal: **medicina transfusional** — umbrales de transfusión de glóbulos rojos y plaquetas, reacciones transfusionales, aféresis terapéutica.
- **Glóbulos rojos:** tabla de umbrales por población (AABB 2023, Carson et al.) — restrictivo Hb < 7 g/dL en adultos estables y hemato-oncológicos, ajustes por cirugía cardíaca/ortopédica y cardiopatía congénita pediátrica.
- **Plaquetas:** umbrales profilácticos (< 10 × 10⁹/L, AABB 2015 y ASCO 2018) vs. procedimentales (CVC < 20, PL y cirugía mayor < 50), alternativa de transfusión al primer sangrado en TAPH autólogo (Schiffer et al., ASCO 2018).
- **Reacciones transfusionales:** clasificación por tiempo de aparición (algoritmo Mermaid), tabla por mecanismo (AHTR, FNHTR, alérgica/anafiláctica, TRALI, TACO, séptica), distinción clínica TRALI vs. TACO (Delaney et al., Lancet 2016).
- **Aféresis:** sistema de categorías y grados ASFA 9.ª edición 2023 (Connelly-Smith et al.), ejemplos relevantes a hematología (trombocitaféresis, PTT, leucaféresis).
- Nueva página transversal: **urgencias hematológicas** — neutropenia febril, síndrome de lisis tumoral, leucostasis/hiperleucocitosis, CID (por remisión) y hemorragia crítica/transfusión masiva.
- **Lisis tumoral:** criterios de Cairo-Bishop (laboratorio y clínico), factores de riesgo, algoritmo Mermaid de prevención/tratamiento (alopurinol vs. rasburicasa, no combinar).
- **Leucostasis:** definición de hiperleucocitosis vs. leucostasis sintomática, algoritmo Mermaid de manejo, rol individualizado de leucaféresis (Giammarco et al. 2017).
- **Neutropenia febril:** ampliación de lo ya cubierto en citopenias — estratificación MASCC/CISNE, flujo de manejo con tiempos ASCO/IDSA 2018 (Taplitz et al.), criterios de manejo ambulatorio.
- **CID:** sin duplicar contenido — remisión directa a Hemostasia y trombosis § 5.3/§ 8.2.
- **Hemorragia crítica:** terminología MTP→MHP, evidencia PROPPR (Holcomb et al., JAMA 2015) sobre razones 1:1:1 vs. 1:1:2, algoritmo Mermaid de activación y transición a resucitación guiada por laboratorio, mnemotecnia "ABC tras 3", consideraciones por escenario (trauma, digestivo, variceal, posparto).
- Algoritmo Mermaid integrado de reconocimiento de la urgencia hematológica.
- Índice transversal, nav de mkdocs y changelog actualizados.
- Referencias [106]–[116] añadidas.

## 2026-11-12 (11) — Laboratorio y diagnóstico
- Nueva página transversal: **laboratorio y diagnóstico** — hemograma e índices, frotis de sangre periférica, aspirado y biopsia de médula ósea, citometría de flujo, citogenética/FISH, biología molecular/NGS, enfermedad residual medible (ERM/MRD).
- **Hemograma e índices:** VCM, HCM, ADE, reticulocitos, IRF, índice de producción reticulocitaria (IPR), criterios de revisión de frotis tras alerta automatizada.
- **Frotis:** nomenclatura y gradación estandarizada ICSH 2015 (Palmer et al.), tabla de hallazgos de alta relevancia clínica inmediata (blastos, esquistocitos, dacriocitos, rouleaux, etc.).
- **Médula ósea:** guías ICSH 2008 (Lee et al.) — aspirado vs. biopsia trefina como estudios complementarios, indicaciones, técnica, precauciones (orden de obtención, aspirado esternal, dry tap).
- **Citometría de flujo:** estandarización EuroFlow (Kalina et al. y van Dongen et al., Leukemia 2012), algoritmo Mermaid de la estrategia EuroFlow (ALOT → paneles de clasificación), usos en ERM.
- **Citogenética/FISH:** cariotipo convencional y nomenclatura ISCN, indicaciones de FISH, tabla de sondas/alteraciones por enfermedad, complementariedad cariotipo-FISH-CMA-NGS (Balciuniene et al., Blood Rev 2024).
- **Biología molecular/NGS:** rol diagnóstico/pronóstico/seguimiento (Cho, Blood Res 2024, texto completo), paneles mieloides dirigidos por enfermedad, limitación de NGS en LMC.
- **ERM/MRD:** tabla comparativa de métodos de referencia por enfermedad (LMA: ELN 2018; LLA-B: EuroFlow; LMC: escala internacional BCR-ABL1, ELN 2020; mieloma: IMWG/Munshi et al. JAMA Oncol 2017).
- Algoritmo Mermaid integrado: de la sospecha clínica al diagnóstico de precisión.
- Índice transversal y navegación actualizados.
- Referencias [97]–[105] añadidas.

## 2026-11-12 (10) — Citopenias y estudio inicial
- Nueva página: **citopenias y estudio inicial** — enfoque diagnóstico de pancitopenia, trombocitopenia, neutropenia, eosinofilia y eritrocitosis/poliglobulia en el adulto.
- **Pancitopenia:** algoritmo Mermaid basado en reticulocitos (producción vs. destrucción), indicaciones de BMO, alertas de emergencia (LPMA, CID, HLH). Chew & Kamangar Clin Med 2024 (texto completo), Gnanaraj et al. Blood Rev 2018.
- **Trombocitopenia:** algoritmo Mermaid de enfoque escalonado (pseudotrombocitopenia → frotis → aislada vs. asociada). Swain & Bird Platelets 2020. Referencia cruzada a PTI y hemostasia/trombosis.
- **Neutropenia:** clasificación congénita/adquirida/Duffy-null, grados de gravedad, estudio inicial, neutropenia febril como emergencia. EHA/EuNet-INNOCHRON 2023 (diagnóstico) y 2025 (tratamiento), Kim AAFP 2025.
- **Eosinofilia:** algoritmo Mermaid (causas secundarias → clonalidad → SHE), evaluación de daño orgánico, clasificación OMS 2022 de neoplasias eosinofílicas. Klion ASH 2022, Shomali & Gotlib Am J Hematol 2022, Valent Allergy 2023.
- **Eritrocitosis:** algoritmo Mermaid (JAK2/EPO), criterios OMS 2022 de PV, PV enmascarada, eritrocitosis secundaria. Alberta PV guideline 2025.
- Índice de hematología benigna y navegación actualizados.
- Referencias [87]–[96] añadidas.

## 2026-11-11 (5) — Anemias: megaloblástica y enfermedad crónica
- Nueva página: **anemia megaloblástica (B12/folato)** — NICE NG239 2024, BSH Devalia 2014, Delphi Consensus 2024. Algoritmo diagnóstico Mermaid (B12 <180 confirmada, 180-350 zona gris → MMA), tablas de tratamiento (hidroxocobalamina IM, cianocobalamina oral, folato 5 mg), monitorización de respuesta (crisis reticulocitaria día 5-7), gastritis autoinmune y vigilancia de cáncer gástrico.
- Nueva página: **anemia de enfermedad crónica** — Nemeth & Ganz 2014, Weiss et al. 2019. Fisiopatología centrada en hepcidina/ferroportina, algoritmo diferencial AEC vs. ferropenia (ferritina, sTfR, índice sTfR/log ferritina), perfil comparativo, tratamiento (enfermedad de base, hierro IV si ferropenia coexistente, AEE en ERC/QT), terapias emergentes (anti-hepcidina, HIF-PHD).
- Índice de hematología benigna y navegación actualizados.
- Referencias [40]–[44] añadidas.
