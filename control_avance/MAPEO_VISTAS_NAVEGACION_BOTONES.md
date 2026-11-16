# Mapeo Completo de Vistas, Navegación, Botones e Indicadores — SpaceScan

> **Propósito:** Inventario verificado directamente sobre el código fuente actual de `wakax-nasa-challenge-2026/frontend/app/` para visualizar toda la arquitectura de pantallas, navegación, botones interactivos y, con **mayor detalle**, cada indicador presente en la **vista inicial (`/login` + zona pública)** y la **vista principal (`Profile` y sus sub-pestañas)** para facilitar la priorización de indicadores principales.
>
> **Nota de alcance:** Documento de análisis y mapeo únicamente (`docs/control_avance/`). No altera código fuente ni especificaciones normativas.

---

## 1. Arquitectura de Navegación y Shell Global

### 1.1 Árbol de Rutas y Guardas de Acceso (`middleware/auth.global.ts`)

En `layouts/default.vue` y `middleware/auth.global.ts` existen **2 niveles de navegación**:

```text
/ (pages/index.vue) ──redirect──▶ /login  [VISTA INICIAL PÚBLICA]
│
├── NIVEL 1 · ZONA PÚBLICA (sin PIN · PublicHierarchyBar de 3 pestañas)
│   ├── /login               (01 · Sign In)
│   ├── /crew-overview       (02 · Crew Overview)
│   └── /crew-streaks        (03 · Crew Streaks)
│
└── NIVEL 2 · CABINA AUTENTICADA (tras PIN de 4 dígitos · BottomCockpitDock de 7 módulos)
    ├── TopTelemetryBar (siempre visible arriba)
    │   └── /notifications   (16 · Notifications + Pending Reviews [solo PHYSICIAN])
    │
    └── Dock Inferior Simétrico (7 ranuras)
        ├── [1] /vision               (08 · Vision & Ocular Exam)
        ├── [2] /sleep                (07 · Sleep Architecture & Quality)
        ├── [3] /auscultation         (09 · Cardiac & Pulmonary Auscultation)
        ├── [4] /profile/personal ◀── [SLOT CENTRAL ELEVADO · VISTA PRINCIPAL POST-LOGIN]
        │       ├── Sub-tab: /profile/personal       (04 · Personal Data)
        │       ├── Sub-tab: /profile/psychological  (05 · Psychological)
        │       ├── Sub-tab: /profile/physical       (06 · Physical)
        │       ├── Sub-tab: /profile/streak         (Personal Streak)
        │       └── Botón rol OPERATOR: /crew-management (Crew Administration)
        ├── [5] /capture/auscultation (Módulo Capture · 4 sub-pestañas)
        │       ├── Sub-tab: /capture/auscultation   (10 · Auscultation Audio)
        │       ├── Sub-tab: /capture/physical       (11 · Physical & Labs)
        │       ├── Sub-tab: /capture/vision         (12 · Vision & Ocular + Modal SANDRA)
        │       └── Sub-tab: /capture/psych-sleep    (13 · Psych, Motor & Sleep)
        ├── [6] /guide                (14 · Medical Guide & Kit Locator)
        └── [7] /comms                (15 · Mission Control & Solar Weather)
```

---

### 1.2 Componentes del Shell y Controles Transversales

| Componente | Ubicación | Elementos / Controles Interactivos / Indicadores |
| :--- | :--- | :--- |
| **`ShellTopTelemetryBar`** (`TopTelemetryBar.vue`) | Barra superior fija (`56px`, todas las vistas) | • Logo (`logo.svg`) + `SpaceScan` + `mission_code`<br>• Título y subtítulo dinámico de la vista activa (`usePageHeader`)<br>• **`MISSION CLOCK`**: reloj UTC continuo sincronizado con servidor<br>• **Botón / Link `Notifications (N)`** *(solo autenticado)* → navega a `/notifications`; muestra punto rojo si `unread > 0`<br>• **Píldora de estado global** *(condicional por vista)*: texto y tono (`ok` / `critical` / `neutral`) |
| **`ShellPublicHierarchyBar`** (`PublicHierarchyBar.vue`) | Dock inferior público (`72px`, sin sesión o en rutas públicas) | 3 botones/links de navegación:<br>1. `Sign In` (`/login`)<br>2. `Crew Overview` (`/crew-overview`)<br>3. `Crew Streaks` (`/crew-streaks`) |
| **`ShellBottomCockpitDock`** (`BottomCockpitDock.vue`) | Dock inferior autenticado (`72px`, tras PIN) | • **Izquierda:** Tarjeta de sesión activa (`{crew.code} · {crew.short_name}`)<br>• **Centro trapezoidal (7 links):** `Vision` (`/vision`), `Sleep` (`/sleep`), `Auscultation` (`/auscultation`), **`Profile`** (`/profile/personal`, slot central elevado), `Capture` (`/capture/auscultation`), `Guide` (`/guide`), `Comms` (`/comms`)<br>• **Derecha:** Botón **`Sign Out`** (cierra sesión y navega a `/login`) |
| **`UiParamHelp`** (`ParamHelp.vue`) | Botón **`?`** junto a títulos y parámetros | Hover/clic abre popover (`Teleport` a `body`) con: *What it measures*, *How to read it*, *Mission impact*, *Normal range* (diferenciado por sexo si aplica) y *Your baseline* (si está autenticado). |
| **`UiInteractiveChartFrame`** (`InteractiveChartFrame.vue`) | Contenedor de todas las gráficas | • **Botones de periodo** (cuando aplica: ej. `7D`/`14D`/`30D`/`ALL` o `24H`/`7D`/`30D`)<br>• **Clic sobre serie** → fija punto clínico (pin con valor, fecha UTC, etapa y `Δ` vs referencia)<br>• **Botón `×`** en cada pin → quita el pin<br>• **Botón `Reset Zoom`** → restablece zoom de ECharts al 100% |
| **`UiAiWatermark`** (`AiWatermark.vue`) | Esquina de hologramas e IA | Etiqueta pasiva `AI Used` (sin interacción). |

