# Documentación Oficial y Espacio de Trabajo — SpaceScan (`Scan Space · ARES VII`)

> **Repositorio Oficial de Código (`dev`):** `wakax-nasa-challenge-2026/` (`willor16/wakax-nasa-challenge-2026`)  
> **Diseño Oficial en Figma (`1568 × 940`):** [SpaceScan — Figma Design (`node-id=7382-2`)](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2&t=tzbC2RhJeGZ2Dlov-1)

---

## Estructura en 5 Capas Documentales

| Capa | Directorio / Archivo | Propósito Principal |
| :--- | :--- | :--- |
| **1. Especificaciones Normativas (Fuente de Verdad)** | [`control_avance/`](./control_avance/) | Reglas inquebrantables ([`REGLAS_INQUEBRANTABLES.md`](./control_avance/REGLAS_INQUEBRANTABLES.md)), estándar UI/UX y 6 colores ([`REGLAS_DISENO_UI_UX.md`](./control_avance/REGLAS_DISENO_UI_UX.md)), requerimientos funcionales y no funcionales ([`ESPECIFICACION_REQUERIMIENTOS.md`](./control_avance/ESPECIFICACION_REQUERIMIENTOS.md)), stack técnico ([`ARQUITECTURA_Y_STACK_TECNICO.md`](./control_avance/ARQUITECTURA_Y_STACK_TECNICO.md)) y reparto por desarrollador ([`DIVISION_TRABAJO_DEVS.md`](./control_avance/DIVISION_TRABAJO_DEVS.md)). |
| **2. Estado de Implementación (`dev`)** | [`control_avance/BITACORA_AVANCE_RETO.md`](./control_avance/BITACORA_AVANCE_RETO.md) | Bitácora verificada con el cierre completo de Fase 0 y Fase 1 (`D1-01`..`D1-07`, `D2-01`..`D2-06`, `D3-01`..`D3-06`) y las revisiones integrales de cumplimiento (`PR #14` y `PR #16`) en la rama `dev`. |
| **3. Investigación y Abstracción Biomédica** | [`docs-investigacion/`](./docs-investigacion/README.md) | 6 fichas clínicas por dominio (`01` a `06_*.md`) y [`parametros_investigacion.json`](./docs-investigacion/parametros_investigacion.json), que alimentan `backend/db/seed_snapshots/reference_ranges.json` (`38` métricas clínicas). |
| **4. Recursos Oficiales del Reto** | [`bases_reto/`](./bases_reto/RETO_OFICIAL_NASA_2026.md) | Consigna oficial (`?tab=details`), guía de evaluación y 10 premios globales ([`RETO_OFICIAL_NASA_2026.md`](./bases_reto/RETO_OFICIAL_NASA_2026.md)), recursos oficiales de NASA HRP y CSA en `?tab=resources` ([`RECURSOS_OFICIALES_RETO_2026.md`](./bases_reto/RECURSOS_OFICIALES_RETO_2026.md)) y [`reto_oficial_nasa_2026.json`](./bases_reto/reto_oficial_nasa_2026.json). |
| **5. Directivas de IA y Torre de Control Interna** | [`instrucciones_ia/DIRECTIVAS_AGENTE_AI.md`](./instrucciones_ia/DIRECTIVAS_AGENTE_AI.md)<br>[`miWork/`](./miWork/ESPECIFICACION_CONTROL_AVANCE.md) | Directivas operativas para agentes de IA y dashboard colaborativo local (`Puerto 8000`), junto con las guías operativas en [`miWork/docs/GUIA_INICIO_tecnica_EQUIPO.md`](./miWork/docs/GUIA_INICIO_tecnica_EQUIPO.md), [`miWork/docs/guia_pruebas_funcionales_web.md`](./miWork/docs/guia_pruebas_funcionales_web.md) y [`miWork/docs/usuarios.md`](./miWork/docs/usuarios.md). |
