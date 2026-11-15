# 📋 Especificación Técnica y Funcional: Sistema de Control de Avance (SCAN SPACE)

> **Documento:** Manual y Especificación de la Aplicación de Control de Avance, Torre de Control y Workspace Colaborativo  
> **Ubicación:** `docs/miWork/`  
> **Propósito:** Servir como pizarra digital interactiva y colaborativa en tiempo real para coordinar la investigación biomédica, la validación de parámetros, el desarrollo técnico y la redacción de prompts/instrucciones para el reto NASA Space Apps Challenge sin tocar el repositorio de código antes de tiempo.

---

## 1. Visión General del Sistema

La **App de Control de Avance** funciona como la **"Torre de Control de la Misión"**:
Permite a los integrantes del equipo (conectados desde sus laptops, celulares o tablets a través de la misma red Wi-Fi local) registrar avances, asignarse responsabilidades, compartir fuentes científicas (enlaces a la NASA, Nature, PubMed), ordenar secciones y trabajar en conjunto sobre documentos Markdown (.md) e instrucciones para la IA sin riesgo de pisarse el trabajo ni perder información.

```
       [ Dispositivo Wilson ]       [ Dispositivo Carlos ]       [ Dispositivo Steve ]       [ Dispositivo Foco ]
             (Laptop)                     (Laptop)                    (Celular)                    (Tablet)
                 │                            │                            │                           │
                 └────────────────────────────┴─────────────┬──────────────┴───────────────────────────┘
                                                            ▼
                                               [ Red Wi-Fi Local (Módem) ]
                                                            │
                                                            ▼
                                                 [ Servidor en Python ]
                                                  (docs/miWork/server.py)
                                                      │           │
                                   ┌──────────────────┘           └─────────────────┐
                                   ▼                                                ▼
                         [ Almacén de Estado ]                           [ Almacén de Documentos ]
                       (docs/miWork/state.json)                          (docs/miWork/docs/*.md)
```

---

## 2. Arquitectura de Software

El sistema está diseñado en una arquitectura ligera y autónoma, que **no requiere internet para funcionar** en la red local:

| Componente | Archivo / Ubicación | Función |
|---|---|---|
| **Interfaz Visual (Frontend)** | `docs/miWork/index.html` | Panel web interactivo con diseño responsivo (computadoras y celulares). Maneja el renderizado, modales, formularios, checklist modular, reordenamiento de secciones y el editor Markdown colaborativo tipo Colab. |
| **Motor de Comunicación (Backend)** | `docs/miWork/server.py` | Servidor HTTP multi-hilo en Python que escucha peticiones en el puerto `8000`, sincroniza las modificaciones al instante y escribe automáticamente en disco. |
| **Base de Datos de Estado** | `docs/miWork/state.json` | Archivo de texto estructurado en el disco duro donde quedan grabadas todas las tareas, estados, asignaciones, orden de secciones, enlaces y notas. |
| **Repositorio de Documentos Markdown** | `docs/miWork/docs/` | Carpeta física en disco donde se guardan automáticamente los archivos `.md` editados en la pestaña Colab (prompts, instrucciones del asistente IA y fichas técnicas). |
| **Lanzador para Mac** | `docs/miWork/iniciar_servidor.command` | Script que detecta la IP local de la computadora y enciende el servidor con doble clic en macOS. |
| **Lanzador para Windows** | `docs/miWork/iniciar_servidor.bat` | Script por lotes para encendido rápido en Windows. |

---

## 3. Módulos y Funcionalidades

### 3.1 Identificación de Usuario y Asignación de Roles
* **Propósito:** Saber con certeza quién está investigando o programando cada parámetro para evitar duplicar esfuerzos.
* **Mecánica:**
  * Al ingresar, el usuario hace clic en el selector superior derecho (**"Identifícate"**).
  * Puede elegir con un solo clic su nombre dentro de las dos categorías del equipo:
    * **Desarrolladores (Devs):** *Wilson, Wilmer, Carlos*
    * **Investigadores / Testers:** *Steve, Sandra, Foco (Poco)*
    * **Personalizado:** Espacio para escribir cualquier otro nombre.
  * **Código de Colores Dinámico:** Cada integrante tiene un color exclusivo (ej. Púrpura para Wilson, Naranja para Wilmer, Azul para Carlos, Amarillo para Steve, Verde para Foco, Teal para Sandra). Cuando un miembro toma una tarea, el botón se ilumina con su color característico.