---

## 2. Mapeo Detallado de la Vista Inicial (Nivel 1 Público)

> **Nota para priorización:** Al abrir la app (`/`), el sistema redirige a **`/login`**. Desde ahí existen dos botones directos hacia **`/crew-overview`** y **`/crew-streaks`** que funcionan como tableros iniciales públicos sin sesión. Se detallan las 3 pantallas públicas.

### 2.1 Pantalla Inicial de Entrada: `01 · Sign In` (`/login` — `pages/login.vue`)

| Bloque | Elementos Visuales / Indicadores | Botones / Inputs / Comportamiento | Prioridad *(A definir)* |
| :--- | :--- | :--- | :--- |
| **Encabezado de vista** | Título `Select Crew Profile` (`TopTelemetryBar` muestra solo marca, código de misión y reloj `MISSION CLOCK`) | Sin botón `Notifications` ni píldora de estado | — |
| **Selector de Tripulantes** (`radiogroup`) | 4 tarjetas (`profiles` de `/crew/profiles`), cada una muestra:<br>• Código (`ID·01`..`ID·04`)<br>• Píldora de estado (`LOCKED` / `SELECTED` / `OPTIMAL` / `ATTENTION`)<br>• Figura holográfica `UiHoloFigure` (`body`, adaptada por sexo `F`/`M` y tono de estado)<br>• `full_name`<br>• `title_en` (puesto) | **4 botones `role="radio"`** (uno por tripulante): selecciona el perfil, limpia el PIN previo y enfoca el campo PIN. | |
| **Ventana `Enter PIN · {Nombre}`** (`HudWindow`) | • Tag `4-DIGIT PIN`<br>• 4 cajas visuales de dígitos ocultos (`•`)<br>• Mensaje de error/intentos restantes (`role="alert"`) | • **`<input type="password" inputmode="numeric" maxlength="4">`**: acepta solo 4 dígitos numéricos<br>• **Botón submit `Sign In`** (se habilita cuando hay perfil seleccionado, no bloqueado y 4 dígitos) → autentica y navega a **`/profile/personal`** | |
| **Accesos Directos Públicos** | Separador `No sign-in required` | • **Botón/Link `Open Crew Overview`** → `/crew-overview`<br>• **Botón/Link `Open Crew Streaks`** → `/crew-streaks` | |
| **Dock Inferior** | `PublicHierarchyBar` | 3 pestañas: `Sign In`, `Crew Overview`, `Crew Streaks` | — |

---

### 2.2 Vista Pública: `02 · Crew Overview` (`/crew-overview` — `pages/crew-overview.vue`)

Vista de solo lectura que concentra el resumen inicial de toda la tripulación y cabina:

| Bloque | Indicadores Mostrados | Parámetro / `metric_key` (`?`) | Botones / Interacción | Prioridad *(A definir)* |
| :--- | :--- | :--- | :--- | :--- |
| **Header Superior** | Título `Crew Overview` + Píldora `{optimal_count} / {crew_count} crew optimal` | — | Solo `PublicHierarchyBar` | — |
| **4 Columnas de Tripulación** (`HudWindow` × 4) | Por cada tripulante:<br>• Header: `{num} · {full_name}`, `{title_en}`, píldora `OPTIMAL`/`ATTENTION`<br>• `UiHoloFigure` (`body`, sexo y tono)<br>• Caja `Work shift & location`: modo (`IVA`/`EVA`), duración, ubicación<br>• **4 KPIs (grid 2×2):**<br>  1. `Heart Rate` (valor `bpm` + barra)<br>  2. `HRV` (valor `ms` + barra)<br>  3. `Sleep (24h)` (duración + nota vs meta)<br>  4. `Oxygen (SpO₂)` (valor `%` + nota `Optimal`/`Low`) | 1. `resting_hr_bpm`<br>2. `hrv_rmssd_ms`<br>3. `sleep_duration`<br>4. `spo2_pct` | Botones **`?`** (`UiParamHelp`) en cada uno de los 4 KPIs | |
| **Panel Inferior `Crew Readiness & Cabin Environment`** (`HudWindow`) | • **Tag:** `READINESS {crew_score} / 100`<br>• **Gauge circular (`ArcGauge`):** `Crew Score` (`/ 100`)<br>• **3 barras de preparación grupal:**<br>  1. `Hydration` (`%` + promedio `L / goal L`)<br>  2. `Sleep Target` (`%` + conteo bajo meta)<br>  3. `Daily Exercise` (`%` metas cumplidas)<br>• **Tarjeta `Habitat environment`:** estado (`NOMINAL`/`ATTENTION`/`CRITICAL`) y tira `temp_c °C · humidity_pct% RH · noise_dba dBA · CO₂ co2_mmhg mmHg` | • Header: `crew_score`<br>• `hydration_ml`<br>• `sleep_target_nights`<br>• `exercise_min` | Botones **`?`** (`UiParamHelp`) en título de ventana y en las 3 barras | |

