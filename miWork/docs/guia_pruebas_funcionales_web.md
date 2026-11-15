# Plan de Pruebas Funcionales de la Web — SpaceScan

Guía paso a paso con casillas de verificación para validar todas las pantallas, botones, formularios y permisos de la aplicación web desde la perspectiva de un usuario final.

---

## 0. Preparación y Usuarios de Prueba

### Credenciales de Acceso (PIN de 4 dígitos)

> En **SpaceScan** no hay correo ni contraseña alfanumérica: se selecciona una tarjeta de tripulante y se introduce su PIN numérico de 4 dígitos.

| ID | Nombre en pantalla | Puesto / Rol | PIN | Uso principal en pruebas |
| :--- | :--- | :--- | :---: | :--- |
| `ID·01` | **Elena Vargas** | Pilot *(Piloto)* | **`1042`** | Pruebas generales de tripulante estándar. |
| `ID·02` | **Marcus Vance** | Operator *(Operador)* | **`2084`** | **Único** con acceso a **Crew Administration**. |
| `ID·03` | **Amara Okafor** | Physician *(Médico)* | **`3190`** | **Única** con acceso a **Pending Reviews** en **Notifications**. |
| `ID·04` | **Kenji Sato** *(o Jonas Reed)* | Astronaut *(Astronauta)* | **`4275`** | Pruebas generales y comparación entre perfiles. |

### Checklist previo antes de empezar

- [x] La aplicación web carga correctamente en el navegador en la pantalla inicial `Sign In`.
- [x] Se acuerda dejar las pruebas de **bloqueo por 5 PINs erróneos** y **avance de etapa de misión** (`Crew Administration`) para el final de la sesión.

---

## 1. Zona Pública (Sin Iniciar Sesión)

**Barra inferior esperada:** 3 pestañas públicas (`Sign In · Crew Overview · Crew Streaks`).

### 1.1 Pantalla de Acceso (`Sign In`)
**Dónde:** Pantalla inicial `/login` · **Perfil:** Sin sesión

- [x] Se muestran las 4 tarjetas de tripulantes con su código (`ID·01` a `ID·04`), nombre, puesto y píldora de estado (`OPTIMAL` o `ATTENTION`).
- [x] Al hacer clic en una tarjeta, cambia a estado `SELECTED` y su nombre aparece en el encabezado `Enter PIN · <Nombre>`.
- [x] El campo de PIN solo acepta hasta 4 dígitos numéricos y los oculta como puntos.
- [ ] El botón `Open Crew Overview` abre la vista grupal sin pedir PIN.
- [ ] El botón `Open Crew Streaks` abre la vista de rachas del equipo sin pedir PIN.
- [ ] Al ingresar un PIN incorrecto, aparece un mensaje indicando cuántos intentos quedan antes del bloqueo (`Incorrect PIN. X attempts remaining.`).
- [ ] *(Hacer al final o con permiso de Operator disponible)* Al fallar 5 veces seguidas el PIN de un perfil, la tarjeta queda marcada como `LOCKED` y no permite iniciar sesión durante 5 minutos (o hasta ser desbloqueada por el `Operator`).

### 1.2 Vista General de Tripulación (`Crew Overview`)
**Dónde:** Pestaña `Crew Overview` · **Perfil:** Sin sesión

- [ ] Se muestran 4 columnas (una por tripulante) con estado (`OPTIMAL` / `ATTENTION`), turno (`IVA` / `EVA`) y ubicación.
- [ ] Cada tarjeta de tripulante muestra sus 4 indicadores clave: `Heart Rate`, `HRV`, `Sleep (24h)` y `Oxygen (SpO₂)`.
- [ ] En el panel inferior `Crew Readiness & Cabin Environment` se muestran: el medidor circular `Crew Score` (`/ 100`), las barras de `Hydration`, `Sleep Target` y `Daily Exercise`, y el resumen ambiental de cabina (temperatura, humedad, ruido y CO₂).
- [ ] La pantalla es 100% de solo lectura (no existen campos de texto ni botones para registrar mediciones).

### 1.3 Rachas de Tripulación (`Crew Streaks`)
**Dónde:** Pestaña `Crew Streaks` · **Perfil:** Sin sesión

- [ ] Cada tarjeta muestra el medidor `Active Streak`, su mejor marca (`Best: X days`) o estado `ATTENTION` / `SHIELD`.
- [ ] La tira de `Last 7 days` muestra 7 bloques con su estado (completado, parcial `X/4`, vacío `—` o escudo `SHD` por descanso post-EVA).
- [ ] Cada tarjeta muestra las barras de cumplimiento de los hábitos de hoy (`today habits`).
- [ ] El panel inferior `Collective Streak & Daily Habits` muestra el `Team Streak`, `Crew Hydration`, `Daily Nutrition`, `Scheduled Exercise` y el resumen de consistencia a 30 días.

