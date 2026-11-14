# Bitácora de Avance y Resumen Maestro del Proyecto — SpaceScan

> **ESTADO ACTUAL:** Especificación de requerimientos, reglas inquebrantables, estándar global de diseño UI/UX (`Scan Space · ARES VII`), stack técnico y división de trabajo en paralelo (Fase 0 y Fase 1) cerrados y consolidados en `docs/`.  
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

## 4. Registro Cronológico de Decisiones (Bitácora)

| Fecha | Hito / Decisión | Descripción Técnica | Responsable |
| :--- | :--- | :--- | :--- |
| **2026-11-14** | **Consolidación de Especificación, Reglas, Stack y División de Trabajo** | Integración prioritaria de los documentos validados (`reglas inquebrantables.md`, `Especifcacion.md`, `requerimientos tecnicos.md`, `divicion del trabajo.md` y `MyWork comentarios.md`). | Equipo / IA |
| **2026-11-14** | **Renombrado a `docs/` e Integración del Estándar de Diseño UI/UX** | Actualización de rutas del repositorio documental a `docs/` (`willor16/docs`) e incorporación de [`REGLAS_DISENO_UI_UX.md`](./REGLAS_DISENO_UI_UX.md) con las 5 Leyes de Diseño, Paleta Oficial de 6 Colores (`tokens.css`), mapeo de las 16 pantallas Figma y plantillas de construcción. | Equipo / IA |
