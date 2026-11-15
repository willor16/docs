# Especificación de Requerimientos — SpaceScan

## 1. Objetivos y Alcance

### 1.1 Objetivo General
Captura, análisis e interpretación de datos orientados exclusivamente a la salud general de todos los tripulantes (excluyendo datos operativos o externos ajenos a la salud).

### 1.2 Objetivos Específicos
- **Recopilación de datos por etapa:** Despegue, Misión y Regreso.
- **Diagnóstico asistido:** Entrenamiento e integración de red neuronal convencional + LLM para apoyo diagnóstico.
- **Wiki de respaldo:** Creación de una Wiki médica de respaldo alimentada mediante los datos obtenidos previamente.

---

## 2. Actores y Roles

- **Astronauta:** Tripulante base sujeto al monitoreo integral de salud general en Despegue, Misión y Regreso; registra sus mediciones y consulta su estado personal y grupal.
- **Piloto:** Tripulante cuya evaluación de salud corrobora los requerimientos físicos y neurocognitivos necesarios para desempeñar sus funciones (como retención de atención, tiempo de reacción, agudeza visual y descanso).
- **Operador:** Tripulante encargado de actividades fuera de la nave cuya evaluación de salud corrobora su estado físico, cardiorrespiratorio y recuperación post-esfuerzo; además, gestiona usuarios de forma local.
- **Médico:** Oficial médico a bordo que, además de su propio monitoreo, supervisa los indicadores clínicos, alertas y diagnósticos de la tripulación y atiende escalamientos de salud.
- **Control a tierra:** Equipo remoto que recibe de forma asíncrona (sin inicio de sesión en cabina) los resúmenes y registros de salud de la tripulación, emite directrices médicas y gestiona usuarios de forma remota.

> **Niveles de acceso en cabina:** Consulta pública sin sesión para resumen general de salud y rachas de tripulación; acceso mediante selección de perfil y PIN de 4 dígitos para módulos individuales y gestión local.

