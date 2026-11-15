# Estándar Global de Diseño UI/UX y Guía Maestra de Construcción (`Scan Space · ARES VII`)

> **Propósito de este Documento:** Ser la **única fuente de verdad de diseño e implementación** para cualquier desarrollador del equipo. Define qué reglas visuales son obligatorias, la paleta exacta de 6 colores, el uso estricto del idioma inglés sin jerga técnica, y cómo se construye cada módulo del stack **[núcleo]** y **[extra]** cumpliendo la regla **100% a bordo y sin internet (RNF 1)**.
>
> **Diseño Maestro en Figma (Fuente Oficial ante Cualquier Duda Visual, Medidas o Exportación de SVGs):**
> - **Figma Oficial del Proyecto:** [SpaceScan — Figma Design (`node-id=7382-2`)](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2&t=tzbC2RhJeGZ2Dlov-1) *(Todo desarrollador debe guiarse directamente de este archivo de Figma ante cualquier detalle de espaciado, proporción, iconografía o estados visuales).*
> - Recursos vectoriales exportados en el repositorio (`16` pantallas `1568 × 940`): `frontend/app/assets/hologram/` (`body_scan.svg`, `body_small.svg`, `brain.svg`, `heart.svg`, `lungs.svg`, `logo.svg`) y `frontend/app/assets/icons/spacescan/`.

---

## 0. Análisis de Viabilidad y Decisiones Técnicas Clave del Stack

Para mantener coherencia total entre todas las piezas solicitadas (**Nuxt 4 + Tailwind CSS 4 + Reka UI + ECharts + Python 3.13 + FastAPI + SQLite 3 STRICT**):

1. **Arquitectura Unificada de Borde (Un Solo Proceso, Un Solo Puerto, Cero Nube — `RNF 1`):**
   - `Nuxt 4` compila en modo estático (`ssr: false`) y `FastAPI` sirve tanto los archivos estáticos del SPA como la API REST y el canal `SSE` desde un único puerto local (`8080`), sin depender de servidores externos, CDNs ni ORM (`backend/db/schema.sql` es la única verdad con `sqlite3` parametrizado).
2. **Conciliación entre Regla *"Solo Inglés en UI"* y `@nuxtjs/i18n` (Premio *Global Connection*):**
   - Toda la interfaz debe mostrarse **100% en inglés (`en`)**, sin mezclar español/inglés en ningún componente. En `@nuxtjs/i18n` se fija `defaultLocale: 'en'` centralizando las cadenas en `frontend/i18n/locales/en.ts` mediante `defineI18nLocale`, manteniendo la experiencia visual de cabina estrictamente en inglés.
3. **Fluidez de `Apache ECharts` en Ondas de Tiempo Real (`ECG` y Fonocardiograma):**
   - Para evitar carga excesiva de CPU en hardware económico o desconectado, `vue-echarts` debe usar **`CanvasRenderer`**, desactivar animaciones (`animation: false`) en ondas continuas y aplicar muestreo `lttb` al refrescar trazos provenientes de `SSE` o `Web Audio API`.

---

## 1. Las 5 Leyes Inquebrantables de Diseño y Producto

Cualquier componente o pantalla nueva que viole una sola de estas 5 leyes debe rechazarse en revisión de código:

1. **RNF 1 — Cero Red Exterior en Tiempo de Ejecución (`100% Onboard & Air-Gapped`):**
   - Prohibido usar `<link href="https://fonts.googleapis.com...">`, CDNs (`unpkg`, `jsdelivr`), iconos remotos de Iconify o llamadas a APIs en la nube (`OpenAI`, `Gemini`, `NASA API`) mientras corre la app. Fuentes `.woff2`, iconos SVG, datasets `OSDR/DONKI`, modelos `.onnx` y pesos de `Ollama` viven **dentro del contenedor/disco local**.
2. **Idioma 100% Inglés Puro y Cero Jerga Tecnológica en Pantalla:**
   - **Todo texto visible va en inglés claro y humano** (`Sign In`, `Sleep Score`, `Right Eye Elevated`, `Save Lung Recording`).
   - **Prohibido mostrar nombres de tecnologías, formatos o protocolos internos en la UI:** nunca escribir en pantalla palabras como `SQLite`, `JSON`, `FHIR`, `HL7`, `Kiwix`, `ZIM`, `FTS5`, `WAL`, `Offline`, `Break-Glass`, `DTN`, `OSDR`, `DONKI`, `ONNX`, `Ollama`, `Nuxt` o `Python`. Esos conceptos operan bajo el capó; el astronauta solo ve información clínica y operativa limpia.
3. **Separación Estricta entre Vistas de Resultados y Módulo de Captura (`Capture`):**
   - Las pantallas de monitoreo clínico (`Profile`, `Sleep`, `Vision`, `Auscultation`, `Crew Overview`, `Crew Streaks`) son **100% de solo lectura (Solo Resultados)**: cero inputs, cero selectores de ánimo y cero botones `+ Log` incrustados.
   - Toda entrada manual, grabación de audio cardíaco/pulmonar de `30 s` o prueba psicomotriz vive **exclusivamente** dentro del módulo **`Capture`** dividido en sus 4 sub-pestañas (`Auscultation Audio · Physical & Labs · Vision & Ocular · Psych, Motor & Sleep`).
