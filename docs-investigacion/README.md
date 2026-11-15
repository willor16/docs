# Investigación Biomédica y Operativa Recopilada (`docs-investigacion`)

> **Origen:** Consolidación limpia y estructurada de las notas y referencias recopiladas por el equipo en [docs/miWork/state.json](../miWork/state.json).  
> **Nota de gobernanza:** Este directorio recopila la **investigación de soporte científico y biomédico**. Las reglas normativas de arquitectura, diseño UI/UX y contratos del sistema entregable residen en [docs/control_avance/](../control_avance/), y las bases oficiales del desafío residen en [docs/bases_reto/](../bases_reto/).

---

## 1. Índice de Fichas Temáticas

| Archivo | Dominio | Parámetros Cubiertos (`miWork`) | Responsable(s) |
| :--- | :--- | :--- | :--- |
| [01_antropometria_y_composicion.md](./01_antropometria_y_composicion.md) | Antropometría y Composición Corporal | `data-osea`, `data-muscular`, `data-imc` | Steve, Sandra |
| [02_signos_vitales_y_metabolismo.md](./02_signos_vitales_y_metabolismo.md) | Signos Vitales y Metabolismo | `data-ritmo`, `data-presion`, `mis-temp`, `mis-oxigeno`, `mis-glucosa` | Foco (Poco), Steve |
| [03_salud_ocular_sans.md](./03_salud_ocular_sans.md) | Salud Ocular y Síndrome SANS | `res-mot-vista`, `mis-examenes` | Sandra |
| [04_sueno_estres_y_psicologia.md](./04_sueno_estres_y_psicologia.md) | Sueño, Estrés y Salud Conductual | `ind-sueno`, `ind-estres`, `ind-animo`, `ind-soledad`, `ind-motivacion` | Steve, Foco (Poco) |
| [05_nutricion_hidratacion_ejercicio.md](./05_nutricion_hidratacion_ejercicio.md) | Nutrición, Hidratación y Ejercicio | `ind-alimentacion`, `ind-hidratacion`, `mis-ejercicio` | Steve, Sandra |
| [06_ambiente_cabina_y_radiacion.md](./06_ambiente_cabina_y_radiacion.md) | Ambiente de Cabina y Radiación | `mis-humedad`, `res-radiacion` | Foco (Poco), Steve |
| [parametros_investigacion.json](./parametros_investigacion.json) | Catálogo Estructurado JSON | Todos los parámetros anteriores + referencias | Equipo |

---

## 2. Brechas de Documentación Detectadas en `state.json`

Algunos ítems del checklist figuran marcados sin notas detalladas en `subtasks`:

| ID en `miWork` | Nombre en Checklist | Estado en `itemStatus` | Observación |
| :--- | :--- | :--- | :--- |
| `ind-animo` | Estado de ánimo | `listo: true` (`Foco (Poco)`) | Sin subtareas ni notas registradas en `state.json`. |
| `ind-soledad` | Soledad | `listo: true` (`Foco (Poco)`) | Sin subtareas ni notas registradas en `state.json`. |
| `ind-motivacion` | Motivación | `listo: true` (`Foco (Poco)`) | Sin subtareas ni notas registradas en `state.json`. |
| `mis-oscultar` | Auscultación | Booleano `true`, sin `itemStatus` | Sin subtareas ni notas registradas en `state.json`. |
| `mis-motrices` | Motrices | `proceso: true`, `listo: false` (`Foco (Poco)`) | Sin subtareas ni notas registradas en `state.json`. |
| `mis-tiempo-mision` | Tiempo de misión | Archivado (`Foco (Poco)`) | Marcado `listo: true` antes de archivarse; sin notas en `subtasks`. |

---

## 3. Catálogo Consolidado de Fuentes Científicas Citadas

