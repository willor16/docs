# 👥 Guía de Coordinación y Gobernanza del Equipo — SpaceScan (NASA Challenge 2026)

## 1. Arquitectura de los Espacios del Proyecto

El ecosistema de trabajo se estructura estrictamente en **dos repositorios independientes**, con la Torre de Control Interna integrada como subespacio aislado dentro de `docs/`:

1. **`wakax-nasa-challenge-2026/` (Repositorio Oficial de Código — SpaceScan)**:
   * Directorio del software entregable oficial (`willor16/wakax-nasa-challenge-2026`).
   * Contiene el frontend (**Nuxt 4 SPA**) y el backend (**Python 3.13 + FastAPI + SQLite 3 STRICT** en `backend/db/schema.sql`), servidos como un único proceso y en un solo puerto.
   * **Regla de Gobernanza:** Solo se integran módulos validados que cumplan los 10 criterios de premios globales, las 5 Leyes de Diseño UI/UX y bajo confirmación explícita. No se ejecutan operaciones de Git sin instrucción directa.

2. **`docs/` (Repositorio Oficial de Documentación, Gestión y Workspace — `willor16/docs`)**:
   * Centraliza las reglas inquebrantables, el estándar global de diseño UI/UX y guía maestra de construcción, la especificación formal de requerimientos, la arquitectura técnica, la división de trabajo para los 3 Devs fullstack, las bases oficiales del desafío (`bases_reto/`), la investigación biomédica recopilada (`docs-investigacion/`), las directivas para modelos de IA y la Torre de Control Interna (`docs/miWork/`).

   * **`docs/miWork/` (Torre de Control Interna — Aislado dentro de `docs/`)**:
     * Espacio exclusivo de coordinación interactiva en red local (**Scan Workspace**): dashboard web (`index.html`), servidor Python (`server.py`), base de datos colaborativa en tiempo real (`state.json`), notas del editor Colab (`docs/miWork/docs/`) y scripts de arranque (`iniciar_servidor.*`).
     * **Regla de Aislamiento:** Ningún archivo, script, log o dato de `docs/miWork/` debe formar parte del repositorio oficial de código `wakax-nasa-challenge-2026/`.
     * **Jerarquía Documental:** La fuente de verdad normativa del proyecto reside exclusivamente en `docs/control_avance/`; la subcarpeta `docs/miWork/docs/` es solo almacenamiento de trabajo del editor Colab.

---

## 2. Mapa Documental de `docs/`

```text
docs/
├── instrucciones_ia/
│   └── DIRECTIVAS_AGENTE_AI.md                      # Reglas operativas, restricciones, stack e invariantes de IA.
├── bases_reto/
│   ├── RETO_OFICIAL_NASA_2026.md                    # Consigna oficial del reto (?tab=details), criterios y 10 premios.
│   ├── RECURSOS_OFICIALES_RETO_2026.md              # Recursos oficiales del reto (?tab=resources: NASA HRP y CSA).
│   └── reto_oficial_nasa_2026.json                  # Esquema estructurado en JSON de las bases oficiales del reto.
├── docs-investigacion/
│   ├── README.md                                    # Índice maestro, fuentes y brechas de investigación biomédica.
│   ├── 01_antropometria_y_composicion.md            # Densidad ósea, masa muscular (IMM) e IMC por fase.
│   ├── 02_signos_vitales_y_metabolismo.md           # Ritmo cardíaco, presión arterial, temperatura, SpO2 y glucosa.
│   ├── 03_salud_ocular_sans.md                      # Cronograma y 5 pruebas visuales SANS en la ISS.
│   ├── 04_sueno_estres_y_psicologia.md              # Arquitectura de sueño, cortisol, HRV y cobertura conductual.
│   ├── 05_nutricion_hidratacion_ejercicio.md        # Calorías, TMB, colorimetría/osmolalidad y ejercicio.
│   ├── 06_ambiente_cabina_y_radiacion.md            # Confort térmico/humedad y estándares de radiación.
│   └── parametros_investigacion.json                # Catálogo JSON estructurado de rangos y URLs fuente.
├── control_avance/
│   ├── REGLAS_INQUEBRANTABLES.md                    # PRIORITARIO: Los 10 criterios, idioma 100% inglés, prohibiciones y Figma.
│   ├── REGLAS_DISENO_UI_UX.md                       # PRIORITARIO: Estándar UI/UX, 5 Leyes, 6 Colores, 16 Pantallas y Código Guía.
│   ├── ESPECIFICACION_REQUERIMIENTOS.md             # PRIORITARIO: Objetivos, 5 roles, RF 3.1–3.12, Datos y RNF 1–5.
│   ├── ARQUITECTURA_Y_STACK_TECNICO.md              # PRIORITARIO: Stack Nuxt 4 + FastAPI + SQLite3 + ONNX/Ollama offline.
│   ├── DIVISION_TRABAJO_DEVS.md                     # PRIORITARIO: Fase 0 (tablas SQLite) y Fase 1 (tareas D1, D2, D3).
│   └── BITACORA_AVANCE_RETO.md                      # Resumen ejecutivo del estado actual en dev, trazabilidad y bitácora.
└── miWork/                                          # Torre de Control Interna (aislada del código entregable).
    ├── server.py                                    # Servidor HTTP colaborativo en tiempo real (Puerto 8000).
    ├── index.html                                   # Dashboard colaborativo, checklist y editor Markdown Colab.
    ├── state.json                                   # Estado sincronizado de tareas, asignaciones, notas y docs.
    ├── ESPECIFICACION_CONTROL_AVANCE.md             # Manual técnico y funcional de la Torre de Control.
    ├── iniciar_servidor.command / .bat              # Lanzadores rápidos para macOS y Windows.
    └── docs/                                        # Almacén físico de archivos .md sincronizados por Colab.
        ├── GUIA_INICIO_tecnica_EQUIPO.md            # Guía técnica de coordinación, gobernanza y arranque local.
        ├── guia_pruebas_funcionales_web.md          # Plan de pruebas funcionales paso a paso.
        └── usuarios.md                              # Credenciales de acceso (PIN de 4 dígitos) y roles RBAC.
```

