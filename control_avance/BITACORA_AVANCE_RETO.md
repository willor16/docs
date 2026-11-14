# Bitácora de Avance y Resumen Maestro del Proyecto — SpaceScan

> **ESTADO ACTUAL:** Especificación de requerimientos, reglas inquebrantables, stack técnico y división de trabajo en paralelo (Fase 0 y Fase 1) cerrados y consolidados en `wakax-docs/`.  
> **NOMBRE DEL SISTEMA:** **SpaceScan**  
> **DISEÑO OFICIAL (FIGMA):** [SpaceScan — Figma Design](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2)

---

## 1. Índice de Documentación Prioritaria Consolidada

Toda la definición funcional, normativa y técnica revisada por el equipo ha sido integrada en los siguientes documentos dentro de `wakax-docs/control_avance/`:

| Documento | Contenido Clave |
| :--- | :--- |
| [**1. Reglas Inquebrantables**](./REGLAS_INQUEBRANTABLES.md) | Regla de oro de los **10 premios globales** + checklist obligatorio por PR, etapas (*Antes / Durante / Después* del despegue), datos a recolectar, fidelidad al Figma, flujo de trabajo, **idioma 100% inglés estricto** y **palabras/entidades prohibidas** (NASA / China). |
| [**2. Especificación de Requerimientos**](./ESPECIFICACION_REQUERIMIENTOS.md) | Objetivo general y específicos, **5 actores y roles** (`Astronauta`, `Piloto`, `Operador`, `Médico`, `Control a tierra`), niveles de acceso en cabina (público vs. PIN de 4 dígitos), **RF 3.1 a 3.12**, Requerimientos de Información y **RNF 1 a 5**. |
| [**3. Arquitectura y Stack Técnico**](./ARQUITECTURA_Y_STACK_TECNICO.md) | Ejecución **100% a bordo y sin internet** (cero CDNs/APIs cloud): **Nuxt 4 SPA** + Tailwind 4 + Reka UI + ECharts + Web Audio API; **Python 3.13 + FastAPI + SQLite 3** (WAL, STRICT, triggers *append-only*, FTS5, JSON1) + **ONNX Runtime** (Red Neuronal) + **Ollama/llama.cpp** (LLM local). |
| [**4. División del Trabajo (3 Devs)**](./DIVISION_TRABAJO_DEVS.md) | **Fase 0** (`backend/db/schema.sql` con 16 tablas y tabla genérica `measurements` *append-only*) y **Fase 1** en paralelo: **Dev 1** (`D1-01` a `D1-07`), **Dev 2** (`D2-01` a `D2-06`) y **Dev 3** (`D3-01` a `D3-07`), con calendario de 4 semanas y sustitutos temporales sin bloqueos. |

---

## 2. Síntesis Arquitectónica de SpaceScan

### 2.1 Roles Operativos y Control de Acceso
* **Sin sesión (Público en cabina):** Vista General de Salud (*Optimal / Nominal / Attention*, signos clave y ambiente de cabina) y Rachas de Constancia (individuales y grupal).
* **Con sesión (Selección de perfil + PIN de 4 dígitos):**
  * `Astronauta`: Monitoreo longitudinal personal en *Despegue*, *Misión* y *Regreso*.
  * `Piloto`: Énfasis en aptitud neurocognitiva y visual (atención, tiempo de reacción en ms, precisión, agudeza visual y descanso).
  * `Operador`: Énfasis en aptitud cardiorrespiratoria y recuperación post-EVA ($\text{VO}_2\text{ máx}$, auscultación, respuesta ortostática) + **gestión local de usuarios**.
  * `Médico`: Supervisión clínica global, revisión de salud ocular (SANS), **validación de prediagnósticos de IA (RN + LLM)** y atención de escalamientos.
  * `Control a tierra` (Remoto/Asíncrono): Recepción diferida de paquetes médicos (`sync_packets`), emisión de directrices remotas y **gestión remota de usuarios**.

### 2.2 Módulos Nucleares del Sistema
1. **Gestión de Usuarios, Perfiles y Línea Base (`crew`, `baselines`):** Comparación longitudinal por etapa contra la línea base pre-misión individual.
2. **Ingesta Centralizada Inmutable (`measurements`, `metric_catalog`):** Tabla genérica *append-only* para datos manuales y automáticos; nuevas métricas se agregan como filas en `metric_catalog`.
3. **Módulo de Sueño (`sleep_sessions`, `sleep_stages`):** Puntaje de calidad, eficiencia y fases (*Deep, REM, Light, Awake*) filtrables por última noche, 7, 14 y 30 días.
4. **Evaluación Psicológica y Cognitivo-Motriz (`psych_tests`, `cognitive_tests`):** Ánimo, estrés, soledad y motivación (tendencia 14 días) + prueba interactiva de tiempo de reacción y atención.
5. **Módulo de Visión y Salud Ocular SANS (`measurements` L/R):** Seguimiento bilateral de diámetro de vaina del nervio óptico, presión intraocular, grosor retiniano y agudeza visual.
6. **Módulo de Auscultación Acústica (`auscultation_samples`):** Verificación previa de ruido ambiental en cabina y grabación de 30 s cardíaca/pulmonar (Web Audio API + MediaRecorder, audio en disco con hash SHA-256).
7. **Diagnóstico Asistido Dual Offline (`diagnoses`):** Red Neuronal Convencional (ONNX Runtime) para detección temprana de anomalías + LLM local (`Ollama` / `llama.cpp`) para explicación orientativa sujeta a validación del `Médico`.
8. **Guía Médica y Wiki de Respaldo (`wiki_entries` con SQLite FTS5):** Protocolos de emergencia buscables offline ($\text{CO}_2$, visión, sueño/fatiga, trauma, medicación) enriquecidos con diagnósticos ya validados.
9. **Alertas, Chequeos y Quiet Hours (`alerts`, `scheduled_checks`):** Notificaciones vía SSE con protección del horario de descanso para avisos no críticos.
10. **Comunicación Asíncrona con Control a Tierra (`sync_packets`):** Cola *store-and-forward* tolerante a alta latencia inspirada en DTN.

---

## 3. Estado de Tareas de la Herramienta Interna (`miWork/`)

De acuerdo con la revisión de `MyWork comentarios.md`, quedan registrados en [`instrucciones_ia/DIRECTIVAS_AGENTE_AI.md`](../instrucciones_ia/DIRECTIVAS_AGENTE_AI.md) los siguientes ajustes puntuales para cuando se trabaje sobre `miWork/`:
- [ ] Evitar que al marcar una tarea en el checklist y dar clic en "Listo" la vista se desplace automáticamente hasta arriba (`scrollTop`).
- [ ] Cambiar el título principal de la interfaz de `miWork/` de **`Scan Space`** a **`Scan Workspace`**.

---

## 4. Registro Cronológico de Decisiones (Bitácora)

| Fecha | Hito / Decisión | Descripción Técnica | Responsable |
| :--- | :--- | :--- | :--- |
| **2026-11-14** | **Consolidación de Especificación, Reglas, Stack y División de Trabajo** | Integración prioritaria en `wakax-docs/` de los 5 documentos validados (`reglas inquebrantables.md`, `Especifcacion.md`, `requerimientos tecnicos.md`, `divicion del trabajo.md` y `MyWork comentarios.md`), reemplazando supuestos preliminares por la arquitectura definitiva de **SpaceScan**. | Equipo / IA |
