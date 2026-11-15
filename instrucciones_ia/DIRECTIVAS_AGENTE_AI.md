# Directivas Maestras e Instrucciones para Agentes de IA — SpaceScan

> **PROPÓSITO:** Establecer las reglas de gobernanza, arquitectura técnica, estándar visual UI/UX, restricciones normativas y protocolos operativos que debe cumplir cualquier asistente de Inteligencia Artificial al colaborar en el proyecto **SpaceScan (`Scan Space · ARES VII`)**.

---

## 1. Delimitación Estricta de Espacios de Trabajo

El ecosistema del proyecto se divide en **2 repositorios principales** (con la Torre de Control Interna alojada dentro de `docs/miWork/`):

| Espacio | Propósito Principal | Reglas de Gobernanza para la IA |
| :--- | :--- | :--- |
| **`wakax-nasa-challenge-2026/`** | **Repositorio Oficial de Código** (`willor16/wakax-nasa-challenge-2026`). Contiene el software **SpaceScan** (`frontend/` en Nuxt 4 SPA y `backend/` en FastAPI + SQLite 3 STRICT). | **Restringido:** No crear, modificar ni eliminar archivos sin orden y confirmación explícita del usuario. Prohibido ejecutar comandos de Git (`add`, `commit`, `push`, `branch`, `checkout`) sin instrucción directa. |
| **`docs/`** | **Repositorio Oficial de Documentación y Gestión** (`willor16/docs`). Centraliza las reglas inquebrantables, estándar de diseño UI/UX, especificación de requerimientos, stack técnico, división del trabajo (`control_avance/`), bases del reto (`bases_reto/`), investigación biomédica recopilada (`docs-investigacion/`), directivas de IA (`instrucciones_ia/`) y la Torre de Control (`miWork/`). | **Espacio documental oficial:** Toda especificación funcional, reglas visuales, arquitectura, contratos de base de datos y bitácoras se consultan y actualizan en `docs/control_avance/`. La investigación científica recopilada se consolida en `docs/docs-investigacion/`. La subcarpeta `docs/miWork/docs/` es solo almacenamiento de trabajo del editor Colab y **no** sustituye la documentación normativa. |
| **`docs/miWork/`** | **Torre de Control Interna — Scan Workspace (Aislado dentro de `docs/`).** Servidor local Python (`server.py`), dashboard colaborativo (`index.html`), estado en tiempo real (`state.json`) y archivos `.md` de Colab (`docs/miWork/docs/`). | **Aislamiento total respecto al código:** Ningún archivo, script, log o estado de `docs/miWork/` debe copiarse ni integrarse en `wakax-nasa-challenge-2026/`. |

---

## 2. Perfil Técnico y Modo de Comunicación

1. **Rigor Técnico Directo:**
   * Comunicación profesional, concisa y orientada a arquitectura de software fullstack (Nuxt 4, Tailwind CSS 4, Reka UI, Apache ECharts, FastAPI, SQLite 3 STRICT, inferencia local ONNX/Ollama) e ingeniería biomédica espacial.
2. **Cero Condescendencia ni Analogías Forzadas:**
   * Tratar conceptos técnicos de manera directa, sin simplificaciones excesivas ni metáforas innecesarias.
3. **Orientación a la Acción:**
   * Respuestas estructuradas con diagnósticos fundamentados, apego estricto a los documentos de `docs/control_avance/` y pasos concretos.

---

## 3. Reglas Inquebrantables de Producto y Diseño UI/UX que la IA Debe Hacer Cumplir

Al redactar código, especificaciones, estilos CSS, componentes Vue o textos de interfaz para **SpaceScan**, el agente de IA está obligado a verificar el cumplimiento estricto de [`REGLAS_INQUEBRANTABLES.md`](../control_avance/REGLAS_INQUEBRANTABLES.md) y [`REGLAS_DISENO_UI_UX.md`](../control_avance/REGLAS_DISENO_UI_UX.md):