---

## 2. Inicio de Sesión y Navegación Principal

**Dónde:** Desde `Sign In` hacia la cabina autenticada · **Perfil:** `ID·01` Elena Vargas (PIN `1042`)

- [ ] Al seleccionar `Elena Vargas`, ingresar `1042` y pulsar `Sign In`, redirige automáticamente a `Profile → Personal Data`.
- [ ] En la **barra superior** se visualizan: marca `SpaceScan`, título de la pantalla actual, reloj de misión, botón `Notifications (N)` (con punto rojo si hay avisos pendientes) y píldora de estado a la derecha.
- [ ] En la **barra inferior (dock de 7 módulos)** aparecen en orden: `Vision · Sleep · Auscultation · [Profile elevado al centro] · Capture · Guide · Comms`.
- [ ] En la esquina inferior izquierda aparece la tarjeta del usuario activo (`ID·01 · E. VARGAS`).
- [ ] En la esquina inferior derecha aparece el botón `Sign Out` (al probarlo al final, cierra sesión y devuelve a `Sign In`).

---

## 3. Pantallas de Consulta (Solo Lectura)

> **Regla general en toda esta sección:** ninguna de estas vistas debe tener formularios ni botones de captura; solo visualizan datos, gráficas y resúmenes.

### 3.1 `Profile → Personal Data`
**Dónde:** Botón central `Profile`, pestaña `Personal Data` · **Perfil:** Cualquier tripulante

- [ ] En `Personal Biometrics`, la tarjeta superior muestra nombre, puesto, edad, sexo y tipo de sangre.
- [ ] Se muestran las 6 tarjetas biométricas: `Height`, `Weight`, `Body Mass Index`, `Muscle Mass`, `Bone Density` y `Aerobic Capacity`.
- [ ] En `Biometric Scan` se muestra la figura central y abajo `Core temp` e `Hydration` del día (consumido / meta en litros).
- [ ] En `Environment & Work Hours` se muestran los 4 medidores (`Temperature`, `Humidity`, `Ambient Noise`, `Cabin CO₂`) y las 3 tarjetas de tiempo (`Interior Work (IVA)`, `Exterior Work (EVA)` y `Mission Elapsed Time`).

### 3.2 `Profile → Psychological`
**Dónde:** Pestaña `Psychological` · **Perfil:** Cualquier tripulante

- [ ] En `Behavioral & Mood Results` aparece el último estado registrado (`Calm & Focused`, `Focused`, `Tired`, etc.) con la hora UTC.
- [ ] Se muestran las 4 barras de escalas: `Overall Mood`, `Stress Index`, `Isolation` y `Motivation`.
- [ ] En `Mood & Calmness Trend · Last 14 Days` se renderiza la gráfica de 14 días con la zona óptima marcada.
- [ ] En `Cognitive & Motor Reaction Results` se muestran el medidor `Reaction Time` y las tarjetas `Attention Lapses`, `Motor Precision` y `Vigilance Score`.

### 3.3 `Profile → Physical`
**Dónde:** Pestaña `Physical` · **Perfil:** Cualquier tripulante

- [ ] En `Daily Vitals, Exercise & Nutrition` se listan los signos vitales y hábitos diarios con su barra comparativa contra meta o línea base.
- [ ] En `Live ECG & Body Temperature` se visualiza la gráfica del trazo ECG con frecuencia cardíaca, HRV y temperatura.
- [ ] En `Periodic Clinical Lab Results` se muestran las 4 tarjetas de laboratorio (glucosa, hemoglobina, densidad urinaria y SpO₂) con su estado.

### 3.4 `Vision`
**Dónde:** Dock inferior → `Vision` · **Perfil:** Cualquier tripulante

- [ ] En `Ocular Measurements` se muestra el resumen de alerta ocular y los dos medidores circulares (`left eye` y `right eye`) en milímetros.
- [ ] Se muestran las filas de `Intraocular Pressure`, `Retinal Layer Thickness` y `Visual Acuity`, más el recuadro inferior con fecha/hora del último ultrasonido.
- [ ] En `Optic Nerve Sheath Trend (mm)` se visualiza la gráfica comparativa de ojo derecho vs. ojo izquierdo con línea de umbral de alerta y banda de línea base.
- [ ] En `Preventive Care Plan` se muestran los 3 pasos de cuidado preventivo.