---

### 2.3 Vista Pública: `03 · Crew Streaks` (`/crew-streaks` — `pages/crew-streaks.vue`)

| Bloque | Indicadores Mostrados | Parámetro / `metric_key` (`?`) | Botones / Interacción | Prioridad *(A definir)* |
| :--- | :--- | :--- | :--- | :--- |
| **Header Superior** | Título `Crew Streaks` + Píldora `Team streak · {N} days` | — | `PublicHierarchyBar` | — |
| **4 Columnas de Tripulación** | • Header: nombre, puesto, pill `{N} DAYS` / `{N} DAYS · SHIELD` / `ATTENTION`<br>• **Gauge `Active Streak`** (`{N} Days`, subtítulo `Best: X days` o `EVA Rest Shield` o hábito bajo meta)<br>• **Tira `Last 7 days`:** 7 celdas (`check` 4/4, `X/4`, `SHD`, `—`)<br>• **Bloque `{today_label} habits`:** barras por hábito (`Hydration`, `Nutrition`, `Exercise`/`Post-EVA Rest`, `Sleep Routine`) | • `habit_streak`<br>• `hydration_ml`<br>• `calories_kcal`<br>• `exercise_min`<br>• `sleep_duration` | Botones **`?`** (`UiParamHelp`) en gauge y en cada hábito | |
| **Panel Inferior `Collective Streak & Daily Habits`** | • Tag `{pct}% COMPLETED`<br>• **Gauge `Team Streak`** (`Days active`)<br>• **3 barras colectivas:** `Crew Hydration`, `Daily Nutrition`, `Scheduled Exercise`<br>• **Tarjeta `30-day mission consistency`:** `%` hábitos cumplidos y rachas activas | • Header: `habit_streak`<br>• `hydration_ml`<br>• `calories_kcal`<br>• `exercise_min` | Botones **`?`** (`UiParamHelp`) en header y en las 3 barras | |

---

## 3. Mapeo Detallado de la Vista Principal Autenticada (`Profile`)

> **Vista principal post-login:** Al hacer clic en `Sign In` en `/login`, el sistema abre **`/profile/personal`**. Además, **`Profile`** ocupa el slot central elevado (`#4`) del `BottomCockpitDock` y agrupa **4 sub-pestañas** + **1 acceso condicional por rol** en `ShellProfileTabs.vue`.

### 3.1 Navegación Interna de `Profile` (`ShellProfileTabs.vue`)

| Elemento | Tipo | Ruta Destino | Visibilidad |
| :--- | :--- | :--- | :--- |
| **`Personal Data`** | Tab (Reka UI) | `/profile/personal` | Todos los roles autenticados *(Vista por defecto)* |
| **`Psychological`** | Tab (Reka UI) | `/profile/psychological` | Todos los roles autenticados |
| **`Physical`** | Tab (Reka UI) | `/profile/physical` | Todos los roles autenticados |
| **`Streak`** | Tab (Reka UI) | `/profile/streak` | Todos los roles autenticados |
| **`Crew Administration`** | Link / Botón | `/crew-management` | **Solo rol `OPERATOR`** |

---

### 3.2 Sub-vista Principal por Defecto: `04 · Profile · Personal Data` (`/profile/personal` — `pages/profile/personal.vue`)

**Header superior:** Título `Astronaut Profile · Personal Data` · Píldora derecha `OPTIMAL` / `ATTENTION` · Botón `Notifications (N)` · `MISSION CLOCK`.

Layout de **3 columnas (`HudWindow`)**:

#### Columna 1 (Izquierda · `33.2%`): `Personal Biometrics` (Tag: `{crew.code}`)
| Elemento / Tarjeta | Qué Muestra | `metric_key` (`?`) | Fuente Backend (`profile_service.py`) | Notas / Observación para Priorización |
| :--- | :--- | :--- | :--- | :--- |
| **Tarjeta de Identidad** (`tile-hi`) | • `full_name` + pill `title_en` (`COMMANDER`/`PILOT`/etc.)<br>• `Age` (yrs), `Sex`, `Blood Type`<br>• Badge `Female ranges` / `Male ranges` + `?` | `sex_reference` | `crew_members` + `SEX_REFERENCE_TEXT` | Identidad demográfica fija y perfil fisiológico de referencia |
| **Biométrica 1: `Height`** | Valor (`cm`) + `Baseline: X cm` | `height_cm` | `measurements` (`height_cm`) | Dato estático de estatura |
| **Biométrica 2: `Weight`** | Valor (`kg`) + `Baseline: X kg` | `body_weight_kg` | `measurements` (`body_weight_kg`) | Indicador de masa corporal longitudinal |
| **Biométrica 3: `Body Mass Index`** | Valor (`kg/m²`) + `Normal: min–max` | `bmi_kg_m2` | Calculado de peso/estatura | Derivado de peso y estatura |
| **Biométrica 4: `Muscle Mass`** | Valor (`kg`) + `% retained` + `SMI X (≥ min)` | `muscle_mass_kg` | `measurements` (`muscle_mass_kg`) + `smi()` | *Ver nota en `correcciones de testers.md` (§5)* |
| **Biométrica 5: `Bone Density`** | Valor (`g/cm²`) + `% of baseline` | `bone_density_g_cm2` | `measurements` (`bone_density_g_cm2`) | *Ver nota en `correcciones de testers.md` (§5)* |
| **Biométrica 6: `Aerobic Capacity`** | Valor (`mL/kg`) + `Optimal range` o `% of pre-flight` | `vo2_max_ml_kg_min` | `measurements` (`vo2_max_ml_kg_min`) | También aparece en `/auscultation`; *ver nota en §5* |

#### Columna 2 (Centro · `30.8%`): `Biometric Scan` (Tag: `OPTIMAL` / `ATTENTION`)
| Elemento / Tarjeta | Qué Muestra | `metric_key` (`?`) | Fuente Backend | Notas / Observación |
| :--- | :--- | :--- | :--- | :--- |
| **Holograma Corporal** | `UiHoloFigure` (`body-scan`, adaptado a sexo `F`/`M`) + watermark `AI Used` | — | Visual SVG (`body_scan.svg` / `body_scan_f.svg`) | Elemento central visual; *ver nota en `Mejoras y Correciones.md` sobre animación* |
| **KPI Inferior Izquierdo: `Core temp`** | Temperatura corporal (`°C`) | `body_temp_c` | `measurements` (`body_temp_c`) | Signo vital clave en vista principal |
| **KPI Inferior Derecho: `Hydration · Day X`** | `{consumido} / {meta} L` | `hydration_ml` | Suma diaria `hydration_ml` vs `personal_targets` | Hábito clave diario |

#### Columna 3 (Derecha · `flex-1`): `Environment & Work Hours` (Tag: `{location_en}`)
| Elemento / Tarjeta | Qué Muestra | `metric_key` (`?`) | Fuente Backend | Notas / Observación |
| :--- | :--- | :--- | :--- | :--- |
| **Dial 1: `Temperature`** (`ArcGauge`) | Valor `°C` | `cabin_temp_c` | `environment_readings` / `cabin_snapshot` | Entorno de cabina |
| **Dial 2: `Humidity`** (`ArcGauge`) | Valor `%` + `Optimal X–Y%` | `cabin_humidity_pct` | `environment_readings` / `cabin_snapshot` | Entorno de cabina |
| **Dial 3: `Ambient Noise`** (`ArcGauge`) | Valor `dBA` + `(<max dBA)` | `cabin_noise_dba` | `environment_readings` / `cabin_snapshot` | Entorno de cabina (crítico para auscultación) |
| **Dial 4: `Cabin CO₂`** (`ArcGauge`) | Valor `mmHg` + `(<alert)` | `cabin_co2_ppm` | `environment_readings` / `cabin_snapshot` | Entorno respiratorio crítico |
| **Tiempo 1: `Interior Work (IVA)`** | Duración (`Xh Ym`) + `{location} · Active Shift` | `work_shift_min` | `measurements` (`work_shift_min`) | Carga laboral interior del día |
| **Tiempo 2: `Exterior Work (EVA)`** | Duración hoy (`Xh Ym`) + `Mission Cumulative` | `eva_shift_min` | Suma diaria y acumulada `eva_shift_min` | Carga laboral EVA |
| **Tiempo 3: `Mission Elapsed Time`** | `{N} Days` + hora UTC + estado horario | `mission_elapsed` | `mission` (`launch_utc` / `current_stage`) | Reloj/etapa de misión |

*(En `/profile/personal`, las únicas interacciones son los 16 botones `?` de `UiParamHelp`, las 4 sub-pestañas de `ProfileTabs`, el botón `Crew Administration` si es `OPERATOR`, y el shell `TopTelemetryBar` + `BottomCockpitDock`.)*

---

### 3.3 Sub-vista de `Profile`: `05 · Profile · Psychological` (`/profile/psychological` — `pages/profile/psychological.vue`)

**Header superior:** `Astronaut Profile · Psychological` · Píldora `Stable` / `Support Advised`.