4. **Jerarquía de Navegación en 2 Niveles (`Profile` al Centro · `Notifications` Solo en Header):**
   - **Nivel 1 Público (sin PIN):** `Sign In` (`01`), `Crew Overview` (`02`) y `Crew Streaks` (`03`) comparten la misma barra inferior pública de 3 pestañas (`Sign In · Crew Overview · Crew Streaks`). En `Sign In`, el acceso personal es **solo por PIN de 4 dígitos** (sin correo ni contraseña) y existen dos botones externos directos a las vistas públicas.
   - **Nivel 2 Autenticado (tras PIN):** Barra inferior trapezoidal **simétrica de 7 módulos** con **`Profile` elevado exactamente al centro**:
     `1 Vision · 2 Sleep · 3 Auscultation · [4 PROFILE — Principal Central] · 5 Capture · 6 Guide · 7 Comms`.
   - **`Notifications (N)` nunca va en el menú inferior:** vive **únicamente en el header superior** de las vistas autenticadas.
5. **Densidad Controlada (Cero Saturación Visual):**
   - Máximo `2` o `3` contenedores `HudWindow` por pantalla, márgenes exteriores de `28 px`, separación entre ventanas de `18 px`, cero pies de página (*footers*) informativos y cero textos explicativos redundantes.

---

## 2. Paleta Oficial de 6 Colores y Tokens Globales (`assets/css/tokens.css`)

Ningún desarrollador debe escribir códigos hexadecimales sueltos en componentes Vue. Todo color se consume desde variables CSS definidas en `frontend/app/assets/css/tokens.css` e integradas en **Tailwind CSS 4**.

### 2.1 Tabla Maestra de la Paleta Oficial

| # | Rol Semántico | Hex Oficial | Variable CSS | Regla de Uso Obligatoria |
| :-: | :--- | :---: | :--- | :--- |
| **1** | **Fondo Principal** | `#001524` | `--color-bg-base` | Fondo oceánico profundo de toda la aplicación (base del degradado multicapa). |
| **2** | **Tarjetas y Botones** | `#15616D` | `--color-surface-card` | Color único para tarjetas *smoked-glass*, cabeceras de ventana, botones y halo radial inferior. |
| **3** | **Texto e Iconos** | `#FFECD1` | `--color-text-primary` | Color único de tipografía, cifras tabulares e iconografía principal (`15.6:1` AAA sobre `#001524`). |
| **4** | **Estado OK / Nominal** | `#2AEF4B` | `--color-status-ok` | Valores óptimos, ondas sanas (`ECG`, fonocardiograma `S1/S2`, `CO₂`), sueño `Deep` y metas cumplidas. |
| **5** | **Selección de Menú / Guías / Pastillas / Warning** | `#000C5C` *(baja opacidad)* | `--color-menu-select` / `--color-status-warn` | **1)** Selección activa exclusiva en menús y filtros (`30%–52%` opacidad). **2)** Líneas guía y bandas meta en gráficas. **3)** Pastillas pequeñas de referencia (`OPTIMAL`, `Positive`, `Low`). **4)** Nivel *Warning* intermedio. |
| **6** | **Estado Crítico / Alerta** | `#D5110B` | `--color-status-critical` | Desviaciones críticas fuera de umbral, despertares (`Awake`), avisos urgentes y modo alerta global. |

### 2.2 Implementación Exacta en `frontend/app/assets/css/tokens.css` (Tailwind CSS 4 + Modo Alerta)

Cambiar toda la cabina a **Modo Alerta Rojo** (Premio *Art & Technology*) no requiere condicionales en los componentes: basta alternar `data-cabin-mode="critical"` en `<html>` para conmutar las variables del resplandor de horizonte y bordes.

```css
/* frontend/app/assets/css/tokens.css */
@import "tailwindcss";

:root {
  /* === 6 COLORES OFICIALES === */
  --color-bg-base: #001524;
  --color-surface-card: #15616D;
  --color-text-primary: #FFECD1;
  --color-status-ok: #2AEF4B;
  --color-navy-accent: #000C5C;
  --color-status-critical: #D5110B;

  /* === DERIVADOS TONALES DE SOPORTE (MISMA FAMILIA CROMÁTICA) === */
  --color-bg-top: #00101C;
  --color-bg-bottom: #062838;
  --color-surface-inset: rgba(4, 30, 46, 0.72);     /* #041E2E para cajas de gráficas e inputs */
  --color-border-card: rgba(21, 97, 109, 0.78);
  --color-border-hi: #25899B;
  --color-rem-accent: #2994A6;                      /* Diferenciación de fase REM derivada de #15616D */
  --color-navy-edge: #263BB0;                       /* Filete de 1px (232°) para legibilidad de #000C5C */
  --color-text-secondary: #F2DEC0;
  --color-text-muted: #C8B69C;
  --color-text-dim: #968976;

  /* === SUPERFICIES DINÁMICAS (CAMBIAN AUTOMÁTICAMENTE EN MODO ALERTA) === */
  --horizon-glow-core: rgba(21, 97, 109, 0.86);
  --horizon-glow-mid: rgba(12, 67, 80, 0.58);
  --upper-glow: rgba(21, 97, 109, 0.34);
  --window-frame-stroke: var(--color-border-card);
}

/* MODO ALERTA CRÍTICA: se activa con document.documentElement.dataset.cabinMode = 'critical' */
:root[data-cabin-mode="critical"] {
  --horizon-glow-core: rgba(122, 22, 18, 0.88);
  --horizon-glow-mid: rgba(61, 18, 24, 0.60);
  --upper-glow: rgba(213, 17, 11, 0.26);
  --window-frame-stroke: rgba(213, 17, 11, 0.85);
}

@theme {
  --color-cabin-bg: var(--color-bg-base);
  --color-cabin-card: var(--color-surface-card);
  --color-cabin-inset: var(--color-surface-inset);
  --color-cabin-text: var(--color-text-primary);
  --color-cabin-ice: var(--color-text-secondary);
  --color-cabin-muted: var(--color-text-muted);
  --color-cabin-ok: var(--color-status-ok);
  --color-cabin-navy: var(--color-navy-accent);
  --color-cabin-navy-edge: var(--color-navy-edge);
  --color-cabin-crit: var(--color-status-critical);

  --font-sans: "Inter", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", monospace;
}

/* Lienzo global con el degradado multicapa exacto del Figma */
.cockpit-canvas {
  background-color: var(--color-bg-base);
  background-image:
    radial-gradient(66% 52% at 50% 86%, var(--horizon-glow-core) 0%, var(--horizon-glow-mid) 38%, rgba(3, 31, 47, 0.28) 74%, transparent 100%),
    radial-gradient(55% 32% at 50% 12%, var(--upper-glow) 0%, transparent 100%),
    linear-gradient(180deg, var(--color-bg-top) 0%, var(--color-bg-base) 52%, var(--color-bg-bottom) 100%);
  color: var(--color-text-primary);
  font-family: var(--font-sans);
  font-variant-numeric: tabular-nums;
}

/* Selección exclusiva de menús, sub-pestañas y filtros (#000C5C con baja opacidad) */
.menu-item-active {
  background: linear-gradient(180deg, rgba(0, 12, 92, 0.30) 0%, rgba(0, 12, 92, 0.52) 100%);
  border: 1.3px solid rgba(38, 59, 176, 0.82);
}
```