### 3.5 `Sleep`
**Dónde:** Dock inferior → `Sleep` · **Perfil:** Cualquier tripulante

- [ ] La pestaña `Last Night` muestra `Sleep Score`, tiempo total dormido, tiempo en cama, eficiencia de sueño y la píldora superior `REST WINDOW` en UTC.
- [ ] Se muestran las tarjetas de etapas (`Deep`, `REM`, `Light`, `Awake`) con duración y porcentaje.
- [ ] En `Last Night` se dibuja el gráfico continuo de etapas (`Sleep Stage Ribbon Chart`) y abajo la tabla `Stage Lapses & Cycle Intervals`.
- [ ] Al cambiar entre `Last 7 Days`, `Last 14 Days` y `Last 30 Days`, la gráfica cambia a barras por noche y el panel inferior derecho muestra el resumen de noches del periodo.

### 3.6 `Auscultation`
**Dónde:** Dock inferior → `Auscultation` · **Perfil:** Cualquier tripulante

- [ ] En `Cardiac & Pulmonary Audio Results` se muestran los resúmenes de audio cardíaco (`bpm`, ritmo) y pulmonar (`rpm`, `SpO₂`), además de `VO₂ Max`, `Orthostatic Response` y `Cardiorespiratory Index`.
- [ ] En `Recorded Cardiac & Pulmonary Acoustic Waveforms` se visualizan las 2 ondas acústicas (`Channel 1` cardíaco y `Channel 2` pulmonar).
- [ ] En `24-Hour Cabin CO₂ Trend (mmHg)` se visualiza la gráfica de CO₂ de las últimas 24 horas con sus líneas de zona objetivo y límite de alerta.

---

## 4. Módulo `Capture` (Registro de Datos y Efecto en Vivo)

> En cada prueba de esta sección, después de guardar, navega a la pantalla de consulta correspondiente para confirmar que el dato nuevo aparece inmediatamente.

### 4.1 `Capture → Auscultation Audio`
**Dónde:** Dock `Capture` → pestaña `Auscultation Audio` · **Perfil:** Cualquier tripulante

- [ ] En el panel izquierdo (corazón) se pueden seleccionar los 4 sitios (`Aortic · 2nd R`, `Pulmonic · 2nd L`, `Tricuspid · 4th L`, `Mitral Apex`).
- [ ] En el panel derecho (pulmones) se pueden seleccionar las 4 zonas (`Upper Left`, `Upper Right`, `Lower Left`, `Lower Right`).
- [ ] La barra superior indica el nivel de ruido en cabina (`Cabin quiet` por debajo de `55 dBA`; si supera el límite, bloquea los botones de grabación).
- [ ] Al pulsar `Record / Stop Heart Audio` (o `Record Pulmonary Audio`) y aceptar el micrófono, el medidor de ganancia (`dB`), la onda en vivo y el contador (`00:XX / 00:30 SEC`) funcionan correctamente.
- [ ] Al detener o completar los 30 segundos, se habilita `Save Cardiac Recording` (o `Save Lung Recording`).
- [ ] Al guardar, muestra el resultado calculado (`bpm`/`rpm` y `%` de señal), marca el sitio como `Saved (30s)` y el nuevo registro aparece en `Auscultation`.

### 4.2 `Capture → Physical & Clinical Labs`
**Dónde:** Dock `Capture` → pestaña `Physical & Clinical Labs` · **Perfil:** Cualquier tripulante

- [ ] **Validación vacía / formato:** al intentar guardar sin llenar campos, muestra `"Enter at least one reading"`; al escribir mal la presión (ej. `120` sin `/`) o un turno inválido, marca el error en rojo bajo ese campo sin borrar los demás.
- [ ] **Vista previa de hidratación:** al escribir `400` en `Hydration Intake`, la barra informativa inferior calcula y muestra en vivo cómo quedará el total de litros del día.
- [ ] **Guardado normal (panel izquierdo):** al llenar peso, presión (`118 / 76`), pulso, temperatura, agua, calorías, ejercicio y turno (`5h 20m` en `IVA` o `EVA`) y pulsar `Save Daily Vitals & Habits`, confirma el guardado y actualiza `Profile → Physical`, `Profile → Personal Data` y `Crew Streaks`.
- [ ] **Guardado fuera de rango (panel derecho):** al ingresar un valor alterado en `Periodic Clinical Labs Entry` (por ejemplo `89` en `Oxygen Saturation (SpO₂)`) y pulsar `Save Clinical Lab Results`, muestra un aviso rojo indicando que se generó una alerta (`advisory raised`) y aumenta el contador en `Notifications (N)`.

