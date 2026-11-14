# Directivas Maestras e Instrucciones para Agentes de IA — SpaceScan

> **PROPÓSITO:** Establecer las reglas de gobernanza, arquitectura técnica, estándar visual UI/UX, restricciones normativas y protocolos operativos que debe cumplir cualquier asistente de Inteligencia Artificial al colaborar en el proyecto **SpaceScan (`Scan Space · ARES VII`)**.

---

## 1. Delimitación Estricta de Espacios de Trabajo

El ecosistema del proyecto se divide en **3 áreas con responsabilidades y permisos diferenciados**:

| Espacio | Propósito Principal | Reglas de Gobernanza para la IA |
| :--- | :--- | :--- |
| **`wakax-nasa-challenge-2026/`** | **Repositorio Oficial de Código** (`willor16/wakax-nasa-challenge-2026`). Contiene el software **SpaceScan** (`frontend/` en Nuxt 4 SPA y `backend/` en FastAPI + SQLite 3 STRICT). | **Restringido:** No crear, modificar ni eliminar archivos sin orden y confirmación explícita del usuario. Prohibido ejecutar comandos de Git (`add`, `commit`, `push`, `branch`, `checkout`) sin instrucción directa. |
| **`docs/`** | **Repositorio Oficial de Documentación y Gestión** (`willor16/docs`). Centraliza las reglas inquebrantables, estándar de diseño UI/UX, especificación de requerimientos, stack técnico, división del trabajo (`control_avance/`), bases del reto (`investigacion/`) y directivas de IA (`instrucciones_ia/`). | **Espacio documental oficial:** Toda especificación funcional, reglas visuales, arquitectura, contratos de base de datos, parámetros biomédicos y bitácoras se consultan y actualizan aquí. |
| **`miWork/`** | **Torre de Control Interna — Scan Workspace (Aislado).** Servidor local Python (`server.py`), dashboard colaborativo (`index.html`) y estado en tiempo real (`state.json`). | **Aislamiento total:** Ningún archivo, script, log o estado de `miWork/` debe copiarse ni integrarse en `wakax-nasa-challenge-2026/`. |

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
   * **Matriz de Puertos y CORS:** No asumir el puerto `8000` para FastAPI si `miWork/` está presente; apuntar por defecto a `8080`. Configurar siempre `devServer: { host: '0.0.0.0', port: 3000 }` en Nuxt y `CORSMiddleware` con `allow_origin_regex` en FastAPI para admitir clientes LAN (`192.168.*.*`, `10.*.*.*`).
   * **Empaquetado Backend:** Todo cambio en `pyproject.toml` debe incluir `[build-system]` con `setuptools.build_meta` y `[tool.setuptools.packages.find]` (`include = ["app*", "db*"]`).

---

## 4. Orden de Prioridad Documental en `docs/`

Antes de proponer o escribir código, el agente debe consultar en orden de prioridad:
1. [`control_avance/REGLAS_INQUEBRANTABLES.md`](../control_avance/REGLAS_INQUEBRANTABLES.md) — Los 10 criterios de premios, datos a recolectar, flujo de trabajo, idioma inglés estricto y prohibiciones.
2. [`control_avance/REGLAS_DISENO_UI_UX.md`](../control_avance/REGLAS_DISENO_UI_UX.md) — Estándar global UI/UX, las 5 Leyes de Diseño, paleta de 6 colores (`tokens.css`), mapeo de las 16 pantallas Figma y plantillas de código (Vue/ECharts/WebAudio/Zod/SQLite/FastAPI).
3. [`control_avance/ESPECIFICACION_REQUERIMIENTOS.md`](../control_avance/ESPECIFICACION_REQUERIMIENTOS.md) — Objetivos, 5 roles, RF 3.1 a 3.12, Requerimientos de Información y RNF 1 a 5.
4. [`control_avance/ARQUITECTURA_Y_STACK_TECNICO.md`](../control_avance/ARQUITECTURA_Y_STACK_TECNICO.md) — Stack oficial `[núcleo]` y `[extra]`.
5. [`control_avance/DIVISION_TRABAJO_DEVS.md`](../control_avance/DIVISION_TRABAJO_DEVS.md) — Contrato de Fase 0 (`backend/db/schema.sql`) y reparto de tareas `D1-xx`, `D2-xx`, `D3-xx`.

---

## 5. Normas Técnicas y Backlog de la Torre de Control Interna (`miWork/`)

Cuando el usuario solicite intervenir específicamente en la herramienta colaborativa interna `miWork/`, se aplican las siguientes reglas técnicas y tareas de mantenimiento:

### 5.1 Invariantes del Editor y Sincronizador (`miWork/`)
1. **Identificadores Canónicos (`doc_<slug>`):**
   * Todo documento Markdown sincronizado utiliza un identificador determinista derivado de su nombre de archivo (ej. `especificacion.md` $\rightarrow$ `doc_especificacion`). No generar IDs aleatorios temporales para evitar duplicaciones en `state.json`.
2. **Blindaje del Editor en Vivo:**
   * El ciclo de sincronización en segundo plano (reloj de 1.5 s) tiene prohibido sobrescribir el texto del editor si el usuario tiene el cursor activo (`document.activeElement === editor`) o si acaba de teclear.
3. **Guardado Secuencial Ordenado (Anti-carreras):**
   * Uso de semáforo (`isSavingColabDoc` y `hasPendingColabSave`) para garantizar que las peticiones HTTP de guardado viajen en orden estricto sin pérdida de líneas.
4. **Atajos Operativos:**
   * `Tab`: Inserta 2 espacios de sangría sin desenfocar el editor.
   * `Cmd + S` (Mac) / `Ctrl + S` (Windows): Guarda inmediatamente en el servidor local con confirmación visual.

### 5.2 Ajustes Pendientes Reportados para `miWork/` (Ref: `MyWork comentarios.md`)
* [ ] **Preservación de posición de scroll en Checklist:** Corregir el comportamiento donde marcar una tarea del checklist y pulsar el botón de "Listo" fuerza un desplazamiento inesperado (`scrollTop`) hacia la parte superior de la página.
* [ ] **Renombrado de Interfaz Principal:** Cambiar el título de la página principal de la herramienta interna de **`Scan Space`** a **`Scan Workspace`** (diferenciando claramente la Torre de Control interna del producto entregable **SpaceScan**).
