# Guía del Reto y Evaluación: NASA International Space Apps Challenge

> **Reto Oficial:** [Create Health Monitoring Software for Astronauts on Space Missions](https://www.spaceappschallenge.org/2026/challenges/health-monitoring-software/?tab=details)  
> **Guía Oficial de Juzgamiento y Premios:** [NASA Space Apps Challenge - Judging & Awards Guide](https://www.spaceappschallenge.org/resources/judging-awards-guide/)  
> **Página Oficial de Premios:** [NASA Space Apps Challenge - Awards](https://www.spaceappschallenge.org/awards/)  
> **Propósito:** Documento unificado y estructurado exclusivamente con la información oficial del reto, las reglas de entrega de la guía de evaluación y las 10 categorías de premios globales de la NASA.

---

## 1. El Reto Oficial: Create Health Monitoring Software for Astronauts on Space Missions

* **Título del Reto:** *Create Health Monitoring Software for Astronauts on Space Missions* (Crear Software de Monitoreo de Salud para Astronautas en Misiones Espaciales).
* **Enlace oficial:** [Ver detalles del reto en Space Apps Challenge](https://www.spaceappschallenge.org/2026/challenges/health-monitoring-software/?tab=details)
* **Nivel de Dificultad:** Intermedio (*Intermediate*).
* **Áreas Temáticas:** Exploración Humana (*Human Exploration*), Software y Exploración Espacial (*Space Exploration*).

### 1.1 Contexto y Antecedentes (The Background)
Las misiones de exploración a espacio profundo —como el programa **Artemis** (retorno a la Luna) y futuras misiones tripuladas a **Marte**— implican periodos prolongados lejos de la Tierra en entornos hostiles.

El Programa de Investigación Humana de la NASA (*Human Research Program*) clasifica los riesgos del vuelo espacial en **5 grandes peligros (*The 5 Hazards of Human Spaceflight*)**:
1. ☢️ **Radiación Espacial (*Space Radiation*):** Mayor exposición a rayos cósmicos galácticos y eventos de partículas solares, incrementando riesgos oncológicos y daño celular.
2. 🧘 **Aislamiento y Confinamiento (*Isolation and Confinement*):** Espacios reducidos con la misma tripulación durante meses/años, lo que provoca fatiga cognitiva, estrés, alteración del sueño y cambios en el estado de ánimo.
3. 📡 **Distancia de la Tierra (*Distance from Earth*):** Retrasos significativos en las comunicaciones (de varios minutos hasta más de 20 minutos por trayecto hacia Marte). **El control de misión terrestre no puede ofrecer telemedicina en tiempo real ante una emergencia médica.**
4. 🌌 **Campos de Gravedad Alterados (*Altered Gravity Fields*):** Microgravedad que causa pérdida progresiva de masa muscular (atrofia), disminución de densidad ósea (osteopenia espacial), redistribución de fluidos y alteraciones cardiovasculares.
5. 🛡️ **Entornos Cerrados y Hostiles (*Hostile Closed Environments*):** Calidad del aire, acumulación de CO₂, control de temperatura/humedad y proliferación microbiológica en hábitats herméticos.

> **El Problema Clave:** En el espacio profundo, los astronautas son sus propios médicos de primera respuesta. Necesitan herramientas autónomas que les permitan detectar a tiempo deterioros físicos y psicológicos sin depender de la Tierra.

### 1.2 Objetivos Principales del Reto (The Challenge Goals)
El objetivo central es diseñar y desarrollar una aplicación de software interactiva y fácil de usar que permita:
1. **Recolección Integral de Indicadores de Salud (*Data Gathering*):** Capturar datos tanto fisiológicos (ritmo cardíaco, presión, temperatura, glucosa, masa muscular, etc.) como psicológicos y conductuales (sueño, estrés, estado de ánimo).
2. **Autoevaluación Intuitiva (*Self-Assessment*):** Traducir variables médicas complejas en gráficos y semáforos claros para que el astronauta identifique instantáneamente si sus valores están en rango seguro o en degradación.
3. **Recomendaciones de Acción (*Actionable Guidance*):** Sugerir protocolos preventivos, rutinas de ejercicio compensatorio, ajustes nutricionales o descanso cuando se detecten riesgos.
4. **Operación Autónoma (*Autonomous Operation*):** Funcionar localmente sin requerir conexión constante a internet o a servidores terrestres.

### 1.3 Consideraciones Potenciales de Diseño (Potential Considerations)
Para destacar en la solución, la NASA sugiere considerar los siguientes aspectos:
* **Entornos Operativos Diversos:** La herramienta debe ser útil dentro de la nave espacial en tránsito, en la estación orbital, en rovers de exploración o en hábitats de superficie lunar/marciana.
* **Entradas de Datos y Rutinas Periódicas (*Data Inputs & Routine Prompts*):**
  * *Texto oficial de la NASA en la sección "Potential Considerations":*
    > *"Data can be gathered through various inputs (e.g., keyboard, mouse, or camera) to track health indicators... Your tool could provide prompts for astronauts to take measurements from time to time as part of their routine."*  
    *(Los datos pueden recopilarse a través de varias vías como teclado, ratón o cámara para rastrear indicadores de salud... Su herramienta podría ofrecer recordatorios para que los astronautas tomen mediciones periódicamente como parte de su rutina).*
  * *Métricas específicas que la NASA menciona en el reto:* Presión arterial, frecuencia cardíaca, glucosa en sangre, temperatura corporal, horas de sueño diarias, estado anímico e imágenes médicas (como ultrasonidos).
* **Salud Mental y Conductual (*Behavioral Health*):** No limitarse solo a constantes vitales; el monitoreo del sueño, estado anímico, motivación y niveles de estrés es igual de crítico para la supervivencia de la misión.
* **Adherencia y Gamificación (*User Engagement*):** Incorporar mecánicas interactivas, interfaces limpias o dinámicas que motiven a los astronautas a registrar sus datos a diario a pesar del cansancio o la alta carga de trabajo.

---

## 2. Reglas Oficiales de Entrega y Elegibilidad (Judging & Awards Guide)

Esta sección resume las reglas oficiales extraídas de la **Judging & Awards Guide** de la NASA. Seguir estas reglas al pie de la letra es fundamental para que el proyecto no sea descalificado.

### 2.1 Requisitos de Elegibilidad para el Jurado
* **Alineación con el reto:** El proyecto debe responder de forma directa y explícita a la consigna oficial del desafío elegido.
* **Registro de miembros:** Todos los miembros del equipo deben estar registrados en la plataforma de NASA Space Apps antes de que venza el plazo de entrega. No se permite añadir ni cambiar integrantes después del cierre.
* **Tamaño del equipo:**
  * Para eventos locales (*Local Events*): De 1 a 6 integrantes.
  * Para el evento universal (*Universal Event*): De 2 a 6 integrantes.
* **Uso explícito de datos espaciales abiertos:** Es **obligatorio** citar y explicar qué recursos, APIs, datos o modelos de la NASA o de sus agencias asociadas (ESA, JAXA, CSA, CNES) fueron utilizados.

### 2.2 Formato Obligatorio de la Demo del Proyecto (Project Demo)
Para que los jueces puedan evaluar el proyecto rápidamente, la NASA exige **elegir estrictamente UNO de los dos siguientes formatos**:

| Formato | Límite Máximo Estricto | Idioma y Subtítulos | Requisitos Clave |
|---|---|---|---|
| **Opción A: Presentación de Diapositivas** (*Slide Deck*) | **Máximo 7 diapositivas** | Escrito completamente en **Inglés** | Incluye portada y créditos. Si tiene 8 diapositivas, las diapositivas extra son ignoradas o penalizadas. |
| **Opción B: Video Demostrativo** (*Video Presentation*) | **Máximo 30 segundos** | Cualquier idioma, pero **obligatorio con subtítulos en Inglés** | Debe ser un enlace público a YouTube o Vimeo. Si dura 31 segundos, se corta en el segundo 30. |

> [!IMPORTANT]
> **Alojamiento y Permisos Públicos:**  
> La plataforma de la NASA **no almacena archivos de video ni presentaciones**. Debes alojarlos en un servicio externo (YouTube para videos, Google Drive/OneDrive/Canva para diapositivas, GitHub para código) y asegurarte de que el enlace sea **100% público** (que cualquiera con el enlace pueda abrirlo sin iniciar sesión ni pedir permisos).

---

## 3. Resumen de las 10 Categorías de Premios Globales (Global Awards)

Cada año, el comité ejecutivo de expertos de la NASA y de las agencias espaciales asociadas evalúa los proyectos nominados en todo el mundo y otorga **10 premios globales**:

| # | Categoría (Oficial en Inglés) | Nombre en Español | Descripción Oficial del Premio |
|---|---|---|---|
| 1 | **Best Use of Science** | Mejor Uso de la Ciencia | Al proyecto que haga el mejor y más válido uso de la ciencia y/o del método científico. |
| 2 | **Best Use of Data** | Mejor Uso de Datos | Al proyecto que mejor facilite el acceso a los datos espaciales o los aproveche para una aplicación única. |
| 3 | **Best Use of Technology** | Mejor Uso de la Tecnología | Al proyecto que ejemplifique el uso más innovador de la tecnología. |
| 4 | **Galactic Impact** | Impacto Galáctico | Al proyecto con el mayor potencial para mejorar la vida en la Tierra o en el universo. |
| 5 | **Best Mission Concept** | Mejor Concepto de Misión | Al proyecto con el concepto y diseño de misión más verosímil, viable y estructurado. |
| 6 | **Most Inspirational** | El Más Inspirador | Al proyecto que capture los corazones y conmueva la imaginación del jurado y la comunidad. |
| 7 | **Best Use of Storytelling** | Mejor Uso de la Narrativa | Al proyecto que comunique más creativamente el potencial de los datos abiertos mediante el arte de contar historias. |
| 8 | **Global Connection** | Conexión Global | Al proyecto que mejor conecte a personas de todo el mundo mediante la tecnología. |
| 9 | **Art & Technology** | Arte y Tecnología | Al proyecto que combine de la manera más efectiva habilidades técnicas con artes creativas. |
| 10 | **Local Impact** | Impacto Local | Al proyecto que demuestre el mayor potencial para resolver problemas locales o beneficiar a una comunidad específica. |

---

## 4. Detalle de Cada Categoría y Qué Busca el Jurado

### 1. Best Use of Science (Mejor Uso de la Ciencia)
* **Objetivo:** Demostrar rigor científico en la solución.
* **Qué buscan los jueces:** Modelos basados en física, medicina, biología o matemáticas sólidas; uso correcto del método científico (hipótesis, experimentación, validación) y precisión teórica.
* **Aplicación ideal:** Proyectos de investigación médica, simulaciones físicas o análisis orbital.

### 2. Best Use of Data (Mejor Uso de Datos)
* **Objetivo:** Poner en valor los datos abiertos de la NASA y agencias asociadas.
* **Qué buscan los jueces:** Cómo el equipo procesó, limpió, estructuró o visualizó datos satelitales o telemétricos complejos, haciéndolos comprensibles o usables para el usuario común o para científicos.
* **Aplicación ideal:** Dashboards, procesadores de datos crudos o modelos predictivos.

### 3. Best Use of Technology (Mejor Uso de la Tecnología)
* **Objetivo:** Innovación y maestría en la implementación técnica.
* **Qué buscan los jueces:** Arquitectura técnica bien diseñada, interfaces funcionales, uso inteligente de hardware/software, prototipos interactivos funcionales.
* **Aplicación ideal:** Sistemas de software en tiempo real, prototipos de sensores, apps de alta interactividad.

### 4. Galactic Impact (Impacto Galáctico)
* **Objetivo:** Trascendencia y escalabilidad de la solución.
* **Qué buscan los jueces:** Proyectos que resuelvan un reto crítico tanto para la exploración espacial como para la vida en la Tierra (doble propósito / tecnología dual).
* **Aplicación ideal:** Soluciones de telemedicina para astronautas que también sirvan en zonas remotas de la Tierra.

### 5. Best Mission Concept (Mejor Concepto de Misión)
* **Objetivo:** Factibilidad y visión de ingeniería.
* **Qué buscan los jueces:** Que la propuesta no sea solo una idea abstracta, sino un plan de misión estructurado, técnicamente plausible, con fases operativas claras y análisis de riesgos.
* **Aplicación ideal:** Misiones espaciales tripuladas, protocolos de supervivencia y monitoreo en bases lunares o marcianas.

### 6. Most Inspirational (El Más Inspirador)
* **Objetivo:** Conexión emocional y visión humana.
* **Qué buscan los jueces:** Proyectos que aborden temas de inclusión, superación humana, salud mental en aislamiento o divulgación accesible.
* **Aplicación ideal:** Proyectos centrados en la salud integral y el bienestar humano ante la adversidad.

### 7. Best Use of Storytelling (Mejor Uso de la Narrativa)
* **Objetivo:** Comunicación y empatía visual/narrativa.
* **Qué buscan los jueces:** Un proyecto cuya presentación (video, textos, diseño interactivo) explique un problema complejo de manera atrapante, accesible y memorable.
* **Aplicación ideal:** Recorridos interactivos, visualizaciones explicativas paso a paso, experiencias guiadas.

### 8. Global Connection (Conexión Global)
* **Objetivo:** Unir a la humanidad a través de la tecnología.
* **Qué buscan los jueces:** Soluciones colaborativas, de código abierto, accesibles en múltiples idiomas y que permitan conectar personas, científicos o comunidades a nivel global.

### 9. Art & Technology (Arte y Tecnología)
* **Objetivo:** Fusión entre estética y funcionalidad técnica.
* **Qué buscan los jueces:** Interfaces visualmente deslumbrantes, modelos 3D atractivos, infografías estéticas y experiencias interactivas donde el diseño artístico potencie la comprensión técnica.

### 10. Local Impact (Impacto Local)
* **Objetivo:** Resolver problemas comunitarios o regionales.
* **Qué buscan los jueces:** Impacto directo y medible en un problema específico de una comunidad local (gestión de agua, cultivos, desastres naturales locales, etc.).

---

## 5. Las Fases del Proceso de Evaluación (Judging Pipeline)

El proceso de selección se divide en tres fases consecutivas:

```
┌─────────────────────────────────────────────────────────────┐
│  Fase 1: Evaluación Local (Local / Universal Event Judging) │
│  - Los jueces locales evalúan los proyectos de cada sede.   │
│  - Se seleccionan los "Global Nominees" (Nominados Globales)│
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  Fase 2: Evaluación Global (Global Judging)                 │
│  - Expertos de NASA, ESA, JAXA, CSA, etc., revisan nominados│
│  - Se eligen "Global Finalists" y "Menciones de Honor"      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  Fase 3: Juzgamiento Ejecutivo (Executive Judging)          │
│  - Comité directivo de NASA selecciona los 10 Ganadores     │
│  - Anuncio oficial de los "Global Winners"                  │
└─────────────────────────────────────────────────────────────┘
```

1. **Nominados Globales (Global Nominees):** Al terminar el hackathon, cada sede local nomina a sus mejores proyectos (habitualmente 1 o 2 por sede, más nominados del evento universal).
2. **Finalistas Globales (Global Finalists):** Un panel internacional de científicos e ingenieros reduce los miles de nominados a unos 30-40 finalistas mundiales.
3. **Ganadores Globales (Global Winners):** El comité ejecutivo elige a un ganador por cada una de las 10 categorías (10 proyectos ganadores a nivel mundial).

---

## 6. Criterios de Evaluación Oficiales (Evaluation Criteria)

Los jueces califican cada proyecto basándose en 5 pilares fundamentales:

1. **Impacto (Impact):** ¿Qué tan grande es el problema que aborda? ¿Qué tan significativa y positiva sería la solución si se implementa en la realidad?
2. **Creatividad (Creativity):** ¿Qué tan novedoso, ingenioso o innovador es el enfoque del equipo? ¿Ofrece algo diferente a las soluciones convencionales?
3. **Validez Científica (Validity):** ¿La solución tiene rigor científico? ¿Usa de forma correcta los principios de física, medicina, astronomía y el método científico?
4. **Relevancia (Relevance):** ¿El proyecto responde directamente a la consigna del reto y aprovecha de forma genuina los recursos y datos abiertos provistos por la NASA?
5. **Presentación (Presentation):** ¿El equipo comunica su idea con total claridad? (Incluye la redacción del proyecto, demo funcional, repositorio ordenado y el video/pitch explicativo).

---

## 7. El Gran Premio para los Ganadores Globales

Los equipos ganadores a nivel mundial reciben:
* **Reconocimiento Oficial de la NASA:** Difusión internacional en los canales oficiales de la NASA.
* **Invitación a un Centro de la NASA:** Los ganadores son invitados a visitar un centro espacial de la NASA (como el *Kennedy Space Center* en Florida o el *Goddard Space Flight Center* en Maryland).
* **Presenciar un Lanzamiento de Cohete:** Si las fechas operativas lo permiten, los integrantes del equipo tienen la oportunidad única de presenciar un despegue espacial en directo.

---

## 8. Estrategias y Recomendaciones Clave para este Reto (Basadas en las Guías Oficiales)

* 🎯 **Alineación con el Desafío:**
  * El factor diferenciador de cualquier solución para este reto es resolver la **autonomía médica**: la herramienta debe permitir a los astronautas evaluar su estado de salud sin depender de la telemedicina en tiempo real desde la Tierra debido al retraso en las comunicaciones en espacio profundo.
* 🏆 **Categorías de Premios con Mayor Afinidad:**
  * **Best Mission Concept:** Ideal si la propuesta demuestra una arquitectura de misión robusta, realista y bien estructurada para monitorear tripulaciones en misiones de larga duración (como Artemis o Marte).
  * **Best Use of Science:** Si la solución fundamenta rigurosamente los modelos fisiológicos (pérdida de masa muscular, densidad ósea, radiación espacial) usando el método científico y datos abiertos de investigación espacial.
  * **Galactic Impact:** Si se demuestra cómo esta tecnología de telemedicina autónoma no solo sirve en el espacio, sino también en zonas remotas, expediciones extremas o comunidades aisladas en la Tierra.
* 📋 **Lista de Verificación de Entrega Oficial:**
  - [ ] Página de proyecto creada en Space Apps con todos los miembros vinculados antes de la hora de cierre.
  - [ ] Demo del proyecto terminada eligiendo estrictamente una opción: o video de máx. 30 segundos con subtítulos en inglés, o presentación de máx. 7 diapositivas en inglés.
  - [ ] Enlace al código o repositorio público con licencia abierta (Open Source).
  - [ ] Sección de descripción citando explícitamente los datos abiertos de NASA / agencias espaciales asociadas utilizados.
  - [ ] Verificación de todos los enlaces externos en modo incógnito para certificar acceso 100% público sin contraseñas ni permisos restringidos.