### 4.3 `Capture → Vision & Ocular Exam`
**Dónde:** Dock `Capture` → pestaña `Vision & Ocular Exam` · **Perfil:** Cualquier tripulante

- [ ] **Detección en vivo antes de guardar:** al escribir valores altos en `Left/Right Optic Nerve Sheath` (ej. `5.9` y `6.1`), el recuadro `Threshold detection` cambia automáticamente antes de enviar para advertir que supera el límite.
- [ ] **Validación de agudeza visual:** si en `Visual Acuity` se escribe un formato distinto a `20/XX`, muestra el mensaje de formato esperado.
- [ ] **Guardado completo:** al llenar los campos oculares (ej. `5.5`, `5.9`, `15.8`, `16.2`, `104`, `20 / 20`) y pulsar `Save Vision & Ocular Exam`, confirma el guardado (y si superó el umbral, crea un aviso en `Notifications`).
- [ ] Al entrar después a `Vision`, el nuevo examen aparece en las tarjetas y como el punto más reciente de la gráfica bilateral.

### 4.4 `Capture → Psych, Motor & Sleep`
**Dónde:** Dock `Capture` → pestaña `Psych, Motor & Sleep` · **Perfil:** Cualquier tripulante

- [ ] **Check-in emocional y sueño (panel izquierdo):**
  - [ ] Permite elegir un estado (`Calm`, `Focused`, `Tired`, `Stressed`) y marcar valores del `1` al `5` en las 4 escalas (`Overall Mood`, `Perceived Stress`, `Sense of Isolation`, `Mission Motivation`).
  - [ ] Si falta alguna de las 4 escalas al intentar guardar, muestra aviso solicitando completar todas.
  - [ ] Al escribir `Sleep onset` y `Wake time` en formato 24h UTC (ej. `22:15` y `06:00`), calcula y muestra automáticamente la duración (`7h 45m window`).
  - [ ] Si solo se llena una de las dos horas de sueño, advierte que deben ingresarse ambas o ninguna.
  - [ ] Al pulsar `Save Behavioral & Sleep Log`, confirma el guardado y actualiza tanto `Profile → Psychological` como `Sleep`.
  - [ ] *(Opcional)* Al registrar estrés alto (`5`) y ánimo bajo (`1`), genera un aviso de apoyo en `Notifications`.
- [ ] **Prueba de reacción de 2 minutos (panel derecho):**
  - [ ] Al pulsar `Start 2-Min Reaction Test`, inicia el temporizador hacia `02:00`.
  - [ ] Si se toca/hace clic antes de que aparezca el estímulo verde, suma `1` en `False Starts`.
  - [ ] Al aparecer el círculo verde (`TAP`) y hacer clic (o presionar `Espacio` / `Enter`), registra la latencia (`ms`), actualiza `Mean reaction time` y `Motor hit precision`.
  - [ ] Al finalizar los 2 minutos (`TEST COMPLETE`), se habilita `Save Motor Session`; tras guardarlo, los nuevos resultados aparecen en `Profile → Psychological`.

---

## 5. Alertas, Guía Médica y Control a Tierra

### 5.1 `Notifications`
**Dónde:** Botón `Notifications (N)` en la barra superior · **Perfil:** Cualquier tripulante

- [ ] Funcionan los filtros superiores: `All`, `Health Advisories` y `Scheduled Checks`.
- [ ] Se muestra la píldora de horario de silencio (`QUIET HOURS 22:00 – 06:00 UTC`).
- [ ] Al seleccionar un aviso en la lista izquierda (`View Care Plan`), se muestran en el panel derecho (`Recommended Care`) sus 3 pasos preventivos.
- [ ] Al hacer clic en cada paso preventivo, cambia visualmente a completado (paloma verde y hora UTC).
- [ ] El botón `Open Medical Guide` abre la pantalla `Guide` directamente en el protocolo relacionado con ese aviso.
- [ ] El botón `Acknowledge Advisory` confirma el aviso, lo retira de la lista de pendientes y descuenta el contador en la barra superior.
- [ ] En elementos de `Scheduled Checks`, el botón `Open Capture` lleva al módulo de captura.

### 5.2 `Guide` (Guía Médica y Botiquín)
**Dónde:** Dock inferior → `Guide` · **Perfil:** Cualquier tripulante

