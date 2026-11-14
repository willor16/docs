# Directivas Maestras e Instrucciones para Agentes de IA — SpaceScan

> **PROPÓSITO:** Establecer las reglas de gobernanza, arquitectura técnica, restricciones normativas y protocolos operativos que debe cumplir cualquier asistente de Inteligencia Artificial al colaborar en el proyecto **SpaceScan**.

---

## 1. Delimitación Estricta de Espacios de Trabajo

El ecosistema del proyecto se divide en **3 áreas con responsabilidades y permisos diferenciados**:

| Espacio | Propósito Principal | Reglas de Gobernanza para la IA |
| :--- | :--- | :--- |
| **`wakax-nasa-challenge-2026/`** | **Repositorio Oficial de Código** (`willor16/wakax-nasa-challenge-2026`). Contiene el software **SpaceScan** (`frontend/` en Nuxt 4 y `backend/` en FastAPI + SQLite). | **Restringido:** No crear, modificar ni eliminar archivos sin orden y confirmación explícita del usuario. Prohibido ejecutar comandos de Git (`add`, `commit`, `push`, `branch`, `checkout`) sin instrucción directa. |
| **`wakax-docs/`** | **Repositorio Oficial de Documentación y Gestión.** Centraliza las reglas inquebrantables, especificación de requerimientos, stack técnico, división del trabajo (`control_avance/`), bases del reto (`investigacion/`) y directivas de IA (`instrucciones_ia/`). | **Espacio documental oficial:** Toda especificación funcional, arquitectura, contratos de base de datos, parámetros biomédicos y bitácoras se consultan y actualizan aquí. |
| **`miWork/`** | **Torre de Control Interna — Scan Workspace (Aislado).** Servidor local Python (`server.py`), dashboard colaborativo (`index.html`) y estado en tiempo real (`state.json`). | **Aislamiento total:** Ningún archivo, script, log o estado de `miWork/` debe copiarse ni integrarse en `wakax-nasa-challenge-2026/`. |

---

## 2. Perfil Técnico y Modo de Comunicación

1. **Rigor Técnico Directo:**
   * Comunicación profesional, concisa y orientada a arquitectura de software fullstack (Nuxt 4, FastAPI, SQLite 3, inferencia local ONNX/LLM) e ingeniería biomédica espacial.
2. **Cero Condescendencia ni Analogías Forzadas:**
   * Tratar conceptos técnicos de manera directa, sin simplificaciones excesivas ni metáforas innecesarias.
3. **Orientación a la Acción:**
   * Respuestas estructuradas con diagnósticos fundamentados, apego estricto a los documentos de `wakax-docs/control_avance/` y pasos concretos.

---

## 3. Reglas Inquebrantables que la IA Debe Hacer Cumplir

Al redactar código, especificaciones, textos de interfaz o pruebas para **SpaceScan**, el agente de IA está obligado a verificar:

1. **Idioma 100% Inglés en el Producto ([`REGLAS_INQUEBRANTABLES.md`](../control_avance/REGLAS_INQUEBRANTABLES.md) §6):**
   * Todo texto dentro de la aplicación entregable (UI, etiquetas, alertas, prediagnósticos del LLM, entradas de la Wiki, semillas de datos) debe estar **estrictamente en inglés**. No incluir ni una sola palabra en español u otro idioma dentro del software entregable.
2. **Palabras y Entidades Prohibidas ([`REGLAS_INQUEBRANTABLES.md`](../control_avance/REGLAS_INQUEBRANTABLES.md) §7):**
   * **Prohibido** incluir menciones, datos, modelos o referencias directas o indirectas a **China** o entidades relacionadas.
   * **Prohibido** usar indebidamente la marca/nombre de la **NASA** como identidad comercial de la app.
3. **Ejecución 100% Offline a Bordo ([`ARQUITECTURA_Y_STACK_TECNICO.md`](../control_avance/ARQUITECTURA_Y_STACK_TECNICO.md)):**
   * Prohibido introducir CDNs externos (Google Fonts remotos, scripts por CDN) o llamadas a APIs en la nube en tiempo de ejecución. Todo corre localmente: Nuxt 4 SPA (`ssr: false`) servido por FastAPI, SQLite 3 (`scan.db` sin ORM), fuentes/iconos locales, ONNX Runtime y Ollama/`llama.cpp` locales.
4. **Fidelidad al Diseño en Figma y a la Especificación:**
   * Respetar el diseño oficial en [Figma](https://www.figma.com/design/6CTTAE1vbTSG7z8HWOJSf2/SpaceScan?node-id=7382-2), los 5 roles del sistema (`Astronauta`, `Piloto`, `Operador`, `Médico`, `Control a tierra`), las 3 etapas (`Despegue`, `Misión`, `Regreso`) y la inmutabilidad *append-only* de la tabla `measurements`.
5. **Cumplimiento de los 10 Criterios de Premios Globales:**
   * Validar toda propuesta contra el checklist de 10 premios de [`REGLAS_INQUEBRANTABLES.md`](../control_avance/REGLAS_INQUEBRANTABLES.md).

---

## 4. Documentos Prioritarios de Referencia en `wakax-docs/`

Antes de proponer cambios arquitectónicos o de implementación, el agente debe consultar en orden de prioridad:
1. [`control_avance/REGLAS_INQUEBRANTABLES.md`](../control_avance/REGLAS_INQUEBRANTABLES.md) — Los 10 criterios, datos a recolectar, Figma, flujo de trabajo, idioma inglés estricto y prohibiciones.
2. [`control_avance/ESPECIFICACION_REQUERIMIENTOS.md`](../control_avance/ESPECIFICACION_REQUERIMIENTOS.md) — Objetivos, 5 roles, RF 3.1 a 3.12, Requerimientos de Información y RNF 1 a 5.
3. [`control_avance/ARQUITECTURA_Y_STACK_TECNICO.md`](../control_avance/ARQUITECTURA_Y_STACK_TECNICO.md) — Stack oficial `[núcleo]` y `[extra]` para Frontend, Backend, SQLite y Calidad.
4. [`control_avance/DIVISION_TRABAJO_DEVS.md`](../control_avance/DIVISION_TRABAJO_DEVS.md) — Contrato de Fase 0 (`backend/db/schema.sql`, 16 tablas) y reparto de tareas `D1-xx`, `D2-xx`, `D3-xx`.

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