---

## 3. Reglas Tipográficas, Iconográficas y Geométricas

1. **Fuentes Locales (`@nuxt/fonts` — `[núcleo]`):**
   - Colocar los archivos `.woff2` en `frontend/public/fonts/` (`Inter-Regular.woff2`, `Inter-SemiBold.woff2`, `Inter-Bold.woff2`, `JetBrainsMono-Medium.woff2`, `JetBrainsMono-Bold.woff2`).
   - Configurar `@nuxt/fonts` con `provider: 'local'` para cero descargas externas.
   - **Uso:** `Inter` para títulos, etiquetas clínicas y navegación; `JetBrains Mono` (`tabular-nums`) obligatorio en relojes `UTC`, duraciones (`7h 12m`), intervalos (`22:54–23:36`), ejes numéricos y cronómetros (`00:18 / 00:30 SEC`).
2. **Iconos Locales (`@nuxt/icon` — `[núcleo]`):**
   - Guardar los iconos vectoriales del Figma en `frontend/app/assets/icons/spacescan/` (`rocket.svg`, `sans.svg`, `moon.svg`, `stethoscope.svg`, `profile.svg`, `capture.svg`, `wiki.svg`, `earth.svg`, `bell.svg`, `mic.svg`, `lock.svg`, `flame.svg`, `vitruvian.svg`, `reticle.svg`, `kit.svg`, `shield.svg`).
   - Registrar colección personalizada `spacescan` en `nuxt.config.ts` (`clientBundle: { scan: true }`) para empaquetarlos dentro del bundle estático.
3. **Proporciones de Pantalla (`1568 × 940` Escalable):**
   - **Top Header (`TopTelemetryBar.vue`):** altura fija `56 px`, fondo `rgba(0, 21, 36, 0.86)`, reloj `MISSION CLOCK`, botón `Notifications (N)` (`x=1166` relativo / alineado a la derecha antes del estado de cabina) y pastilla global de estado (`CABIN NOMINAL` / `SCORE 84 · OPTIMAL`).
   - **Sub-barra de Pestañas o Filtros (`36 px` de alto):** usada solo en `Profile` (3 pestañas), `Sleep` (4 filtros de tiempo), `Capture` (4 categorías) y `Notifications` (3 filtros).
   - **Bottom Dock Autenticado (`BottomCockpitDock.vue`, `72 px` de alto):**
     - Izquierda: tarjeta de sesión activa (`ID·01 · E. VARGAS`).
     - Centro trapezoidal simétrico (`7` ranuras): `1 Vision` (`138 px`), `2 Sleep` (`138 px`), `3 Auscultation` (`138 px`), **`4 Profile` (`192 px`, elevado `+8 px` por encima del trapecio en el centro exacto)**, `5 Capture` (`138 px`), `6 Guide` (`138 px`), `7 Comms` (`138 px`).
     - Derecha: botón `Sign Out` en `#15616D`.

---

## 4. Cómo Construir Cada Componente y Tecnología (Con Ejemplos Reales)

### 4.1 Contenedor Universal `HudWindow.vue` + `Reka UI` (`[núcleo]`)

Todo módulo visual va envuelto en `<HudWindow>` y usa primitivas sin estilo de **`reka-ui`** (`TabsRoot`, `DialogRoot`, `SelectRoot`) para accesibilidad por teclado sin romper el diseño del Figma:

```vue
<!-- frontend/app/components/shell/HudWindow.vue -->
<script setup lang="ts">
withDefaults(defineProps<{
  title?: string
  subtitle?: string
  tagText?: string
  tagTone?: 'reference' | 'warn' | 'critical'
  icon?: string
}>(), {
  tagTone: 'reference',
})
</script>

<template>
  <section
    class="relative rounded-[6px] bg-cabin-card/28 border flex flex-col overflow-hidden"
    :style="{ borderColor: 'var(--window-frame-stroke)' }"
  >
    <!-- Esquinas angulares de precisión de 8px (#FFECD1 al 44%) -->
    <span class="pointer-events-none absolute top-0 left-0 w-2 h-2 border-t-[1.4px] border-l-[1.4px] border-cabin-text/45" />
    <span class="pointer-events-none absolute top-0 right-0 w-2 h-2 border-t-[1.4px] border-r-[1.4px] border-cabin-text/45" />
    <span class="pointer-events-none absolute bottom-0 left-0 w-2 h-2 border-b-[1.4px] border-l-[1.4px] border-cabin-text/45" />
    <span class="pointer-events-none absolute bottom-0 right-0 w-2 h-2 border-b-[1.4px] border-r-[1.4px] border-cabin-text/45" />

    <header
      v-if="title"
      class="px-4 py-2.5 bg-cabin-card/58 border-b border-cabin-text/18 flex items-center justify-between gap-3"
    >
      <div class="flex items-center gap-2.5">
        <div
          v-if="icon"
          class="w-[22px] h-[22px] rounded-[4px] bg-[#062534]/90 border border-[#25899B]/70 flex items-center justify-center"
        >
          <Icon :name="`spacescan:${icon}`" class="w-3.5 h-3.5 text-cabin-text" />
        </div>
        <div>
          <h2 class="text-[12.5px] font-bold tracking-[0.03em] uppercase text-cabin-text">{{ title }}</h2>
          <p v-if="subtitle" class="text-[10.5px] text-cabin-muted">{{ subtitle }}</p>
        </div>
      </div>

      <!-- Pastilla pequeña de referencia siempre en #000C5C translúcido salvo alerta crítica -->
      <span
        v-if="tagText"
        class="px-3 h-[22px] rounded-full text-[9.8px] font-semibold tracking-[0.03em] inline-flex items-center gap-1.5 border"
        :class="{
          'bg-cabin-navy/42 border-cabin-navy-edge/70 text-cabin-text': tagTone === 'reference',
          'bg-cabin-navy/55 border-cabin-navy-edge/90 text-cabin-text': tagTone === 'warn',
          'bg-cabin-crit/25 border-cabin-crit/85 text-cabin-text': tagTone === 'critical',
        }"
      >
        <i v-if="tagTone === 'warn'" class="w-1.5 h-1.5 rounded-full bg-cabin-navy-edge" />
        {{ tagText }}
      </span>
    </header>

    <div class="p-5 flex-1">
      <slot />
    </div>
  </section>
</template>
```

**Ejemplo de Pestañas (`SubnavTabs.vue`, `CaptureTabs.vue` y `ProfileTabs.vue`):**
```vue
<script setup lang="ts">
import { TabsList, TabsRoot, TabsTrigger } from 'reka-ui'

const activeTab = defineModel<string>({ default: 'auscultation' })
const tabs = [
  { id: 'auscultation', label: 'Auscultation Audio' },
  { id: 'physical', label: 'Physical & Labs' },
  { id: 'vision', label: 'Vision & Ocular' },
  { id: 'psych-sleep', label: 'Psych, Motor & Sleep' },
]
</script>

<template>
  <TabsRoot v-model="activeTab">
    <TabsList class="flex items-center gap-2">
      <TabsTrigger
        v-for="tab in tabs"
        :key="tab.id"
        :value="tab.id"
        class="relative h-9 px-6 rounded-[4px] text-[11.2px] transition-colors bg-cabin-inset border border-cabin-card/60 text-cabin-text/80 data-[state=active]:menu-item-active data-[state=active]:font-extrabold data-[state=active]:text-cabin-text"
      >
        {{ tab.label }}
      </TabsTrigger>
    </TabsList>
  </TabsRoot>
</template>
```

---

### 4.2 Tema Holográfico Propio en `Apache ECharts` (`vue-echarts` — `[núcleo]`)

Todas las gráficas de la aplicación (arcos `Sleep Score` / `Crew Score`, curva bilateral `Vision`, tendencia `CO₂`, ondas `ECG`/fonocardiograma y **gráfica de barra de cintas de fases de sueño**) deben usar el tema registrado `'spacescan-hud'` para garantizar que las líneas guía sean `#000C5C` / `#263BB0`, las etiquetas `#C8B69C` y los trazos `#2AEF4B` / `#D5110B`:

```ts
// frontend/app/plugins/echarts.client.ts
import { registerTheme, use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { BarChart, CustomChart, GaugeChart, LineChart } from 'echarts/charts'
import { GridComponent, MarkAreaComponent, MarkLineComponent, TooltipComponent } from 'echarts/components'

export default defineNuxtPlugin(() => {
  use([CanvasRenderer, LineChart, BarChart, GaugeChart, CustomChart, GridComponent, TooltipComponent, MarkLineComponent, MarkAreaComponent])

  registerTheme('spacescan-hud', {
    backgroundColor: 'rgba(4, 30, 46, 0.72)', // #041E2E inset
    textStyle: {
      fontFamily: "'JetBrains Mono', monospace",
      color: '#FFECD1',
    },
    color: ['#2AEF4B', '#2994A6', '#263BB0', '#D5110B'],
    categoryAxis: {
      axisLine: { lineStyle: { color: '#15616D' } },
      axisLabel: { color: '#C8B69C', fontSize: 10 },
      splitLine: { show: true, lineStyle: { color: 'rgba(38, 59, 176, 0.42)', width: 1 } }, // Guía #000C5C legible
    },
    valueAxis: {
      axisLine: { show: false },
      axisLabel: { color: '#C8B69C', fontSize: 10 },
      splitLine: { show: true, lineStyle: { color: 'rgba(38, 59, 176, 0.42)', width: 1 } },
    },
    tooltip: {
      backgroundColor: '#041E2E',
      borderColor: '#25899B',
      textStyle: { color: '#FFECD1', fontSize: 11 },
    },
  })
})
```

- **Cómo construir la Gráfica de Barra de Cintas de Sueño (`07_Sleep_Monitor.svg`):** Usar `type: 'custom'` en ECharts (`renderItem` dibuja un `rect` redondeado `[startUtcMin, endUtcMin, stageIndex]` con `#D5110B` para `Awake`, `#2994A6` para `REM`, `#263BB0` para `Light` y `#2AEF4B` para `Deep`, más la pista continua inferior en `stageIndex = 0`).
- **Cómo construir Ondas `ECG` y Fonocardiograma (`06`, `09`, `10`):** Serie `type: 'line'`, `showSymbol: false`, `animation: false`, `sampling: 'lttb'`, `lineStyle: { color: '#2AEF4B', width: 2 }`.

