# Scores y calculadoras

!!! info "Ficha de la página"
    **Última revisión:** 2026-11-20 · **Fuentes base:** publicaciones originales de derivación/validación de cada score, verificadas por resumen en PubMed: Wells TEP [175], Wells TVP [174], Khorana [176], Padua [177], HAS-BLED [178], CHA₂DS₂-VASc [179], HScore [180], ISS [181], R-ISS [182], CLL-IPI [13], IPI [132], NCCN-IPI [133], 4Ts [73], PLASMIC [85]. **Alcance:** adultos.

!!! warning "Cómo leer las calculadoras de esta página"
    - Son **herramientas docentes**: estiman riesgo en la población en que se derivó el score y **no reemplazan el juicio clínico** ni la fuente original.
    - Cada tabla indica si los **pesos de cada variable** se verificaron en el resumen de la publicación (**[V-RS]**) o provienen de la publicación original sin verificación de texto completo en esta revisión (**[PV]**). Las calculadoras usan exactamente los pesos de la tabla que tienen encima.
    - Las calculadoras funcionan en el navegador; no guardan ni envían datos. **No ingreses datos identificables de pacientes.**

---

## 1. Principios para usar un score

| Pregunta | Por qué importa |
|---|---|
| **¿En qué población se derivó?** | Wells se derivó en pacientes ambulatorios; Padua, en hospitalizados de medicina interna; Khorana, en pacientes ambulatorios con quimioterapia. Fuera de esa población, el rendimiento cae. |
| **¿Es diagnóstico o pronóstico?** | Wells, 4Ts, PLASMIC y HScore estiman **probabilidad pretest** de una enfermedad; IPI, CLL-IPI y R-ISS estiman **supervivencia**. Un score pronóstico no indica por sí solo cuándo tratar. |
| **¿Qué se hace con el resultado?** | Un score diagnóstico solo es útil combinado con una prueba (Wells + dímero D; 4Ts + inmunoensayo; PLASMIC + ADAMTS13). |
| **¿Sigue vigente?** | Los scores pronósticos de la era pre-rituximab o pre-terapias dirigidas pueden sobrestimar el riesgo actual (por eso existen NCCN-IPI, R-ISS y R2-ISS). |

---

## 2. Mapa de scores de la wiki

Scores ya desarrollados en otras páginas (con sus tablas y fuentes):

| Área | Score | Página |
|---|---|---|
| **Hemostasia** | 4Ts (TIH), PLASMIC (PTT), ISTH CID | [Hemostasia y trombosis](../benigna/hemostasia-trombosis.md) · [Urgencias](urgencias-hematologicas.md) |
| **Soporte** | MASCC, CISNE (neutropenia febril), Cairo-Bishop (lisis tumoral) | [Urgencias hematológicas](urgencias-hematologicas.md) |
| **Linfomas** | IPI, NCCN-IPI, R-IPI, FLIPI, MIPI, IPS (Hasenclever) | [Linfomas](../hemato-onco/linfomas.md) |
| **LLC** | CLL-IPI, Rai, Binet | [LLC](../hemato-onco/llc.md) |
| **Mieloma y gammapatías** | ISS, R-ISS, R2-ISS, Mayo MGUS, Mayo 20/2/20 (SMM), Mayo revisada 2012 (amiloidosis AL), IPSSWM/R-IPSSWM | [Mieloma y gammapatías](../hemato-onco/mieloma.md) |
| **Mieloides** | IPSS-R, IPSS-M (SMD), CPSS-Mol (LMMC), ELN 2022 (LMA) | [SMD](../hemato-onco/sindrome-mielodisplasico.md) · [LMMC](../hemato-onco/lmmc.md) · [LMA](../hemato-onco/lma.md) |
| **Mieloproliferativas** | IPSET-trombosis, MIPSS70+v2.0, GIPSS, ELTS | [Neoplasias mieloproliferativas](../hemato-onco/neoplasias-mieloproliferativas.md) |

!!! note "Scores que requieren calculadora oficial"
    **IPSS-M** (SMD) y **MIPSS70+ v2.0** (mielofibrosis) usan modelos ponderados con muchas variables moleculares; no se reproducen aquí porque un error de implementación tendría consecuencias clínicas. Usa la calculadora web oficial de cada grupo, enlazada desde su página.

---

## 3. Trombosis y anticoagulación

### 3.1 Wells para tromboembolismo pulmonar (TEP)

Pesos y puntos de corte **[V-RS]** [175]:

| Variable | Puntos |
|---|---|
| Signos clínicos de TVP | 3,0 |
| Diagnóstico alternativo menos probable que TEP | 3,0 |
| Frecuencia cardíaca >100/min | 1,5 |
| Inmovilización o cirugía en las 4 semanas previas | 1,5 |
| TVP o TEP previos | 1,5 |
| Hemoptisis | 1,0 |
| Cáncer | 1,0 |

- **Tres niveles:** <2 baja · 2–6 moderada · >6 alta.
- **Dos niveles:** ≤4 **TEP improbable** · >4 **TEP probable**. Con TEP improbable y dímero D negativo, la frecuencia de TEP fue 2,2 % en la cohorte de derivación y 1,7 % en la de validación [175] **[V-RS]**.

<div class="calc" data-bands='[[1.5,"probabilidad baja"],[6,"probabilidad moderada"],[99,"probabilidad alta"]]' data-bands2='[[4,"TEP improbable (≤4)"],[99,"TEP probable (>4)"]]'>
<label><input type="checkbox" data-pts="3"> Signos clínicos de TVP <span class="pts">+3</span></label>
<label><input type="checkbox" data-pts="3"> Diagnóstico alternativo menos probable que TEP <span class="pts">+3</span></label>
<label><input type="checkbox" data-pts="1.5"> FC &gt;100/min <span class="pts">+1,5</span></label>
<label><input type="checkbox" data-pts="1.5"> Inmovilización o cirugía ≤4 semanas <span class="pts">+1,5</span></label>
<label><input type="checkbox" data-pts="1.5"> TVP/TEP previos <span class="pts">+1,5</span></label>
<label><input type="checkbox" data-pts="1"> Hemoptisis <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Cáncer <span class="pts">+1</span></label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

### 3.2 Wells para trombosis venosa profunda (TVP)

La estrategia **TVP improbable + dímero D negativo** permite omitir la ecografía de forma segura (eventos a 3 meses 0,4 %; 39 % de los pacientes evitó la ecografía) [174] **[V-RS]**. Los pesos de cada variable provienen de la publicación original y no figuran en el resumen verificado **[PV]**:

| Variable | Puntos |
|---|---|
| Cáncer activo (tratamiento en curso, en los 6 meses previos o paliativo) | 1 |
| Parálisis, paresia o inmovilización con yeso de extremidad inferior | 1 |
| Encamado ≥3 días o cirugía mayor en las 12 semanas previas | 1 |
| Dolor localizado a lo largo del sistema venoso profundo | 1 |
| Edema de toda la extremidad | 1 |
| Aumento del diámetro de la pantorrilla >3 cm respecto de la contralateral | 1 |
| Edema con fóvea confinado a la extremidad sintomática | 1 |
| Venas superficiales colaterales (no varicosas) | 1 |
| TVP previa documentada | 1 |
| Diagnóstico alternativo al menos tan probable como TVP | −2 |

**<2: TVP improbable · ≥2: TVP probable** **[PV]**.

<div class="calc" data-bands='[[1,"TVP improbable (<2): dímero D; si es negativo, no requiere ecografía"],[99,"TVP probable (≥2): ecografía"]]'>
<label><input type="checkbox" data-pts="1"> Cáncer activo <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Parálisis, paresia o yeso en EEII <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Encamado ≥3 días o cirugía mayor ≤12 semanas <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Dolor en trayecto venoso profundo <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Edema de toda la extremidad <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Pantorrilla &gt;3 cm mayor que la contralateral <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Edema con fóvea en extremidad sintomática <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Venas colaterales superficiales no varicosas <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> TVP previa documentada <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="-2"> Diagnóstico alternativo al menos tan probable <span class="pts">−2</span></label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

### 3.3 Khorana: riesgo de TEV asociado a quimioterapia

Variables, pesos y tasas de TEV **[V-RS]** [176]; la lista de sitios de cáncer por categoría proviene de la publicación original **[PV]**:

| Variable | Puntos |
|---|---|
| Sitio de muy alto riesgo (estómago, páncreas) **[PV]** | 2 |
| Sitio de alto riesgo (pulmón, **linfoma**, ginecológico, vejiga, testículo) **[PV]** | 1 |
| Plaquetas prequimioterapia ≥350 × 10⁹/L | 1 |
| Hemoglobina <10 g/dL o uso de agentes estimulantes de eritropoyesis | 1 |
| Leucocitos prequimioterapia >11 × 10⁹/L | 1 |
| IMC ≥35 kg/m² | 1 |

