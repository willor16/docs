# 👩‍🚀 Proceso Devs — Reparto de trabajo en paralelo (3 desarrolladores fullstack)

## Contexto
SpaceScan (NASA Space Apps 2026) usa **Nuxt + Python (FastAPI) + SQLite**. Ya existe un frontend en `frontend/` con login, panel, perfil, rachas y notificaciones leyendo datos simulados de `frontend/public/data/*.json`.

**Los 3 desarrolladores son fullstack.** Cada uno es dueño de módulos completos, de punta a punta: **sus tablas + sus endpoints en Python + sus pantallas en Nuxt**.

**Orden de trabajo:**
1. **Fase 0 — Base de datos** (primero, la revisan los 3 juntos).
2. **Fase 1 — Tareas en paralelo**: cada quien toma sus tareas `D1-xx`, `D2-xx`, `D3-xx`.

> Cada desarrollador toma del [Figma](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2) las pantallas de sus tareas.

---

## Fase 0 — Base de datos (primera tarea, los 3 juntos, ~2–3 h)
**Archivo:** `backend/db/schema.sql` (ya creado). Crear la base: `sqlite3 scan.db < backend/db/schema.sql`

*Qué es:* la estructura completa de la base, con **todas** las tablas de todos los módulos definidas desde el inicio.
*Para qué:* es lo único que los 3 comparten. Con la estructura cerrada, nadie espera a nadie ni choca con otro.

**Tarea de los 3:** leer el archivo juntos, ajustar lo que falte y hacer un solo PR a `main`. Desde ese momento se considera el contrato.

### Decisión clave: una tabla genérica de mediciones
Todo dato numérico (vitales, peso, hábitos, laboratorio, ojos, VO₂…) va a **`measurements`**, una fila por dato:
`crew_id` + `metric` + `value` + `ts_utc` + `stage` (despegue/mision/regreso) + `source` (manual/auto).
Los rangos clínicos y la fuente científica de cada métrica viven en **`metric_catalog`**.

👉 **¿Necesitas una métrica nueva?** Agregas una fila al catálogo, **no** una columna. Así nadie rompe la base de otro.

`measurements` es **append-only**: unos triggers impiden editar o borrar mediciones. Así se garantiza un historial íntegro aunque haya cortes o reinicios (RNF 5).

### Tablas y dueños
| Tabla | Qué guarda | Dueño |
|---|---|---|
| `mission` | nombre de la misión, despegue, regreso y latencia con la Tierra | Dev 1 |
| `crew` | tripulantes: rol, datos demográficos, PIN cifrado, activo | Dev 1 |
| `metric_catalog` | métricas con unidad, rango clínico y fuente científica | Dev 1 (cada dev agrega sus filas) |
| `baselines` | línea base pre-misión por tripulante y métrica (media y desviación) | Dev 1 |
| `measurements` | todas las mediciones numéricas (append-only) | Dev 1 |
| `environment_readings` | CO₂, ruido, temperatura, humedad y radiación de cabina | Dev 1 |
| `streak_days` | cumplimiento diario de hábitos (base para las rachas) | Dev 1 |
| `sync_packets` | paquetes enviados a Control a tierra y recibidos de ahí | Dev 1 |
| `sleep_sessions` + `sleep_stages` | noches de sueño y sus fases | Dev 2 |
| `auscultation_samples` | grabaciones de corazón y pulmón con sus hallazgos | Dev 2 |
| `psych_tests` | test de ánimo, estrés, soledad y motivación | Dev 3 |
| `cognitive_tests` | tiempo de reacción, precisión y atención | Dev 3 |
| `scheduled_checks` | chequeos programados | Dev 3 |
| `alerts` | avisos de salud y recordatorios | Dev 3 |
| `diagnoses` | detecciones de la red neuronal y explicaciones del LLM, con validación del Médico | Dev 3 |
| `wiki_entries` | protocolos y casos de la guía médica | Dev 3 |

### Reglas
- Solo el dueño modifica la estructura de sus tablas. Cualquiera puede **leer** cualquier tabla.
- Los cambios de estructura van en un PR pequeño a `main` y se avisa a los demás.
- Cada dev agrega al catálogo las métricas que usa (algunas fuentes dicen "Por confirmar" y hay que investigarlas).