- [ ] Al escribir un síntoma en el buscador (ej. `headache`, `cut`, `eye pressure`, `CO2`) y pulsar `Search Guide`, se muestran resultados y se abre un protocolo con pasos numerados y caja roja de escalamiento (`Escalate immediately to...`).
- [ ] Al pulsar las pastillas de categorías bajo el buscador, filtran los protocolos (y al volver a pulsar la misma pastilla, quitan el filtro).
- [ ] Al pulsar `Emergency Index` (botón rojo), muestra la lista de protocolos de emergencia; al hacer clic en cualquiera de ellos, abre su guía completa.
- [ ] En el panel derecho (`Medical Kit Locator`), el cajón asignado al protocolo abierto queda resaltado como `ACTIVE` y lista sus insumos y estado.
- [ ] Al pulsar `Illuminate Drawer ... Light`, el botón indica que la luz del cajón está encendida durante 30 segundos.

### 5.3 `Comms` (Control a Tierra y Clima Solar)
**Dónde:** Dock inferior → `Comms` · **Perfil:** Cualquier tripulante

- [ ] En `Flight Surgeon Messages · Houston` se muestran los mensajes recibidos con su estado (`NEW`, `CONFIRMED`, `ARCHIVED`).
- [ ] Si hay un mensaje `NEW`, al pulsar `CONFIRM READ` cambia su estado a `CONFIRMED`.
- [ ] Al pulsar `Send Daily Crew Summary to Houston`, muestra confirmación con la hora estimada de llegada (+12 min) y agrega el envío en `Transmission Log` con estado `QUEUED` / `IN TRANSIT`.
- [ ] En `Solar Weather & Cabin Radiation` se muestran los medidores circulares `Solar Activity` (`Kp`), `Cabin Radiation` (`mSv / day`) y el pronóstico de 48 horas.

---

## 6. Pruebas Exclusivas por Rol Especial

### 6.1 Rol `Physician` — Revisión de Hallazgos Asistidos
**Dónde:** `Notifications` → pestaña `Pending Reviews` · **Perfil:** `ID·03` Amara Okafor (PIN `3190`)

- [ ] Iniciar sesión con `ID·03` (`3190`) y comprobar que en `Notifications` aparece la pestaña **`Pending Reviews`** (y verificar que **no aparece** con `ID·01`, `ID·02` ni `ID·04`).
- [ ] Si hay hallazgos pendientes en la lista izquierda, al seleccionar uno se muestran a la derecha el resumen sugerido, los pasos preventivos y el campo `Physician note (optional)`.
- [ ] Al escribir una nota opcional y pulsar `Approve & Notify`, `Add to Guide` o `Reject`, el hallazgo se procesa y sale de la lista de pendientes.

### 6.2 Rol `Operator` — Administración de Tripulación y Etapas
**Dónde:** `Profile` → botón `Crew Administration` · **Perfil:** `ID·02` Marcus Vance (PIN `2084`)

- [ ] Iniciar sesión con `ID·02` (`2084`), entrar a `Profile` y verificar que aparece el botón **`Crew Administration`** (comprobar que **no aparece** con `ID·01`, `ID·03` ni `ID·04`).
- [ ] **Crear nuevo perfil:** en `Add Crew Member`, capturar `ID-05`, PIN `5555`, nombre, puesto, edad y rol `ASTRONAUT`; pulsar `Create Crew Profile`. Luego cerrar sesión y confirmar que `ID-05` aparece en `Sign In` y entra con el PIN `5555`.
- [ ] **Activar / Desactivar cuentas:** volver con `ID·02` a `Crew Administration` y probar `Deactivate` y `Activate` sobre `ID-05`.
- [ ] **Protección del último operador:** intentar desactivar al único `OPERATOR` activo (`ID·02`) y verificar que el sistema lo impide con un mensaje de aviso.
- [ ] **Desbloquear cuenta bloqueada:** *(si se probó el bloqueo de 5 intentos en la sección 1.1)* verificar que aparece el botón `Unlock` junto al tripulante bloqueado, pulsarlo y comprobar que ya puede volver a iniciar sesión en `Sign In`.
- [ ] **Avance de etapa de misión *(dejar para el final absoluto)*:** en `Mission Stage`, comprobar que pide doble clic de confirmación para avanzar a la siguiente etapa (`Launch → Mission → Return`), sabiendo que no es reversible.

---

## 7. Cierre de Sesión y Verificación Final

- [ ] Al pulsar `Sign Out` en cualquier pantalla autenticada, regresa a `Sign In` y desaparece la barra inferior de 7 módulos.
- [ ] Tras cerrar sesión, intentar navegar manualmente a una ruta privada (por ejemplo `/profile/personal` o `/capture/physical`) redirige a `/login` sin mostrar datos privados.
- [ ] Todo el flujo completo (`Sign In → Capture → Alerta en Notifications → Guide → Comms → Sign Out`) funciona sin errores bloqueantes.
