# 02. Signos Vitales y Metabolismo

> **Parámetros cubiertos:** `data-ritmo` (Ritmo Cardíaco), `data-presion` (Presión Arterial), `mis-temp` (Temperatura), `mis-oxigeno` (Saturación de Oxígeno) y `mis-glucosa` (Glucosa).

---

## 1. Ritmo Cardíaco (`data-ritmo`)

* **Responsable:** Foco (Poco) (`listo: true`)
* **Fuente:** MedlinePlus — *Pulse*: https://medlineplus.gov/ency/article/003399.htm?utm_source

| Población | Rango Normal (bpm) |
| :--- | :---: |
| **Adultos y mayores (≥ 10 años, incluyendo adultos mayores)** | `60 – 100 bpm` |
| **Atletas bien entrenados** | `40 – 60 bpm` |

---

## 2. Presión Arterial (`data-presion`)

* **Responsable:** Foco (Poco) (`listo: true`)
* **Fuente:** MedlinePlus (ES) — *Medición de la presión arterial*: https://medlineplus.gov/spanish/pruebas-de-laboratorio/medicion-de-la-presion-arterial/?utm_source

| Categoría | Presión Sistólica (mmHg) | Operador | Presión Diastólica (mmHg) |
| :--- | :---: | :---: | :---: |
| **Normal** | `< 120` | y | `< 80` |
| **Elevada** | `120 – 129` | y | `< 80` |
| **Hipertensión grado 1** | `130 – 139` | o | `80 – 89` |
| **Hipertensión grado 2** | `≥ 140` | o | `≥ 90` |
| **Crisis hipertensiva** *(atención médica inmediata)* | `> 180` | y | `> 120` |

---

## 3. Temperatura Corporal (`mis-temp`)

* **Responsable:** Foco (Poco) (`listo: true`)
* **Fuente:** MedlinePlus — *Body temperature norms*: https://www.medlineplus.gov/ency/article/002341.htm?utm_source

* **Rango normal:** `36.5 °C – 37.3 °C` (`97.7 °F – 99.1 °F`).
* **Media de referencia:** `37.0 °C` (`98.6 °F`).

---

## 4. Saturación de Oxígeno — $\text{SpO}_2$ (`mis-oxigeno`)

* **Responsable:** Steve (`listo: true`)
* **Fuentes:**
  * WHO / Americares — *WHO Pulse Oximetry Training Manual*: https://www.americares.org/wp-content/uploads/globalassets/_mo/focus/ss/who-pulse-oximetry-training-manual2.pdf
  * NASA — *OCHMO-TB-003: Habitable Atmosphere*: https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-003-habitable-atmosphere.pdf

### Rangos Estándar en Tierra

| Clasificación | $\text{SpO}_2$ | Implicación Clínica |
| :--- | :---: | :--- |
| **Normal (Estándar saludable)** | `95 % – 100 %` | Oxigenación tisular adecuada. |
| **Aceptable / Límite inferior** | `93 % – 94 %` | Seguimiento preventivo. |
| **Hipoxemia leve** | `91 % – 92 %` | Requiere vigilancia médica; comienza a disminuir el suministro eficiente de oxígeno. |
| **Hipoxemia moderada** | `86 % – 90 %` | Señal de alerta clínica; generalmente requiere oxígeno suplementario. |

### Consideraciones Operativas en el Espacio
* **Estación Espacial Internacional (ISS):** Mantiene presión equivalente al nivel del mar (`~101.3 kPa` / `14.7 psi`) con `21 %` de $\text{O}_2$; la $\text{SpO}_2$ en reposo se mantiene normal (`96 % – 99 %`). Durante el sueño pueden presentarse ligeras caídas por redistribución de fluidos hacia el tórax y el cuello.
* **Naves futuras (Artemis / Marte) y trajes EVA:** Operan a menor presión total (`30 % – 55 %` de la presión terrestre) con concentraciones mayores de $\text{O}_2$ (`32 % – 100 %`), generando escenarios de hipoxia normobárica/hipobárica leve (p. ej., hábitats planificados a `8.2 psi` / `34 %` $\text{O}_2$).

---

## 5. Glucosa en Sangre (`mis-glucosa`)

* **Responsable:** Steve (`listo: true`)
* **Fuente:** MedlinePlus (ES) — *Examen de glucosa en sangre*: https://medlineplus.gov/spanish/ency/article/003482.htm

| Prueba / Momento de Medición | Rango Normal |
| :--- | :---: |
| **Glucosa en ayunas** *(mínimo 8 h sin calorías)* | `70 – 99 mg/dL` |
| **Glucosa postprandial (2 h)** *(tolerancia oral con 75 g de glucosa)* | `< 140 mg/dL` |
| **Hemoglobina glicosilada ($\text{HbA}_{1\text{c}}$)** *(promedio de últimos 2–3 meses)* | `< 5.7 %` |
| **Glucosa aleatoria** *(cualquier hora del día, con síntomas clásicos)* | `70 – 139 mg/dL` |