---

### 3.2 Navegación por Pestañas Principales (4 Módulos)
La aplicación organiza el trabajo en 4 vistas especializadas:

1. **🏠 Pestaña "Inicio & Roles":**
   * **Métricas Globales:** Tarjetas de avance porcentual global, avance en investigación (`Test / Invest`) y avance técnico (`Devs`).
   * **Tarjetas de Roles:** Detalle de las misiones y responsabilidades de los **Testers / Investigadores** (*Steve, Sandra, Foco*) frente a los **Desarrolladores** (*Wilson, Wilmer, Carlos*).
   * **👥 Asignaciones de Equipo (Devs & Testers):** Lista consolidada de responsabilidades individuales donde cada integrante ve exactamente qué tiene a su cargo y qué tareas tiene pendientes.
   * **Ciclo de Validación:** Diagrama visual interactivo del flujo de trabajo en parejas (*Investigar → Filtrar → JSON → Módulo → Revisión → OK*).

2. **🧪 Pestaña "Test / Invest":**
   * Agrupa los bloques de investigación médica y parámetros de vuelo:
     * *4. Obj 1 (Fases de misión, Antropometría, Sistema Óseo/Muscular).*
     * *5. Misión (Variables Automáticas y Manuales).*
     * *6. Mediciones Indirectas e Investigación Científica.*
     * *Nuevas secciones personalizadas de investigación añadidas por el equipo.*

3. **👨‍💻 Pestaña "Devs":**
   * Agrupa las tareas técnicas y de ingeniería de software:
     * *1. Entorno y Recursos de Software (Git, clone, Agent IA, entorno local).*
     * *2. Flujo de Trabajo y Validación Técnica.*
     * *Nuevas secciones técnicas añadidas dinámicamente por el equipo (ej. Base de Datos, APIs, etc.).*

4. **📓 Pestaña "Docs & Prompts (Colab)":**
   * Espacio de trabajo colaborativo para redacción y edición de documentos Markdown `.md` en vivo con estilo similar a Google Colab / VS Code.
   * Diseñado específicamente para que el equipo pueda redactar y ajustar las **instrucciones de los agentes de IA**, diseñar **prompts especializados (Gems)** y documentar el avance en tiempo real sin fricción de Git (sin necesidad de hacer commits, pushes o pulls).

---

### 3.3 Reordenamiento Modular de Elementos y Secciones

El sistema permite organizar el flujo de trabajo tanto a nivel de tareas individuales como a nivel de secciones completas:

#### A. Reordenamiento de Secciones Completas
Cada tarjeta de sección (tanto las predeterminadas como las nuevas creadas por el equipo) funciona como un estante modular independiente:
* **Flechas de subida y bajada (`▲` y `▼`):** Ubicadas en la cabecera de la sección (a la derecha de la insignia de progreso). Un solo clic intercambia de posición la sección con su vecina sin alterar las tareas internas.
* **Agarrador de sección (`⠿`):** Ubicado en el extremo izquierdo del título de la sección para arrastrar y soltar la sección completa a la posición deseada.
* **Persistencia sincronizada:** El orden de las secciones se almacena en `state.json` bajo la clave `sectionOrders` y se sincroniza en vivo con todos los clientes conectados.

#### B. Reordenamiento de Tareas y Subtareas
* Cada fila del checklist cuenta con su propio agarrador **`⠿`**.
* Al hacer clic sostenido (o arrastrar con el dedo en pantallas táctiles), cualquier tarea puede moverse libremente hacia arriba o abajo dentro de su grupo.
* Las subtareas dentro del panel de notas también pueden reordenarse de la misma forma.

---

### 3.4 Plegado y Desplegado de Secciones (Colapsables)
* Cada cabecera de sección cuenta con un indicador de flecha **`▼`** y es completamente interactiva.
* Al hacer clic sobre el encabezado, la sección se pliega o despliega instantáneamente, permitiendo concentrarse en un bloque específico sin saturar la pantalla.
* La insignia de progreso (ej. `3/15`) permanece siempre visible aun con la sección plegada.

