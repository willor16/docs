# 01. Antropometría y Composición Corporal

> **Parámetros cubiertos:** `data-osea` (Densidad Ósea), `data-muscular` (Masa Muscular) y `data-imc` (IMC).

---

## 1. Densidad Ósea (`data-osea`)

* **Responsable:** Steve (`listo: true`)
* **Fuentes:**
  * NASA — *Risk of Reduced Cardiorespiratory and Musculoskeletal Fitness*: https://www.nasa.gov/reference/risk-of-reduced-cardiorespiratory-and-musculoskeletal-fitness/
  * Nature (*npj Microgravity*) — *Revisión sistemática y metaanálisis de la pérdida ósea en viajeros espaciales*: https://www.nature.com/articles/s41526-020-0103-2

### Hallazgos y Pérdida de Densidad por Región Anatómica (Figura 2 del metaanálisis)
* El documento de NASA aborda el riesgo de manera macro con cuidados y recomendaciones; el artículo de *Nature* aporta mediciones micro por región corporal en misiones mayores a 28 días:

| Región | Cambio de Densidad Mineral Ósea | Condición / Observación |
| :--- | :---: | :--- |
| **Región 1 — Cráneo y cuello** | `+2.2 %` (ganancia) | Redistribución de carga y fluidos en microgravedad. |
| **Región 2 — Tórax y extremidades superiores** | `-0.7 %` (pérdida) | Misiones mayores a 28 días. |
| **Región 3 — Pelvis y columna lumbar** | `-6.2 %` (pérdida severa) | Zona crítica de soporte de carga. |
| **Región 4 — Extremidades inferiores** | `-5.4 %` (pérdida severa) | Misiones mayores a 28 días. |

---

## 2. Masa Muscular Esquelética (`data-muscular`)

* **Responsable:** Steve (`listo: true`)
* **Fuentes:**
  * NASA — *Counteracting Bone and Muscle Loss in Microgravity*: https://www.nasa.gov/missions/station/iss-research/counteracting-bone-and-muscle-loss-in-microgravity/
  * NASA — *Risk of Reduced Cardiorespiratory and Musculoskeletal Fitness*: https://www.nasa.gov/reference/risk-of-reduced-cardiorespiratory-and-musculoskeletal-fitness/

### Estándares de Referencia (18 – 39 años)

| Sexo | Masa Muscular Absoluta Promedio | IMM Saludable (Bioimpedancia) | IMM Saludable (DXA apendicular) |
| :--- | :---: | :---: | :---: |
| **Hombres (18–39 años)** | `28 – 36 kg` | `≥ 8.50 kg/m²` | `≥ 7.00 kg/m²` |
| **Mujeres (18–39 años)** | `18 – 24 kg` | `≥ 5.75 kg/m²` | `≥ 5.50 kg/m²` |

### Fórmula del Índice de Masa Muscular Esquelética (IMM)

$$
\text{IMM}\;(\text{kg/m}^2) = \frac{\text{Masa Muscular Esquelética (kg)}}{\text{Estatura (m)}^2}
$$

### Dinámica en Microgravedad
* **Atrofia por descarga mecánica inmediata:** Sin ejercicio intenso, los astronautas pueden perder hasta un **`20 %`** de su masa muscular en **`5 a 11 días`** en el espacio.
* **Misiones de 4 a 6 meses con rutinas estándar:** La pérdida promedio de fuerza y masa muscular se sitúa entre **`10 %` y `12 %`**.
* Se observa además **transformación del tipo de fibra muscular**.

---

## 3. Índice de Masa Corporal por Fases de Misión (`data-imc`)

* **Responsable:** Foco (Poco) en ítem padre (`listo: true`), Sandra en subtarea (`tomado: true`, `enProceso: true`).
* **Fuente:** NASA-STD-3001 Volume 2: https://www.nasa.gov/wp-content/uploads/2025/05/nasa-std-3001-vol-2.pdf

### Criterios por Fase

#### Fase Pre-vuelo
* **Óptimo (bueno):** `18.5 – 24.9 kg/m²` *(en la nota original decía `g/m2`; normalizado a `kg/m²`)*.
* **Aceptable (precaución):** `25.0 – 27.9 kg/m²` (o `18.0 – 18.4 kg/m²` condicionado a composición corporal magra).
* **Crítico (no apto):** `< 18.0 kg/m²` o `≥ 28.0 – 30.0+ kg/m²`.

#### Fase En Vuelo
* **Norma nutricional:** Cubrir el **`100 %`** de los requerimientos calóricos y de nutrientes calculados según edad, sexo, masa corporal (`kg`) y estatura (`m`).

#### Fase Post-vuelo
* **Óptimo (bueno):** Retención `> 95 %` de masa basal al aterrizar (IMC dentro de `±1.0 kg/m²` respecto al inicial).
* **Aceptable (precaución):** Retención entre `90 %` y `95 %` al aterrizar y recuperación del `95 % – 97 %`.
* **Crítico (alerta médica):** Retención `< 90 %` al aterrizar (pérdida `> 10 %`) o `< 95 %` tras `45 – 60 días` de rehabilitación.
* **Norma de recuperación:** Evaluación y tratamiento nutricional dirigidos a retornar al valor basal previo a la misión.