1. **Idioma 100% Inglés Puro (Incluye el Código) y Cero Jerga Tecnológica en Pantalla:**
   * Ni una sola palabra en español u otro idioma dentro de la aplicación entregable, **incluyendo el código fuente** (identificadores, variables, rutas, endpoints, tablas, comentarios y textos).
   * Todo texto visible dentro de la aplicación debe estar en **inglés claro y humano** (`Sign In`, `Sleep Score`, `Right Eye Elevated`, `Save Lung Recording`). Si se usa `@nuxtjs/i18n`, se fija `defaultLocale: 'en'` mediante archivos TypeScript con la macro nativa `defineI18nLocale` en `frontend/i18n/locales/en.ts` (prohibido usar catálogos `.json` planos que colisionen con los transformadores de Vite 6).
   * **Prohibido mostrar jerga técnica interna en la UI:** Nunca escribir en pantalla palabras como `SQLite`, `JSON`, `FHIR`, `HL7`, `Kiwix`, `ZIM`, `FTS5`, `WAL`, `Offline`, `Break-Glass`, `DTN`, `OSDR`, `DONKI`, `ONNX`, `Ollama`, `Nuxt` o `Python`.
2. **Palabras y Entidades Prohibidas:**
   * **Prohibido usar "NASA" de ninguna forma en el producto/interfaz:** Esto incluye el nombre, logos y menciones de ningún tipo dentro de la aplicación o el código visible.
   * **Prohibido** incluir menciones, datos, modelos o referencias directas o indirectas a **China** o entidades relacionadas.
3. **Ejecución 100% Onboard & Air-Gapped (`RNF 1`):**
   * Prohibido introducir CDNs externos (`googleapis`, `unpkg`, `jsdelivr`, Iconify remoto) o llamadas a APIs en la nube en tiempo de ejecución.
   * Un solo proceso y un solo puerto: FastAPI sirve el build estático de Nuxt 4 (`ssr: false`), la API REST y el stream `SSE`. Fuentes `.woff2` (`Inter`, `JetBrains Mono`) y los 16 iconos de la colección `spacescan` son 100% locales.
4. **Paleta Oficial de 6 Colores (`frontend/app/assets/css/tokens.css`):**
   * Prohibido escribir códigos hexadecimales sueltos en componentes. Usar exclusivamente los tokens basados en los 6 colores oficiales:
     * `#001524` (`--color-bg-base` — Fondo Principal)
     * `#15616D` (`--color-surface-card` — Tarjetas *smoked-glass* y Botones)
     * `#FFECD1` (`--color-text-primary` — Texto e Iconos principales)
     * `#2AEF4B` (`--color-status-ok` — Estado OK / Nominal, trazos ECG/S1-S2/Deep)
     * `#000C5C` (`--color-navy-accent` — Selección activa en menús/filtros al 30%–52% opacidad con filete `#263BB0`, líneas guía en gráficas, pastillas de referencia y nivel Warning)
     * `#D5110B` (`--color-status-critical` — Estado Crítico / Alerta, Awake y modo alerta global `data-cabin-mode="critical"`)
5. **Separación Estricta entre Vistas de Resultados y Módulo `Capture`:**
   * Las pantallas de monitoreo (`Profile`, `Sleep`, `Vision`, `Auscultation`, `Crew Overview`, `Crew Streaks`) son **100% de solo lectura (Solo Resultados)**: cero inputs y cero botones de registro incrustados.
   * Toda entrada manual, validación con `Zod`, grabación acústica de `30 s` o prueba psicomotriz vive **exclusivamente** en el módulo **`Capture`** (`/capture/auscultation`, `/capture/physical`, `/capture/vision`, `/capture/psych-sleep`).
6. **Jerarquía de Navegación en 2 Niveles y Densidad Controlada:**
   * **Nivel 1 Público (sin PIN):** Barra inferior de 3 pestañas (`Sign In · Crew Overview · Crew Streaks`).
   * **Nivel 2 Autenticado (tras PIN de 4 dígitos):** Dock inferior trapezoidal **simétrico de 7 módulos** con **`Profile` elevado exactamente al centro**: `1 Vision · 2 Sleep · 3 Auscultation · [4 PROFILE] · 5 Capture · 6 Guide · 7 Comms`.
   * **`Notifications (N)` nunca va en el dock inferior:** vive **únicamente en el header superior** (`/notifications`).
   * Máximo 2 o 3 contenedores `<HudWindow>` por pantalla (`28 px` margen exterior, `18 px` gap), sin footers informativos redundantes.