---

### 3.5 Creación Dinámica de Nuevas Secciones y Tareas

#### A. Creación de Nuevas Secciones
* Al final de las pestañas *Test / Invest* y *Devs* se encuentra el botón **`➕ Crear Nueva Sección`**.
* Al pulsarlo, se abre una ventana modal donde se escribe el título de la nueva sección (ej. *7. Telemetría de Cabina* o *3. Base de Datos*).
* La sección se crea de inmediato con su propio contador de progreso, botones de reordenamiento `▲`/`▼`, agarrador `⠿`, botón para eliminar sección (`✕`), y su propio botón para agregar tareas.
* Se guarda de inmediato en `state.json` bajo `customSections` y se propaga a todos los dispositivos.

#### B. Creación de Nuevas Tareas Principales
* Al pie de cada sección se encuentra el botón: **`➕ Agregar nueva tarea`**.
* Permite ingresar el título de cualquier nueva actividad técnica o biomédica.
* La nueva tarea nace con todas las funcionalidades: agarrador `⠿`, botones de estado (**Tomado**, **En Proceso**, **Listo**), botón de notas/enlaces `👁️` y botón de descarte `🗑️`.
* Se guarda de inmediato en `state.json` bajo `customTasks`.

---

### 3.6 Sistema de Descarte Flexible y Registro de Ocultos
Para mantener un historial transparente de qué parámetros se descartaron y por qué:
1. **Botón de Descarte (`🗑️`):** Cada tarea y subtarea tiene su icono de papelera.
2. **Ventana de Justificación Opcional:**
   * Al pulsar `🗑️`, se despliega una ventana modal donde el usuario puede:
     * Seleccionar un atajo rápido (*"No aplica a esta fase"*, *"Dato redundante"*, *"No viable en vuelo"*, *"Baja prioridad"*).
     * Escribir un motivo personalizado.
     * O simplemente confirmar el descarte de inmediato sin necesidad de especificar motivo.
3. **Cajón de Elementos Ocultos / Descartados por Sección:**
   * El elemento descartado se traslada a una gaveta al pie de su sección: **`[ 🗑️ Ver Elementos Descartados (X) ]`**.
   * Al desplegar la gaveta se muestra el nombre tachado, el motivo (si se indicó), quién lo descartó y la fecha/hora.
   * Incluye un botón verde **`Restaurar ↩️`** para regresar el ítem a la lista activa en cualquier instante.

---

### 3.7 Semáforo de Estado en Cada Fila (Inline Status)
Cada renglón del checklist contiene botones rápidos de estado que registran la trazabilidad:

```
[ ⠿ ] [ Casilla ] [ Título de la Tarea ] ──▶ [ Tomado ] [ En Proceso ] [ Listo ] [ 👁 ] [ 🗑️ ]
```

1. **Tomado (Asignación):**
   * Registra quién es el responsable de investigar o programar ese elemento.
   * Se ilumina con el color característico del usuario activo y guarda su nombre (ej. *"Tomado por: Steve"*).
2. **En Proceso (Ámbar / Amarillo):**
   * Indica que se están analizando estudios científicos, calculando límites o programando el código.
3. **Listo (Verde):**
   * Indica que la tarea ya fue completada y validada por el equipo.

---

### 3.8 Panel Lateral Desplegable de Notas y Subtareas (Botón `👁`)
Al pulsar el icono del ojo `👁` en cualquier tarea, se abre un panel lateral dedicado:
* **Formulario de Entrada:**
  * **Título del paso:** Nombre descriptivo (ej. *"Estudio de pérdida de densidad ósea en fémur"*).
  * **Enlace / Link Web (URL):** Campo `https://` para pegar enlaces oficiales de la NASA, PubMed o Nature.
  * **Notas / Observaciones:** Área de texto enriquecida para fórmulas, rangos biomédicos, conclusiones y recomendaciones.
* **Subtareas Dinámicas:** Cada subtarea tiene su propio semáforo (*Tomado*, *En Proceso*, *Listo*), sus botones para editar (✏️) y descartar (🗑️).
* **Contador en Checklist Principal:** El botón del ojo en la lista muestra un distintivo fraccional (ej. `2/3`) indicando el número de subtareas completadas.

