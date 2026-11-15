# 👩‍🚀 División del Trabajo y Plan de Desarrollo en Paralelo (3 Devs Fullstack)

## 1. Contexto Operativo

**SpaceScan** utiliza **Nuxt 4 + Python 3.13 (FastAPI) + SQLite 3 STRICT**.

* **3 Desarrolladores Fullstack:** Cada desarrollador es dueño de módulos completos de punta a punta: **sus tablas en SQLite + sus endpoints en FastAPI + sus pantallas en Nuxt**.
* **Idioma Estrictamente 100% en Inglés (UI y Código):** Ni una sola palabra en español dentro del software entregable, **incluyendo el código fuente** (rutas, variables, funciones, endpoints, tablas y comentarios), y cero jerga técnica interna en pantalla (`SQLite`, `JSON`, `Offline`, `DTN`, etc.), conforme a [`REGLAS_INQUEBRANTABLES.md`](./REGLAS_INQUEBRANTABLES.md) y [`REGLAS_DISENO_UI_UX.md`](./REGLAS_DISENO_UI_UX.md).
* **Prohibición de "NASA" y "China":** Prohibido incluir el nombre, logos o menciones de ningún tipo a **NASA** o a **China** dentro del producto/interfaz.
* **Referencia Visual y de Construcción Obligatoria:** Todo desarrollador debe seguir las 16 pantallas del [Figma de SpaceScan (`node-id=7382-2`)](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2) y las plantillas de [`REGLAS_DISENO_UI_UX.md`](./REGLAS_DISENO_UI_UX.md).

### Secuencia de Ejecución
1. **Fase 0 — Base de datos (`backend/db/schema.sql`)**: Revisada y cerrada por los 3 desarrolladores juntos al inicio.
2. **Fase 1 — Desarrollo en paralelo**: Ejecución simultánea de los bloques `D1-xx`, `D2-xx` y `D3-xx`.

---

## 2. Fase 0 — Contrato de Base de Datos (Los 3 Devs Juntos, ~2–3 h)

* **Archivo fuente:** `backend/db/schema.sql` (`PRAGMA journal_mode = WAL; PRAGMA foreign_keys = ON;`, tablas `STRICT`).
* **Comando de inicialización:** `sqlite3 scan.db < backend/db/schema.sql`
* **Propósito:** Definir desde el día 1 todas las tablas de todos los módulos para que ningún desarrollador dependa de otro ni existan conflictos de esquema.
* **Entregable de Fase 0:** Revisar el esquema juntos, ajustar detalles pendientes y fusionar un único PR a `main`.

### Decisión Arquitectónica Clave: Tabla Genérica de Mediciones (`measurements`)
Todo dato numérico (signos vitales, peso, hábitos, laboratorio, parámetros oculares, $\text{VO}_2\text{ máx}$, etc.) se almacena en **`measurements`** (una fila por medición):
* Campos clave: `crew_id` + `metric_key` + `value_num` + `recorded_at_utc` + `mission_stage` (`LAUNCH` / `MISSION` / `RETURN`) + `payload_json`.
* Los rangos clínicos nominales/críticos y la referencia científica de cada métrica residen en **`metric_catalog`**.
* **Escalabilidad sin fricción:** Para añadir una métrica nueva se inserta una fila en `metric_catalog`, nunca una columna nueva.
* **Inmutabilidad (RNF 5):** `measurements` es **append-only** mediante triggers SQL (`trg_measurements_no_update`, `trg_measurements_no_delete`) que bloquean cualquier `UPDATE` o `DELETE`.

### Mapa de Tablas y Responsables