### Organización del código (para no pisarse)
- Backend: `backend/app/routers/<modulo>.py`, un archivo por módulo.
- Frontend: páginas propias y un composable por módulo (`useSueno`, `useWiki`…).
- Traducciones (`i18n/locales/*.json`): cada quien bajo su prefijo (`dev1.*`, `dev2.*`, `dev3.*`).
- Estilo visual (`assets/css/tokens.css`, `components/` base): dueño Dev 1. Los demás crean componentes nuevos o piden cambios.
- Ramas: `feat/D1-01-login`, `feat/D2-03-sueno`… Un PR por tarea terminada (tabla + API + pantalla). El validador revisa con el checklist de `SCAN_SPACE.md`.

---

## Fase 1 — Tareas en paralelo
Cada tarea indica:
- **Tablas:** las que usa.
- **Depende de:** otras tareas que necesita.
- **Mientras no exista:** el sustituto temporal para no quedarse esperando.

### Dev 1 — Acceso, tripulación y conexión con la Tierra
**En resumen:** la base sobre la que todo funciona (API inicial, usuarios, sesión), las vistas de grupo y la comunicación con la Tierra.

**D1-01 · Arranque del backend y datos iniciales**
*Qué es:* proyecto FastAPI en `backend/app/`, conexión a SQLite y un script `seed.py` que llena la base con los JSON simulados actuales, 4 tripulantes de prueba y datos reales de NASA (OSDR/GeneLab).
*Para qué:* que los 3 tengan desde el día 1 un backend que corre y datos realistas ("Best Use of Data").
*Tablas:* todas las de Dev 1 · *Depende de:* Fase 0 · **Hacer primero:** Dev 2 y Dev 3 crean sus routers sobre este proyecto. Mientras tanto, cada uno puede arrancar con su propio `main.py` mínimo.

**D1-02 · Estilo visual base** (RNF 4)
*Qué es:* ajustar colores, tipografías y componentes base al Figma, con alto contraste.
*Para qué:* que toda la app se vea consistente y se lea bien en cabina.
*Depende de:* nada.

**D1-03 · Login con perfil + PIN** (§3.1, RNF 3) — back + front
*Qué es:* `GET /crew/perfiles` (con color de estado) y `POST /auth/login` (PIN de 4 dígitos cifrado), más la pantalla `pages/index.vue` con las tarjetas de los tripulantes y el teclado del PIN.
*Para qué:* proteger los datos individuales; sin sesión solo se ven el resumen y las rachas.
*Tablas:* `crew` · *Depende de:* D1-01 · *Mientras no exista:* los demás usan la sesión simulada actual (`useSession`).

**D1-04 · Gestión de usuarios y línea base** (§3.1) — back + front
*Qué es:* alta, edición y desactivación de tripulantes con su rol; cálculo de la línea base a partir de las mediciones de la etapa pre-misión (reutilizar la lógica de `utils/status.ts`).
*Para qué:* el Operador (a bordo) y Control a tierra (remoto) administran la tripulación; la línea base es contra lo que se compara todo.
*Tablas:* `crew`, `baselines` · *Depende de:* D1-01.

**D1-05 · Vista general de salud** (§3.2) — back + front
*Qué es:* `GET /panel` y `pages/panel.vue`: estado de cada tripulante (Óptimo / Nominal / Atención), signos clave y ambiente de cabina.
*Para qué:* saber de un vistazo cómo está toda la tripulación.
*Tablas:* `measurements`, `baselines`, `environment_readings` · *Depende de:* D1-01.

**D1-06 · Rachas** (§3.2) — back + front
*Qué es:* la función `update_streaks(crew_id, fecha)` llena `streak_days`, más `GET /rachas` y `pages/rachas.vue` (individual, grupal, mejor marca, últimos 7 días).
*Para qué:* motivar la constancia ("Most Inspirational").
*Tablas:* `streak_days`, `measurements` · *Depende de:* D1-01. **Publicar la firma de `update_streaks` el día 1**, porque D2-01 la llama.

**D1-07 · Comunicación con Control a tierra** (§3.12, RNF 1) — back + front
*Qué es:* cola que arma el resumen diario, lo "envía" cuando hay enlace (simulando la latencia), registra el estado de entrega y recibe directivas médicas; más la pantalla para ver envíos y directivas.
*Para qué:* la nave funciona sin conexión continua; la comunicación es diferida, como en una misión real.
*Tablas:* `sync_packets` · *Depende de:* D1-01.

