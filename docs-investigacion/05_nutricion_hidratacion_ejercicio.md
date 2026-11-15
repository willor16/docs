# 05. Nutrición, Hidratación y Ejercicio Contramedida

> **Parámetros cubiertos:** `ind-alimentacion` (Alimentación), `ind-hidratacion` (Hidratación) y `mis-ejercicio` (Ejercicio).

---

## 1. Alimentación y Requerimientos Energéticos (`ind-alimentacion`)

* **Responsable:** Steve (`listo: true`)
* **Fuentes:**
  * AJCN — *Caloric Requirements*: https://ajcn.nutrition.org/article/S0002-9165(23)16698-6/abstract
  * Dietary Guidelines for Americans 2020–2025: https://www.dietaryguidelines.gov/sites/default/files/2020-12/Dietary_Guidelines_for_Americans_2020-2025.pdf

### Requerimiento Calórico Diario por Edad y Sexo

| Grupo | Nivel Base / Moderado | Nivel Activo |
| :--- | :---: | :---: |
| **Hombres (19–30 años)** | `2,400 kcal / día` | `2,600 – 2,800 kcal / día` |
| **Hombres (31–50 años)** | `2,200 kcal / día` | `2,400 – 2,600 kcal / día` |
| **Mujeres (19–30 años)** | `1,800 – 2,000 kcal / día` | `2,000 – 2,200 kcal / día` |
| **Mujeres (31–50 años)** | `1,800 kcal / día` | `2,000 kcal / día` |

### Distribución de Macronutrientes
* **Carbohidratos:** `45 % – 65 %` (`4 kcal/g`).
* **Grasas (Lípidos):** `20 % – 35 %` (`9 kcal/g`).
* **Proteínas:** `10 % – 35 %` (`4 kcal/g`; mínimo clínico `0.8 g/kg` de peso corporal, subiendo a `1.2 – 2.0 g/kg` en personas activas).

### Tasa Metabólica Basal (TMB — Mifflin-St Jeor)

**Hombres:**

$$
\text{TMB} = (10 \times \text{Peso en kg}) + (6.25 \times \text{Estatura en cm}) - (5 \times \text{Edad en años}) + 5
$$

**Mujeres:**

$$
\text{TMB} = (10 \times \text{Peso en kg}) + (6.25 \times \text{Estatura en cm}) - (5 \times \text{Edad en años}) - 161
$$

---

## 2. Hidratación (`ind-hidratacion`)

* **Responsable:** Steve (`listo: true`)
* **Fuentes:**
  * HPRC — *Urine Color Charts*: https://www.hprc-online.org/nutrition/nutrition-fundamentals/how-accurately-assess-hydration-status-using-urine-color-charts
  * GSSI — *Urine Markers for Hydration Monitoring*: https://www.gssiweb.org/en/sports-science-exchange/article/urine-markers-for-hydration-monitoring--practical-assessment-and-interpretation

### Test de Hidratación por Colorimetría de Orina

| Nivel en Escala de Color | Estado de Hidratación |
| :---: | :--- |
| `1 – 3` | **Bien hidratado** |
| `4 – 6` | **Hipohidratado** |
| `≥ 7` | **Deshidratado** |

### Estándares de Ingesta y Marcador Plasmático
* **Ingesta total (Hombres adultos):** `2.5 – 3.7 L/día`.
* **Ingesta total (Mujeres adultas):** `2.0 – 2.7 L/día`.
* **Fórmula por peso corporal:** `30 – 35 mL/kg`.
* **Osmolalidad plasmática (Sangre):** `275 – 295 mOsm/kg` (marcador fisiológico más estricto; valores `> 295 mOsm/kg` indican deshidratación).

---

## 3. Ejercicio Contramedida (`mis-ejercicio`)

* **Responsable:** Sandra (`listo: true`), subtarea validada por Steve (`listo: true`).
* **Fuente:** NASA — *SP-20250000273*: https://www.nasa.gov/wp-content/uploads/2025/02/sp-20250000273.pdf?emrc=

| Duración de la Misión | Frecuencia de Ejercicio | Duración por Sesión | Norma Aeróbica |
| :--- | :---: | :---: | :--- |
| **Muy corta (`< 10 días`)** | Sin ejercicio | Sin ejercicio | — |
| **Corta (`hasta 14 días`)** | `3 días / semana` | `20 min` (variable) | — |
| **Larga (`≥ 180 días`)** | `6 – 7 días / semana` | `30 min` | Mantener al menos **`80 %`** del $\text{VO}_2\text{ máx}$ previo al vuelo. |
