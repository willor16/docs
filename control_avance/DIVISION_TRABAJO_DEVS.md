# 👩‍🚀 División del Trabajo y Plan de Desarrollo en Paralelo (3 Devs Fullstack)

## 1. Contexto Operativo

**SpaceScan** utiliza **Nuxt 4 + Python (FastAPI) + SQLite 3**. Ya existe una base de frontend en `frontend/` con login, panel, perfil, rachas y notificaciones leyendo datos simulados desde `frontend/public/data/*.json`.

* **3 Desarrolladores Fullstack:** Cada desarrollador es dueño de módulos completos de punta a punta: **sus tablas en SQLite + sus endpoints en FastAPI + sus pantallas en Nuxt**.
* **Idioma de la Interfaz y Datos:** Estrictamente **100% en inglés** (sin textos en español dentro de la app, conforme a [`REGLAS_INQUEBRANTABLES.md`](./REGLAS_INQUEBRANTABLES.md)).
* **Referencia Visual Obligatoria:** Cada desarrollador toma del [Figma de SpaceScan](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2) las pantallas correspondientes a sus tareas.

### Secuencia de Ejecución
1. **Fase 0 — Base de datos (`backend/db/schema.sql`)**: Revisada y cerrada por los 3 desarrolladores juntos al inicio.
2. **Fase 1 — Desarrollo en paralelo**: Ejecución simultánea de los bloques `D1-xx`, `D2-xx` y `D3-xx`.

---

## 2. Fase 0 — Contrato de Base de Datos (Los 3 Devs Juntos, ~2–3 h)

* **Archivo fuente:** `backend/db/schema.sql`.
* **Comando de inicialización:** `sqlite3 scan.db < backend/db/schema.sql`
* **Propósito:** Definir desde el día 1 todas las tablas de todos los módulos para que ningún desarrollador dependa de otro ni existan conflictos de esquema.
* **Entregable de Fase 0:** Revisar el esquema juntos, ajustar detalles pendientes y fusionar un único PR a `main`.

### Decisión Arquitectónica Clave: Tabla Genérica de Mediciones (`measurements`)
Todo dato numérico (signos vitales, peso, hábitos, laboratorio, parámetros oculares, $\text{VO}_2\text{ máx}$, etc.) se almacena en **`measurements`** (una fila por medición):
* Campos clave: `crew_id` + `metric` + `value` + `ts_utc` + `stage` (`takeoff` / `mission` / `return`) + `source` (`manual` / `auto`) + `side` opcional (`L` / `R` para visión).
* Los rangos clínicos nominales/críticos y la fuente científica de cada métrica residen en **`metric_catalog`**.
* **Escalabilidad sin fricción:** Para añadir una métrica nueva se inserta una fila en `metric_catalog`, nunca una columna nueva.
* **Inmutabilidad (RNF 5):** `measurements` es **append-only** mediante triggers SQL que bloquean cualquier `UPDATE` o `DELETE`.

### Mapa de las 16 Tablas y Responsables

| Tabla | Contenido Principal | Dueño |
| :--- | :--- | :--- |
| `mission` | Nombre de la misión, fecha de despegue, regreso y latencia con la Tierra | **Dev 1** |
| `crew` | Tripulantes: rol, datos demográficos, PIN cifrado y estado activo | **Dev 1** |
| `metric_catalog` | Catálogo de métricas con unidad, rango clínico y fuente científica citada | **Dev 1** *(cada dev agrega sus filas)* |
| `baselines` | Línea base pre-misión por tripulante y métrica (media y desviación estándar) | **Dev 1** |
| `measurements` | Todas las mediciones numéricas con trazabilidad completa (*append-only*) | **Dev 1** |
| `environment_readings` | $\text{CO}_2$, ruido, temperatura, humedad y radiación de cabina | **Dev 1** |
| `streak_days` | Cumplimiento diario de hábitos y registros (base para cálculo de rachas) | **Dev 1** |
| `sync_packets` | Paquetes médicos enviados a Control a tierra y directrices recibidas | **Dev 1** |
| `sleep_sessions` + `sleep_stages` | Sesiones nocturnas de sueño y desglose por fases (Deep, REM, Light, Awake) | **Dev 2** |
| `auscultation_samples` | Metadatos, ruta en disco, hash SHA-256 y hallazgos de grabaciones de corazón/pulmón | **Dev 2** |
| `psych_tests` | Evaluaciones de ánimo, estrés, soledad y motivación (escala 1–5) | **Dev 3** |
| `cognitive_tests` | Resultados de tiempo de reacción (ms), precisión y atención | **Dev 3** |
| `scheduled_checks` | Agenda de chequeos periódicos programados | **Dev 3** |
| `alerts` | Avisos clínicos de salud y recordatorios con soporte de *Quiet Hours* | **Dev 3** |
| `diagnoses` | Detecciones de la Red Neuronal y explicaciones del LLM con estado de validación del `Médico` | **Dev 3** |
| `wiki_entries` | Protocolos clínicos buscables (FTS5) y casos incorporados a la guía médica | **Dev 3** |

