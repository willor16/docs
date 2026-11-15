# 04. Sueño, Estrés y Salud Conductual

> **Parámetros cubiertos:** `ind-sueno` (Sueño), `ind-estres` (Nivel de estrés), y estado de cobertura de `ind-animo`, `ind-soledad`, `ind-motivacion`.

---

## 1. Arquitectura y Calidad del Sueño (`ind-sueno`)

* **Responsable:** Steve (`listo: true`)
* **Fuentes:**
  * NCBI Bookshelf — *Physiology, Sleep Stages (`NBK526132`)*: https://www.ncbi.nlm.nih.gov/books/NBK526132/
  * National Sleep Foundation — *What is Sleep Quality?*: https://www.thensf.org/what-is-sleep-quality/

### Duración y Distribución de Fases (Adultos 26–64 años)
* **Duración recomendada:** `7 – 9 horas`
* **Duración no recomendada:** `< 6 h` o `> 10 h`

| Fase del Sueño | Proporción Esperada | Características |
| :--- | :---: | :--- |
| **N1 (Sueño ligero — transición)** | `~5 %` | Transición inicial al sueño. |
| **N2 (Sueño ligero estable)** | `45 % – 55 %` | Desciende la temperatura corporal. |
| **N3 (Sueño profundo / Ondas lentas — SWS)** | `15 % – 25 %` | Predomina en la primera mitad de la noche. |
| **REM (Movimientos oculares rápidos)** | `20 % – 25 %` | Consolidación cognitiva y regulación emocional. |

### Indicadores Fisiológicos Durante el Sueño

| Indicador | Rango / Comportamiento Normal |
| :--- | :--- |
| **Frecuencia Cardíaca (FC)** | `45 – 65 lpm` (caída del `10 % – 20 %` respecto al estado despierto) |
| **Variabilidad de Frecuencia Cardíaca (VFC / HRV — RMSSD)** | `40 – 80+ ms` (aumento del `15 % – 40 %` sobre la media diurna) |
| **Frecuencia Respiratoria** | `12 – 15 respiraciones/min` (caída de `1 – 3 rpm`) |
| **Movimiento (Acelerómetro)** | `< 1 movimiento cada 10 – 15 min` (inmovilidad sostenida) |
| **Temperatura cutánea (Muñeca)** | `34.5 °C – 35.5 °C` (sube ligeramente en piel mientras baja la temperatura interna) |

---

## 2. Biomarcadores de Estrés (`ind-estres`)

* **Responsable:** Foco (Poco) en ítem padre (`listo: true`), Steve en subtareas (`listo: true`).
* **Fuentes:**
  * MedlinePlus (ES) — *Prueba de cortisol*: https://medlineplus.gov/spanish/pruebas-de-laboratorio/prueba-de-cortisol/
  * Frontiers in Public Health — *HRV Metrics and Norms*: https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2017.00258/full

| Biomarcador | Rango Normal (Reposo / Bajo Estrés) | Indicador de Estrés Agudo o Crónico |
| :--- | :--- | :--- |
| **Cortisol sérico (Sangre)** | Mañana (8:00 a.m.): `5 – 25 mcg/dL`<br>Tarde (4:00 p.m.): `3 – 16 mcg/dL` | `> 25 mcg/dL` en la mañana o pérdida del descenso nocturno. |
| **Cortisol salival** | Mañana: `0.10 – 1.50 mcg/dL`<br>Noche: `< 0.15 mcg/dL` | `> 0.15 – 0.20 mcg/dL` antes de dormir. |
| **VFC / HRV (RMSSD)** | Adulto sano: `30 – 100+ ms` *(varía según edad)* | `< 20 – 30 ms` (caída sostenida respecto a la línea base individual). |

---

## 3. Indicadores Psicológicos sin Notas Detalladas en `state.json`

* `ind-animo` (Estado de ánimo), `ind-soledad` (Soledad) e `ind-motivacion` (Motivación) figuran marcados con `listo: true` por `Foco (Poco)`, pero no tienen subtareas, enlaces ni rangos documentados en `state.json`.