### Dev 2 — Salud física y clínica del tripulante
**En resumen:** cómo **entran** las mediciones y cómo se **consulta** la salud física de cada persona.

**D2-01 · Ingesta de mediciones** (§3.4) — back
*Qué es:* `POST /measurements` valida que la métrica exista en el catálogo, guarda la medición y luego llama a `evaluate_alerts()` (Dev 3) y `update_streaks()` (Dev 1).
*Para qué:* es la puerta de entrada de todos los datos.
*Tablas:* `measurements`, `metric_catalog` · *Depende de:* Fase 0 · *Mientras no exista:* `evaluate_alerts` y `update_streaks` como funciones vacías con la firma acordada.

**D2-02 · Formularios de captura** (§3.4) — front
*Qué es:* pantallas paso a paso para signos vitales, peso, hidratación, calorías, ejercicio, laboratorio y horario de sueño.
*Para qué:* registrar datos rápido y sin errores, incluso estando cansado.
*Depende de:* D2-01 · *Mientras no exista:* mostrar el JSON que se enviaría.

**D2-03 · Perfil del tripulante** (§3.3) — back + front
*Qué es:* `GET /crew/{id}/perfil` y `pages/perfil/`: datos personales, biometría y estado físico-clínico, comparando Despegue / Misión / Regreso contra la línea base.
*Para qué:* ver cómo cambia el cuerpo de cada persona a lo largo de la misión.
*Tablas:* `crew`, `measurements`, `baselines` · *Depende de:* Fase 0 · *Mientras no exista D1-04:* calcular la línea base al vuelo con `utils/status.ts`.

**D2-04 · Módulo de Sueño** (§3.5) — back + front
*Qué es:* registro de noches y pantalla con puntaje, horas frente a la meta y fases (profundo, REM, ligero, despierto), con filtros de última noche, 7, 14 y 30 días.
*Para qué:* evaluar si el tripulante descansa y se recupera bien.
*Tablas:* `sleep_sessions`, `sleep_stages` · *Depende de:* Fase 0.

**D2-05 · Módulo de Visión** (§3.4, §3.7) — back + front
*Qué es:* captura de ojo izquierdo y derecho (nervio óptico, presión ocular, retina, agudeza) y pantalla comparativa con tendencia, umbrales y estado de revisión del Médico.
*Para qué:* vigilar el síndrome neuro-ocular (SANS), un problema real en astronautas.
*Tablas:* `measurements` (con `side` L/R) · *Depende de:* D2-01.

**D2-06 · Módulo de Auscultación** (§3.4, §3.8) — back + front
*Qué es:* grabar 30 s de corazón o pulmón con el micrófono (verificando antes el ruido ambiente), guardar el audio y mostrar resultados (ritmo, soplos, fonocardiograma, respiración, VO₂ máx, CO₂ de cabina).
*Para qué:* evaluar la salud cardiorrespiratoria, clave para el Operador que sale de la nave.
*Tablas:* `auscultation_samples`, `measurements` · *Depende de:* Fase 0.

### Dev 3 — Mente, inteligencia y atención médica
**En resumen:** la salud psicológica, la IA que interpreta los datos y todo lo que ayuda a **actuar**: alertas y guía médica.

**D3-01 · Motor de alertas** (§3.11) — back
*Qué es:* la función `evaluate_alerts(measurement_id)` compara contra el rango clínico y la línea base (misma lógica que `utils/status.ts`) y crea alertas. Incluye Quiet Hours: los avisos no urgentes se difieren mientras el tripulante duerme.
*Para qué:* avisar temprano sin interrumpir el descanso por cosas menores.
*Tablas:* `alerts`, `measurements`, `metric_catalog` · *Depende de:* Fase 0. **Publicar la firma el día 1**, porque D2-01 la llama.

**D3-02 · Notificaciones y chequeos programados** (§3.11) — back + front
*Qué es:* `GET /alertas` y `pages/notificaciones.vue` con *Avisos de Salud* y *Chequeos Programados*, botón de "leído" y enlace al protocolo de la Wiki.
*Para qué:* que nadie se pierda una alerta y sepa de inmediato qué hacer.
*Tablas:* `alerts`, `scheduled_checks` · *Depende de:* D3-01 · *Mientras no exista:* insertar alertas de prueba.