| Riesgo | Puntaje | TEV sintomático (derivación / validación, mediana 2,5 meses) |
|---|---|---|
| Bajo | 0 | 0,8 % / 0,3 % |
| Intermedio | 1–2 | 1,8 % / 2 % |
| Alto | ≥3 | 7,1 % / 6,7 % |

!!! note "Khorana en hemato-oncología"
    El score se derivó en pacientes ambulatorios con tumores sólidos y linfoma; **no se validó en mieloma** (donde se usa la estratificación IMWG para IMiDs, ver [Mieloma](../hemato-onco/mieloma.md), §13) ni en leucemias agudas.

<div class="calc" data-bands='[[0,"riesgo bajo (TEV ≈0,3–0,8 %)"],[2,"riesgo intermedio (≈2 %)"],[99,"riesgo alto (≈7 %)"]]'>
<label>Sitio del cáncer
<select>
<option data-pts="0">Otro sitio</option>
<option data-pts="1">Alto riesgo: pulmón, linfoma, ginecológico, vejiga, testículo (+1)</option>
<option data-pts="2">Muy alto riesgo: estómago, páncreas (+2)</option>
</select></label>
<label><input type="checkbox" data-pts="1"> Plaquetas ≥350 × 10⁹/L <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Hb &lt;10 g/dL o uso de AEE <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Leucocitos &gt;11 × 10⁹/L <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> IMC ≥35 kg/m² <span class="pts">+1</span></label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

### 3.4 Padua: profilaxis de TEV en pacientes médicos hospitalizados

En la cohorte de validación (1180 pacientes de medicina interna), los pacientes de **alto riesgo sin profilaxis** tuvieron TEV en **11,0 %** vs **2,2 %** con profilaxis (HR 0,13), y los de **bajo riesgo**, 0,3 % [177] **[V-RS]**. Los pesos y el punto de corte provienen de la publicación original **[PV]**:

| Variable | Puntos |
|---|---|
| Cáncer activo (metástasis locales o a distancia, o quimio/radioterapia en los 6 meses previos) | 3 |
| TEV previo (excluida trombosis venosa superficial) | 3 |
| Movilidad reducida (reposo en cama ≥3 días) | 3 |
| Trombofilia conocida | 3 |
| Trauma o cirugía reciente (≤1 mes) | 2 |
| Edad ≥70 años | 1 |
| Insuficiencia cardíaca o respiratoria | 1 |
| Infarto agudo de miocardio o ACV isquémico | 1 |
| Infección aguda o enfermedad reumatológica | 1 |
| Obesidad (IMC ≥30) | 1 |
| Tratamiento hormonal en curso | 1 |

**≥4: alto riesgo** (considerar profilaxis si el riesgo hemorrágico lo permite) **[PV]**.

!!! warning "Trombocitopenia y profilaxis"
    En el paciente oncohematológico hospitalizado, el puntaje Padua suele ser alto (cáncer activo + inmovilidad), pero la **trombocitopenia** cambia el balance riesgo-beneficio: la profilaxis farmacológica con plaquetas bajas (habitualmente <50 × 10⁹/L) suele suspenderse o sustituirse por medidas mecánicas **[PV]** (umbral institucional).

<div class="calc" data-bands='[[3,"bajo riesgo (<4)"],[99,"alto riesgo (≥4): considerar profilaxis"]]'>
<label><input type="checkbox" data-pts="3"> Cáncer activo <span class="pts">+3</span></label>
<label><input type="checkbox" data-pts="3"> TEV previo <span class="pts">+3</span></label>
<label><input type="checkbox" data-pts="3"> Movilidad reducida ≥3 días <span class="pts">+3</span></label>
<label><input type="checkbox" data-pts="3"> Trombofilia conocida <span class="pts">+3</span></label>
<label><input type="checkbox" data-pts="2"> Trauma o cirugía ≤1 mes <span class="pts">+2</span></label>
<label><input type="checkbox" data-pts="1"> Edad ≥70 años <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Insuficiencia cardíaca o respiratoria <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> IAM o ACV isquémico <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Infección aguda o enfermedad reumatológica <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> IMC ≥30 <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Tratamiento hormonal en curso <span class="pts">+1</span></label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

### 3.5 CHA₂DS₂-VASc y HAS-BLED (fibrilación auricular)

