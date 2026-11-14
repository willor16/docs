# Arquitectura y Stack Técnico Oficial — SpaceScan

> **Regla de Ejecución (RNF 1):** Todo el sistema corre **a bordo y sin internet**. Cero CDNs y cero APIs en la nube en tiempo de ejecución: tipografías, iconos, modelos de IA y datasets espaciales residen localmente dentro del proyecto.  
> **Guía Maestra de Construcción y UI/UX:** Ver plantillas de código, paleta de 6 colores (`tokens.css`) y mapeo de las 16 pantallas en [`REGLAS_DISENO_UI_UX.md`](./REGLAS_DISENO_UI_UX.md).  
> **Convención de Prioridad:** `[núcleo]` = obligatorio para la demo oficial · `[extra]` = solo si sobra tiempo tras completar el núcleo.

---

## 1. Frontend (`frontend/`)

* **Nuxt 4 (Vue 3 + TypeScript estricto), modo SPA (`ssr: false`)** `[núcleo]`
  * Se compila como aplicación estática y es servida directamente por el mismo backend Python: una sola pieza desplegable a bordo en un único puerto.
  * **Idioma y Limpieza Visual:** Estrictamente 100% en inglés claro y cero jerga técnica en pantalla.
  * **Estándar de Internacionalización (i18n en Nuxt 4):** Catálogo configurado en `@nuxtjs/i18n` v9 mediante archivo TypeScript nativo con la macro oficial `defineI18nLocale` en `frontend/i18n/locales/en.ts` (convención `restructureDir: "i18n"`). **Prohibido el uso de catálogos `.json` planos** en tiempo de desarrollo/build para evitar colisiones con el compilador/transformador de Vite 6 (`EnvironmentPluginContainer.transform`).
  * **Exposición en Red Local (LAN / Cabina):** Bloque `devServer: { host: '0.0.0.0', port: 3000 }` para acceso multi-dispositivo de los tripulantes/testers sin restricciones de loopback.
* **Tailwind CSS 4 + Paleta Oficial de 6 Colores en Variables CSS (`frontend/app/assets/css/tokens.css`)** `[núcleo]`
  * Fidelidad visual exacta al diseño en Figma (`#001524`, `#15616D`, `#FFECD1`, `#2AEF4B`, `#000C5C`, `#D5110B`) y alto contraste (`15.6:1` AAA); la conmutación al **Modo Alerta Crítica** se activa cambiando `data-cabin-mode="critical"` en `<html>`.
* **Reka UI (Componentes accesibles sin estilo preimpuesto) + `<HudWindow>`** `[núcleo]`
  * Contenedor universal con esquinas angulares de precisión y primitivas `TabsRoot`, `DialogRoot`, `SelectRoot` con el aspecto exacto del Figma.
* **Apache ECharts (`vue-echarts`) con Tema Propio `'spacescan-hud'`** `[núcleo]`
  * Usa `CanvasRenderer`, `animation: false` y muestreo `lttb` en ondas continuas (`ECG`, fonocardiograma `S1/S2`) para fluidez en CPU; serie `type: 'custom'` para la gráfica de barra de cintas de fases de sueño (`Awake`, `REM`, `Light`, `Deep`).
* **SVG Exportado del Figma + CSS (Brillo y línea de barrido)** `[núcleo]`
  * Representación holográfica de cuerpo humano y órganos (`SpaceScanHologram.vue`).
  * **Motion for Vue (`motion-v`)** `[extra]` para micro-transiciones; **TresJS (Three.js)** `[extra]` para visualización corporal 3D opcional (`.glb` local).
* **Pinia + VueUse** `[núcleo]`
  * Gestión de sesión autenticada por PIN, estado reactivo de cabina y utilidades nativas (temporizadores, acceso a micrófono).
* **`@nuxt/fonts` (`Inter` + `JetBrains Mono` en `.woff2`) + `@nuxt/icon` (colección local `spacescan` con 16 SVGs)** `[núcleo]`
  * Fuentes e iconos 100% autoalojados (`provider: 'local'` y `clientBundle: { scan: true }`) para garantizar cero peticiones externas.