### Reglas de Convivencia en el Código
* **Propiedad de tablas:** Solo el dueño modifica el DDL de sus tablas (mediante PR pequeño a `main` avisando al equipo); cualquier desarrollador puede hacer `SELECT` sobre cualquier tabla.
* **Backend:** Un router por módulo en `backend/app/routers/<modulo>.py`.
* **Frontend:** Páginas propias por módulo y un composable dedicado (`useSleep`, `useWiki`, etc.), manteniendo todos los textos de UI estrictamente en inglés.
* **Estilo visual base (`assets/css/tokens.css` y componentes base):** Dueño **Dev 1**.
* **Flujo de ramas:** `feat/D1-01-backend-seed`, `feat/D2-04-sleep`… Un PR por tarea terminada (tabla + API + pantalla) revisado por el validador con el checklist de los 10 premios de [`REGLAS_INQUEBRANTABLES.md`](./REGLAS_INQUEBRANTABLES.md).

---

## 3. Fase 1 — Desglose de Tareas en Paralelo

### 👤 Dev 1 — Acceso, Tripulación y Conexión con la Tierra
> **Alcance:** Infraestructura base del backend, semillas de datos espaciales, autenticación por PIN, vistas grupales (panel general y rachas) y cola asíncrona con Control a tierra.

* **`D1-01` · Arranque del backend y carga de datos iniciales (`seed.py`)**
  * **Qué es:** Proyecto FastAPI en `backend/app/`, conexión a SQLite y script `seed.py` que inicializa la base con datos simulados, 4 tripulantes de prueba y datasets reales de OSDR/GeneLab y DONKI.
  * **Tablas:** Todas las de Dev 1 · **Depende de:** Fase 0 · **Prioridad Día 1.**
* **`D1-02` · Estilo visual base (RNF 4)**
  * **Qué es:** Ajuste de colores, tipografías locales y componentes base al Figma con alto contraste.
  * **Depende de:** Nada.
* **`D1-03` · Login con perfil + PIN de 4 dígitos (§3.1, RNF 3) — Back + Front**
  * **Qué es:** `GET /crew/perfiles` (con indicador de estado) y `POST /auth/login` (PIN de 4 dígitos con Argon2 + JWT), más `pages/index.vue` con tarjetas de tripulantes y teclado numérico de PIN.
  * **Tablas:** `crew` · **Depende de:** `D1-01` · **Sustituto temporal:** `useSession` simulado actual.
* **`D1-04` · Gestión de usuarios y cálculo de línea base (§3.1) — Back + Front**
  * **Qué es:** Alta, edición y desactivación de tripulantes (`Operador` local y `Control a tierra` remoto); cálculo de `baselines` a partir de las mediciones de la etapa pre-misión (`utils/status.ts`).
  * **Tablas:** `crew`, `baselines` · **Depende de:** `D1-01`.
* **`D1-05` · Vista general de salud (§3.2) — Back + Front**
  * **Qué es:** `GET /panel` y `pages/panel.vue`: estado global de cada tripulante (*Optimal / Nominal / Attention*), signos clave recientes y variables ambientales de cabina.
  * **Tablas:** `measurements`, `baselines`, `environment_readings` · **Depende de:** `D1-01`.
* **`D1-06` · Rachas de constancia (§3.2) — Back + Front**
  * **Qué es:** Función `update_streaks(crew_id, fecha)` que actualiza `streak_days`, más `GET /rachas` y `pages/rachas.vue` (individual, grupal, mejor marca, últimos 7 días).
  * **Tablas:** `streak_days`, `measurements` · **Depende de:** `D1-01`. *(Publicar firma de `update_streaks` el Día 1 para `D2-01`).*
* **`D1-07` · Comunicación asíncrona con Control a tierra (§3.12, RNF 1) — Back + Front**
  * **Qué es:** Cola *store-and-forward* que empaqueta el resumen diario en JSON, simula el envío con latencia espacial, registra estado de entrega y recibe directrices médicas remotas.
  * **Tablas:** `sync_packets` · **Depende de:** `D1-01`.

---

### 👤 Dev 2 — Salud Física y Clínica del Tripulante
> **Alcance:** Puerta de entrada de todas las mediciones numéricas, formularios ergonómicos de captura, perfil longitudinal por etapa y módulos clínicos de Sueño, Visión (SANS) y Auscultación.

