# 👥 Guía de Coordinación y Gobernanza del Equipo — SpaceScan (NASA Challenge 2026)

## 1. Arquitectura de los Tres Espacios del Proyecto

El ecosistema de trabajo se estructura estrictamente en tres directorios con responsabilidades independientes:

1. **`wakax-nasa-challenge-2026/` (Repositorio Oficial de Código — SpaceScan)**:
   * Directorio del software entregable oficial (`willor16/wakax-nasa-challenge-2026`).
   * Contiene el frontend (**Nuxt 4 SPA**), el backend (**Python 3.13 + FastAPI**) y el esquema de base de datos (**SQLite 3** en `backend/db/schema.sql`).
   * **Regla de Gobernanza:** Solo se integran módulos validados que cumplan los 10 criterios de premios globales y bajo confirmación explícita. No se ejecutan operaciones de Git sin instrucción directa.

2. **`wakax-docs/` (Repositorio Oficial de Documentación y Gestión)**:
   * Centraliza las reglas inquebrantables, la especificación formal de requerimientos, la arquitectura técnica, la división de trabajo para los 3 Devs fullstack, las bases oficiales del desafío y las directivas para modelos de IA.

3. **`miWork/` (Torre de Control Interna — Aislado)**:
   * Espacio exclusivo de coordinación interactiva en red local (**Scan Workspace**): dashboard web (`index.html`), servidor Python (`server.py`), base de datos colaborativa en tiempo real (`state.json`) y scripts de arranque (`iniciar_servidor.*`).
   * **Regla de Aislamiento:** Ningún archivo, script, log o dato de `miWork/` debe formar parte del repositorio oficial de código `wakax-nasa-challenge-2026/`.

---

## 2. Mapa Documental de `wakax-docs/`

```text
wakax-docs/
├── GUIA_INICIO_EQUIPO.md                            # Gobernanza general, mapa documental y flujo de trabajo.
├── instrucciones_ia/
│   └── DIRECTIVAS_AGENTE_AI.md                      # Reglas operativas, restricciones, stack e invariantes de IA.
├── investigacion/
│   ├── RETO_OFICIAL_NASA_2026.md                    # Consigna oficial del reto, criterios del jurado y 10 premios.
│   └── reto_oficial_nasa_2026.json                  # Esquema estructurado en JSON de las bases oficiales del reto.
└── control_avance/
    ├── REGLAS_INQUEBRANTABLES.md                    # PRIORITARIO: Los 10 criterios, idioma 100% inglés, prohibiciones y Figma.
    ├── ESPECIFICACION_REQUERIMIENTOS.md             # PRIORITARIO: Objetivos, 5 roles, RF 3.1–3.12, Datos y RNF 1–5.
    ├── ARQUITECTURA_Y_STACK_TECNICO.md              # PRIORITARIO: Stack Nuxt 4 + FastAPI + SQLite3 + ONNX/Ollama offline.
    ├── DIVISION_TRABAJO_DEVS.md                     # PRIORITARIO: Fase 0 (16 tablas) y Fase 1 (tareas D1, D2, D3).
    └── BITACORA_AVANCE_RETO.md                      # Resumen ejecutivo del estado actual, trazabilidad y bitácora.
```

---

## 3. Reglas Inquebrantables de Operación y Entrega

> El detalle completo y el checklist obligatorio por entregable se encuentran en [`control_avance/REGLAS_INQUEBRANTABLES.md`](./control_avance/REGLAS_INQUEBRANTABLES.md).

1. **Cumplimiento de los 10 Premios Globales:**
   * Todo módulo, pantalla, tabla, tarea o commit debe satisfacer los 10 criterios de premios globales. Si un cambio no aporta a ellos, se replantea antes de implementarlo.
2. **Idioma Estrictamente en Inglés (100% English):**
   * Toda la aplicación entregable (interfaz, textos clínicos, alertas, Wiki, catálogos y demostración) debe estar **exclusivamente en inglés**, sin integrar ni una sola palabra en español u otro idioma.
3. **Palabras y Entidades Prohibidas:**
   * Prohibido hacer mención o incluir referencias directas o indirectas a **China** o entidades relacionadas.
   * No utilizar de forma indebida el nombre o marca de la **NASA** dentro de la identidad del producto.
4. **Fidelidad Estricta al Diseño en Figma:**
   * Toda pantalla e interacción debe ser fiel al diseño oficial de **SpaceScan**: [Ver Diseño en Figma](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2&t=tzbC2RhJeGZ2Dlov-1).
5. **Ejecución 100% a Bordo y Sin Internet (RNF 1):**
   * Cero CDNs y cero APIs en la nube en tiempo de ejecución. Fuentes, iconos, modelos de IA (ONNX + Ollama) y datasets espaciales precargados (`seed.py`) corren localmente.

---

## 4. Flujo de Trabajo Oficial y Roles del Equipo

1. **Investigadores de Datos (Independiente de Devs):**
   * **Flujo:** `Investigar → Filtrar → Estructurar en JSON`.
   * Definen rangos clínicos de referencia, frecuencias de medición y fuentes científicas verificables para alimentar `metric_catalog` y `seed.py`.
2. **Desarrolladores (3 Devs Fullstack — Wilson, Wilmer, Carlos):**
   * Cada desarrollador es dueño de módulos completos de punta a punta: **sus tablas en SQLite (`schema.sql`) + sus endpoints en FastAPI + sus pantallas en Nuxt**.
   * **Dev 1:** Acceso, tripulación (`crew`, `baselines`), vistas grupales (`panel`, `rachas`) y cola asíncrona con Control a tierra (`sync_packets`).
   * **Dev 2:** Ingesta de mediciones (`measurements`), formularios de captura, perfil por etapas (*Despegue / Misión / Regreso*) y módulos de Sueño, Visión (SANS) y Auscultación (30 s).
   * **Dev 3:** Motor de alertas + *Quiet Hours*, pruebas psicológicas y cognitivo-motrices, IA local (Red Neuronal + LLM con validación del `Médico`) y Wiki médica de respaldo (FTS5).
3. **Validadores:**
   * **Flujo:** `Módulo Terminado → Revisan contra Checklist de 10 Premios y Especificación → OK`.
   * Si un PR no cumple el checklist o se desvía del Figma/especificación, regresa a Devs.
4. **Testers (Steve, Sandra, Foco):**
   * **Flujo:** `GIT → Clonar → Pruebas E2E contra backend real`.
   * Verifican el flujo completo: `Login con PIN → Captura → Alerta → Notificación → Protocolo Wiki → Paquete a Tierra`.