* **Web Audio API + MediaRecorder (Nativo del navegador)** `[núcleo]`
  * Medidor de nivel de ruido ambiental de cabina en tiempo real y grabación acústica de 30 segundos para auscultación cardíaca y pulmonar.
* **Zod** `[núcleo]`
  * Validación de esquemas en formularios de captura clínica antes del envío al backend.
* **`@vite-pwa/nuxt`** `[extra]`
  * Empaquetado instalable en tablet con caché local para su reutilización en clínicas rurales con conectividad intermitente.

---

## 2. Backend (`backend/`)

* **Python 3.13 + FastAPI + Pydantic v2 + Uvicorn** `[núcleo]`
  * API REST tipada con generación automática de especificación OpenAPI; arquitectura modular con un archivo router por módulo (`backend/app/routers/<modulo>.py`).
  * **Matriz Oficial de Puertos en Desarrollo Local:**
    * **`Puerto 8000`:** Reservado para la Torre de Control interna (`miWork/server.py`).
    * **`Puerto 8080`:** Servidor FastAPI + SSE (`backend/app/main.py`) para evitar colisiones de enlace (`[Errno 48] Address already in use`).
    * **`Puerto 3000`:** Frontend Nuxt 4 en modo desarrollo (`frontend/`).
  * **Política de CORS para Red Local:** `CORSMiddleware` configurado con expresión regular (`allow_origin_regex = r"^https?://(localhost|127\.0\.0\.1|192\.168\.\d+\.\d+|10\.\d+\.\d+\.\d+)(:\d+)?$"`) para permitir conexiones seguras desde cualquier cliente LAN/Wi-Fi en cabina.
  * **Empaquetado Estándar (`pyproject.toml` con `setuptools`):** Declaración explícita de `[build-system]` (`setuptools.build_meta`) y `[tool.setuptools.packages.find]` (`include = ["app*", "db*"]`) para resolver la detección de paquetes en estructuras planas (*flat-layout*) al instalar en modo editable (`pip install -e .`).
* **`sqlite3` (Librería estándar) con consultas SQL parametrizadas** `[núcleo]`
  * `backend/db/schema.sql` actúa como única fuente de verdad del modelo de datos, evitando que un ORM duplique o desincronice el esquema.
* **`argon2-cffi` + `PyJWT`** `[núcleo]`
  * Hash criptográfico del PIN de 4 dígitos, emisión de sesiones firmadas y protección contra intentos fallidos.
* **Server-Sent Events (SSE)** `[núcleo]`
  * Canal unidireccional ligero para empujar alertas clínicas y lecturas de sensores en vivo hacia la interfaz sin la sobrecarga de WebSockets.
* **APScheduler** `[núcleo]`
  * Programador en segundo plano para chequeos periódicos (*Routine Prompts*), gestión de horario silencioso (*Quiet Hours*) y procesamiento de la cola *store-and-forward* hacia Control a tierra con simulación de latencia espacial (inspirada en *Delay-Tolerant Networking - DTN*).
* **`httpx` (Script `seed.py` de precarga pre-misión)** `[núcleo]`
  * Descarga datasets espaciales reales (OSDR/GeneLab, DONKI) **antes del despegue** para poblar la base de datos local que viaja a bordo.
* **Simulador de Sensores en Python** `[núcleo]`
  * Reproduce series temporales reales y simuladas para alimentar el flujo continuo durante la demostración en vivo.
* **Inferencia Local de IA (`ONNX Runtime` + `Ollama` / `llama.cpp`)** `[núcleo]`
  * **Red Neuronal Convencional (Autoencoder / LSTM en ONNX Runtime):** Detección ligera en CPU de anomalías multivariadas frente a la línea base personal.
  * **LLM Local (`Ollama` / `llama.cpp`):** Explicación clínica orientativa en inglés claro y sugerencias preventivas sujetas a validación del `Médico`.

---

## 3. Base de Datos (`backend/db/schema.sql`)