| Ventana (`HudWindow`) | Indicadores / Elementos | `metric_key` (`?`) | Botones / Interacción |
| :--- | :--- | :--- | :--- |
| **1. `Behavioral & Mood Results`** (`40.5%`, tag `OPTIMAL`/`SUPPORT`) | • Tarjeta `Latest daily state · {Calm & Focused / Focused / Tired / Under Strain}` + pill `{HH:MM} UTC LOG`<br>• **4 escalas con barra de banda óptima:**<br>  1. `Overall Mood` (`/ 5`) + pill<br>  2. `Stress Index` (`/ 100`) + pill<br>  3. `Isolation` (`/ 5`) + pill<br>  4. `Motivation` (`/ 5`) + pill | `overall_mood`, `stress_index`, `isolation`, `motivation` | 4 botones **`?`** |
| **2. `Mood & Calmness Trend · {Periodo}`** (tag `STABILITY {pct}%`) | • Gráfica ECharts doble línea: `Mood Score` y `Calmness` + zona óptima (`OPTIMAL WELLBEING ZONE`) | `mood_calmness` (en header) | • Botón **`?`** en header<br>• **`UiInteractiveChartFrame`**: botones periodo **`7D` / `14D` / `30D` / `ALL`**, clic en puntos para fijar pins, botón **`×`** en pin, botón **`Reset Zoom`** |
| **3. `Cognitive & Motor Reaction Results`** (tag `OPTIMAL`/`BELOW TARGET`) | • **Gauge `Reaction Time`** (`ms` vs `< target ms`)<br>• **3 tarjetas:** `Attention Lapses` (errores), `Motor Precision` (`%`), `Vigilance Score` (`/ 100`) | `reaction_time`, `attention_lapses`, `motor_precision`, `vigilance_score` | 4 botones **`?`** |

---

### 3.4 Sub-vista de `Profile`: `06 · Profile · Physical` (`/profile/physical` — `pages/profile/physical.vue`)

**Header superior:** `Astronaut Profile · Physical` · Píldora `{on_target} / {daily_count} on target`.

