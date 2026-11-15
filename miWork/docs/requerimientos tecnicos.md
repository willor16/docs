**Regla:** todo corre **a bordo y sin internet** (RNF 1). Cero CDNs y cero APIs en la nube en tiempo de ejecución: fuentes, iconos, modelos y datos de NASA van dentro del proyecto.
> **[núcleo]** = obligatorio para la demo · **[extra]** = solo si sobra tiempo.

### frontend
- **Nuxt 4 (Vue 3 + TypeScript estricto), modo SPA (`ssr: false`)** [núcleo] — se genera estático y lo sirve el mismo backend: una sola pieza a bordo, un solo puerto.
- **Tailwind CSS 4 + tokens del Figma como variables CSS** (`assets/css/tokens.css`) [núcleo] — fidelidad al diseño y alto contraste; el modo "alerta" rojo es solo cambiar variables.
- **Reka UI** (componentes sin estilo, accesibles) [núcleo] — diálogos, pestañas y selectores con el aspecto exacto del Figma, sin pelear contra estilos ajenos.
- **Apache ECharts (`vue-echarts`)** [núcleo] — barras, áreas, gauges radiales y ondas (ECG, fonocardiograma) con un tema holográfico propio.
- **SVG exportado del Figma + CSS (brillo, líneas de escaneo)** [núcleo] — hologramas de cuerpo y órganos. **Motion for Vue (`motion-v`)** [extra] para transiciones; **TresJS (Three.js)** [extra] si se quiere el cuerpo en 3D.
- **Pinia + VueUse** [núcleo] — sesión, estado y utilidades (temporizadores, micrófono).
- **@nuxt/fonts + @nuxt/icon con colecciones locales** [núcleo] — fuentes e iconos autoalojados.
- **Web Audio API + MediaRecorder** (nativo del navegador) [núcleo] — medidor de ruido ambiente y grabación de 30 s de auscultación.
- **Zod** [núcleo] — validación de los formularios de captura antes de enviar.
- **@vite-pwa/nuxt** [extra] — instalable en tablet y con caché; es lo que permite reusarla en clínicas con internet intermitente.

### backend
- **Python 3.13 + FastAPI + Pydantic v2 + Uvicorn** [núcleo] — API tipada con OpenAPI automático; un router por módulo.
- **`sqlite3` (librería estándar) con consultas parametrizadas** [núcleo] — `backend/db/schema.sql` es la única fuente de verdad; sin ORM que la duplique.
- **argon2-cffi + PyJWT** [núcleo] — PIN cifrado, sesión firmada y bloqueo tras intentos fallidos.
- **Server-Sent Events (SSE)** [núcleo] — alertas y lecturas de sensores en vivo hacia la pantalla; más simple que WebSocket.
- **APScheduler** [núcleo] — chequeos programados, Quiet Hours y la cola *store-and-forward* hacia Control a tierra con latencia simulada (inspirada en la red tolerante a retardos, DTN, de NASA).
- **httpx** [núcleo] — `seed.py` descarga datos reales de NASA (OSDR/GeneLab, DONKI) **antes del despegue**; a bordo quedan guardados en la base.
- **Simulador de sensores en Python** [núcleo] — reproduce series reales y simuladas como si llegaran de los sensores.

### db
- **SQLite 3** [núcleo] — un solo archivo, sin servidor, resistente a cortes y reinicios; es la base usada en software embebido y aeroespacial.
  - Modo **WAL**, `foreign_keys = ON`, tablas `STRICT` y disparadores *append-only* en `measurements` (RNF 5).
  - **FTS5** — búsqueda de texto completo en la Wiki médica, sin internet.
  - **JSON1** — paquetes de sincronización y exportación en JSON estándar.
- **Audio de auscultación en disco** (WebM/WAV) [núcleo] — en la base solo la ruta y su hash SHA-256.

### frameworks y calidad
- **uv + Ruff + pytest** (Python) y **@nuxt/eslint + Vitest** (Nuxt) [núcleo] — entorno reproducible, formato y pruebas.
- **openapi-typescript** [núcleo] — los tipos del frontend se generan del OpenAPI del backend; el contrato no se desincroniza.
- **Playwright** [extra] — prueba del flujo completo: login → captura → alerta → notificación → Wiki → paquete a Tierra.
- **Licencia MIT en repo público** [núcleo].
### Qué premio cubre cada tecnología
| # | Premio | Tecnología que lo sostiene |
|---|---|---|
| 1 | Best Use of Data | `seed.py` + httpx con OSDR/GeneLab y DONKI; ECharts para mostrarlos claros; exportación JSON |
| 2 | Best Use of Science | `metric_catalog` con rango y fuente; z-score contra línea base; comparación de modelos; LLM que cita la Wiki |
| 3 | Best Use of Technology | Red neuronal en ONNX Runtime + LLM local con Ollama, todo sin conexión |
| 4 | Best Storytelling | Etapa (Despegue / Misión / Regreso) en cada dato + gráficas comparativas + simulador para la demo en vivo |
| 5 | Best Mission Concept | SQLite en un archivo, cola con latencia tipo DTN, inferencia en CPU, equipo pequeño |
| 6 | Galactic Impact | PWA offline + Docker: la misma app sirve para telemedicina remota |
| 7 | Global Connection | @nuxtjs/i18n, repo público MIT, OpenAPI y JSON estándar |
| 8 | Local Impact | Funciona sin internet y en equipo barato: centros de salud rurales |
| 9 | Most Inspirational | Rachas, test psicológico y prueba cognitiva como mini juego (Vue + Motion) |
| 10 | Art & Technology | Tokens del Figma, hologramas SVG/3D, tema ECharts propio, modo alerta |