---

### 4.3 Hologramas SVG del Figma (`HoloFigure.vue` — `[núcleo]`) y 3D (`[extra]`)

Extraer los vectores limpios del cuerpo y órganos (`body_scan.svg`, `body_small.svg`, `heart.svg`, `lungs.svg`, `brain.svg`, `logo.svg`) hacia `frontend/app/assets/hologram/` y renderizarlos mediante `frontend/app/components/ui/HoloFigure.vue`:

```css
/* Brillo holográfico y línea de escaneo vertical sin dependencias externas */
.hologram-shell {
  filter: drop-shadow(0 0 12px rgba(42, 239, 75, 0.22));
}
.hologram-scanline::after {
  content: "";
  position: absolute;
  inset-inline: 12%;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(42, 239, 75, 0.65), transparent);
  animation: scan-sweep 4.5s ease-in-out infinite;
}
@keyframes scan-sweep {
  0%, 100% { top: 10%; opacity: 0.25; }
  50% { top: 88%; opacity: 0.85; }
}
```
> **[extra]:** Si sobra tiempo, envolver transiciones de entrada de tarjetas con `motion-v` (`<Motion :initial="{ opacity: 0, y: 6 }" :animate="{ opacity: 1, y: 0 }">`) y habilitar una vista opcional 3D en `04_Profile_Personal_Data` con `TresJS` cargando un `.glb` local desde `public/models/astronaut.glb`.

---

### 4.4 Grabación de Auscultación Cardíaca y Pulmonar de 30 s (`Web Audio API` + `MediaRecorder` — `[núcleo]`)

Para la pantalla `10_Capture_Auscultation.svg`, el composable mide primero el ruido de cabina (`< 55 dBA`), captura exactamente `30 s` por foco anatómico (`aortic | pulmonic | tricuspid | mitral | upper_left | upper_right | lower_left | lower_right`) y calcula el hash `SHA-256` local antes de enviar el archivo al backend:

```ts
// frontend/app/composables/useAuscultationRecorder.ts
export function useAuscultationRecorder() {
  const cabinDba = ref(48)
  const secondsElapsed = ref(0)
  const isRecording = ref(false)
  const waveform = shallowRef<number[]>([])

  async function recordThirtySeconds(site: string): Promise<{ blob: Blob; sha256: string; site: string }> {
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: { echoCancellation: false, noiseSuppression: false, autoGainControl: false }, // Crudo para fonocardiograma
    })
    const ctx = new AudioContext()
    const source = ctx.createMediaStreamSource(stream)
    const analyser = ctx.createAnalyser()
    analyser.fftSize = 512
    source.connect(analyser)

    const recorder = new MediaRecorder(stream, { mimeType: 'audio/webm' })
    const chunks: BlobPart[] = []
    recorder.ondataavailable = e => chunks.push(e.data)

    isRecording.value = true
    secondsElapsed.value = 0

    return new Promise((resolve) => {
      const timer = setInterval(() => {
        secondsElapsed.value += 1
        if (secondsElapsed.value >= 30) recorder.stop()
      }, 1000)

      recorder.onstop = async () => {
        clearInterval(timer)
        isRecording.value = false
        stream.getTracks().forEach(t => t.stop())
        await ctx.close()

        const blob = new Blob(chunks, { type: 'audio/webm' })
        const buf = await blob.arrayBuffer()
        const hashBuf = await crypto.subtle.digest('SHA-256', buf)
        const sha256 = Array.from(new Uint8Array(hashBuf)).map(b => b.toString(16).padStart(2, '0')).join('')
        resolve({ blob, sha256, site })
      }

      recorder.start(250)
    })
  }

  return { cabinDba, secondsElapsed, isRecording, waveform, recordThirtySeconds }
}
```

---

### 4.5 Validación con `Zod` + Tipos Generados con `openapi-typescript` (`[núcleo]`)

1. **Contrato Único Backend $\rightarrow$ Frontend:** Cada vez que cambia un modelo Pydantic en FastAPI, ejecutar:
   ```bash
   npx openapi-typescript http://127.0.0.1:8080/openapi.json -o frontend/app/types/api.d.ts
   ```
2. **Validación Pre-envío en `Capture` (`11`, `12`, `13`) con mensajes 100% en inglés:**
   ```ts
   // frontend/app/schemas/capture.ts
   import { z } from 'zod'

   export const ocularCaptureSchema = z.object({
     missionStage: z.enum(['LAUNCH', 'MISSION', 'RETURN']),
     leftOpticSheathMm: z.number().min(3.0, 'Minimum 3.0 mm').max(9.0, 'Maximum 9.0 mm'),
     rightOpticSheathMm: z.number().min(3.0, 'Minimum 3.0 mm').max(9.0, 'Maximum 9.0 mm'),
     leftIopMmhg: z.number().min(8).max(35),
     rightIopMmhg: z.number().min(8).max(35),
     retinalThicknessUm: z.number().min(70).max(160),
     visualAcuity: z.string().regex(/^20\/\d{2}$/, 'Use Snellen format, e.g. 20/20'),
   })
   ```

---

### 4.6 Reglas de Redirección y Rutas en Nuxt SPA (Prevención de Pantalla Blanca)