7. **Patrones Técnicos de Arranque, Puertos y Redirección en Nuxt/FastAPI:**
   * **Redirección de Rutas:** Usar siempre `definePageMeta({ redirect: '/login' })` para navegación declarativa en SPA. Prohibido usar `await navigateTo()` en nivel superior de `<script setup>` en páginas puente sin vista.
   * **Matriz de Puertos y CORS:** No asumir el puerto `8000` para FastAPI si `docs/miWork/` está presente; apuntar por defecto a `8080`. Configurar siempre `devServer: { host: '0.0.0.0', port: 3000 }` en Nuxt y `CORSMiddleware` con `allow_origin_regex` en FastAPI para admitir clientes LAN (`192.168.*.*`, `10.*.*.*`).
   * **Empaquetado Backend:** Todo cambio en `pyproject.toml` debe incluir `[build-system]` con `setuptools.build_meta` y `[tool.setuptools.packages.find]` (`include = ["app*", "db*"]`).

---

## 4. Taxonomía de las 5 Capas Documentales y Orden de Prioridad en `docs/`

El repositorio `docs/` se estructura en **5 capas con roles diferenciados** para evitar mezclar borradores preliminares con especificaciones normativas o estado de código:

| Capa | Directorio / Archivo | Propósito y Regla de Uso para el Agente |
| :--- | :--- | :--- |
| **1. Especificaciones Normativas (Prioridad 1–5)** | `docs/control_avance/` | **Única fuente de verdad de producto y arquitectura:**<br>1. [`REGLAS_INQUEBRANTABLES.md`](../control_avance/REGLAS_INQUEBRANTABLES.md) — Los 10 criterios de premios, datos a recolectar, flujo de trabajo, idioma inglés estricto y prohibiciones.<br>2. [`REGLAS_DISENO_UI_UX.md`](../control_avance/REGLAS_DISENO_UI_UX.md) — Estándar global UI/UX, las 5 Leyes de Diseño, paleta de 6 colores (`tokens.css`), mapeo de las 16 pantallas Figma (`1568 × 940`) y componentes de construcción (`HoloFigure.vue`, `CaptureTabs.vue`, `ProfileTabs.vue`, `SubnavTabs.vue`, `ArcGauge.vue`, `BandRow.vue`).<br>3. [`ESPECIFICACION_REQUERIMIENTOS.md`](../control_avance/ESPECIFICACION_REQUERIMIENTOS.md) — Objetivos, 5 roles, RF 3.1 a 3.12, Requerimientos de Información y RNF 1 a 5.<br>4. [`ARQUITECTURA_Y_STACK_TECNICO.md`](../control_avance/ARQUITECTURA_Y_STACK_TECNICO.md) — Stack oficial `[núcleo]` y `[extra]`.<br>5. [`DIVISION_TRABAJO_DEVS.md`](../control_avance/DIVISION_TRABAJO_DEVS.md) — Contrato de Fase 0 (`backend/db/schema.sql`) y reparto de tareas `D1-xx`, `D2-xx`, `D3-xx`. |
| **2. Estado de Implementación (`dev`)** | [`control_avance/BITACORA_AVANCE_RETO.md`](../control_avance/BITACORA_AVANCE_RETO.md) | **Registro real de lo implementado en `wakax-nasa-challenge-2026/` (rama `dev`):** Documenta el cierre completo de Fase 0 y Fase 1 (`D1-01`..`D1-07`, `D2-01`..`D2-06`, `D3-01`..`D3-06`) y las revisiones integrales de cumplimiento (`PR #14` y `PR #16`). |
| **3. Investigación y Abstracción Biomédica** | [`docs-investigacion/`](../docs-investigacion/README.md) | **Soporte científico del equipo:** 6 fichas clínicas (`01` a `06_*.md`) y [`parametros_investigacion.json`](../docs-investigacion/parametros_investigacion.json). Es la fuente que alimenta el catálogo maestro del backend en `backend/db/seed_snapshots/reference_ranges.json` (`38` métricas clínicas en `metric_catalog`). |
| **4. Recursos Oficiales del Reto** | [`bases_reto/`](../bases_reto/RETO_OFICIAL_NASA_2026.md) | **Bases oficiales del desafío:** [`RETO_OFICIAL_NASA_2026.md`](../bases_reto/RETO_OFICIAL_NASA_2026.md) (`?tab=details` y *Judging Guide*), [`RECURSOS_OFICIALES_RETO_2026.md`](../bases_reto/RECURSOS_OFICIALES_RETO_2026.md) (`?tab=resources`: NASA HRP y CSA) y [`reto_oficial_nasa_2026.json`](../bases_reto/reto_oficial_nasa_2026.json). Se usan para justificar elegibilidad y trazabilidad en la entrega de Space Apps, respetando siempre la prohibición de mostrar la palabra `"NASA"` dentro de la interfaz de la aplicación. |
| **5. Notas Operativas y Borradores Colab** | `docs/miWork/docs/` | **Almacén de trabajo del editor Colab:**<br>• **Guías operativas vigentes:** [`GUIA_INICIO_tecnica_EQUIPO.md`](../miWork/docs/GUIA_INICIO_tecnica_EQUIPO.md) (arranque y puertos), [`guia_pruebas_funcionales_web.md`](../miWork/docs/guia_pruebas_funcionales_web.md) (plan de pruebas funcionales paso a paso) y [`usuarios.md`](../miWork/docs/usuarios.md) (credenciales PIN y RBAC).<br>• **Borradores iniciales superados:** `Especifcacion.md`, `reglas inquebrantables.md`, `divicion del trabajo.md` y `requerimientos tecnicos.md` son apuntes preliminares cuyo contenido oficial ya fue consolidado en `docs/control_avance/`. **Nunca usar estos borradores por encima de `docs/control_avance/`.** |