Relevantes en hematología porque la **fibrilación auricular** es frecuente con **ibrutinib** y otros BTKi (ver [Mieloma — Waldenström](../hemato-onco/mieloma.md), §15, y [LLC](../hemato-onco/llc.md)), y porque la decisión de anticoagular a un paciente con trombocitopenia o neoplasia activa exige ponderar ambos riesgos.

**CHA₂DS₂-VASc** — el resumen verifica el esquema y el aumento de tromboembolia con el puntaje creciente (p de tendencia 0,003) [179] **[V-RS]**; los pesos provienen de la publicación original **[PV]**:

| Variable | Puntos |
|---|---|
| **C** Insuficiencia cardíaca congestiva / disfunción ventricular izquierda | 1 |
| **H** Hipertensión | 1 |
| **A₂** Edad ≥75 años | 2 |
| **D** Diabetes mellitus | 1 |
| **S₂** ACV, AIT o tromboembolia previos | 2 |
| **V** Enfermedad vascular (IAM previo, enfermedad arterial periférica, placa aórtica) | 1 |
| **A** Edad 65–74 años | 1 |
| **Sc** Sexo femenino | 1 |

<div class="calc" data-bands='[[0,"riesgo bajo"],[1,"riesgo intermedio: individualizar"],[99,"riesgo alto: anticoagulación indicada si no hay contraindicación"]]'>
<label><input type="checkbox" data-pts="1"> Insuficiencia cardíaca / disfunción VI <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Hipertensión <span class="pts">+1</span></label>
<label>Edad
<select>
<option data-pts="0">&lt;65 años</option>
<option data-pts="1">65–74 años (+1)</option>
<option data-pts="2">≥75 años (+2)</option>
</select></label>
<label><input type="checkbox" data-pts="1"> Diabetes <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="2"> ACV, AIT o tromboembolia previos <span class="pts">+2</span></label>
<label><input type="checkbox" data-pts="1"> Enfermedad vascular <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Sexo femenino <span class="pts">+1</span></label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

Las categorías de la calculadora (0 bajo, 1 intermedio, ≥2 alto) siguen la convención clásica; las guías actuales de fibrilación auricular ajustan el umbral por sexo **[PV]**.

**HAS-BLED** — riesgo de sangrado mayor a 1 año en fibrilación auricular anticoagulada; el resumen verifica los componentes y su capacidad predictiva (C 0,72) [178] **[V-RS]**; el peso de 1 punto por componente y el umbral ≥3 provienen de la publicación original **[PV]**:

| Variable | Puntos |
|---|---|
| **H** Hipertensión (sistólica >160 mmHg) | 1 |
| **A** Función renal anormal | 1 |
| **A** Función hepática anormal | 1 |
| **S** ACV previo | 1 |
| **B** Sangrado previo o predisposición (incluye anemia, trombocitopenia) | 1 |
| **L** INR lábil | 1 |
| **E** Edad >65 años | 1 |
| **D** Fármacos (antiplaquetarios, AINE) | 1 |
| **D** Alcohol | 1 |

<div class="calc" data-bands='[[2,"riesgo de sangrado no alto"],[99,"riesgo de sangrado alto (≥3): corregir factores modificables y seguimiento estrecho"]]'>
<label><input type="checkbox" data-pts="1"> Hipertensión no controlada <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Función renal anormal <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Función hepática anormal <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> ACV previo <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Sangrado previo o predisposición <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> INR lábil <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Edad &gt;65 años <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Antiplaquetarios o AINE <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Alcohol <span class="pts">+1</span></label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

!!! tip "HAS-BLED alto no contraindica por sí solo la anticoagulación"
    Un puntaje alto identifica a quién vigilar y qué factores corregir (presión arterial, AINE, alcohol); no es una regla para negar la anticoagulación **[PV]**. HAS-BLED se derivó en fibrilación auricular; su uso en TEV o en pacientes con cáncer es una extrapolación.

### 3.6 4Ts (TIH) y PLASMIC (PTT)

Las tablas completas y la conducta según el puntaje están en [Hemostasia y trombosis](../benigna/hemostasia-trombosis.md). Calculadoras con los mismos pesos:

**4Ts** [73]: 0–3 baja · 4–5 intermedia · 6–8 alta.