---

### 3.9 Workspace Colaborativo Markdown Estilo Colab (Pestaña `Docs & Prompts`)
Diseñado para la gestión ágil del conocimiento y la interacción con modelos de Inteligencia Artificial:

#### 1. Explorador de Archivos (Sidebar Izquierdo):
* Encabezado con título `📁 DOCUMENTOS (.MD)` y botón **`➕ Nuevo`**.
* Lista de archivos Markdown cargados desde `docs/miWork/docs/` con selector activo y botón de eliminación individual `🗑️`.
* **Modal de Creación:** Permite nombrar el archivo y seleccionar entre 4 plantillas predefinidas:
  * 📄 *Documento en Blanco*
  * 🤖 *Prompt Especializado para Asistente IA (NASA)*
  * 📜 *Instrucciones Operativas de Agente*
  * 🔬 *Ficha de Investigación Científica (Biomarcador)*

#### 2. Barra Superior de Control del Documento:
* **Nombre Editable:** Campo para renombrar el archivo en caliente. Si se omite la extensión, el sistema le añade automáticamente `.md`.
* **Indicador de Sincronización en Tiempo Real:** Muestra el estado activo (`🟢 Sincronizado en tiempo real` / `💾 Guardando...`).
* **Selector de Modos de Vista:**
  * **`◫ Dividido`:** Muestra en paralelo el editor a la izquierda y la vista previa a la derecha.
  * **`✏️ Editor`:** Expande el editor Markdown a todo el ancho.
  * **`👁️ Previa`:** Oculta el editor y muestra únicamente el documento renderizado en limpio.
* **Botones de Acción Rápida:**
  * **`📋 Copiar Prompt`:** Copia todo el contenido al portapapeles con un clic para pegarlo directamente en ChatGPT, Gemini o Claude.
  * **`⬇️ Descargar`:** Descarga una copia local del archivo `.md` en la computadora.

#### 3. Editor y Barra de Herramientas Markdown:
* Tipografía monoespaciada oscura con tabulación suave.
* Barra de botones de formato rápido: Negrita (`B`), Cursiva (`I`), Títulos (`H1`, `H2`, `H3`), Cita (`""`), Código inline (`</>`), Bloque de código, Lista con viñetas, Lista numerada, Casillas de verificación (`☑ Tarea`), Enlaces (`🔗`) y Tablas (`📊`).
* Contador dinámico de palabras y líneas en el pie del editor.

#### 4. Vista Previa Renderizada en Tiempo Real:
* Renderiza encabezados, párrafos, bloques de advertencia, tablas, listas de tareas interactivas, enlaces clicables y bloques de código con estilo visual moderno.