| Tabla | Contenido Principal | Dueño |
| :--- | :--- | :--- |
| `mission` | Nombre de la misión, fecha de despegue, regreso y latencia con la Tierra | **Dev 1** |
| `crew` / `crew_members` | Tripulantes: código (`ID·01`), rol, datos demográficos, PIN cifrado (Argon2id) y bloqueo | **Dev 1** |
| `metric_catalog` | Catálogo de métricas con unidad, rango clínico y referencia científica | **Dev 1** *(cada dev agrega sus filas)* |
| `baselines` | Línea base pre-misión por tripulante y métrica (media y desviación estándar) | **Dev 1** |
| `measurements` | Todas las mediciones numéricas con trazabilidad completa (*append-only*) | **Dev 1** |
| `environment_readings` | $\text{CO}_2$, ruido, temperatura, humedad y radiación de cabina | **Dev 1** |
| `streak_days` | Cumplimiento diario de hábitos y registros (base para cálculo de rachas) | **Dev 1** |
| `sync_packets` / `ground_outbox` | Paquetes médicos enviados a Control a tierra y directrices recibidas | **Dev 1** |
| `sleep_sessions` + `sleep_stages` | Sesiones nocturnas de sueño y desglose por fases (`DEEP`, `REM`, `LIGHT`, `AWAKE`) | **Dev 2** |
| `auscultation_samples` / `auscultation_recordings` | Metadatos, ruta relativa en disco, hash SHA-256 y hallazgos de grabaciones de corazón/pulmón | **Dev 2** |
| `psych_tests` | Evaluaciones de ánimo, estrés, soledad y motivación (escala 1–5) | **Dev 3** |
| `cognitive_tests` | Resultados de tiempo de reacción (ms), precisión y atención | **Dev 3** |
| `scheduled_checks` | Agenda de chequeos periódicos programados | **Dev 3** |
| `alerts` | Avisos clínicos de salud y recordatorios con soporte de *Quiet Hours* | **Dev 3** |
| `diagnoses` | Detecciones de la Red Neuronal (ONNX) y explicaciones del LLM con validación del `Médico` | **Dev 3** |
| `wiki_entries` / `wiki_articles` (+ `fts5`) | Protocolos clínicos buscables offline (FTS5) y casos incorporados a la guía médica | **Dev 3** |

### Reglas de Convivencia en el Código (100% Inglés)
* **Propiedad de tablas:** Solo el dueño modifica el DDL de sus tablas (mediante PR pequeño a `main` avisando al equipo); cualquier desarrollador puede hacer `SELECT` sobre cualquier tabla.
* **Backend:** Un router por módulo en `backend/app/routers/<module>.py` (nombres de archivos, endpoints y funciones 100% en inglés).
* **Frontend:** Rutas y composables en inglés (`useSleep`, `useAuscultationRecorder`, `useWiki`, etc.) siguiendo la estructura de las 16 pantallas de [`REGLAS_DISENO_UI_UX.md`](./REGLAS_DISENO_UI_UX.md).
* **Estilo visual base (`frontend/app/assets/css/tokens.css`, `<HudWindow>`, `<TopTelemetryBar>`, `<BottomCockpitDock>`):** Dueño **Dev 1**.
* **Flujo de ramas:** `feat/D1-01-backend-seed`, `feat/D2-04-sleep-monitor`… Un PR por tarea terminada revisado contra el checklist de los 10 premios y el *Definition of Done* de diseño.

---

## 3. Fase 1 — Desglose de Tareas en Paralelo (Mapeadas a las 16 Pantallas Figma)

### 👤 Dev 1 — Acceso, Tripulación, Shell Visual y Conexión con la Tierra
> **Pantallas Figma a cargo:** `01_Sign_In.svg` (`/login`), `02_Crew_Overview.svg` (`/crew-overview`), `03_Crew_Streaks.svg` (`/crew-streaks`), `15_Mission_Control.svg` (`/comms`) + Shell Global (`tokens.css`, `HudWindow.vue`, `TopTelemetryBar.vue`, `BottomCockpitDock.vue`).

* **`D1-01` · Arranque del backend y carga de datos iniciales (`seed.py`)**
  * **Qué es:** Proyecto FastAPI en `backend/app/`, conexión SQLite parametrizada, stream `SSE` (`/api/v1/stream/telemetry`), montaje estático del SPA en un solo puerto y script `seed.py` con snapshots locales de ciencia espacial abierta y 4 tripulantes de prueba.
  * **Tablas:** Todas las de Dev 1 · **Depende de:** Fase 0 · **Prioridad Día 1.**
* **`D1-02` · Tokens de 6 Colores y Shell de Navegación en 2 Niveles (RNF 4)**
  * **Qué es:** Implementar `tokens.css` (6 colores oficiales + modo alerta `data-cabin-mode="critical"`), `<HudWindow>`, `<TopTelemetryBar>` (con campana de `Notifications` en el header), barra pública de 3 pestañas y `<BottomCockpitDock>` trapezoidal simétrico de 7 módulos con **`Profile` elevado al centro**.
  * **Depende de:** Nada.
* **`D1-03` · Sign In con Perfil + PIN de 4 dígitos (§3.1, RNF 3) — Back + Front (`01_Sign_In.svg` · `/login`)**
  * **Qué es:** `GET /api/v1/crew/profiles` y `POST /api/v1/auth/login` (PIN de 4 dígitos con Argon2id + JWT), más `/login` con selector de tripulante, `PinPad4Digits` y accesos públicos.
  * **Tablas:** `crew` · **Depende de:** `D1-01` · **Sustituto temporal:** `useSession` simulado.