<div class="calc" data-bands='[[3,"probabilidad baja (VPN 99,8 %): no testear ni tratar"],[5,"probabilidad intermedia: suspender heparina, anticoagulante no heparínico e inmunoensayo"],[99,"probabilidad alta: suspender heparina y anticoagular con no heparínico"]]'>
<label>Trombocitopenia
<select>
<option data-pts="0">Caída &lt;30 % o nadir &lt;10 (0)</option>
<option data-pts="1">Caída 30–50 % o nadir 10–19 (1)</option>
<option data-pts="2">Caída &gt;50 % y nadir ≥20 (2)</option>
</select></label>
<label>Timing
<select>
<option data-pts="0">&lt;4 días sin exposición reciente (0)</option>
<option data-pts="1">Compatible pero no claro (1)</option>
<option data-pts="2">Días 5–10, o ≤1 día con exposición en 30 días previos (2)</option>
</select></label>
<label>Trombosis
<select>
<option data-pts="0">Ninguna (0)</option>
<option data-pts="1">Progresiva, recurrente o sospechosa (1)</option>
<option data-pts="2">Nueva, necrosis cutánea o reacción sistémica (2)</option>
</select></label>
<label>Otras causas
<select>
<option data-pts="0">Definitiva (0)</option>
<option data-pts="1">Posible (1)</option>
<option data-pts="2">Ninguna evidente (2)</option>
</select></label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

**PLASMIC** [85]: 0–4 bajo · 5 intermedio · 6–7 alto.

<div class="calc" data-bands='[[4,"riesgo bajo (≈4 %): buscar diagnóstico alternativo"],[5,"riesgo intermedio (≈57 %): ADAMTS13, considerar recambio plasmático"],[99,"riesgo alto (&gt;90 %): recambio plasmático y ADAMTS13"]]'>
<label><input type="checkbox" data-pts="1"> Plaquetas &lt;30 × 10⁹/L <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Hemólisis (reticulocitos &gt;2,5 %, haptoglobina indetectable o LDH &gt;2× LSN) <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Sin cáncer activo <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Sin trasplante de órgano o de progenitores <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> VCM &lt;90 fL <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> INR &lt;1,5 <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Creatinina &lt;2 mg/dL <span class="pts">+1</span></label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

---

## 4. HScore: síndrome hemofagocítico reactivo

El HScore estima la probabilidad de **síndrome hemofagocítico (HLH) reactivo** en adultos. Se derivó en 312 pacientes; incluye 9 variables (3 clínicas, 5 de laboratorio y 1 citológica). La probabilidad de HLH va de **<1 % con HScore ≤90** a **>99 % con HScore ≥250**; la mediana fue 230 en pacientes con HLH y 125 sin HLH [180] **[V-RS]**. El rango de puntos por variable va de 0–18 (inmunosupresión) a 0–64 (triglicéridos) [180] **[V-RS]**; los puntos intermedios de cada variable y el punto de corte de 169 provienen de la publicación original **[PV]**:

| Variable | Categorías y puntos |
|---|---|
| Inmunosupresión conocida (VIH, inmunosupresores crónicos) | No 0 · Sí 18 |
| Temperatura (°C) | <38,4: 0 · 38,4–39,4: 33 · >39,4: 49 |
| Organomegalia | No 0 · Hepatomegalia **o** esplenomegalia 23 · Ambas 38 |
| Citopenias (Hb ≤9,2 g/dL; leucocitos ≤5 × 10⁹/L; plaquetas ≤110 × 10⁹/L) | 1 línea 0 · 2 líneas 24 · 3 líneas 34 |
| Ferritina (ng/mL) | <2000: 0 · 2000–6000: 35 · >6000: 50 |
| Triglicéridos (mmol/L) | <1,5: 0 · 1,5–4: 44 · >4: 64 |
| Fibrinógeno (g/L) | >2,5: 0 · ≤2,5: 30 |
| AST/GOT (UI/L) | <30: 0 · ≥30: 19 |
| Hemofagocitosis en médula ósea | No 0 · Sí 35 |

Triglicéridos: 1,5 mmol/L ≈ 133 mg/dL; 4 mmol/L ≈ 354 mg/dL.