* **SQLite 3** `[núcleo]`
  * Base de datos transaccional embebida en un único archivo (`scan.db`), sin proceso de servidor externo, resiliente ante cortes eléctricos o reinicios (estándar en sistemas aeroespaciales y embebidos).
  * **Configuración de Integridad (RNF 5):** Modo **WAL** (*Write-Ahead Logging*), `PRAGMA foreign_keys = ON`, tablas declaradas como `STRICT` y disparadores (*triggers*) **append-only** sobre la tabla `measurements` que impiden cualquier `UPDATE` o `DELETE` de registros históricos.
  * **SQLite FTS5:** Motor de búsqueda de texto completo (*Full-Text Search*) local para consultar protocolos y síntomas en la Wiki médica sin conexión.
  * **SQLite JSON1:** Construcción y exportación de paquetes médicos de sincronización en formato JSON estándar.
* **Almacenamiento de Muestras de Auscultación** `[núcleo]`
  * Los archivos de audio (`.webm` / `.wav` de 30 s) se resguardan en disco local; la tabla `auscultation_samples` almacena únicamente la ruta relativa y su huella de integridad **SHA-256**.

---

## 4. Calidad de Software, Pruebas y Licencia

* **`uv` + `Ruff` + `pytest` (Python)** y **`@nuxt/eslint` + `Vitest` (Nuxt)** `[núcleo]`
  * Gestión determinista de dependencias, formateo/linting estático y pruebas unitarias/integración de API.
* **`openapi-typescript`** `[núcleo]`
  * Generación automática de interfaces TypeScript en el frontend a partir del esquema OpenAPI de FastAPI para impedir desincronizaciones de contrato.
* **Playwright** `[extra]`
  * Pruebas *end-to-end* del flujo crítico: `Login con PIN → Captura → Alerta → Notificación → Protocolo Wiki → Paquete a Tierra`.
* **Licencia MIT en Repositorio Público** `[núcleo]`

---

## 5. Trazabilidad Tecnológica frente a los 10 Premios Globales

| # | Categoría de Premio | Tecnología y Diseño que lo Sostiene en SpaceScan |
| :--- | :--- | :--- |
| **1** | **Best Use of Data** | `seed.py` + `httpx` precargando datos de OSDR/GeneLab y DONKI; visualizaciones claras en Apache ECharts; exportación JSON estándar. |
| **2** | **Best Use of Science** | Tabla `metric_catalog` con rangos clínicos y fuentes científicas; cálculo de *z-score* contra línea base (`baselines`); LLM que referencia protocolos de la Wiki. |
| **3** | **Best Use of Technology** | Inferencia dual 100% offline: Red Neuronal en ONNX Runtime para series temporales + LLM local con Ollama/llama.cpp. |
| **4** | **Best Use of Storytelling** | Segmentación nativa por etapa (`Despegue / Misión / Regreso`) en cada medición + gráficas comparativas longitudinales + simulador en vivo para la demo. |
| **5** | **Best Mission Concept** | SQLite en archivo único con triggers *append-only*, cola asíncrona tipo DTN con latencia simulada, inferencia en CPU sin GPU dedicada. |
| **6** | **Galactic Impact** | Arquitectura offline autónoma (SPA servida por FastAPI + PWA/Docker) directamente transferible a telemedicina en zonas extremas de la Tierra. |
| **7** | **Global Connection** | Interfaz estandarizada 100% en inglés, repositorio público bajo licencia MIT, contratos OpenAPI y paquetes médicos en JSON estándar. |
| **8** | **Local Impact** | Ejecución sin internet y con bajo consumo de hardware, ideal para clínicas rurales o brigadas médicas desconectadas. |
| **9** | **Most Inspirational** | Sistema de rachas (`streak_days`), seguimiento psicológico de ánimo/soledad/motivación, *Quiet Hours* y prueba cognitiva interactiva. |
| **10** | **Art & Technology** | Variables CSS sincronizadas con tokens de Figma, hologramas corporales en SVG/CSS, tema holográfico en ECharts y modo visual de alerta. |