* **`D1-04` · Gestión de usuarios y cálculo de línea base (§3.1) — Back + Front**
  * **Qué es:** Alta, edición y desactivación de tripulantes (`Operador` local y `Control a tierra` remoto); cálculo de `baselines` a partir de las mediciones de la etapa `LAUNCH` (`utils/status.ts`).
  * **Tablas:** `crew`, `baselines` · **Depende de:** `D1-01`.
* **`D1-05` · Crew Overview (§3.2) — Back + Front (`02_Crew_Overview.svg` · `/crew-overview`)**
  * **Qué es:** `GET /api/v1/crew-overview` y vista **100% de solo lectura** con 4 tarjetas de tripulantes, `ECharts` Gauge `84/100` y ambiente de cabina.
  * **Tablas:** `measurements`, `baselines`, `environment_readings` · **Depende de:** `D1-01`.
* **`D1-06` · Crew Streaks (§3.2) — Back + Front (`03_Crew_Streaks.svg` · `/crew-streaks`)**
  * **Qué es:** Función `update_streaks(crew_id, date_utc)`, `GET /api/v1/crew-streaks` y vista **100% de solo lectura** con rachas individuales, grupal, mejor marca y últimos 7 días.
  * **Tablas:** `streak_days`, `measurements` · **Depende de:** `D1-01`. *(Publicar firma de `update_streaks` el Día 1 para `D2-01`).*
* **`D1-07` · Mission Control Comms (§3.12, RNF 1) — Back + Front (`15_Mission_Control.svg` · `/comms`)**
  * **Qué es:** Cola *store-and-forward* con `APScheduler` que empaqueta el resumen diario, simula la latencia de transmisión (`+12 min`), registra estado de entrega y recibe directrices del *Flight Surgeon*.
  * **Tablas:** `sync_packets` / `ground_outbox` · **Depende de:** `D1-01`.

---

### 👤 Dev 2 — Captura Multimodal y Salud Física/Clínica del Tripulante
> **Pantallas Figma a cargo:** Vistas de **Solo Resultados**: `04_Profile_Personal_Data.svg` (`/profile/personal`), `06_Profile_Physical.svg` (`/profile/physical`), `07_Sleep_Monitor.svg` (`/sleep`), `08_Vision_Exam.svg` (`/vision`), `09_Auscultation_Results.svg` (`/auscultation`) + Vistas de **Captura (`Capture`)**: `10_Capture_Auscultation.svg` (`/capture/auscultation`), `11_Capture_Physical_Labs.svg` (`/capture/physical`), `12_Capture_Vision_Ocular.svg` (`/capture/vision`).

* **`D2-01` · Ingesta centralizada de mediciones (§3.4) — Back**
  * **Qué es:** `POST /api/v1/measurements` valida la métrica contra `metric_catalog`, inserta el registro *append-only* (`LAUNCH` / `MISSION` / `RETURN`) y dispara `evaluate_alerts()` (Dev 3) y `update_streaks()` (Dev 1).
  * **Tablas:** `measurements`, `metric_catalog` · **Depende de:** Fase 0 · **Sustituto temporal:** Stubs vacíos con la firma acordada.
* **`D2-02` · Módulo `Capture`: Sub-pestañas de Captura Física y Ocular (§3.4) — Front (`11` y `12`)**
  * **Qué es:** `CaptureSubnavBar.vue` con `Reka UI` y formularios validados con `Zod` en `/capture/physical` (signos vitales, hábitos, laboratorio) y `/capture/vision` (parámetros oculares bilaterales + guía axial `3.0 mm`).
  * **Depende de:** `D2-01`.
* **`D2-03` · Perfil del Tripulante: Datos Personales y Estado Físico (§3.3) — Back + Front (`04` y `06`)**
  * **Qué es:** `GET /api/v1/crew/{id}/profile` y vistas **100% de solo lectura** en `/profile/personal` (con `SpaceScanHologram.vue`) y `/profile/physical` (6 barras clínicas + onda `ECG` ECharts en vivo con `CanvasRenderer` y `sampling: 'lttb'` + 4 resultados de laboratorio), comparando *Launch / Mission / Return* contra la línea base.
  * **Tablas:** `crew`, `measurements`, `baselines` · **Depende de:** Fase 0.