* **`D2-01` · Ingesta centralizada de mediciones (§3.4) — Back**
  * **Qué es:** `POST /measurements` valida la métrica contra `metric_catalog`, inserta el registro *append-only* y dispara `evaluate_alerts()` (Dev 3) y `update_streaks()` (Dev 1).
  * **Tablas:** `measurements`, `metric_catalog` · **Depende de:** Fase 0 · **Sustituto temporal:** Stubs vacíos con la firma acordada para `evaluate_alerts` y `update_streaks`.
* **`D2-02` · Formularios guiados de captura (§3.4) — Front**
  * **Qué es:** Flujos paso a paso validados con Zod para signos vitales, peso, hidratación, calorías, ejercicio, laboratorio y ventana de sueño.
  * **Depende de:** `D2-01`.
* **`D2-03` · Perfil longitudinal del tripulante (§3.3) — Back + Front**
  * **Qué es:** `GET /crew/{id}/perfil` y `pages/perfil/`: biometría y estado físico-clínico comparando *Takeoff / Mission / Return* contra la línea base personal.
  * **Tablas:** `crew`, `measurements`, `baselines` · **Depende de:** Fase 0 · **Sustituto temporal de `D1-04`:** Cálculo de línea base al vuelo con `utils/status.ts`.
* **`D2-04` · Módulo de Sueño (§3.5) — Back + Front**
  * **Qué es:** Registro de sesiones nocturnas y vista con puntaje de calidad, horas frente a meta, eficiencia y fases (*Deep, REM, Light, Awake*) filtrable por última noche, 7, 14 y 30 días.
  * **Tablas:** `sleep_sessions`, `sleep_stages` · **Depende de:** Fase 0.
* **`D2-05` · Módulo de Visión y Salud Ocular SANS (§3.4, §3.7) — Back + Front**
  * **Qué es:** Captura bilateral (`side` `L`/`R`) de diámetro de vaina del nervio óptico, presión intraocular, grosor retiniano y agudeza visual, con gráfica comparativa de tendencia, umbrales y revisión del `Médico`.
  * **Tablas:** `measurements` · **Depende de:** `D2-01`.
* **`D2-06` · Módulo de Auscultación Acústica (§3.4, §3.8) — Back + Front**
  * **Qué es:** Verificación de ruido ambiental con Web Audio API, grabación de 30 s de corazón/pulmón con MediaRecorder, almacenamiento en disco con hash SHA-256 y visualización de hallazgos (ritmo S1/S2, soplos, fonocardiograma, respiración, $\text{VO}_2\text{ máx}$, $\text{CO}_2$ de cabina).
  * **Tablas:** `auscultation_samples`, `measurements` · **Depende de:** Fase 0.

---

### 👤 Dev 3 — Mente, Inteligencia Artificial y Atención Médica
> **Alcance:** Motor de alertas con protección de sueño, salud psicológica y cognitivo-motriz, inferencia local con Red Neuronal + LLM y Wiki médica evolutiva.

* **`D3-01` · Motor de alertas y Quiet Hours (§3.11) — Back**
  * **Qué es:** Función `evaluate_alerts(measurement_id)` que contrasta cada nueva medición contra `metric_catalog` y `baselines`, generando alertas y difiriendo avisos no urgentes durante el horario de descanso (*Quiet Hours*).
  * **Tablas:** `alerts`, `measurements`, `metric_catalog` · **Depende de:** Fase 0. *(Publicar firma el Día 1 para `D2-01`).*
* **`D3-02` · Bandeja de notificaciones y chequeos programados (§3.11) — Back + Front**
  * **Qué es:** `GET /alertas` y `pages/notificaciones.vue` separando *Health Alerts* y *Scheduled Checks*, confirmación de lectura y enlace directo al protocolo en la Wiki.
  * **Tablas:** `alerts`, `scheduled_checks` · **Depende de:** `D3-01`.
* **`D3-03` · Evaluación psicológica (§3.3, §3.6) — Back + Front**
  * **Qué es:** Test periódico de ánimo, estrés, soledad y motivación (1–5) y visualización de tendencia de 14 días frente a la zona óptima individual.
  * **Tablas:** `psych_tests` · **Depende de:** Fase 0.
* **`D3-04` · Prueba interactiva cognitivo-motriz (§3.6) — Back + Front**
  * **Qué es:** Mini-evaluación interactiva que mide tiempo de reacción (latencia en ms), precisión y retención de atención (crítico para el rol `Piloto`).
  * **Tablas:** `cognitive_tests` · **Depende de:** Fase 0.
