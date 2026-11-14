# Bitácora de Avance y Resumen Maestro del Proyecto — SpaceScan

> **ESTADO ACTUAL:** Fase 0 cerrada y arranque de Fase 1 (Semana 1: `D1-01`, `D1-02` y contratos base `D3-01`/`D1-06`) implementado en `wakax-nasa-challenge-2026/` (`chore/foundation-and-schema`).  
> **NOMBRE DEL SISTEMA:** **SpaceScan (`Scan Space · ARES VII`)**  
> **DISEÑO OFICIAL (FIGMA):** [SpaceScan — Figma Design (`node-id=7382-2`)](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2&t=tzbC2RhJeGZ2Dlov-1)

---

## 1. Índice de Documentación Prioritaria Consolidada en `docs/`

Toda la definición funcional, visual, normativa y técnica revisada por el equipo ha sido integrada en los siguientes documentos dentro de `docs/control_avance/`:

| Documento | Contenido Clave |
| :--- | :--- |
| [**1. Reglas Inquebrantables**](./REGLAS_INQUEBRANTABLES.md) | Regla de oro de los **10 premios globales** + checklist obligatorio por PR, etapas (*Antes / Durante / Después* del despegue), datos a recolectar, fidelidad al Figma, flujo de trabajo, **idioma 100% inglés puro sin jerga técnica en UI** y **palabras/entidades prohibidas** (NASA / China). |
| [**2. Estándar Global de Diseño UI/UX**](./REGLAS_DISENO_UI_UX.md) | **Única fuente de verdad de diseño y construcción:** las **5 Leyes Inquebrantables de Diseño**, **Paleta Oficial de 6 Colores** (`#001524`, `#15616D`, `#FFECD1`, `#2AEF4B`, `#000C5C`, `#D5110B` en `tokens.css`), tipografía (`Inter` + `JetBrains Mono`) e iconos locales, **mapeo de las 16 pantallas Figma (`1568 × 940`)**, plantillas de código y checklist *Definition of Done*. |
| [**3. Especificación de Requerimientos**](./ESPECIFICACION_REQUERIMIENTOS.md) | Objetivo general y específicos, **5 actores y roles** (`Astronauta`, `Piloto`, `Operador`, `Médico`, `Control a tierra`), niveles de acceso en cabina (público vs. PIN de 4 dígitos), **RF 3.1 a 3.12**, Requerimientos de Información y **RNF 1 a 5**. |
| [**4. Arquitectura y Stack Técnico**](./ARQUITECTURA_Y_STACK_TECNICO.md) | Ejecución **100% a bordo y sin internet** en un solo proceso y puerto: **Nuxt 4 SPA** + Tailwind 4 + Reka UI + ECharts (`'spacescan-hud'`) + Web Audio API; **Python 3.13 + FastAPI + SQLite 3 STRICT** (WAL, triggers *append-only*, FTS5, JSON1) + **ONNX Runtime** + **Ollama** local. |
| [**5. División del Trabajo (3 Devs)**](./DIVISION_TRABAJO_DEVS.md) | **Fase 0** (`backend/db/schema.sql` con tablas `STRICT` y `measurements` *append-only*) y **Fase 1** en paralelo: **Dev 1** (`D1-01` a `D1-07`), **Dev 2** (`D2-01` a `D2-06`) y **Dev 3** (`D3-01` a `D3-07`), con calendario de 4 semanas y sustitutos temporales sin bloqueos. |

---

## 2. Síntesis Arquitectónica y Visual de SpaceScan (`16 Pantallas Figma`)

### 2.1 Jerarquía de Navegación en 2 Niveles y Separación Resultados vs. Captura
* **Nivel 1 Público (Sin PIN — Barra inferior de 3 pestañas):**
  * `01_Sign_In.svg` (`/login`): Acceso exclusivo por PIN de 4 dígitos + botones directos a vistas públicas.
  * `02_Crew_Overview.svg` (`/crew-overview`): Resumen grupal de solo lectura (*Optimal / Nominal / Attention*, signos clave y ambiente de cabina).
  * `03_Crew_Streaks.svg` (`/crew-streaks`): Rachas individuales y grupal de solo lectura.
* **Nivel 2 Autenticado (Tras PIN — Dock inferior trapezoidal simétrico de 7 módulos con `Profile` elevado al centro):**
  * `1 Vision` (`/vision` — `08_Vision_Exam.svg`, **Solo Resultados**).
  * `2 Sleep` (`/sleep` — `07_Sleep_Monitor.svg`, **Solo Resultados** con barra de cintas ECharts).
  * `3 Auscultation` (`/auscultation` — `09_Auscultation_Results.svg`, **Solo Resultados** con fonocardiograma `S1/S2` y $\text{CO}_2$).
  * **`[4 PROFILE — Principal Central]`** (`/profile/personal` `04`, `/profile/psychological` `05`, `/profile/physical` `06`, **Solo Resultados**).
  * `5 Capture` (**Único módulo con formularios e inputs**, dividido en 4 sub-pestañas: `/capture/auscultation` `10`, `/capture/physical` `11`, `/capture/vision` `12`, `/capture/psych-sleep` `13`).
  * `6 Guide` (`/guide` — `14_Medical_Guide.svg`, buscador instantáneo FTS5 y localizador de botiquín).
  * `7 Comms` (`/comms` — `15_Mission_Control.svg`, cola diferida *store-and-forward* hacia Tierra y clima solar).