En Nuxt 4 configurado en modo SPA puro (`ssr: false`):
1. **Redirecciones Declarativas Obligatorias:** En páginas puente o de redirección inicial (como `app/pages/index.vue`), debe utilizarse exclusivamente la macro declarativa de compilación de Nuxt:
   ```vue
   <script setup lang="ts">
   definePageMeta({
     redirect: '/login',
   })
   </script>
   ```
2. **Prohibición de `await navigateTo()` en Nivel Superior:** Prohibido invocar `await navigateTo('/...')` en la raíz del `<script setup>` de componentes vacíos. En modo SPA, esto suspende indefinidamente el árbol de renderizado de Vue Suspense antes de montar la aplicación, provocando una pantalla en blanco (`<div id="__nuxt"></div>` vacío).
3. **Internacionalización Nativa en TypeScript:** Toda localización en `@nuxtjs/i18n` debe declararse en archivos TypeScript mediante `defineI18nLocale` (`frontend/i18n/locales/en.ts`). Prohibido usar archivos `.json` planos para catálogos que deban ser transformados dinámicamente por Vite en tiempo de desarrollo.

---

## 5. Construcción del Backend (`Python 3.13 + FastAPI`) y Base de Datos (`SQLite 3 STRICT`)

### 5.1 Esquema Único `backend/db/schema.sql` (`WAL` + `STRICT` + `Append-Only` + `FTS5` + `JSON1`)

`backend/db/schema.sql` es la **única fuente de verdad** de datos (sin ORM). Incluye la etapa narrativa (`LAUNCH`, `MISSION`, `RETURN`) en cada medición para cubrir *Best Storytelling*, `metric_catalog` con rangos científicos para *Best Use of Science*, inmutabilidad *append-only* en `measurements` (RNF 5) y ruta + `SHA-256` para grabaciones de auscultación:

```sql
-- backend/db/schema.sql
PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;
PRAGMA synchronous = NORMAL;

CREATE TABLE IF NOT EXISTS crew_members (
  id TEXT PRIMARY KEY,
  code TEXT NOT NULL UNIQUE,           -- Ej: 'ID·01'
  full_name TEXT NOT NULL,             -- Ej: 'Elena Vargas'
  role TEXT NOT NULL,                  -- Ej: 'Commander'
  pin_hash TEXT NOT NULL,              -- Argon2id hash del PIN de 4 dígitos
  failed_attempts INTEGER NOT NULL DEFAULT 0,
  locked_until_utc TEXT
) STRICT;

CREATE TABLE IF NOT EXISTS metric_catalog (
  metric_key TEXT PRIMARY KEY,         -- Ej: 'optic_sheath_right_mm', 'sleep_total_min'
  display_name_en TEXT NOT NULL,
  unit TEXT NOT NULL,
  nominal_min REAL NOT NULL,
  nominal_max REAL NOT NULL,
  critical_threshold REAL,
  clinical_reference TEXT NOT NULL     -- Fuente científica (usada en backend/reportes, no jerga en UI)
) STRICT;

CREATE TABLE IF NOT EXISTS measurements (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  crew_id TEXT NOT NULL REFERENCES crew_members(id),
  metric_key TEXT NOT NULL REFERENCES metric_catalog(metric_key),
  mission_stage TEXT NOT NULL CHECK (mission_stage IN ('LAUNCH', 'MISSION', 'RETURN')),
  recorded_at_utc TEXT NOT NULL,
  value_num REAL,
  payload_json TEXT NOT NULL DEFAULT '{}' CHECK (json_valid(payload_json))
) STRICT;

-- RNF 5: Inmutabilidad biomédica (Append-Only en measurements)
CREATE TRIGGER IF NOT EXISTS trg_measurements_no_update
BEFORE UPDATE ON measurements
BEGIN
  SELECT RAISE(ABORT, 'Measurements table is append-only');
END;

CREATE TRIGGER IF NOT EXISTS trg_measurements_no_delete
BEFORE DELETE ON measurements
BEGIN
  SELECT RAISE(ABORT, 'Measurements table is append-only');
END;

-- Audio de auscultación en disco: en SQLite solo metadatos, ruta relativa y SHA-256
CREATE TABLE IF NOT EXISTS auscultation_recordings (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  crew_id TEXT NOT NULL REFERENCES crew_members(id),
  organ_type TEXT NOT NULL CHECK (organ_type IN ('CARDIAC', 'PULMONARY')),
  anatomical_site TEXT NOT NULL,       -- 'mitral', 'upper_right', etc.
  duration_sec INTEGER NOT NULL CHECK (duration_sec <= 30),
  cabin_noise_dba REAL NOT NULL,
  file_rel_path TEXT NOT NULL UNIQUE,  -- Ej: 'audio/ID01_cardiac_mitral_20261114.webm'
  sha256_hex TEXT NOT NULL,
  recorded_at_utc TEXT NOT NULL
) STRICT;

-- Wiki médica local con búsqueda instantánea sin internet (FTS5)
CREATE TABLE IF NOT EXISTS wiki_articles (
  id TEXT PRIMARY KEY,
  category_en TEXT NOT NULL,
  title_en TEXT NOT NULL,
  drawer_code TEXT NOT NULL,           -- Ej: 'DRAWER B2'
  steps_json TEXT NOT NULL CHECK (json_valid(steps_json)),
  escalation_en TEXT NOT NULL
) STRICT;

CREATE VIRTUAL TABLE IF NOT EXISTS wiki_articles_fts USING fts5(
  title_en,
  category_en,
  steps_json,
  content='wiki_articles',
  content_rowid='rowid'
);

-- Cola Store-and-Forward hacia Tierra con latencia simulada (APScheduler)
CREATE TABLE IF NOT EXISTS ground_outbox (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  bundle_json TEXT NOT NULL CHECK (json_valid(bundle_json)),
  created_at_utc TEXT NOT NULL,
  deliver_after_utc TEXT NOT NULL,     -- +12 min (Marte/Tránsito) calculado al encolar
  status TEXT NOT NULL CHECK (status IN ('QUEUED', 'IN_TRANSIT', 'DELIVERED'))
) STRICT;
```