| Fuente / Institución | Documento / Recurso | URL |
| :--- | :--- | :--- |
| **NASA** | Risk of Reduced Cardiorespiratory and Musculoskeletal Fitness | https://www.nasa.gov/reference/risk-of-reduced-cardiorespiratory-and-musculoskeletal-fitness/ |
| **NASA** | Counteracting Bone and Muscle Loss in Microgravity | https://www.nasa.gov/missions/station/iss-research/counteracting-bone-and-muscle-loss-in-microgravity/ |
| **NASA** | The Human Body in Space | https://www.nasa.gov/humans-in-space/the-human-body-in-space/ |
| **NASA** | About the Space Radiation Element (SRE) | https://www.nasa.gov/reference/about-the-space-radiation-element/ |
| **NASA** | OCHMO-TB-020: Radiation Protection | https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-020-radiation-protection.pdf |
| **NASA** | OCHMO-TB-003: Habitable Atmosphere | https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-003-habitable-atmosphere.pdf |
| **NASA** | OCHMO-MTB-001: Spaceflight Associated Neuro-ocular Syndrome (SANS) | https://www.nasa.gov/wp-content/uploads/2024/02/ochmo-mtb-001-sans.pdf?emrc=d4c581 |
| **NASA** | NASA-STD-3001 Volume 2 (Human Factors, Habitability, and Environmental Health) | https://www.nasa.gov/wp-content/uploads/2025/05/nasa-std-3001-vol-2.pdf |
| **NASA** | Natural and Induced Environments Vol. 2 | https://www.nasa.gov/reference/6-0-natural-and-induced-environments-vol-2/?utm_source |
| **NASA** | SP-20250000273 (Exercise Countermeasures) | https://www.nasa.gov/wp-content/uploads/2025/02/sp-20250000273.pdf?emrc= |
| **Nature (`npj Microgravity`)** | Revisión sistemática y metaanálisis de la pérdida ósea en viajeros espaciales | https://www.nature.com/articles/s41526-020-0103-2 |
| **MedlinePlus** | Body temperature norms | https://www.medlineplus.gov/ency/article/002341.htm?utm_source |
| **MedlinePlus** | Pulse (Heart rate) | https://medlineplus.gov/ency/article/003399.htm?utm_source |
| **MedlinePlus (ES)** | Medición de la presión arterial | https://medlineplus.gov/spanish/pruebas-de-laboratorio/medicion-de-la-presion-arterial/?utm_source |
| **MedlinePlus (ES)** | Prueba de cortisol | https://medlineplus.gov/spanish/pruebas-de-laboratorio/prueba-de-cortisol/ |
| **MedlinePlus (ES)** | Examen de glucosa en sangre | https://medlineplus.gov/spanish/ency/article/003482.htm |
| **NCBI Bookshelf** | Physiology, Sleep Stages (`NBK526132`) | https://www.ncbi.nlm.nih.gov/books/NBK526132/ |
| **National Sleep Foundation** | What is Sleep Quality? | https://www.thensf.org/what-is-sleep-quality/ |
| **Frontiers in Public Health** | An Overview of Heart Rate Variability Metrics and Norms (2017) | https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2017.00258/full |
| **HPRC** | How to Accurately Assess Hydration Status Using Urine Color Charts | https://www.hprc-online.org/nutrition/nutrition-fundamentals/how-accurately-assess-hydration-status-using-urine-color-charts |
| **GSSI** | Urine Markers for Hydration Monitoring | https://www.gssiweb.org/en/sports-science-exchange/article/urine-markers-for-hydration-monitoring--practical-assessment-and-interpretation |
| **WHO / Americares** | WHO Pulse Oximetry Training Manual | https://www.americares.org/wp-content/uploads/globalassets/_mo/focus/ss/who-pulse-oximetry-training-manual2.pdf |
| **AJCN** | Energy / Caloric Requirements (`S0002-9165(23)16698-6`) | https://ajcn.nutrition.org/article/S0002-9165(23)16698-6/abstract |
| **Dietary Guidelines** | Dietary Guidelines for Americans 2020–2025 | https://www.dietaryguidelines.gov/sites/default/files/2020-12/Dietary_Guidelines_for_Americans_2020-2025.pdf |