---

## 5. Normas Técnicas y Backlog de la Torre de Control Interna (`docs/miWork/`)

Cuando el usuario solicite intervenir específicamente en la herramienta colaborativa interna `docs/miWork/`, se aplican las siguientes reglas técnicas y tareas de mantenimiento:

### 5.1 Invariantes del Editor y Sincronizador (`docs/miWork/`)
1. **Identificadores Canónicos (`doc_<slug>`):**
   * Todo documento Markdown sincronizado utiliza un identificador determinista derivado de su nombre de archivo (ej. `especificacion.md` $\rightarrow$ `doc_especificacion`). No generar IDs aleatorios temporales para evitar duplicaciones en `state.json`.
2. **Blindaje del Editor en Vivo:**
   * El ciclo de sincronización en segundo plano (reloj de 1.5 s) tiene prohibido sobrescribir el texto del editor si el usuario tiene el cursor activo (`document.activeElement === editor`) o si acaba de teclear.
3. **Guardado Secuencial Ordenado (Anti-carreras):**
   * Uso de semáforo (`isSavingColabDoc` y `hasPendingColabSave`) para garantizar que las peticiones HTTP de guardado viajen en orden estricto sin pérdida de líneas.
4. **Atajos Operativos:**
   * `Tab`: Inserta 2 espacios de sangría sin desenfocar el editor.
   * `Cmd + S` (Mac) / `Ctrl + S` (Windows): Guarda inmediatamente en el servidor local con confirmación visual.

### 5.2 Ajustes Pendientes Reportados para `docs/miWork/` (Ref: `MyWork comentarios.md`)
* [ ] **Preservación de posición de scroll en Checklist:** Corregir el comportamiento donde marcar una tarea del checklist y pulsar el botón de "Listo" fuerza un desplazamiento inesperado (`scrollTop`) hacia la parte superior de la página.
* [ ] **Renombrado de Interfaz Principal:** Cambiar el título de la página principal de la herramienta interna de **`Scan Space`** a **`Scan Workspace`** (diferenciando claramente la Torre de Control interna del producto entregable **SpaceScan**).