* **`D2-04` · Sleep Monitor (§3.5) — Back + Front (`07_Sleep_Monitor.svg` · `/sleep`)**
  * **Qué es:** Vista **100% de solo lectura** con `SleepTimeFilterBar` (*Last Night, 7D, 14D, 30D*), arco `Sleep Score`, **gráfica de barra de cintas de fases en ECharts (`type: 'custom'`)** y tabla de intervalos `UTC`.
  * **Tablas:** `sleep_sessions`, `sleep_stages` · **Depende de:** Fase 0.
* **`D2-05` · Vision Exam (§3.7) — Back + Front (`08_Vision_Exam.svg` · `/vision`)**
  * **Qué es:** Vista **100% de solo lectura** con arcos comparativos de ojo izquierdo y derecho, curva bilateral de vaina del nervio óptico (`ONSD`) frente a umbral y 3 pasos preventivos.
  * **Tablas:** `measurements` · **Depende de:** `D2-01`.
* **`D2-06` · Auscultación: Captura de 30 s (`10`) y Vista de Resultados (`09`) (§3.4, §3.8) — Back + Front**
  * **Qué es:** En `/capture/auscultation` (`10`): composable `useAuscultationRecorder.ts` (medidor de ruido `< 55 dBA`, grabación cruda de `30 s` por foco anatómico y hash `SHA-256`). En `/auscultation` (`09`, **Solo Resultados**): fonocardiograma `S1/S2`, envolvente pulmonar y tendencia de $\text{CO}_2$ de 24 h.
  * **Tablas:** `auscultation_recordings`, `measurements` · **Depende de:** Fase 0.

---

### 👤 Dev 3 — Mente, Inteligencia Artificial, Wiki y Notificaciones en Header
> **Pantallas Figma a cargo:** `05_Profile_Psychological.svg` (`/profile/psychological`), `13_Capture_Psych_Sleep.svg` (`/capture/psych-sleep`), `14_Medical_Guide.svg` (`/guide`), `16_Notifications_Header.svg` (`/notifications`).

* **`D3-01` · Motor de alertas y Quiet Hours (§3.11) — Back**
  * **Qué es:** Función `evaluate_alerts(measurement_id)` que contrasta cada nueva medición contra `metric_catalog` y `baselines`, generando alertas y difiriendo avisos no urgentes durante el horario de sueño (*Quiet Hours* `22:00–06:00 UTC`).
  * **Tablas:** `alerts`, `measurements`, `metric_catalog` · **Depende de:** Fase 0. *(Publicar firma el Día 1 para `D2-01`).*
* **`D3-02` · Notifications Header View (§3.11) — Back + Front (`16_Notifications_Header.svg` · `/notifications`)**
  * **Qué es:** `GET /api/v1/alerts` y pantalla abierta **exclusivamente desde la campana del header superior**, con filtros, confirmación de lectura, plan preventivo de 3 pasos y enlace directo al protocolo en `/guide`.
  * **Tablas:** `alerts`, `scheduled_checks` · **Depende de:** `D3-01`.
* **`D3-03` · Perfil Psicológico (`05`) y Captura Psicológica/Sueño/Motriz (`13`) (§3.3, §3.6) — Back + Front**
  * **Qué es:** En `/capture/psych-sleep` (`13`): escalas `1–5` (ánimo, estrés, soledad, motivación), ventana `UTC` de sueño y arena interactiva de reacción de `2 min` (`cognitive_tests`). En `/profile/psychological` (`05`, **Solo Resultados**): curva ECharts de 14 días (`Mood`/`Calmness`) y métricas de tiempo de reacción (`ms`) y precisión.
  * **Tablas:** `psych_tests`, `cognitive_tests`, `sleep_sessions` · **Depende de:** Fase 0.
* **`D3-04` · Red Neuronal de detección de anomalías en ONNX Runtime (§3.9) — Back**
  * **Qué es:** Inferencia ligera en CPU con `onnxruntime` (`backend/models/*.onnx`) entrenada con series simuladas y datos abiertos espaciales para detectar desviaciones multivariadas frente a la línea base; `POST /api/v1/diagnosis/anomalies` persiste el hallazgo.
  * **Tablas:** `diagnoses` (lee `measurements`) · **Depende de:** Fase 0.
* **`D3-05` · LLM local sin internet (`Ollama`) y validación del Médico (§3.9, RNF 1) — Back + Front**
  * **Qué es:** Modelo de lenguaje local (`Ollama` con *fallback* determinista instantáneo) que genera orientación preventiva de 3 pasos en inglés claro citando artículos de la guía médica, sujeta a validación del `Médico`.
  * **Tablas:** `diagnoses` · **Depende de:** `D3-04`.
