# Recursos Oficiales del Reto (`?tab=resources`) — NASA Space Apps Challenge 2026

> **Fuente Oficial:** [Create Health Monitoring Software for Astronauts on Space Missions — Resources Tab](https://www.spaceappschallenge.org/2026/challenges/health-monitoring-software/?tab=resources)  
> **Documento Complementario:** [RETO_OFICIAL_NASA_2026.md](./RETO_OFICIAL_NASA_2026.md) (`?tab=details` y Guía de Evaluación)  
> **Propósito:** Registrar íntegramente los recursos oficiales publicados por la NASA y agencias espaciales asociadas en la pestaña **Resources** del reto, y establecer su trazabilidad con la investigación del equipo ([docs/docs-investigacion/](../docs-investigacion/README.md)) para cumplir el requisito obligatorio de elegibilidad ante el jurado.

---

## 1. Aviso Legal Oficial en la Pestaña `Resources`

> *"NASA does not endorse any non-U.S. Government entity and is not responsible for information contained on non-U.S. Government websites. For non-U.S. Government websites, participants must comply with any data use parameters of that specific website."*  
> *(La NASA no respalda a ninguna entidad ajena al Gobierno de los EE. UU. ni es responsable de la información contenida en sitios web no gubernamentales. Para sitios web ajenos al Gobierno de los EE. UU., los participantes deben cumplir con los parámetros de uso de datos de dicho sitio web).*

---

## 2. NASA Data & Resources (Datos y Recursos de la NASA)

| # | Recurso Oficial | Enlace Oficial | Descripción Oficial (EN / ES) |
| :---: | :--- | :--- | :--- |
| **1** | **5 Hazards of Human Spaceflight** | https://www.nasa.gov/hrp/hazards/ | **EN:** *Basic information from NASA’s human research program on the main hazards that affect humans on space missions. It also provides links to detailed NASA articles and reports related to a specific hazard.*<br>**ES:** Información base del Programa de Investigación Humana (*Human Research Program*, HRP) sobre los 5 peligros principales que afectan al ser humano en misiones espaciales (radiación, aislamiento/confinamiento, distancia de la Tierra, campos de gravedad alterados y entornos cerrados hostiles), con enlaces a artículos y reportes detallados por peligro. |
| **2** | **Risks of Human Spaceflight** | https://www.nasa.gov/hrp/risks/ | **EN:** *Basic information from NASA’s human research program on the main risks faced by humans on space missions. It also provides links to detailed NASA articles and reports related to a specific risk.*<br>**ES:** Información base del HRP sobre los riesgos clínicos y operativos específicos que enfrentan los astronautas en misiones espaciales, con enlaces a reportes técnicos detallados por riesgo (cardiovascular, musculoesquelético, SANS, sueño, inmunológico, conductual). |
| **3** | **Ongoing HRP Research in Space** | https://www.nasa.gov/hrp/ongoing-hrp-research/ | **EN:** *Articles from ongoing research on NASA’s human research program.*<br>**ES:** Artículos y avances de investigaciones activas en curso dentro del Programa de Investigación Humana de la NASA. |

---

## 3. Space Agency Partner Resources (Recursos de Agencias Espaciales Asociadas)

### CSA — Canadian Space Agency (Agencia Espacial Canadiense)

| # | Recurso Oficial | Enlace Oficial | Descripción Oficial (EN / ES) |
| :---: | :--- | :--- | :--- |
| **1** | **Monitoring Radiation for Astronaut Health** | https://www.asc-csa.gc.ca/eng/news/articles/2026/2026-02-26-monitoring-radiation-astronaut-health.asp | **EN:** *Learn how the CSA is helping monitor space radiation to better protect astronaut health during long-duration missions. This resource highlights Canadian technologies and research used to measure radiation exposure in space and improve our understanding of its effects on the human body.*<br>**ES:** Explica cómo la CSA contribuye al monitoreo de radiación espacial para proteger la salud de los astronautas en misiones de larga duración, destacando tecnologías e investigación canadiense para medir la exposición a la radiación y comprender sus efectos en el cuerpo humano. |
| **2** | **Why Do We Conduct Science Experiments in Space?** | https://www.asc-csa.gc.ca/eng/iss/science/why-do-we-conduct-science-experiments-in-space.asp | **EN:** *This CSA resource explains how the unique environment of space allows scientists to conduct experiments that cannot be performed on Earth. Learn how research aboard the International Space Station advances our understanding of human health, technology, and the universe. The discoveries made in space help improve life on Earth while supporting future exploration missions.*<br>**ES:** Explica cómo el entorno único del espacio permite realizar experimentos imposibles en la Tierra y cómo la investigación a bordo de la ISS impulsa el conocimiento sobre salud humana, tecnología y el universo, generando descubrimientos que mejoran la vida en la Tierra y respaldan futuras misiones de exploración. |

---

## 4. Trazabilidad con la Investigación del Equipo y Módulos del Proyecto

Para satisfacer el criterio de elegibilidad de la **Judging & Awards Guide** (*uso explícito y citado de recursos de NASA y agencias asociadas*), así se conectan los 5 recursos oficiales de `?tab=resources` con la investigación en [docs/docs-investigacion/](../docs-investigacion/README.md) y el diseño funcional:

| Recurso Oficial (`?tab=resources`) | Ficha en `docs-investigacion/` que lo Aterriza | Aplicación en el Sistema y Premios Globales que Refuerza |
| :--- | :--- | :--- |
| **NASA HRP — 5 Hazards of Human Spaceflight**<br>https://www.nasa.gov/hrp/hazards/ | [01_antropometria_y_composicion.md](../docs-investigacion/01_antropometria_y_composicion.md)<br>[04_sueno_estres_y_psicologia.md](../docs-investigacion/04_sueno_estres_y_psicologia.md)<br>[06_ambiente_cabina_y_radiacion.md](../docs-investigacion/06_ambiente_cabina_y_radiacion.md) | Estructura integral de monitoreo frente a microgravedad, aislamiento, radiación, ambiente cerrado ($\text{CO}_2$, temperatura, humedad) y distancia a Tierra (operación 100% autónoma y cola diferida en `/comms`).<br>*Premios:* **Best Mission Concept**, **Best Use of Science**. |
| **NASA HRP — Risks of Human Spaceflight**<br>https://www.nasa.gov/hrp/risks/ | [01_antropometria_y_composicion.md](../docs-investigacion/01_antropometria_y_composicion.md) (`risk-of-reduced-cardiorespiratory-and-musculoskeletal-fitness`)<br>[03_salud_ocular_sans.md](../docs-investigacion/03_salud_ocular_sans.md) (`OCHMO-MTB-001 SANS`)<br>[05_nutricion_hidratacion_ejercicio.md](../docs-investigacion/05_nutricion_hidratacion_ejercicio.md) | Catálogo de métricas clínicas (`metric_catalog`), cálculo de desviación (*z-score*) contra línea base personal, módulo ocular bilateral (`/vision`), monitoreo de sueño (`/sleep`) y contramedidas.<br>*Premios:* **Best Use of Science**, **Best Use of Data**. |
| **NASA HRP — Ongoing HRP Research in Space**<br>https://www.nasa.gov/hrp/ongoing-hrp-research/ | [01_antropometria_y_composicion.md](../docs-investigacion/01_antropometria_y_composicion.md) (`counteracting-bone-and-muscle-loss-in-microgravity`)<br>[02_signos_vitales_y_metabolismo.md](../docs-investigacion/02_signos_vitales_y_metabolismo.md) | Seguimiento longitudinal por etapas de misión (`LAUNCH` / `MISSION` / `RETURN`) en `/profile/*` y protocolos clínicos en la guía médica (`/guide`).<br>*Premios:* **Best Use of Storytelling**, **Best Use of Science**. |
| **CSA — Monitoring Radiation for Astronaut Health**<br>https://www.asc-csa.gc.ca/eng/news/articles/2026/2026-02-26-monitoring-radiation-astronaut-health.asp | [06_ambiente_cabina_y_radiacion.md](../docs-investigacion/06_ambiente_cabina_y_radiacion.md) (`res-radiacion`, límites en $\text{mSv/año}$ y `SRE`) | Monitoreo de dosis acumulada de radiación (`mSv`), estado de escudo (`eva_shield_ready` en `/crew-streaks`) y telemetría de clima solar en `/comms`.<br>*Premios:* **Best Use of Data**, **Global Connection**, **Best Mission Concept**. |
| **CSA — Why Do We Conduct Science Experiments in Space?**<br>https://www.asc-csa.gc.ca/eng/iss/science/why-do-we-conduct-science-experiments-in-space.asp | [README.md](../docs-investigacion/README.md) | Justificación de impacto dual: cómo la telemedicina autónoma diseñada para el espacio transfiere beneficios directos a clínicas rurales y entornos desconectados en la Tierra.<br>*Premios:* **Galactic Impact**, **Local Impact**, **Most Inspirational**. |

---

## 5. Bloque Listo para Citar en la Entrega Oficial (En Inglés)

> *(Para incluir en la sección de referencias de la página de proyecto en Space Apps — recordar que dentro de la interfaz de la aplicación entregable rige la prohibición de mostrar la marca "NASA" establecida en `REGLAS_INQUEBRANTABLES.md`, pero en el formulario web de entrega de Space Apps sí es obligatorio listar los recursos oficiales utilizados)*:

```markdown
### Official Space Agency Resources Used (Challenge Resources Tab)
- **NASA Human Research Program (HRP) — 5 Hazards of Human Spaceflight:** https://www.nasa.gov/hrp/hazards/
- **NASA Human Research Program (HRP) — Risks of Human Spaceflight:** https://www.nasa.gov/hrp/risks/
- **NASA Human Research Program (HRP) — Ongoing HRP Research in Space:** https://www.nasa.gov/hrp/ongoing-hrp-research/
- **Canadian Space Agency (CSA) — Monitoring Radiation for Astronaut Health:** https://www.asc-csa.gc.ca/eng/news/articles/2026/2026-02-26-monitoring-radiation-astronaut-health.asp
- **Canadian Space Agency (CSA) — Why Do We Conduct Science Experiments in Space?:** https://www.asc-csa.gc.ca/eng/iss/science/why-do-we-conduct-science-experiments-in-space.asp
```