### 5.2 Patrón del Backend (`FastAPI` + `sqlite3` Parametrizado + `SSE` + Build Estático en Un Solo Puerto)

```python
# backend/app/main.py
import asyncio
import json
import sqlite3
from contextlib import asynccontextmanager
from pathlib import Path
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

DB_PATH = Path(__file__).resolve().parents[1] / "db" / "spacescan.db"
SCHEMA_PATH = Path(__file__).resolve().parents[1] / "db" / "schema.sql"
STATIC_SPA_DIR = Path(__file__).resolve().parents[2] / "frontend" / ".output" / "public"

def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

@asynccontextmanager
async def lifespan(app: FastAPI):
    with get_db() as conn:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    scheduler = AsyncIOScheduler()
    # Procesa cada 15 s la cola store-and-forward hacia Houston respetando Quiet Hours (22:00-06:00 UTC)
    scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(title="Scan Space Onboard API", version="1.0.0", lifespan=lifespan)

# Server-Sent Events (SSE): telemetría y alertas en vivo sin complejidad de WebSocket
@app.get("/api/v1/stream/telemetry")
async def stream_telemetry(crew_id: str = "ID·01"):
    async def event_generator():
        while True:
            with get_db() as conn:
                rows = conn.execute(
                    """
                    SELECT metric_key, value_num, recorded_at_utc
                    FROM measurements
                    WHERE crew_id = ?
                    ORDER BY id DESC LIMIT 8
                    """,
                    (crew_id,),  # SIEMPRE consulta parametrizada (?)
                ).fetchall()
            payload = json.dumps([dict(r) for r in rows])
            yield f"event: vitals\ndata: {payload}\n\n"
            await asyncio.sleep(1.0)

    return StreamingResponse(event_generator(), media_type="text/event-stream")

# En producción a bordo: el mismo FastAPI sirve el SPA estático de Nuxt 4 en un solo puerto
if STATIC_SPA_DIR.exists():
    app.mount("/", StaticFiles(directory=STATIC_SPA_DIR, html=True), name="spa")
```

### 5.3 Separación Pre-Despegue vs. En Vuelo (`seed.py` + `ONNX Runtime` + `Ollama`)

- **Antes del despegue (`uv run python backend/db/seed.py`):** Usa `httpx` para descargar series reales de **NASA OSDR / GeneLab** y eventos solares de **DONKI**, guardándolos en `backend/db/seed_snapshots/` y poblando `spacescan.db`. Si en una demo no hay internet, `seed.py` lee los snapshots locales incluidos en el repositorio.
- **Durante la misión (100% sin red):**
  - Clasificación automática de fonocardiograma (`S1/S2` normal vs. artefacto/soplo) o riesgo de fatiga con **`onnxruntime`** en CPU cargando `backend/models/auscultation_clf.onnx`.
  - Recomendación preventiva de 3 pasos en `16_Notifications_Header` generada localmente con **`Ollama`** citando artículos de `wiki_articles_fts` (con *fallback* determinista instantáneo si el equipo no tiene `Ollama` activo).

---

## 6. Mapeo Global de las 16 Pantallas Figma para el Equipo

| Sección | Pantalla Figma | Ruta Nuxt 4 | Rol de Datos | Componentes Clave en `dev` |
| :--- | :--- | :--- | :---: | :--- |
| **1. Pública** | `01_Sign_In.svg` | `/login` | Auth PIN | Teclado PIN de 4 dígitos + 2 botones públicos + `PublicHierarchyBar` |
| **1. Pública** | `02_Crew_Overview.svg` | `/crew-overview` | **Solo Resultados** | 4 tarjetas de tripulantes + `ArcGauge` (`Crew Score`) + ambiente |
| **1. Pública** | `03_Crew_Streaks.svg` | `/crew-streaks` | **Solo Resultados** | Rachas activas de los 4 tripulantes + escudo `EVA` |
| **2. Resultados** | `04_Profile_Personal_Data.svg` | `/profile/personal` | **Solo Resultados** | `ProfileTabs` + `HoloFigure` (`body_scan.svg`) + biometría |
| **2. Resultados** | `05_Profile_Psychological.svg` | `/profile/psychological` | **Solo Resultados** | `ProfileTabs` + curva ECharts 14 días (`Mood`/`Calmness`) + PVT |
| **2. Resultados** | `06_Profile_Physical.svg` | `/profile/physical` | **Solo Resultados** | `ProfileTabs` + 6 `BandRow` clínicos + `ECG` en vivo + 4 labs |
| **2. Resultados** | `07_Sleep_Monitor.svg` | `/sleep` | **Solo Resultados** | `SubnavTabs` + `ArcGauge` (`Sleep Score`) + **Barra de Cintas ECharts** + Lapsos |
| **2. Resultados** | `08_Vision_Exam.svg` | `/vision` | **Solo Resultados** | `ArcGauge` Ojo Izq/Der + Curva bilateral `ONSD` + 3 pasos preventivos |
| **2. Resultados** | `09_Auscultation_Results.svg` | `/auscultation` | **Solo Resultados** | `HoloFigure` (`heart.svg`/`lungs.svg`) + ondas `Channel 1/2` + `CO₂` 24 h |
| **3. Captura** | `10_Capture_Auscultation.svg` | `/capture/auscultation` | **Entrada Audio** | `CaptureTabs` + `useAuscultationRecorder` (`30 s` cardíaco/pulmonar + `dBA`) |
| **3. Captura** | `11_Capture_Physical_Labs.svg` | `/capture/physical` | **Entrada Datos** | `CaptureTabs` + `NumberField` + `SaveResult` para signos, hábitos y labs |
| **3. Captura** | `12_Capture_Vision_Ocular.svg` | `/capture/vision` | **Entrada Datos** | `CaptureTabs` + formulario ocular bilateral + detección de umbral en vivo |
| **3. Captura** | `13_Capture_Psych_Sleep.svg` | `/capture/psych-sleep` | **Entrada Datos** | `CaptureTabs` + escalas `1–5` + ventana `UTC` de sueño + `useReactionArena` (`2 min`) |
| **4. Soporte** | `14_Medical_Guide.svg` | `/guide` | Consulta `FTS5` | Buscador médico instantáneo + `Emergency Index` + localizador `DRAWER` |
| **4. Soporte** | `15_Mission_Control.svg` | `/comms` | Cola `DTN` | Mensajes `Flight Surgeon` (`+12 min`) + clima solar `DONKI` |
| **4. Header** | `16_Notifications_Header.svg` | `/notifications` | **Solo Header** | `SubnavTabs` + avisos, `Scheduled Checks` y `Pending Reviews` (`PHYSICIAN`) |