---

## 3. Reglas Inquebrantables de Producto, Diseño y Entrega

> El detalle normativo y técnico completo se encuentra en [`../../control_avance/REGLAS_INQUEBRANTABLES.md`](../../control_avance/REGLAS_INQUEBRANTABLES.md) y [`../../control_avance/REGLAS_DISENO_UI_UX.md`](../../control_avance/REGLAS_DISENO_UI_UX.md).

1. **Cumplimiento de los 10 Premios Globales:**
   * Todo módulo, pantalla, tabla, tarea o commit debe satisfacer los 10 criterios de premios globales. Si un cambio no aporta a ellos, se replantea antes de implementarlo.
2. **Idioma Estrictamente en Inglés Puro (Incluye el Código) y Cero Jerga Técnica en UI:**
   * Toda la aplicación entregable debe estar **100% en inglés**; ni una sola palabra en español u otro idioma dentro de la aplicación, **incluyendo el código fuente** (variables, rutas, endpoints, tablas, componentes y comentarios).
   * **Prohibido mostrar jerga técnica interna en pantalla:** Nunca escribir en la UI términos como `SQLite`, `JSON`, `FHIR`, `HL7`, `FTS5`, `WAL`, `Offline`, `Break-Glass`, `DTN`, `OSDR`, `DONKI`, `ONNX`, `Ollama`, `Nuxt` o `Python`.
3. **Palabras y Entidades Prohibidas:**
   * **Prohibición total de "NASA" en el producto/interfaz:** No usar de ninguna forma el nombre o marca **"NASA"**; esto incluye el nombre, logos y menciones de ningún tipo dentro de la aplicación.
   * **Prohibición total de China:** Prohibido hacer mención o incluir referencias directas o indirectas a **China** o entidades relacionadas.
4. **Fidelidad Estricta al Diseño en Figma y las 5 Leyes Visuales:**
   * Toda pantalla debe ser fiel al diseño oficial de **SpaceScan (`1568 × 940`)**: [Ver Diseño en Figma (`node-id=7382-2`)](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2&t=tzbC2RhJeGZ2Dlov-1).
   * **Paleta única de 6 colores** desde `tokens.css`: `#001524` (Fondo), `#15616D` (Tarjetas/Botones), `#FFECD1` (Texto/Iconos), `#2AEF4B` (OK/Nominal), `#000C5C` (Selección activa de menú/Guías/Pastillas/Warning) y `#D5110B` (Crítico/Alerta).
   * **Separación estricta Resultados vs. Captura:** Las vistas de monitoreo (`Profile`, `Sleep`, `Vision`, `Auscultation`, `Crew Overview`, `Crew Streaks`) son **100% de solo lectura**; todo formulario o grabación va exclusivamente en **`Capture`** (`/capture/*`).
   * **Jerarquía de Navegación en 2 Niveles:** Barra pública de 3 pestañas sin PIN (`Sign In · Crew Overview · Crew Streaks`) y dock autenticado trapezoidal simétrico de 7 módulos con **`Profile` elevado exactamente al centro** (`1 Vision · 2 Sleep · 3 Auscultation · [4 PROFILE] · 5 Capture · 6 Guide · 7 Comms`), manteniendo **`Notifications (N)` únicamente en el header superior**.