#### 5. Sincronización de Doble Vía con el Disco:
* Cualquier cambio realizado en el editor web se guarda automáticamente en `state.json` y se escribe de inmediato como un archivo `.md` real en la carpeta física [docs/miWork/docs/](file:///Users/wilsonjonatan/Downloads/nasa-challenge/docs/miWork/docs/).
* Cualquier archivo `.md` agregado manualmente a la carpeta `docs/miWork/docs/` es detectado automáticamente por el servidor al iniciar y puesto a disposición del equipo.

---

### 3.10 Tareas Marcables en Modo Vista y Comentarios Plegables en Línea (Opción B)

#### A. Tareas Marcables en Vista Previa (Interactive Task Checklists)
* **Objetivo:** Permitir marcar o desmarcar tareas directamente desde el modo de lectura/vista previa (`👁️ Previa` o `◫ Dividido`) sin tener que pasar al modo de edición de texto.
* **Mecánica:**
  * Las casillas de verificación `- [ ]` y `- [x]` se renderizan interactivas (sin el atributo restrictivo `disabled`).
  * Al hacer clic en cualquier casilla de la vista previa:
    1. La casilla cambia visualmente de estado con animación suave y el texto de la tarea se tacha de forma inmediata.
    2. El sistema localiza la tarea correspondiente en el código fuente Markdown y conmuta la marca entre `- [ ]` y `- [x]`.
    3. Se ejecuta automáticamente el guardado persistente (`saveActiveColabDoc()`), actualizando el archivo físico en `docs/miWork/docs/` y sincronizando el estado en tiempo real con el equipo.

#### B. Sistema de Comentarios Plegables en Línea (Opción B: Burbujas Directas bajo el Texto)
* **Objetivo:** Permitir al equipo debatir, plantear dudas o dejar observaciones y retroalimentación técnica sobre párrafos, tareas o secciones específicas del documento sin alterar el texto del prompt ni romper el formato para la IA.
* **Arquitectura de Datos Separada (Doble Capa):**
  * El archivo `.md` se mantiene 100% limpio (código Markdown puro listo para copiar a ChatGPT, Claude o Gemini sin comentarios incrustados que confundan al modelo).
  * Los comentarios se almacenan en `state.json` bajo la clave `docComments[docId][blockId]`.
* **Mecánica de Uso:**
  1. **Disparador contextual:** Al pasar el cursor sobre cualquier bloque (párrafo, título, cita o tarea) en la vista previa, aparece a la derecha un botón discreto: `💬 Comentar` (o si ya hay comentarios, una insignia activa `💬 X comentarios`).
  2. **Tarjeta de Discusión Desplegable:** Al hacer clic, se abre una tarjeta plegable justo debajo del bloque de texto:
     * **Historial de mensajes estilo chat:** Muestra los comentarios ordenados cronológicamente con el nombre del integrante, su avatar con color oficial (*Wilson*, *Carlos*, *Steve*, *Foco*, *Sandra*) y la fecha/hora relativa.
     * **Estado de resolución:** Cada hilo cuenta con un botón `✓ Marcar como Resuelto` para archivar observaciones ya acordadas.
     * **Caja de respuesta rápida:** Campo para redactar y enviar comentarios con la tecla `Enter` o el botón `Enviar`.

---

## 4. Persistencia y Seguridad de Datos (Mecanismo Multinivel)

Para garantizar que ningún dato se pierda ante caídas de red o reinicios de computadora:

1. **Nivel 1 — Memoria Local del Navegador (`localStorage`):**
   * Guarda de inmediato en el navegador bajo la clave `scan_space_state_v2`.
   * Permite que la pantalla no se borre si la conexión Wi-Fi sufre microcortes.
2. **Nivel 2 — Servidor HTTP en Segundo Plano (`server.py`):**
   * Recibe las peticiones vía POST y procesa las acciones atómicas (`save_markdown_doc`, `delete_markdown_doc`, `add_custom_section`, `delete_custom_section`, `update_section_order`, etc.).
3. **Nivel 3 — Base de Datos Central (`state.json`):**
   * Escribe en el archivo estructurado del disco duro.
4. **Nivel 4 — Sistema de Archivos Físicos (`docs/miWork/docs/*.md`):**
   * Mantiene los archivos Markdown disponibles directamente para scripts de Python, agentes terminales o editores de texto tradicionales.

---

## 5. Estructura del Archivo de Datos (`state.json`)

El archivo `state.json` utiliza una estructura JSON limpia y modular:

```json
{
  "itemStatus": {
    "data-osea": {
      "tomado": true,
      "tomadoPor": "Steve",
      "proceso": true,
      "procesoPor": "Steve",
      "listo": true,
      "listoPor": "Steve"
    }
  },
  "subtasks": {
    "data-osea": [
      {
        "id": "t_1794634815157_ku9b",
        "title": "Riesgo de disminución cardiorrespiratoria y musculoesquelética",
        "link": "https://www.nasa.gov/reference/...",
        "notes": "Pérdida severa en pelvis y columna lumbar...",
        "tomado": true,
        "tomadoPor": "Steve",
        "enProceso": false,
        "listo": true,
        "listoPor": "Steve",
        "createdBy": "Steve",
        "createdAt": "2026-11-14T05:40:15.157Z"
      }
    ]
  },
  "customTasks": {
    "cust_1794671759412_sfbk": {
      "id": "cust_1794671759412_sfbk",
      "title": "Base de datos",
      "section": "sec_1794671751237_2fez",
      "createdBy": "Carlos",
      "createdAt": "2026-11-14T15:55:59.412Z"
    }
  },
  "customSections": {
    "sec_1794671751237_2fez": {
      "id": "sec_1794671751237_2fez",
      "title": "Base de Datos",
      "tab": "devs",
      "createdBy": "Carlos",
      "createdAt": "2026-11-14T15:55:51.237Z"
    }
  },
  "sectionOrders": {
    "devs": [
      "card-sec-workflow",
      "card-sec-env",
      "sec_1794671783762_ch2u",
      "sec_1794671751237_2fez"
    ]
  },
  "markdownDocs": {
    "doc_instrucciones_agente_ai": {
      "id": "doc_instrucciones_agente_ai",
      "title": "INSTRUCCIONES_AGENTE_AI.md",
      "content": "# Instrucciones Operativas del Asistente IA\n...",
      "updatedBy": "Carlos",
      "updatedAt": "2026-11-14T16:07:14.225Z"
    }
  },
  "docComments": {
    "doc_instrucciones_agente_ai": {
      "block_3": [
        {
          "id": "comm_1794689000_a1b2",
          "author": "Steve",
          "text": "Verifiquemos si la pérdida ósea del 6.2% en pelvis requiere citar la tabla 2 de Nature.",
          "createdAt": "2026-11-15T10:45:00.000Z",
          "resolved": false
        }
      ]
    }
  }
}
```

---

## 6. Guía Rápida de Operación

### Cómo encender el sistema:
* **En macOS (Mac):**
  * Abrir la carpeta `docs/miWork/` en el Finder.
  * Hacer doble clic sobre `iniciar_servidor.command`.
  * La terminal mostrará los enlaces listos para abrir y compartir con el equipo.
* **En Windows:**
  * Hacer doble clic sobre `iniciar_servidor.bat`.

### Enlaces de acceso:
* **Desde tu propia computadora:** `http://localhost:8000`
* **Desde celulares u otras laptops en la misma red Wi-Fi:** `http://<IP-DE-TU-COMPUTADORA>:8000` (la terminal muestra la IP detectada automáticamente, por ejemplo `http://192.168.1.56:8000`).

### Cómo apagar el servidor:
* Basta con presionar `Control + C` en la ventana de la terminal o cerrar la ventana. Todos los datos, órdenes de secciones y documentos Markdown quedan grabados permanentemente en el disco.

---

## 7. Workspace de Documentos y Prompts Markdown (`docs/miWork/docs/`)

El sistema incluye un entorno de edición y previsualización en tiempo real estilo Google Colab para documentación técnica, bitácoras y prompts de IA.

### 7.1 Identificadores Canónicos y Sincronización Dual
* **Doble persistencia:** Cada documento se almacena en el estado JSON (`state.json` bajo la clave `markdownDocs`) y simultáneamente como un archivo físico `.md` dentro de `docs/miWork/docs/`.
* **Identificadores canónicos:** Los identificadores siguen el formato `doc_<slug>` generado a partir del título limpio del documento (ej. `INSTRUCCIONES_AGENTE_AI.md` $\rightarrow$ `doc_instrucciones_agente_ai`).
* **Detección inteligente anti-duplicados:** El servidor comprueba la existencia de archivos tanto por clave lógica como por nombre de archivo real en disco y título en minúsculas, previniendo duplicaciones al reiniciar o consultar el estado.

### 7.2 Blindaje de Escritura en Vivo y Prevención de Pérdida de Líneas
* **Aislamiento del buffer activo:** Mientras el usuario tenga el cursor dentro del editor (`document.activeElement === editor`) o esté escribiendo, el ciclo periódico de sincronización (1.5 s) tiene prohibido sobrescribir el contenido de la caja de texto.
* **Cola de guardado secuencial:** Si el usuario continúa tecleando mientras un paquete de guardado (`POST save_markdown_doc`) está viajando, el sistema encola automáticamente el nuevo contenido y lo envía secuencialmente al concluir el anterior, evitando carreras HTTP que recorten líneas.

### 7.3 Atajos de Teclado del Editor
* `Tab`: Inserta una sangría de 2 espacios en la posición del cursor sin perder el foco del editor.
* `Cmd + S` (macOS) / `Ctrl + S` (Windows): Ejecuta el guardado forzado inmediato en el servidor y muestra la confirmación visual de sincronización sin activar el diálogo nativo del navegador.