| Ventana (`HudWindow`) | Indicadores / Elementos | `metric_key` (`?`) | Botones / Interacción |
| :--- | :--- | :--- | :--- |
| **1. `Daily Vitals, Exercise & Nutrition`** (`41%`, tag `CONTINUOUS`) | **6 `UiBandRow`** (valor + unidad + pill de estado + referencia + barra con banda nominal/baseline):<br>1. `Resting Heart Rate` (`bpm`)<br>2. `Blood Pressure` (`systolic/diastolic mmHg`)<br>3. `Oxygen Saturation (SpO₂)` (`%`)<br>4. `Daily Exercise` / `Post-EVA Rest` (`min`)<br>5. `Hydration` (`L`)<br>6. `Caloric Intake` (`kcal`) | `resting_hr_bpm`, `blood_pressure`, `spo2_pct`, `exercise_min`, `hydration_ml`, `calories_kcal` | 6 botones **`?`** |
| **2. `Live ECG & Body Temperature`** (tag `LIVE SENSOR STREAM · ACTIVE` / `RECONNECTING…` / `NO LIVE SIGNAL · LAST STRIP`) | • Cabecera trazo: `LEAD II · {speed} mm/s · {rhythm}`<br>• Lecturas vivas: `{bpm} BPM · HRV {hrv} MS · {temp} °C`<br>• Gráfica ECG continua (125 Hz en vivo o último trazo guardado) | `ecg_lead_ii_mv` (en header) | • Botón **`?`** en header<br>• **`UiInteractiveChartFrame`**: clic sobre muestra para fijar pin, botón **`×`** en pin, botón **`Reset Zoom`** |
| **3. `Periodic Clinical Lab Results`** (tag `LATEST RESULTS`) | **Grid 2×2 (4 tarjetas):**<br>1. `Blood Glucose` (`mg/dL`)<br>2. `Blood Panel` (`Hemoglobin g/dL`)<br>3. `Urine Specific Gravity` (`SG`)<br>4. `Auscultation & Vision` (ritmo cardíaco + agudeza Snellen + vaina óptica peor lado) | `blood_glucose_mg_dl`, `hemoglobin_g_dl`, `urine_specific_gravity` *(el #4 no lleva `?`)* | 3 botones **`?`** |

---

### 3.5 Sub-vista de `Profile`: `Profile · Streak` (`/profile/streak` — `pages/profile/streak.vue`)

**Header superior:** `Astronaut Profile · Streak` · Píldora `{active_streak_days} day streak`.

| Ventana (`HudWindow`) | Indicadores / Elementos | `metric_key` (`?`) | Botones / Interacción |
| :--- | :--- | :--- | :--- |
| **1. `Personal Consistency Streak`** (`31.1%`, tag `POST-EVA SHIELD` / `TODAY COUNTS` / `IN PROGRESS`) | • `ArcGauge` `Active Streak` (`{N} Days` · `Best: X days`)<br>• `Today · {today_label}` (`X / 4 habits`)<br>• `14-day consistency` (`%`)<br>• Regla explicativa (3 de 4 hábitos; 2 con escudo EVA) | `habit_streak` (en header) | 1 botón **`?`** en header |
| **2. `Today's Habits vs Personal Target`** (tag `{done} / 4 MET`) | **4 `UiBandRow`:** `Hydration` (`L`), `Nutrition` (`kcal`), `Exercise`/`Post-EVA Rest` (`min`), `Sleep Window` (`Xh Ym`) | `hydration_ml`, `calories_kcal`, `exercise_min`, `sleep_duration` | 4 botones **`?`** |
| **3. `Last 14 Days`** (`27%`, tag `{N} / 14 COUNTED`) | • Grid `2×7` de últimos 14 días (`check`, `SHIELD`, `X/4`, `—`) + leyenda (`Counted`, `Shield / today`, `Missed`) | — | Sin botones internos |

---

## 4. Inventario Completo del Resto de Vistas, Navegación y Botones de la App

Para tener el mapa 100% completo de cada pantalla y botón de SpaceScan:

| Ruta | Título / Secciones (`HudWindow`) | Indicadores / Contenido | Botones y Controles Interactivos |
| :--- | :--- | :--- | :--- |
| **`/vision`** (`pages/vision.vue`) | 1. `Ocular Measurements`<br>2. `Optic Nerve Sheath Trend (mm)`<br>3. `Visual Battery Summary & Preventive Care` (o `Preventive Care Plan`) | • `HoloFigure` (`brain`) + resumen alerta ocular<br>• 2 `ArcGauge`: `left eye`, `right eye` (`mm`)<br>• 3 `BandRow`: `Intraocular Pressure`, `Retinal Layer Thickness`, `Visual Acuity`<br>• Último examen y próximo hito<br>• Gráfica bilateral ONSD (`mm`) + `Target`<br>• Si existe `functional_exam`: tarjetas `Amsler Grid (OD / OS)`, `Landolt C Acuity & Schedule`, `SANS Symptoms & Risk`<br>• 3 tarjetas de cuidado preventivo | • 6 botones **`?`** (`optic_sheath_left_mm`, `optic_sheath_right_mm`, `iop_left_mmhg`, `retinal_thickness_um`, `visual_acuity_snellen`, header gráfica)<br>• `UiInteractiveChartFrame`: **`30D` / `ALL`**, pin de puntos, **`×`**, **`Reset Zoom`** |
| **`/sleep`** (`pages/sleep.vue`) | Sub-barra `ShellSubnavTabs` + píldora `REST WINDOW`<br>1. `Sleep Quality & Stage Time`<br>2. `Sleep Stage Ribbon Chart` / `Nightly Sleep Stages`<br>3. `Stage Lapses & Cycle Intervals` | • `ArcGauge` `Sleep Score`<br>• `Total/Average sleep time`, `In Bed`, `Sleep Efficiency`<br>• 4 tarjetas de etapas: `Deep`, `REM`, `Light`, `Awake` (con duración, `%`, barra)<br>• Gráfica custom ribbon por fase (en `Last Night`) o barras por noche (en `7d`/`14d`/`30d`)<br>• Tabla de intervalos UTC y bouts o resumen de periodo | • **4 Sub-tabs:** `Last Night`, `Last 7 Days`, `Last 14 Days`, `Last 30 Days`<br>• Botones **`?`** (`sleep_score`, `sleep_duration`, `sleep_efficiency`, `sleep_deep/rem/light/awake`, y en periodos multi-día también `sleep_target_nights`)<br>• `UiInteractiveChartFrame`: pin de bloques/noches, **`×`**, **`Reset Zoom`** |
| **`/auscultation`** (`pages/auscultation.vue`) | 1. `Cardiac & Pulmonary Audio Results`<br>2. `Recorded Cardiac & Pulmonary Acoustic Waveforms`<br>3. `24-Hour / 7-Day / 30-Day Cabin CO₂ Trend (mmHg)` | • Tarjetas `Heart` (`bpm`, ritmo, sitios) y `Lungs` (`rpm`, `SpO₂`, zonas) con `HoloFigure` (`heart`/`lungs` + `AI Used`)<br>• Tarjeta `Assisted sound interpretation` (clasificación CNN, `% likely`, estado de revisión del médico, watermark `AI Used`)<br>• 3 `BandRow` fitness: `Aerobic Capacity (VO₂ Max)`, `Orthostatic Response`, `Cardiorespiratory Index`<br>• Envolventes acústicas `Channel 1` (cardiac) y `Channel 2` (pulmonary)<br>• Gráfica de tendencia `CO₂` en cabina | • 7 botones **`?`** (`heart_sound_rate`, `lung_sound_rate`, `vo2_max_ml_kg_min`, `orthostatic_hr_delta_bpm`, `cardiorespiratory_index`, `signal_quality`, `cabin_co2_ppm`)<br>• **2 Botones audio:** **`▶ Play` / `❚❚ Pause`** en Channel 1 y Channel 2<br>• `UiInteractiveChartFrame` ondas: pin de momentos, **`×`**, **`Reset Zoom`**<br>• `UiInteractiveChartFrame` CO₂: **`24H` / `7D` / `30D`**, pin, **`×`**, **`Reset Zoom`** |
| **`/capture/auscultation`** (`pages/capture/auscultation.vue`) | `ShellCaptureTabs` (4 sub-tabs)<br>1. `Cardiac Audio Recording` (`HEART · 30S`)<br>2. `Pulmonary Audio Recording` (`LUNGS · 30S`) | • `HoloFigure` (`heart`/`lungs`) + ruido ambiental dBA (bloqueo si ≥ 55 dBA)<br>• Barra de ganancia (`dB`), onda en vivo (ECharts), contador `00:XX / 00:30 SEC`, progreso por sitio | • **4 Sub-tabs `CaptureTabs`**<br>• 2 botones **`?`** (`signal_quality`)<br>• **8 botones radio de sitio:** `Aortic · 2nd R`, `Pulmonic · 2nd L`, `Tricuspid · 4th L`, `Mitral Apex` · `Upper Left`, `Upper Right`, `Lower Left`, `Lower Right`<br>• **Botones acción (×2 paneles):** `Record / Stop Heart Audio` / `Record Pulmonary Audio` (o `Stop Recording`), `Save Cardiac Recording` / `Save Lung Recording` |
| **`/capture/physical`** (`pages/capture/physical.vue`) | `ShellCaptureTabs`<br>1. `Daily Vitals, Biometrics & Habits Entry`<br>2. `Periodic Clinical Labs Entry` | • Validación en tiempo real de admisibilidad fisiológica por sexo (`UiNumberField` notice)<br>• Cálculo en vivo de hidratación acumulada | • **8 inputs izquierda:** `Body Weight`, `Blood Pressure`, `Resting Heart Rate`, `Core Body Temp`, `Hydration Intake`, `Caloric Intake`, `Daily Exercise`, `Work Shift`<br>• **2 botones radio:** `IVA` / `EVA`<br>• **Botón submit:** `Save Daily Vitals & Habits`<br>• **4 inputs derecha:** `Fasting Blood Glucose`, `Hemoglobin`, `Urine Specific Gravity`, `Oxygen Saturation (SpO₂)`<br>• **Botón submit:** `Save Clinical Lab Results`<br>• 12 botones **`?`** (uno por cada campo) |
| **`/capture/vision`** (`pages/capture/vision.vue` + `SandraVisualBatteryModal.vue`) | `ShellCaptureTabs`<br>1. `Ocular Ultrasound & Visual Battery Entry`<br>2. `Interactive Visual Battery & Probe Guide` | • Detección en vivo de umbral `ONSD` vs baseline<br>• Resumen de estado batería visual (`Acuity`, `Amsler`, `Symptoms`, triage SANS)<br>• Guía axial `3.0 mm` (`AI Used`) y 3 pasos | • **6 inputs izquierda:** `Left/Right Optic Nerve Sheath`, `Left/Right Intraocular Pressure`, `Retinal Layer Thickness`, `Visual Acuity`<br>• 6 botones **`?`**<br>• **Botón submit:** `Save Vision & Ocular Exam`<br>• **Botones hito `EXAM_MILESTONES`** en tarjeta derecha<br>• **Botón `Launch Fullscreen Visual Battery` / `Expand & Resume Visual Battery`** → abre `SandraVisualBatteryModal`:<br>  - Header modal: selector milestones, `AUDIO HUD`/`MUTED`, `Clinical Report`, `Minimize`, `Exit`<br>  - Sub-tabs modal: `Module Menu`, `1 · Visual Acuity` (calibración pantalla + botones dirección/teclado), `2 · Amsler Grid` (selector `OD`/`OS`, herramientas `metamorphopsia`/`scotoma`/`eraser`, timer `30s`), `3 · Symptom Questionnaire` (13 preguntas en 4 bloques)<br>  - Pie modal: `Reset Session`, `Review Summary & Apply`, `Save Exam Now`, `Print Log`, `Apply & Minimize to Form` |
| **`/capture/psych-sleep`** (`pages/capture/psych-sleep.vue`) | `ShellCaptureTabs`<br>1. `Behavioral & Sleep Window Entry`<br>2. `Motor & Reaction Test Capture` | • Cálculo automático de duración de ventana de sueño (`Xh Ym window`)<br>• Timer `02:00`, ensayos, latencia previa, falsos arranques, `Mean reaction time`, `Motor hit precision` | • **4 botones radio estado:** `Calm`, `Focused`, `Tired`, `Stressed`<br>• **20 botones radio escalas (1–5 × 4):** `Overall Mood`, `Perceived Stress`, `Sense of Isolation`, `Mission Motivation`<br>• **2 inputs UTC:** `Sleep onset (UTC)`, `Wake time (UTC)`<br>• **Botón submit:** `Save Behavioral & Sleep Log`<br>• **Área táctil/teclado arena PVT** (`role="button"`, Space/Enter/Tap)<br>• **Botones:** `Start 2-Min Reaction Test`, `Save Motor Session`<br>• 7 botones **`?`** |
| **`/guide`** (`pages/guide.vue`) | 1. Barra de búsqueda y temas<br>2. `Care Protocol` o `Emergency Index`<br>3. `Medical Kit Locator` | • Pasos numerados de protocolo (con watermark `AI Used` si `assisted`), caja roja `Escalate immediately to...`<br>• Cajones del botiquín (`DRAWER ... · ACTIVE`) y lista de insumos/estado | • **Input buscador** por síntoma<br>• **Botón `Search Guide`**<br>• **Botón crítico `Emergency Index`**<br>• **Botones pill de categorías** (toggle filtro)<br>• **Botones lista `Emergency Index`** (abren protocolo)<br>• **Botón `Illuminate Drawer X Light`** (activa estado 30 s) |
| **`/comms`** (`pages/comms.vue`) | 1. `Flight Surgeon Messages · Houston`<br>2. `Solar Weather & Cabin Radiation`<br>3. `Transmission Log` | • Mensajes con estado (`NEW`, `CONFIRMED`, `ARCHIVED`)<br>• 2 `ArcGauge`: `Solar Activity` (`Kp`) y `Cabin Radiation` (`mSv / day`) + pronóstico 48h y dosis de misión<br>• Bitácora de paquetes (`UTC`, título, estado `QUEUED`/`IN TRANSIT`/`DELIVERED`) | • **Botón `CONFIRM READ`** en mensajes `NEW`<br>• **Botón `Send Daily Crew Summary to Houston`**<br>• 3 botones **`?`** (`solar_activity`, `radiation_daily_msv`, `radiation_mission_dose`) |
| **`/notifications`** (`pages/notifications.vue`) | `ShellSubnavTabs` + píldora `QUIET HOURS`<br>Vista estándar: `Recent Notifications` + `Recommended Care`<br>Vista `Pending Reviews` *(solo `PHYSICIAN`)*: `Assisted Findings Awaiting Review` + `Physician Review` | • Tarjetas de avisos (`ADVISORY`, `SCHEDULED`, `MISSION_CONTROL`), watermark `AI Used` si proviene de patrón revisado<br>• 3 pasos preventivos interactivos con marca de hora UTC<br>• En `Pending Reviews`: resumen LLM (`AI Used`), pasos sugeridos y métricas top | • **Filtros `SubnavTabs`:** `All (N)`, `Health Advisories (N)`, `Scheduled Checks (N)`, y `Pending Reviews (N)` *(solo `PHYSICIAN`)*<br>• En lista izquierda: botón **`View Care Plan` / `Selected`** (`ADVISORY`), link **`Open Capture`** (`SCHEDULED` → `/capture/physical`), link **`View`** (`MISSION_CONTROL` → `/comms`)<br>• En panel derecho: **3 botones de paso preventivo** (marcan completado), botón **`Acknowledge Advisory`**, botón **`Open Medical Guide`** (`/guide?article=...`)<br>• En `Pending Reviews` (`PHYSICIAN`): selector de hallazgo, `textarea` `Physician note (optional)`, y botones **`Approve & Notify`**, **`Add to Guide`**, **`Reject`** |
| **`/crew-management`** (`pages/crew-management.vue`) *(Solo `OPERATOR`)* | `ShellProfileTabs`<br>1. `Crew Roster & Access`<br>2. `Add Crew Member`<br>3. `Mission Stage` | • Lista de perfiles (`code`, `full_name`, rol, sexo, edad, estado `ACTIVE`/`INACTIVE`/`LOCKED`)<br>• Etapa actual (`LAUNCH` / `MISSION` / `RETURN`) | • Por tripulante: botón **`Unlock`** *(si bloqueado)*, botón **`Deactivate` / `Activate`**<br>• Formulario creación: inputs `Crew ID`, `4-Digit PIN`, `Full Name`, `Position`, `Age`, 4 botones radio `Role` (`ASTRONAUT`, `PILOT`, `OPERATOR`, `PHYSICIAN`), botón **`Create Crew Profile`**<br>• Botón doble confirmación **`Start mission/return stage`** |

---

## 5. Notas Previas Existentes en `docs/miWork/docs/` Relacionadas con Priorización de Vista Principal

Durante el relevamiento documental se detectaron notas previas del equipo en [`docs/miWork/docs/correcciones de testers.md`](../miWork/docs/correcciones%20de%20testers.md) y [`docs/miWork/docs/Mejoras y Correciones.md`](../miWork/docs/Mejoras%20y%20Correciones.md) que impactan directamente qué indicadores mantener o priorizar en `Profile`:

1. **En `Personal Data` (`/profile/personal` — Ventana `Personal Biometrics`):**
   - `correcciones de testers.md` registra observaciones sobre **eliminar o reubicar**: `Bone Density` (`bone_density_g_cm2`), `Muscle Mass` (`muscle_mass_kg`, proponiendo mostrarla solo pre/post misión en tierra) y `Aerobic Capacity` (`vo2_max_ml_kg_min`), y en su lugar **añadir tiempo de ejercicio aeróbico y de fuerza** al perfil. *(Actualmente las 6 tarjetas siguen activas en `profile_service.py` líneas 80–114 y `pages/profile/personal.vue` líneas 32–95).*
2. **En `Personal Data` (`/profile/personal` — Ventana `Biometric Scan`):**
   - `Mejoras y Correciones.md` mencionaba quitar animación de scanner al cuerpo *(actualmente `HoloFigure.vue` solo aplica `drop-shadow` `.hologram-shell`, sin animación CSS `.hologram-scanline`)*.
3. **Diferenciación por Rol (`Mejoras y Correciones.md`):**
   - Se listaron requisitos para análisis específico por rol (`Piloto`: retención, atención, focus; `Médico`: acceso a historial de todos los tripulantes; `Control a tierra`: gestión y recepción remota). *(En la UI actual de `Profile` todos los roles ven su propio perfil personal y solo `OPERATOR` ve el botón `Crew Administration` y `PHYSICIAN` ve `Pending Reviews` en `/notifications`).*