5. **Ejecución 100% a Bordo y Sin Internet (RNF 1):**
   * Cero CDNs y cero APIs en la nube en tiempo de ejecución. Fuentes `.woff2`, colección de 16 iconos locales `spacescan`, modelos de IA (ONNX + Ollama) y datasets espaciales precargados (`seed.py`) corren localmente desde un solo puerto.

---

## 4. Flujo de Trabajo Oficial y Roles del Equipo

1. **Investigadores de Datos (Independiente de Devs):**
   * **Flujo:** `Investigar → Filtrar → Estructurar en JSON`.
   * Definen rangos clínicos de referencia, frecuencias de medición y fuentes científicas verificables para alimentar `metric_catalog` y `seed.py`.
2. **Desarrolladores (3 Devs Fullstack — Wilson, Wilmer, Carlos):**
   * Cada desarrollador es dueño de módulos completos de punta a punta: **sus tablas en SQLite (`schema.sql`) + sus endpoints en FastAPI + sus pantallas en Nuxt**.
   * **Dev 1:** Acceso (`/login`), tripulación y línea base, vistas públicas grupales (`/crew-overview`, `/crew-streaks`), estilo base (`tokens.css`) y cola asíncrona con Control a tierra (`/comms`).
   * **Dev 2:** Ingesta de mediciones (`POST /measurements`), módulo de captura (`/capture/*`), perfil por etapas (`/profile/*`) y módulos de resultados de Sueño (`/sleep`), Visión SANS (`/vision`) y Auscultación (`/auscultation`).
   * **Dev 3:** Motor de alertas + *Quiet Hours*, bandeja en header (`/notifications`), evaluaciones psicológicas y cognitivo-motrices, IA local (Red Neuronal ONNX + LLM Ollama con validación del `Médico`) y Guía Médica/Wiki FTS5 (`/guide`).
3. **Validadores:**
   * **Flujo:** `Módulo Terminado → Revisan contra Checklist de 10 Premios, DoD de Diseño UI/UX y Especificación → OK`.
   * Si un PR no cumple el checklist o se desvía del Figma/especificación, regresa a Devs.
4. **Testers (Steve, Sandra, Foco):**
   * **Flujo:** `GIT → Clonar → Pruebas E2E en modo avión contra backend real`.
   * Verifican el flujo completo: `Sign In con PIN → Capture → Alerta → Notifications (Header) → Medical Guide → Mission Control (Comms)`.

---

## 5. Puesta en Marcha Local y Acceso en Red (LAN / Cabina)

### 5.1 Matriz Oficial de Puertos en Desarrollo
Para evitar colisiones de enlace en la máquina de desarrollo (`[Errno 48] Address already in use`):
* **`Puerto 8000`:** Torre de Control Interna (`docs/miWork/server.py`).
* **`Puerto 8080`:** Backend FastAPI + Telemetría SSE (`wakax-nasa-challenge-2026/backend`).
* **`Puerto 3000`:** Frontend Nuxt 4 (`wakax-nasa-challenge-2026/frontend`).

### 5.2 Arranque del Backend (`backend/`)
```bash
cd wakax-nasa-challenge-2026/backend
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e ".[dev]"  # Requiere pyproject.toml con build-system de setuptools y paquetes app + db
python -m uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

### 5.3 Arranque del Frontend (`frontend/`)
```bash
cd wakax-nasa-challenge-2026/frontend
npm install
npm run dev
```
*(Nuxt 4 está preconfigurado con `devServer: { host: '0.0.0.0', port: 3000 }` e internacionalización nativa en TypeScript `i18n/locales/en.ts`)*.

### 5.4 Protocolo de Pruebas Multi-dispositivo para Testers
1. Obtener la IP local de la máquina anfitriona (`ifconfig | grep "inet "` o desde la consola de Nuxt en `Network:`).
2. Conectar el teléfono o tableta a la misma red Wi-Fi y navegar a `http://<IP_ANFITRION>:3000`.
3. Validar el flujo de cabina completo en modo avión simulado (cero peticiones externas y visualización adaptada al HUD de alta fidelidad).