<div class="calc" data-bands='[[90,"probabilidad de HLH &lt;1 %"],[168,"probabilidad intermedia: bajo el punto de corte de 169"],[249,"≥169: HLH probable; buscar desencadenante (linfoma, infección, autoinmune)"],[999,"≥250: probabilidad de HLH &gt;99 %"]]'>
<label>Inmunosupresión conocida
<select><option data-pts="0">No (0)</option><option data-pts="18">Sí (18)</option></select></label>
<label>Temperatura
<select><option data-pts="0">&lt;38,4 °C (0)</option><option data-pts="33">38,4–39,4 °C (33)</option><option data-pts="49">&gt;39,4 °C (49)</option></select></label>
<label>Organomegalia
<select><option data-pts="0">No (0)</option><option data-pts="23">Hepatomegalia o esplenomegalia (23)</option><option data-pts="38">Ambas (38)</option></select></label>
<label>Citopenias
<select><option data-pts="0">1 línea (0)</option><option data-pts="24">2 líneas (24)</option><option data-pts="34">3 líneas (34)</option></select></label>
<label>Ferritina
<select><option data-pts="0">&lt;2000 ng/mL (0)</option><option data-pts="35">2000–6000 ng/mL (35)</option><option data-pts="50">&gt;6000 ng/mL (50)</option></select></label>
<label>Triglicéridos
<select><option data-pts="0">&lt;1,5 mmol/L (0)</option><option data-pts="44">1,5–4 mmol/L (44)</option><option data-pts="64">&gt;4 mmol/L (64)</option></select></label>
<label>Fibrinógeno
<select><option data-pts="0">&gt;2,5 g/L (0)</option><option data-pts="30">≤2,5 g/L (30)</option></select></label>
<label>AST
<select><option data-pts="0">&lt;30 UI/L (0)</option><option data-pts="19">≥30 UI/L (19)</option></select></label>
<label>Hemofagocitosis en médula ósea
<select><option data-pts="0">No (0)</option><option data-pts="35">Sí (35)</option></select></label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

!!! note "HScore y linfoma"
    En el adulto, el **linfoma** (especialmente T/NK) es uno de los desencadenantes más frecuentes de HLH. Un HScore alto en un paciente con citopenias, fiebre y ferritina muy elevada obliga a buscar una neoplasia hematológica **[PV]**.

---

## 5. Scores pronósticos oncohematológicos

### 5.1 IPI y NCCN-IPI (linfomas agresivos)

Variables del IPI **[V-RS]** [132] (ver [Linfomas](../hemato-onco/linfomas.md), §10): edad >60, estadio III–IV, LDH elevada, ECOG ≥2, ≥2 sitios extranodales. Grupos: 0–1 bajo · 2 bajo-intermedio · 3 alto-intermedio · 4–5 alto. **R-IPI:** 0 muy bueno · 1–2 bueno · 3–5 pobre.

<div class="calc" data-bands='[[1,"IPI bajo"],[2,"IPI bajo-intermedio"],[3,"IPI alto-intermedio"],[5,"IPI alto"]]' data-bands2='[[0,"R-IPI muy bueno"],[2,"R-IPI bueno"],[5,"R-IPI pobre"]]'>
<label><input type="checkbox" data-pts="1"> Edad &gt;60 años <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Estadio III–IV <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> LDH elevada <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> ECOG ≥2 <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> ≥2 sitios extranodales <span class="pts">+1</span></label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

**NCCN-IPI** [133]: pesos según [Linfomas](../hemato-onco/linfomas.md), §10. Los grupos de riesgo (0–1 bajo, 2–3 bajo-intermedio, 4–5 alto-intermedio, ≥6 alto) provienen de la publicación original **[PV]**.

<div class="calc" data-bands='[[1,"NCCN-IPI bajo"],[3,"NCCN-IPI bajo-intermedio"],[5,"NCCN-IPI alto-intermedio"],[8,"NCCN-IPI alto"]]'>
<label>Edad
<select><option data-pts="0">≤40 años (0)</option><option data-pts="1">41–60 años (1)</option><option data-pts="2">61–75 años (2)</option><option data-pts="3">&gt;75 años (3)</option></select></label>
<label>LDH (relación con el límite superior normal)
<select><option data-pts="0">Normal (0)</option><option data-pts="1">&gt;1 a 3× (1)</option><option data-pts="2">&gt;3× (2)</option></select></label>
<label><input type="checkbox" data-pts="1"> Estadio III–IV <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Extranodal de alto riesgo (médula ósea, SNC, hígado/TGI, pulmón) <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> ECOG ≥2 <span class="pts">+1</span></label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

### 5.2 CLL-IPI (leucemia linfocítica crónica)

Las 5 variables independientes y la supervivencia global a 5 años por grupo están verificadas en el resumen [13] **[V-RS]**; los pesos de cada variable y los rangos de cada grupo provienen de la publicación original **[PV]**:

| Variable | Puntos |
|---|---|
| *TP53* alterado (del(17p) y/o mutación) | 4 |
| *IGHV* no mutado | 2 |
| β2-microglobulina >3,5 mg/L | 2 |
| Estadio Binet B–C o Rai I–IV | 1 |
| Edad >65 años | 1 |

