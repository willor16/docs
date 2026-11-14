# 🚀 Reglas Inquebrantables del Proyecto — SpaceScan

> **Reto Oficial:** NASA Space Apps Challenge 2026 — *Create Health Monitoring Software for Astronauts on Space Missions*  
> **Prioridad Normativa:** Este documento contiene las directrices de cumplimiento obligatorio para todo el equipo. Tiene precedencia sobre cualquier nota o borrador previo.

---

## 1. ⭐ Regla de Oro — Los 10 Criterios de Premios Globales

> **Obligatorio:** Cada módulo, pantalla, dato, decisión, tarea o commit **debe satisfacer los 10 criterios** listados a continuación.  
> Si algún elemento no aporta a ellos, se replantea antes de implementarlo.  
> **Fuentes Oficiales:** [Space Apps — Awards](https://www.spaceappschallenge.org/awards/) y [Judging & Awards Guide](https://www.spaceappschallenge.org/resources/judging-awards-guide/).

| # | Premio Oficial | Qué Evalúa el Jurado | Cómo lo Cumple SpaceScan |
| :--- | :--- | :--- | :--- |
| **1** | **Best Use of Data** | El proyecto que mejor hace accesibles los datos espaciales o los aprovecha en una aplicación única. | Integración de datasets reales de fuentes espaciales abiertas (OSDR/GeneLab, DONKI) además de datos simulados, visualizados con claridad y exportables en JSON. |
| **2** | **Best Use of Science** | El uso más válido y riguroso de la ciencia y/o del método científico. | Rangos clínicos de referencia (`metric_catalog`), cálculo de desviación (*z-score*) contra línea base personal y frecuencias de medición respaldados por fuentes científicas citadas. |
| **3** | **Best Use of Technology** | El uso más innovador de la tecnología. | Detección temprana de anomalías mediante Red Neuronal convencional + interpretación clínica con LLM local (`Ollama` / `llama.cpp`), operando 100% sin conexión con la Tierra. |
| **4** | **Best Use of Storytelling** | Comunicar de forma creativa el potencial de los datos abiertos mediante una narrativa sólida. | Articular la narrativa médica en las 3 etapas de la misión: **Antes (Despegue) / Durante (Misión) / Después (Regreso)** tanto en la interfaz como en la demo y el video. |
| **5** | **Best Mission Concept** | El concepto y diseño de misión más verosímil, viable y estructurado. | Respetar restricciones reales de vuelo espacial: radiación, muestras limitadas de sangre/orina, alta latencia de comunicación (cola diferida tipo DTN) y recursos de cómputo acotados a bordo. |
| **6** | **Galactic Impact** | El mayor potencial para mejorar la vida en la Tierra o en el universo. | Arquitectura de doble propósito: monitoreo autónomo en espacio profundo y aplicación directa en telemedicina remota en la Tierra. |
| **7** | **Global Connection** | El proyecto que mejor conecta a personas de todo el mundo mediante la tecnología. | Código abierto con licencia MIT en repositorio público, contratos OpenAPI y exportación de paquetes médicos en formato estándar (JSON). |
| **8** | **Local Impact** | El proyecto que demuestra el mayor potencial para resolver problemas locales o beneficiar a una comunidad específica. | Operación completamente offline y en hardware accesible para centros de salud rurales, comunidades aisladas o brigadas médicas sin conectividad. |
| **9** | **Most Inspirational** | El proyecto que captura los corazones y pone el factor humano en el centro. | Enfoque integral en el bienestar humano: seguimiento de ánimo, soledad, motivación, protección del sueño (*Quiet Hours*) y rachas grupales/individuales. |
| **10** | **Art & Technology** | Combinar de la manera más efectiva habilidades técnicas con diseño y artes visuales. | Fidelidad absoluta al sistema de diseño en Figma, visualizaciones clínicas de alto contraste, hologramas SVG/CSS y gráficas ECharts personalizadas. |

### Checklist de Validación (Aplicar a TODO Entregable y Pull Request)

- [ ] **1. Best Use of Data** — ¿Usa o hace accesibles datos espaciales reales?
- [ ] **2. Best Use of Science** — ¿Está respaldado por ciencia y fuentes citadas en el catálogo de métricas?
- [ ] **3. Best Use of Technology** — ¿La implementación tecnológica aporta innovación real y funciona offline?
- [ ] **4. Best Use of Storytelling** — ¿Se integra claramente en la historia Antes / Durante / Después de la misión?
- [ ] **5. Best Mission Concept** — ¿Es plausible dentro de las restricciones reales de una nave o hábitat espacial?
- [ ] **6. Galactic Impact** — ¿Demuestra utilidad dual en el espacio y en la Tierra?
- [ ] **7. Global Connection** — ¿Es abierto, documentado y usa formatos estándar interoperables?
- [ ] **8. Local Impact** — ¿Es aplicable en comunidades aisladas o clínicas rurales sin internet?
- [ ] **9. Most Inspirational** — ¿Pone a la persona y su bienestar físico/emocional en el centro?
- [ ] **10. Art & Technology** — ¿Se ve y se siente fiel al diseño de Figma con excelente acabado visual?

---

## 2. Etapas de la Misión (Objetivos 1–3)

Todo registro, análisis y visualización de salud se estructura a través de las **3 etapas operativas**:
1. **Antes del despegue (*Takeoff / Pre-flight*):** Establecimiento de la línea base individual (*baseline*) y aptitud previa.
2. **Durante la misión (*In-Mission*):** Monitoreo continuo en microgravedad/espacio profundo, detección de anomalías y contramedidas.
3. **Después / Regreso (*Return / Post-flight*):** Evaluación de readaptación fisiológica y recuperación.

---

## 3. Clasificación de Datos a Recolectar

> El detalle exhaustivo de cada variable se rige por [`ESPECIFICACION_REQUERIMIENTOS.md`](./ESPECIFICACION_REQUERIMIENTOS.md).

### 3.1 Datos Biométricos y de Entorno Base
* Marca temporal (UTC)
* Edad y Sexo
* Estatura y Peso
* Índice de Masa Corporal (IMC)
* Retención de masa muscular
* Densidad ósea
* Frecuencia cardíaca y Presión arterial
* Ruido ambiental de cabina (verificación previa a auscultación e impacto clínico)

### 3.2 Datos Directos de Misión

| Captura Manual | Captura Automática (Sensores / Telemetría) |
| :--- | :--- |
| Glucosa en sangre | Temperatura corporal y de cabina |
| Auscultaciones (cardíaca y pulmonar de 30 s) | Humedad y $\text{CO}_2$ de cabina |
| Parámetros de sangre | Tiempo transcurrido de misión |
| Parámetros de orina | Tiempo de trabajo/esfuerzo (interior y exterior/EVA) |
| Exámenes neuro-oculares bilaterales (SANS) | Saturación de oxígeno ($\text{SpO}_2$), FC, HRV, ECG |
| Pruebas cognitivo-motrices (reacción y precisión) | Minutos y carga de ejercicio físico |

### 3.3 Datos Indirectos y Conductuales
* Estado de ánimo
* Sueño (duración, eficiencia y etapas: Profundo, REM, Ligero, Despierto)
* Nivel de estrés
* Soledad / Aislamiento percibido
* Motivación
* Alimentación (ingesta calórica)
* Hidratación

---

## 4. Fidelidad Estricta al Diseño (Figma) y las 5 Leyes UI/UX

> La especificación visual completa, la paleta oficial de 6 colores y el mapeo de las 16 pantallas se rigen por [`REGLAS_DISENO_UI_UX.md`](./REGLAS_DISENO_UI_UX.md).

* **Diseño Oficial en Figma (`1568 × 940`):** [SpaceScan — Figma Design (`node-id=7382-2`)](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2&t=tzbC2RhJeGZ2Dlov-1)
* **Paleta Oficial Única de 6 Colores (`tokens.css`):** `#001524` (Fondo Principal), `#15616D` (Tarjetas y Botones), `#FFECD1` (Texto e Iconos), `#2AEF4B` (Estado OK/Nominal), `#000C5C` (Selección activa en menús/filtros al 30%–52% opacidad con filete `#263BB0`, líneas guía, pastillas de referencia y Warning) y `#D5110B` (Estado Crítico/Alerta).
* **Separación Estricta Resultados vs. Captura:** Las pantallas de monitoreo (`Profile`, `Sleep`, `Vision`, `Auscultation`, `Crew Overview`, `Crew Streaks`) son **100% de solo lectura (Solo Resultados)**; toda entrada manual, grabación de 30 s o prueba psicomotriz vive exclusivamente en **`Capture`** (`/capture/*`).
* **Jerarquía de Navegación en 2 Niveles:**
  * **Público (sin PIN):** Barra inferior de 3 pestañas (`Sign In · Crew Overview · Crew Streaks`).
  * **Autenticado (tras PIN):** Dock inferior trapezoidal simétrico de 7 módulos con **`Profile` elevado al centro exacto** (`1 Vision · 2 Sleep · 3 Auscultation · [4 PROFILE] · 5 Capture · 6 Guide · 7 Comms`), y **`Notifications (N)` únicamente en el header superior**.
* **Densidad Controlada:** Máximo 2 o 3 contenedores `<HudWindow>` por pantalla (`28 px` margen exterior, `18 px` gap), sin footers informativos redundantes.

---

## 5. Flujo de Trabajo Oficial por Roles

1. **Investigadores (Datos — Independiente de Devs):**
   * $$\text{Investigar} \longrightarrow \text{Filtrar} \longrightarrow \text{Estructurar en JSON}$$
2. **Desarrolladores (3 Devs Fullstack):**
   * Implementación de punta a punta por módulo: `Tablas SQLite + Endpoints FastAPI + Pantallas Nuxt`.
3. **Validadores:**
   * $$\text{Módulo Terminado} \longrightarrow \text{Revisión contra Checklist y Especificación} \longrightarrow \text{OK}$$
   * *Si no aprueba la revisión, regresa a Devs antes de integrarse.*
4. **Testers:**
   * $$\text{Git Clone} \longrightarrow \text{Pruebas de flujo completo contra backend real}$$

---

## 6. Regla Estricta de Idioma (100% Inglés en Interfaz y Código + Cero Jerga Técnica en UI)

* **Exclusividad de Idioma:** La aplicación, su interfaz de usuario, catálogos de datos, textos clínicos, protocolos de la Wiki, alertas y entregables deben estar **estrictamente en inglés**.
* **Cero mezcla de idiomas (Incluye el Código):** No debe integrarse ningún otro idioma en el software entregable; **ni una sola palabra en español u otro idioma** dentro de la aplicación, **esto incluye el código** (variables, funciones, rutas, endpoints, tablas, comentarios y componentes).
* **Cero Jerga Tecnológica Interna en Pantalla:** Prohibido mostrar en la interfaz palabras técnicas de infraestructura o protocolos internos como `SQLite`, `JSON`, `FHIR`, `HL7`, `Kiwix`, `ZIM`, `FTS5`, `WAL`, `Offline`, `Break-Glass`, `DTN`, `OSDR`, `DONKI`, `ONNX`, `Ollama`, `Nuxt` o `Python`. El astronauta solo ve información clínica y operativa limpia.

---

## 7. Palabras y Referencias Prohibidas

* **Restricción Absoluta de Marca y Geopolítica:**
  1. **Prohibición total respecto a "NASA" en el producto/interfaz:** El producto/interfaz **no debe usar de ninguna forma el nombre o marca "NASA"; esto incluye el nombre, logos y menciones de ningún tipo**.
  2. **Prohibición absoluta respecto a China:** El proyecto no debe contener mención alguna, datos, agencias, modelos ni referencias relacionadas directa o indirectamente con **China** (cumplimiento estricto de las políticas de elegibilidad del evento).