---[Texto del enlace](https://www.nasa.gov)

## 3. Requerimientos Funcionales (RF)

### 3.1 Gestión de Usuarios y Acceso
- **Creación y gestión de usuarios (Operador local y Control a tierra):** Alta, edición y baja/desactivación de perfiles de tripulantes con datos base pre-misión, rol (`Astronauta`, `Piloto`, `Operador`, `Médico`) y PIN de 4 dígitos, ejecutable localmente por el `Operador` y de forma remota/asíncrona por `Control a tierra`.
- **Inicio de sesión con perfil y PIN / Acceso público en cabina:** Selección visual de perfil (con indicador de estado general de salud) e ingreso de PIN de 4 dígitos para acceder a módulos individuales y cerrar sesión; acceso directo sin sesión a la vista general de salud y a las rachas de tripulación.

### 3.2 Vista General de Salud y Rachas de Tripulación
- **Resumen grupal de salud:** Visualización pública del estado global por tripulante (*Óptimo / Nominal / Atención*), signos clave recientes (frecuencia cardíaca, HRV, sueño en 24 h y SpO₂) y variables ambientales de cabina con impacto directo en la salud (CO₂, ruido, temperatura y humedad).
- **Rachas de constancia:** Visualización de rachas individuales y racha grupal de días consecutivos cumpliendo registros y hábitos de salud, incluyendo racha activa, mejor marca personal e historial de los últimos 7 días.

### 3.3 Perfil de Salud del Tripulante (Despegue, Misión y Regreso)
- **Comparativa por etapa y línea base:** Consulta del historial del tripulante segmentado por *Despegue*, *Misión* y *Regreso*, contrastando cada indicador contra su línea base personal.
- **Datos personales y biométricos:** Consulta de edad, sexo, tipo de sangre, estatura, peso, IMC, retención de masa muscular, densidad ósea y capacidad aeróbica (VO₂ máx).
- **Estado psicológico:** Consulta del índice global de bienestar, métricas de ánimo, estrés, soledad y motivación, tendencia de los últimos 14 días y desempeño cognitivo-motriz.
- **Estado físico y clínico:** Consulta de signos vitales (frecuencia cardíaca en reposo, presión arterial, SpO₂, temperatura corporal, ECG y HRV), cumplimiento diario de hábitos (ejercicio, hidratación y calorías) y últimos resultados de glucosa, sangre, orina, visión y auscultación.

### 3.4 Toma y Captura de Datos de Salud
- **Ingesta manual y automática:** Captura guiada de mediciones manuales y recepción automática de sensores con marca temporal y etapa de misión, actualizando de inmediato el perfil, las alertas y las rachas.
- **Captura de auscultación:** Grabación guiada de muestras acústicas cardíacas y pulmonares (30 s) previa verificación de ruido ambiental apto para lectura clínica.
- **Captura física, hábitos y laboratorio:** Registro diario de signos vitales, peso, hidratación, ingesta calórica y minutos de ejercicio, junto con resultados periódicos de glucosa, sangre y orina.
- **Captura ocular y psicofísica:** Registro bilateral de parámetros oculares (diámetro de vaina del nervio óptico, presión intraocular, grosor retiniano y agudeza visual), ventana de sueño, escala psicológica y prueba interactiva de atención y tiempo de reacción.

### 3.5 Módulo de Sueño
- **Indicadores de descanso:** Consulta filtrable por periodo (*última noche, 7, 14 y 30 días*) del puntaje de calidad de sueño, horas dormidas frente a la meta mínima, tiempo en cama y eficiencia de sueño.
- **Etapas y ciclos:** Desglose de duración, porcentaje e intervalos horarios por fase (*Profundo, REM, Ligero y Despierto*) para evaluar la recuperación del tripulante.

### 3.6 Evaluación Psicológica y Cognitivo-Motriz
- **Test psicológico periódico:** Registro y seguimiento estandarizado de estado de ánimo, estrés, aislamiento/soledad y motivación frente a la zona óptima individual.
- **Evaluación cognitivo-motriz:** Pruebas objetivas de retención de atención, coordinación y tiempo de reacción (latencia en ms y precisión), clave para corroborar la aptitud de salud en roles como `Piloto`.

### 3.7 Módulo de Visión y Salud Ocular
- **Seguimiento neuro-ocular bilateral:** Consulta comparativa de ojo izquierdo y derecho para diámetro de vaina del nervio óptico, presión intraocular, grosor retiniano y agudeza visual.
- **Control de riesgo visual:** Gráfica de tendencia frente a línea base y umbrales de alerta clínica, estado de revisión del `Médico` y recomendaciones preventivas.

### 3.8 Módulo de Auscultación
- **Evaluación acústica cardiorrespiratoria:** Consulta de hallazgos cardíacos (ritmicidad S1/S2, frecuencia, presencia de soplos y fonocardiograma) y pulmonares (frecuencia respiratoria, murmullo vesicular por zona y ruidos adventicios).
- **Capacidad física y entorno respiratorio:** Seguimiento de VO₂ máx, respuesta ortostática e índice cardiorrespiratorio (clave para corroborar condición física y recuperación post-esfuerzo en roles como `Operador`), junto con la tendencia de CO₂ en cabina asociada a salud respiratoria.

### 3.9 Diagnóstico Asistido (Red Neuronal Convencional + LLM)
- **Detección de patrones y anomalías (Red Neuronal Convencional):** Análisis conjunto de series biométricas, señales clínicas (ECG, auscultación, mediciones oculares) e indicadores psicofísicos para detectar desviaciones tempranas respecto a la línea base personal.
- **Interpretación clínica orientativa (LLM):** Generación en lenguaje claro de prediagnósticos asistidos, explicación de hallazgos y sugerencias preventivas basadas en el historial del tripulante, sujetas a supervisión y validación del `Médico`.

### 3.10 Guía Médica y Wiki de Respaldo
- **Protocolos de atención y emergencia:** Búsqueda por síntomas o categorías clínicas (*exposición a CO₂, visión/presión, sueño/fatiga, trauma y medicación*) con pasos secuenciales de actuación, criterios de escalamiento al `Médico` y referencia de insumos en el botiquín médico.
- **Wiki evolutiva de respaldo:** Consulta y enriquecimiento local del repositorio médico a partir de los datos, casos e interpretaciones registrados en etapas previas de la misión.

### 3.11 Notificaciones y Alertas de Salud
- **Bandeja clasificada:** Gestión de *Avisos de Salud* (anomalías frente a línea base o umbrales críticos) y *Chequeos Programados* (recordatorios de mediciones y pruebas periódicas).
- **Atención y protección del descanso:** Confirmación de lectura, acciones de cuidado recomendadas, vínculo directo al protocolo de la Wiki médica y modo de horario silencioso (*Quiet Hours*) para avisos no urgentes durante el descanso.

### 3.12 Comunicación Médica Asíncrona con Control a Tierra
- **Envío y recepción diferida:** Transmisión manual o programada de resúmenes diarios de salud y resultados clínicos hacia `Control a tierra`, y recepción asíncrona de directrices médicas remotas.
- **Estado de transmisión:** Registro de latencia estimada y trazabilidad de entrega/sincronización de cada paquete médico.

---

## 4. Requerimientos de Información (Datos)
> Información de salud en Despegue, Misión y Regreso que el sistema debe registrar y conservar.

- **Trazabilidad obligatoria:** Identificador de tripulante, marca temporal (UTC), etapa (*Despegue, Misión o Regreso*) y origen del dato (*manual o automático*) en cada medición.
- **Usuarios y línea base:** Datos demográficos (edad, sexo, tipo de sangre, estatura), rol, PIN de acceso y valores de referencia pre-misión por tripulante.
- **Biometría, signos vitales y carga física:** Peso, IMC, masa muscular, densidad ósea, VO₂ máx, frecuencia cardíaca, HRV, ECG, presión arterial, SpO₂, temperatura corporal, respuesta ortostática y tiempo de esfuerzo físico/exposición (interior y exterior).
- **Registros clínicos, oculares y acústicos:** Glucosa, parámetros de sangre y orina, diámetro de vaina del nervio óptico, presión intraocular, grosor retiniano, agudeza visual y muestras/resultados de auscultación cardíaca y pulmonar.
- **Sueño, estado psicológico, motricidad, hábitos y entorno clínico:** Duración y etapas de sueño, ánimo, estrés, soledad, motivación, tiempo de reacción y precisión motriz, ingesta calórica, hidratación y variables ambientales de cabina con impacto clínico (CO₂, ruido, temperatura y humedad).
- **Diagnósticos, Wiki y bitácoras:** Prediagnósticos e interpretaciones asistidas (RN + LLM), entradas de la Wiki médica de respaldo, alertas, rachas de cumplimiento e historial de sincronización médica con `Control a tierra`.

---

## 5. Requerimientos No Funcionales (RNF)
- **Autonomía offline y sincronización asíncrona:** Operación completa a bordo (captura, consulta, alertas, inferencia diagnóstica RN + LLM y Wiki de respaldo) sin depender de conexión continua con la Tierra, encolando paquetes médicos para transmisión diferida tolerante a alta latencia.
- **Evaluación personalizada con base científica:** Detección de desviaciones contra la línea base individual de cada tripulante y los requerimientos psicofísicos propios de su rol, respaldada por rangos clínicos de referencia.
- **Privacidad y control de acceso en cabina:** Separación entre consulta grupal sin sesión (limitada a resumen general y rachas) y acceso individual autenticado con PIN de 4 dígitos, restringiendo la gestión de usuarios a `Operador` (local) y `Control a tierra` (remota).
- **Usabilidad crítica y baja fatiga visual:** Interfaz legible de alto contraste en cabina, acceso en pocos pasos a protocolos de emergencia y respeto de horarios de sueño (*Quiet Hours*) para notificaciones no críticas.
- **Integridad y conservación histórica:** Resguardo íntegro, inalterable y trazable de todas las series temporales de salud en *Despegue*, *Misión* y *Regreso* ante cortes de enlace o reinicios del sistema.
[[Texto del enlace](https://www.nasa.gov)](https://www.nasa.gov)