| Grupo | Puntaje **[PV]** | SG a 5 años [13] **[V-RS]** |
|---|---|---|
| Bajo | 0–1 | 93,2 % |
| Intermedio | 2–3 | 79,3 % |
| Alto | 4–6 | 63,3 % |
| Muy alto | 7–10 | 23,3 % |

<div class="calc" data-bands='[[1,"CLL-IPI bajo (SG 5 años 93,2 %)"],[3,"CLL-IPI intermedio (79,3 %)"],[6,"CLL-IPI alto (63,3 %)"],[10,"CLL-IPI muy alto (23,3 %)"]]'>
<label><input type="checkbox" data-pts="4"> TP53 alterado (del17p y/o mutación) <span class="pts">+4</span></label>
<label><input type="checkbox" data-pts="2"> IGHV no mutado <span class="pts">+2</span></label>
<label><input type="checkbox" data-pts="2"> β2-microglobulina &gt;3,5 mg/L <span class="pts">+2</span></label>
<label><input type="checkbox" data-pts="1"> Binet B–C o Rai I–IV <span class="pts">+1</span></label>
<label><input type="checkbox" data-pts="1"> Edad &gt;65 años <span class="pts">+1</span></label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

!!! note "CLL-IPI en la era de terapias dirigidas"
    El CLL-IPI se construyó con ensayos de quimioinmunoterapia. Con inhibidores de BTK y venetoclax, el impacto pronóstico de *IGHV* y *TP53* se atenúa, aunque sigue orientando la elección de tratamiento **[PV]**.

### 5.3 ISS y R-ISS (mieloma múltiple)

Ambos sistemas tienen criterios y supervivencias verificados en el resumen [181][182] **[V-RS]**:

| Estadio | ISS (Greipp 2005) | SG mediana |
|---|---|---|
| I | β2M <3,5 mg/L **y** albúmina ≥3,5 g/dL | 62 meses |
| II | Ni I ni III | 44 meses |
| III | β2M ≥5,5 mg/L | 29 meses |

| Estadio | R-ISS (Palumbo 2015) | SG a 5 años | SLP a 5 años |
|---|---|---|---|
| I | ISS I + sin citogenética de alto riesgo [del(17p), t(4;14), t(14;16)] + LDH normal | 82 % | 55 % |
| II | Ni I ni III | 62 % | 36 % |
| III | ISS III + (citogenética de alto riesgo **o** LDH elevada) | 40 % | 24 % |

Para la estadificación actual recomendada (**R2-ISS**, que incorpora 1q+), ver [Mieloma](../hemato-onco/mieloma.md), §6.

<div class="calc" data-calc="riss">
<label>β2-microglobulina (mg/L) <input type="text" inputmode="decimal" size="6" data-field="b2m"></label>
<label>Albúmina (g/dL) <input type="text" inputmode="decimal" size="6" data-field="alb"></label>
<label><input type="checkbox" data-field="ca"> Citogenética de alto riesgo por FISH: del(17p), t(4;14) o t(14;16)</label>
<label><input type="checkbox" data-field="ldh"> LDH sobre el límite superior normal</label>
<div class="calc-out"></div>
<button type="button" class="calc-reset">Limpiar</button>
</div>

---

## 6. Puntos clave para residentes e internos

!!! abstract "Para llevar"
    1. Un score **diagnóstico** (Wells, 4Ts, PLASMIC, HScore) solo sirve combinado con una prueba: su valor está en **descartar** con seguridad cuando la probabilidad pretest es baja.
    2. **Wells TEP ≤4 + dímero D negativo** y **Wells TVP <2 + dímero D negativo** permiten evitar la imagen.
    3. **Khorana** no aplica a mieloma ni a leucemias agudas; en mieloma con IMiD se usa la estratificación IMWG.
    4. En el paciente hospitalizado con neoplasia hematológica, **Padua** suele ser alto, pero la **trombocitopenia** puede contraindicar la profilaxis farmacológica.
    5. **HAS-BLED alto** obliga a corregir factores modificables, no a negar la anticoagulación de forma automática.
    6. **HScore ≥169** con fiebre, citopenias y ferritina muy alta: pensar en HLH y buscar un linfoma subyacente.
    7. Los scores pronósticos (IPI, CLL-IPI, R-ISS) describen supervivencia en la población de derivación; se actualizan cuando cambia el tratamiento (NCCN-IPI, R2-ISS).