* **Header Superior Exclusivo (`TopTelemetryBar.vue`):**
  * Reloj `MISSION CLOCK`, estado global de cabina y campana de **`Notifications (N)`** (`/notifications` — `16_Notifications_Header.svg`, nunca en el dock inferior).

---

## 3. Estado de Tareas de la Herramienta Interna (`miWork/`)

De acuerdo con la revisión de `MyWork comentarios.md`, quedan registrados en [`instrucciones_ia/DIRECTIVAS_AGENTE_AI.md`](../instrucciones_ia/DIRECTIVAS_AGENTE_AI.md) los siguientes ajustes puntuales para cuando se trabaje sobre `miWork/`:
- [ ] Evitar que al marcar una tarea en el checklist y dar clic en "Listo" la vista se desplace automáticamente hasta arriba (`scrollTop`).
- [ ] Cambiar el título principal de la interfaz de `miWork/` de **`Scan Space`** a **`Scan Workspace`**.

---

## 4. Control de Avance de Implementación (`wakax-nasa-challenge-2026/`)

| Fase / Bloque | Alcance Implementado | Estado | Verificación Registrada |
| :--- | :--- | :---: | :--- |
| **Base Repo (`LICENSE`, `.gitignore`)** | Licencia `MIT` (`e6caef9`) y `.gitignore` (`2dfbcc6`), manteniendo `README.md` vacío por directriz del equipo. | **Completado** | Auditoría normativa sin menciones a `NASA` / `China`. |
| **Fase 0 — `backend/db/schema.sql`** | `17` tablas `STRICT`, modo `WAL`, `foreign_keys = ON`, triggers *append-only* en `measurements` y tabla virtual `wiki_articles_fts` (`FTS5`) con triggers de sincronización (`2dfbcc6`). | **Completado** | Ejecución idempotente en `sqlite3` 3.54.0; `UPDATE`/`DELETE` bloqueados en `measurements`; búsqueda `FTS5` verificada. |
| **Fase 1 (`D1-01` + Contratos Día 1)** | `backend/app/` (`FastAPI`, `APScheduler`, `/api/v1/health`, `/api/v1/mission`, `SSE /api/v1/stream/telemetry`), `contracts.py` (`evaluate_alerts`, `is_within_quiet_hours`, `update_streaks`), `seed.py` y snapshot `mission_baseline.json` (`fdd5536`, `cf93d91`). | **Base lista** | `seed.py` idempotente (`4` tripulantes, `18` métricas, `136` mediciones, `4` artículos, `1` alerta); `TestClient` `200 OK` en `/health` y `/mission`. *(Pendiente instalar `pytest` y `ruff` en `.venv`).* |
| **Fase 1 (`D1-02` — Shell Nuxt 4)** | `tokens.css` (6 colores + `data-cabin-mode="critical"`), tema ECharts `'spacescan-hud'`, `16` SVGs locales `spacescan`, `HudWindow`, `TopTelemetryBar`, `PublicHierarchyBar`, `BottomCockpitDock` (Slot 4 `Profile`), `i18n` (`en`) y esqueletos de las `16` rutas Figma (`fdd5536`, `cf93d91`). | **Base lista** | `eslint .` (`0` errores) y `vitest run` (`3/3` pasando en `compliance.test.ts`). *(Pendiente `npm run generate` y fuentes `.woff2` locales).* |
| **Siguientes Módulos (Fase 1)** | `D1-03` (Login PIN `Argon2id` + `JWT`), `D2-01` (`POST /api/v1/measurements`), `D2-02` (`/capture/physical`, `/capture/vision`), `D3-01` (endpoints alertas + *Quiet Hours*), `D3-03` (`/capture/psych-sleep`, `/profile/psychological`). | **Pendiente** | En cola para ejecución paralela. |

---

## 5. Registro Cronológico de Decisiones (Bitácora)

| Fecha | Hito / Decisión | Descripción Técnica | Responsable |
| :--- | :--- | :--- | :--- |
| **2026-11-14** | **Consolidación de Especificación, Reglas, Stack y División de Trabajo** | Integración prioritaria de los documentos validados (`reglas inquebrantables.md`, `Especifcacion.md`, `requerimientos tecnicos.md`, `divicion del trabajo.md` y `MyWork comentarios.md`). | Equipo / IA |
| **2026-11-14** | **Renombrado a `docs/` e Integración del Estándar de Diseño UI/UX** | Actualización de rutas del repositorio documental a `docs/` (`willor16/docs`) e incorporación de [`REGLAS_DISENO_UI_UX.md`](./REGLAS_DISENO_UI_UX.md) con las 5 Leyes de Diseño, Paleta Oficial de 6 Colores (`tokens.css`), mapeo de las 16 pantallas Figma y plantillas de construcción. | Equipo / IA |
| **2026-11-14** | **Cierre de Fase 0 y Arranque de Fase 1 (`D1-01`, `D1-02`)** | Incorporación de `LICENSE` (MIT), `.gitignore`, esquema `backend/db/schema.sql`, backend base `FastAPI` + `seed.py` + contratos `evaluate_alerts`/`update_streaks` y shell Nuxt 4 SPA en `chore/foundation-and-schema` (`e6caef9`..`cf93d91`), validado con `eslint`, `vitest` (`3/3`) y `TestClient`. | Equipo / IA |