* **`D3-05` · Red Neuronal de detección de anomalías (§3.9) — Back**
  * **Qué es:** Modelo (Autoencoder o LSTM en ONNX Runtime) entrenado con series simuladas y datos abiertos espaciales que detecta desviaciones multivariadas frente a la línea base; `POST /diagnosis/anomalies` persiste el hallazgo.
  * **Tablas:** `diagnoses` (lee `measurements`) · **Depende de:** Fase 0.
* **`D3-06` · LLM local sin internet y validación del Médico (§3.9, RNF 1) — Back + Front**
  * **Qué es:** Integración de modelo de lenguaje local (`Ollama` / `llama.cpp`) que traduce las anomalías detectadas en una explicación clínica clara y medidas preventivas, marcadas como *Pending Medical Officer Validation*, junto con la interfaz para que el `Médico` apruebe o rechace.
  * **Tablas:** `diagnoses` · **Depende de:** `D3-05`.
* **`D3-07` · Guía médica y Wiki evolutiva de respaldo (§3.10) — Back + Front**
  * **Qué es:** Buscador local instantáneo (SQLite FTS5) por síntoma o categoría ($\text{CO}_2$, visión, sueño/fatiga, trauma, medicación) con pasos secuenciales, criterios de escalamiento al `Médico` e insumos del botiquín; convierte diagnósticos validados en nuevos casos de la Wiki.
  * **Tablas:** `wiki_entries` · **Depende de:** Fase 0.

---

## 4. Cronograma de Ejecución y Gestión de Dependencias

### Calendario por Bloques
| Bloque | Dev 1 (Acceso, Grupo y Tierra) | Dev 2 (Clínica y Captura) | Dev 3 (Mente, IA y Wiki) |
| :--- | :--- | :--- | :--- |
| **Día 1** | **Fase 0 (`schema.sql` los 3 juntos)** | **Fase 0 (`schema.sql` los 3 juntos)** | **Fase 0 (`schema.sql` los 3 juntos)** |
| **Semana 1** | `D1-01` Arranque + Seed, `D1-02` Estilo | `D2-01` Ingesta API, `D2-02` Captura UI | `D3-01` Motor Alertas, `D3-03` Psicológico |
| **Semana 2** | `D1-03` Login PIN, `D1-04` Usuarios/Base | `D2-03` Perfil Etapas, `D2-04` Sueño | `D3-02` Notificaciones, `D3-04` Cognitivo |
| **Semana 3** | `D1-05` Panel General, `D1-06` Rachas | `D2-05` Visión (SANS) | `D3-05` Red Neuronal, `D3-07` Wiki FTS5 |
| **Semana 4** | `D1-07` Cola Tierra + Integración | `D2-06` Auscultación + Integración | `D3-06` LLM Local + Integración |

### Matriz de Dependencias Cruzadas y Sustitutos (Cero Bloqueos)
| Módulo que Necesita | Interfaz / Recurso | Responsable | Sustituto Temporal (Mock / Stub) |
| :--- | :--- | :--- | :--- |
| `D2-01` Ingesta | `evaluate_alerts(measurement_id)` | Dev 3 (`D3-01`) | Función stub vacía con la firma definitiva acordada el Día 1 |
| `D2-01` Ingesta | `update_streaks(crew_id, date)` | Dev 1 (`D1-06`) | Función stub vacía con la firma definitiva acordada el Día 1 |
| Pantallas privadas | Sesión autenticada con PIN | Dev 1 (`D1-03`) | Composable `useSession` simulado existente |
| `D2-03` Perfil / `D3-01` Alertas | Línea base (`baselines`) | Dev 1 (`D1-04`) | Cálculo dinámico al vuelo mediante `utils/status.ts` |
| Routers de Dev 2 y Dev 3 | Instancia base de FastAPI | Dev 1 (`D1-01`) | `main.py` mínimo local hasta el merge de `D1-01` |

---

## 5. Protocolo de Verificación e Integración

1. **Integridad del Esquema:** `sqlite3 scan.db < backend/db/schema.sql` debe ejecutarse sin errores ni advertencias.
2. **Cero Mocks en PR Final:** Cada Pull Request debe operar contra el backend FastAPI y SQLite reales (`uvicorn` + `pytest` para API; `npm run dev` para Nuxt).
3. **Prueba de Flujo E2E:** Verificación completa de la cadena `Login con PIN → Captura de medición → Disparo de alerta → Notificación en bandeja → Consulta de protocolo en Wiki → Empaquetado asíncrono a Tierra`.
4. **Auditoría de los 10 Criterios:** Todo PR debe aprobar el checklist de [`REGLAS_INQUEBRANTABLES.md`](./REGLAS_INQUEBRANTABLES.md) y estar 100% en inglés.