---

## 7. Autoevaluación

??? question "1. Paciente con sospecha de TEP: FC 110/min, cáncer activo, sin signos de TVP, otro diagnóstico igual de probable. ¿Wells y conducta?"
    1,5 + 1 = **2,5**: probabilidad moderada y **TEP improbable (≤4)**. Pedir dímero D; si es negativo, el TEP queda razonablemente descartado [175].

??? question "2. Paciente con linfoma difuso de células B grandes que inicia R-CHOP: plaquetas 420 × 10⁹/L, Hb 9,5 g/dL, leucocitos 8 × 10⁹/L, IMC 27. ¿Khorana?"
    Linfoma 1 + plaquetas 1 + Hb 1 = **3: riesgo alto** (TEV ≈7 % a corto plazo) [176].

??? question "3. ¿Por qué no se reproduce el IPSS-M en esta página?"
    Porque es un modelo ponderado con decenas de variables moleculares; un error de implementación tendría consecuencias clínicas. Se usa la calculadora oficial.

??? question "4. Mieloma con β2M 6,2 mg/L, albúmina 3,0 g/dL, t(4;14) y LDH normal. ¿ISS y R-ISS?"
    **ISS III** (β2M ≥5,5) y **R-ISS III** (ISS III + citogenética de alto riesgo) [181][182].

??? question "5. Paciente con fiebre de 39,8 °C, hepatoesplenomegalia, bicitopenia, ferritina 12 000 ng/mL, triglicéridos 3 mmol/L, fibrinógeno 1,8 g/L, AST 80 UI/L, sin mielograma ni inmunosupresión. ¿HScore?"
    49 + 38 + 24 + 50 + 44 + 30 + 19 = **254**: probabilidad de HLH >99 % [180]. Buscar desencadenante (linfoma, infección) e iniciar estudio dirigido.

---

## 8. Referencias de esta página

→ Ver numeración completa en [Referencias verificadas](../referencias.md).

| Ref. | Cita abreviada | Verificación |
|---|---|---|
| [13] | International CLL-IPI working group. CLL-IPI. *Lancet Oncol* 2016. | Resumen |
| [73] | Cuker A, et al. ASH 2018: TIH. *Blood Adv* 2018. | Resumen |
| [85] | Bendapudi PK, et al. Score PLASMIC. *Lancet Haematol* 2017. | Resumen |
| [132] | Shipp MA, et al. IPI. *N Engl J Med* 1993. | Resumen |
| [133] | Zhou Z, et al. NCCN-IPI. *Blood* 2014. | Resumen |
| [174] | Wells PS, et al. Dímero D en sospecha de TVP. *N Engl J Med* 2003. | Resumen |
| [175] | Wells PS, et al. Modelo clínico simplificado de probabilidad de TEP. *Thromb Haemost* 2000. | Resumen |
| [176] | Khorana AA, et al. Modelo predictivo de trombosis asociada a quimioterapia. *Blood* 2008. | Resumen |
| [177] | Barbar S, et al. Padua Prediction Score. *J Thromb Haemost* 2010. | Resumen |
| [178] | Pisters R, et al. HAS-BLED. *Chest* 2010. | Resumen |
| [179] | Lip GYH, et al. CHA₂DS₂-VASc (Euro Heart Survey). *Chest* 2010. | Resumen |
| [180] | Fardet L, et al. HScore. *Arthritis Rheumatol* 2014. | Resumen |
| [181] | Greipp PR, et al. International Staging System (ISS). *J Clin Oncol* 2005. | Resumen |
| [182] | Palumbo A, et al. R-ISS. *J Clin Oncol* 2015. | Resumen |

---

## 9. Pendientes

- [ ] Verificar contra texto completo los pesos marcados **[PV]** (Wells TVP, Padua, CHA₂DS₂-VASc, HAS-BLED, HScore, CLL-IPI) y la lista de sitios de Khorana.
- [ ] Agregar calculadoras de FLIPI, IPSSWM, Mayo revisada 2012 (amiloidosis AL) e IPSET-trombosis, que ya tienen tablas verificadas en sus páginas.
- [ ] Evaluar scores de TEV asociado a cáncer más recientes (Vienna CATS, ONKOTEV) y de riesgo de sangrado en TEV (VTE-BLEED) **[PV]**.
- [ ] HCT-CI y escalas de fragilidad (IMWG, G8) cuando se desarrolle la página de [trasplante](index.md).