---

## 7. Matriz de Trazabilidad Tecnológica por Categoría de Premio

Cada pieza del stack **[núcleo]** y **[extra]** sostiene directamente una categoría de evaluación:

| # | Premio | Cómo se Construye en el Proyecto |
| :-: | :--- | :--- |
| **1** | **Best Use of Data** | `seed.py` + `httpx` pre-despegue con series reales de **OSDR/GeneLab** y **DONKI** persistidas en `SQLite`; visualización limpia en `Apache ECharts` y exportación estándar `JSON1`. |
| **2** | **Best Use of Science** | Tabla `metric_catalog` con rangos y fuente científica, cálculo de *z-score* contra línea base personal del tripulante y modelo local que cita artículos de `wiki_articles`. |
| **3** | **Best Use of Technology** | Inferencia acústica/biométrica con **ONNX Runtime** en CPU + orientación preventiva local con **Ollama**, `100%` sin red. |
| **4** | **Best Storytelling** | Columna `mission_stage` (`LAUNCH` / `MISSION` / `RETURN`) en cada medición + gráficas longitudinales comparativas + simulador de sensores Python en vivo para la demo. |
| **5** | **Best Mission Concept** | `SQLite 3` en un único archivo (`WAL` + `STRICT`), cola *store-and-forward* tipo `DTN` con `APScheduler` e inferencia ligera en CPU desde un solo puerto. |
| **6** | **Galactic Impact** | `@vite-pwa/nuxt` **[extra]** + `Docker`: la misma plataforma sirve para telemedicina autónoma fuera de órbita y en zonas aisladas en Tierra. |
| **7** | **Global Connection** | `@nuxtjs/i18n` configurado con `en` por defecto (100% inglés en UI sin mezclas), repositorio público bajo **Licencia MIT**, contrato `OpenAPI` y paquetes `JSON1`. |
| **8** | **Local Impact** | Operación completa sin internet y sobre hardware económico (laptops/tablets de bajo consumo) aplicable en clínicas rurales. |
| **9** | **Most Inspirational** | Tablero público `Crew Streaks` (`03`), check-in conductual y arena interactiva de reacción psicomotriz de `2 min` (`13`) en Vue + `motion-v` **[extra]**. |
| **10** | **Art & Technology** | Variables CSS fieles al [Figma Oficial (`node-id=7382-2`)](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2&t=tzbC2RhJeGZ2Dlov-1), hologramas SVG con barrido CSS (`TresJS` **[extra]**), tema propio `'spacescan-hud'` en ECharts y conmutación instantánea a Modo Alerta. |

---

## 8. Checklist Obligatorio de Definición de Hecho (*Definition of Done*)

Antes de fusionar cualquier rama a `main`, el desarrollador debe verificar:

- [ ] **Fidelidad contra el Figma Oficial:** Comparar visualmente la vista contra [SpaceScan en Figma (`node-id=7382-2`)](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2&t=tzbC2RhJeGZ2Dlov-1) verificando proporciones, márgenes, dock de `7` módulos con `Profile` al centro y `Notifications` solo en el header.
- [ ] **Prueba en Modo Avión (`RNF 1`):** Abrir DevTools $\rightarrow$ pestaña *Network* con Wi-Fi/Ethernet apagado: `0` peticiones fallidas a dominios externos; fuentes `.woff2`, iconos locales y gráficas ECharts cargan al `100%`.
- [ ] **Auditoría de Idioma y Limpieza:** `100%` de las etiquetas visibles están en inglés; `0` menciones a `SQLite`, `JSON`, `FHIR`, `Offline`, `Break-Glass` o tecnologías internas en la interfaz.
- [ ] **Fidelidad Cromática:** Solo existen variables de `tokens.css` (`#001524`, `#15616D`, `#FFECD1`, `#2AEF4B`, `#000C5C`, `#D5110B`); los ítems activos del menú y líneas guía usan `#000C5C` translúcido.
- [ ] **Separación Resultados vs. Captura:** Ninguna pantalla de `Profile`, `Sleep`, `Vision` o `Auscultation` contiene botones de registro; todo formulario pasa por `Zod` dentro de `/capture/*`.
- [ ] **Calidad, Contrato Tipado y Pruebas:** `uv run ruff check .`, `uv run pytest`, `npx openapi-typescript`, `pnpm lint` (`@nuxt/eslint`), `pnpm test` (`Vitest`) y, si aplica **[extra]**, flujo E2E en `Playwright` pasan con `0` errores.