* **`D3-06` · Medical Guide / Wiki con Búsqueda Instantánea FTS5 (§3.10) — Back + Front (`14_Medical_Guide.svg` · `/guide`)**
  * **Qué es:** Buscador local instantáneo (`wiki_articles_fts` con SQLite FTS5) por síntoma o categoría ($\text{CO}_2$, visión, sueño/fatiga, trauma, medicación) con pasos secuenciales, criterios de escalamiento al `Médico` y localizador de cajón del botiquín (`DRAWER B2`); convierte diagnósticos validados en casos de la guía.
  * **Tablas:** `wiki_articles`, `wiki_articles_fts` · **Depende de:** Fase 0.

---

## 4. Cronograma de Ejecución y Gestión de Dependencias

### Calendario por Bloques
| Bloque | Dev 1 (Acceso, Shell y Tierra) | Dev 2 (Captura y Clínica) | Dev 3 (Mente, IA, Guía y Header) |
| :--- | :--- | :--- | :--- |
| **Día 1** | **Fase 0 (`schema.sql` los 3 juntos)** | **Fase 0 (`schema.sql` los 3 juntos)** | **Fase 0 (`schema.sql` los 3 juntos)** |
| **Semana 1** | `D1-01` Backend + Seed, `D1-02` Tokens/Shell | `D2-01` Ingesta API, `D2-02` Capture (`11`, `12`) | `D3-01` Motor Alertas, `D3-03` Psych/Capture (`13`, `05`) |
| **Semana 2** | `D1-03` Sign In (`01`), `D1-04` Usuarios/Base | `D2-03` Profile (`04`, `06`), `D2-04` Sleep (`07`) | `D3-02` Notifications (`16`), `D3-06` Medical Guide (`14`) |
| **Semana 3** | `D1-05` Overview (`02`), `D1-06` Streaks (`03`) | `D2-05` Vision (`08`) | `D3-04` Red Neuronal ONNX |
| **Semana 4** | `D1-07` Comms (`15`) + Integración | `D2-06` Auscultation (`10`, `09`) + Integración | `D3-05` LLM Local + Integración |

### Matriz de Dependencias Cruzadas y Sustitutos (Cero Bloqueos)
| Módulo que Necesita | Interfaz / Recurso | Responsable | Sustituto Temporal (Mock / Stub) |
| :--- | :--- | :--- | :--- |
| `D2-01` Ingesta | `evaluate_alerts(measurement_id)` | Dev 3 (`D3-01`) | Función stub vacía con la firma definitiva acordada el Día 1 |
| `D2-01` Ingesta | `update_streaks(crew_id, date_utc)` | Dev 1 (`D1-06`) | Función stub vacía con la firma definitiva acordada el Día 1 |
| Pantallas privadas | Sesión autenticada con PIN | Dev 1 (`D1-03`) | Composable `useSession` simulado existente |
| `D2-03` Profile / `D3-01` Alertas | Línea base (`baselines`) | Dev 1 (`D1-04`) | Cálculo dinámico al vuelo mediante `utils/status.ts` |
| Routers de Dev 2 y Dev 3 | Instancia base de FastAPI | Dev 1 (`D1-01`) | `main.py` mínimo local hasta el merge de `D1-01` |

---

## 5. Protocolo de Verificación (*Definition of Done*)

1. **Integridad del Esquema:** `sqlite3 scan.db < backend/db/schema.sql` debe ejecutarse sin errores ni advertencias.
2. **Fidelidad Visual contra Figma y 6 Colores:** Verificar proporciones (`1568 × 940`), uso exclusivo de variables de `tokens.css`, dock de 7 módulos con `Profile` al centro, `Notifications` solo en header y separación estricta entre vistas de **Solo Resultados** y **`Capture`**.
3. **Prueba en Modo Avión (`RNF 1`):** `0` peticiones a dominios externos con Wi-Fi apagado.
4. **Auditoría de Idioma, Código y Prohibiciones:** `100%` en inglés tanto en la UI como en el código fuente; `0` menciones a `NASA` o `China`; `0` jerga técnica interna (`SQLite`, `JSON`, `FHIR`, `Offline`, etc.) en pantalla.
5. **Calidad y Pruebas:** `uv run ruff check .`, `uv run pytest`, `npx openapi-typescript`, `pnpm lint` y `pnpm test` con `0` errores.