**D3-03 · Evaluación psicológica** (§3.3, §3.6) — back + front
*Qué es:* test de ánimo, estrés, soledad y motivación (1–5) y pantalla con la tendencia de 14 días frente a la zona óptima de cada persona.
*Para qué:* cuidar la salud mental en aislamiento, uno de los mayores riesgos en misiones largas.
*Tablas:* `psych_tests` · *Depende de:* Fase 0.

**D3-04 · Prueba cognitivo-motriz** (§3.6) — back + front
*Qué es:* mini juego que mide tiempo de reacción (ms), precisión y atención, y guarda el resultado.
*Para qué:* comprobar que el Piloto está mentalmente apto.
*Tablas:* `cognitive_tests` · *Depende de:* Fase 0.

**D3-05 · Red neuronal de anomalías** (§3.9) — back
*Qué es:* modelo (ej. autoencoder o LSTM) entrenado con datos simulados y de NASA que detecta cuando las series de un tripulante se alejan de su línea base; `POST /diagnosis/anomalies` guarda la detección.
*Para qué:* detectar problemas temprano, antes de que crucen un umbral crítico.
*Tablas:* `diagnoses` (lee `measurements`) · *Depende de:* Fase 0 · *Mientras no exista D1-01:* entrenar directamente con los JSON y CSV.

**D3-06 · LLM local sin internet** (§3.9, RNF 1) — back + front
*Qué es:* modelo de lenguaje pequeño en la nave (ej. Ollama o llama.cpp) que explica en lenguaje claro lo detectado y sugiere prevención, marcado como "pendiente de validación del Médico"; más la pantalla donde el Médico valida o rechaza.
*Para qué:* traducir números en explicaciones entendibles sin depender de la Tierra ni reemplazar al Médico.
*Tablas:* `diagnoses` · *Depende de:* D3-05 · *Mientras no exista:* usar diagnósticos de prueba.

**D3-07 · Guía médica / Wiki** (§3.10) — back + front
*Qué es:* protocolos buscables por síntoma o categoría (CO₂, visión, sueño/fatiga, trauma, medicación) con pasos, cuándo llamar al Médico e insumos del botiquín; los diagnósticos ya validados se convierten en casos de la Wiki.
*Para qué:* saber qué hacer en una emergencia en pocos pasos y conservar el conocimiento médico generado a bordo.
*Tablas:* `wiki_entries` · *Depende de:* Fase 0.

---

## Calendario en paralelo
| Bloque | Dev 1 | Dev 2 | Dev 3 |
|---|---|---|---|
| Día 1 | **Fase 0 (los 3 juntos)** | **Fase 0** | **Fase 0** |
| Semana 1 | D1-01 arranque + seed, D1-02 estilo | D2-01 ingesta, D2-02 captura | D3-01 alertas, D3-03 psicológico |
| Semana 2 | D1-03 login, D1-04 usuarios | D2-03 perfil, D2-04 sueño | D3-02 notificaciones, D3-04 cognitivo |
| Semana 3 | D1-05 panel, D1-06 rachas | D2-05 visión | D3-05 red neuronal, D3-07 Wiki |
| Semana 4 | D1-07 Tierra + integración | D2-06 auscultación + integración | D3-06 LLM + integración |

**Únicas dependencias entre devs (todas con sustituto):**
| Quién necesita | Qué | De quién | Sustituto mientras tanto |
|---|---|---|---|
| D2-01 ingesta | `evaluate_alerts()` | Dev 3 (D3-01) | función vacía con la misma firma |
| D2-01 ingesta | `update_streaks()` | Dev 1 (D1-06) | función vacía con la misma firma |
| Todas las pantallas privadas | sesión con PIN | Dev 1 (D1-03) | `useSession` simulado actual |
| D2-03 perfil, D3-01 alertas | línea base | Dev 1 (D1-04) | calcularla al vuelo con `utils/status.ts` |
| Todos los routers | proyecto FastAPI | Dev 1 (D1-01) | `main.py` mínimo propio, luego se une |

---

## Verificación
- La base se crea sin errores: `sqlite3 scan.db < backend/db/schema.sql`.
- Cada PR funciona contra el backend real, no solo con mocks: `uvicorn` + `pytest` para su API y `npm run dev` para sus pantallas.
- Prueba final del flujo completo: login → captura → alerta → notificación → protocolo de la Wiki → paquete a Tierra.
- Cada PR pasa el checklist de los 10 criterios de `SCAN_SPACE.md`.
