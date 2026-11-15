# Usuarios, Roles y Credenciales de Acceso — SpaceScan

Documento de referencia con los usuarios, PINs de acceso, roles y reglas de autenticación verificados en el código fuente y la base de datos SQLite local (`wakax-nasa-challenge-2026/backend/db/spacescan.db`).

***

## 1. Credenciales de Tripulación (SpaceScan)

En **SpaceScan** no existen correos ni contraseñas alfanuméricas: el inicio de sesión (`/login`) funciona seleccionando un perfil de tripulante (`crew_id`) e ingresando un **PIN numérico de 4 dígitos** (`^\d{4}$`).

| `crew_id` | Código UI | Nombre (en `spacescan.db` actual) | Nombre (en `mission_baseline.json`) | Rol (`role`) | Título en UI (`title_en`)                  | PIN (4 dígitos) | Edad / Sexo / Sangre / Estatura | Estado actual en DB           |
| :-------- | :-------- | :-------------------------------- | :---------------------------------- | :----------- | :----------------------------------------- | :-------------: | :------------------------------ | :---------------------------- |
| `ID-01`   | `ID·01`   | **Elena Vargas**                  | Elena Vargas                        | `PILOT`      | `Pilot` *(seed: `Commander`)*              |    **`1042`**   | 36 · `F` · `O+` · 171.0 cm      | Activa · `failed_attempts: 0` |
| `ID-02`   | `ID·02`   | **Marcus Vance**                  | Marcus Vance                        | `OPERATOR`   | `Operator` *(seed: `Flight Engineer`)*     |    **`2084`**   | 39 · `M` · `A+` · 182.0 cm      | Activo · `failed_attempts: 1` |
| `ID-03`   | `ID·03`   | **Amara Okafor**                  | Amara Okafor                        | `PHYSICIAN`  | `Physician` *(seed: `Medical Officer`)*    |    **`3190`**   | 41 · `F` · `B+` · 168.0 cm      | Activa · `failed_attempts: 0` |
| `ID-04`   | `ID·04`   | **Kenji Sato**                    | Jonas Reed                          | `ASTRONAUT`  | `Astronaut` *(seed: `Mission Specialist`)* |    **`4275`**   | 34 · `M` · `AB+` · 176.0 cm     | Activo · `failed_attempts: 1` |

> **Nota sobre la discrepancia detectada en `spacescan.db`:**
>
> * Los 4 PINs anteriores (`1042`, `2084`, `3190`, `4275`) fueron verificados criptográficamente contra los hashes `pin_hash` almacenados actualmente en `wakax-nasa-challenge-2026/backend/db/spacescan.db` y **todos coinciden (`PIN_MATCH=True`)**.
> * En la base SQLite actual (`spacescan.db`), `ID-04` figura como **Kenji Sato** y la columna `title_en` está en `NULL` para los 4 registros (por lo que la API usa el respaldo por rol en `crew_names.py`), mientras que en [`mission_baseline.json`](../wakax-nasa-challenge-2026/backend/db/seed_snapshots/mission_baseline.json) y en los tests (`test_foundation.py`) `ID-04` figura como **Jonas Reed** con `title_en` explícito (`Commander`, `Flight Engineer`, `Medical Officer`, `Mission Specialist`). Si se ejecuta un reset del seeder (`uv run python -m db.seed --reset`), se cargarán los valores de `mission_baseline.json`.

***

## 2. Permisos por Rol (RBAC)

Definido en `app/auth_utils.py` y `app/routers/crew.py`:

* **Acceso Público (sin PIN):**
  * Pantallas `/login`, `/crew-overview`, `/crew-streaks`.
  * Endpoints públicos de resumen general de tripulación, perfiles básicos (sin datos clínicos sensibles), reloj de misión y telemetría de cabina.
* **Tripulante autenticado (`ASTRONAUT`, `PILOT`, `OPERATOR`, `PHYSICIAN`):**
  * Acceso a sus propios registros médicos, captura de mediciones, sueño, visión, auscultación, guía médica y comunicaciones.
* **`OPERATOR` (`ID-02` — Marcus Vance):**
  * Único rol habilitado (`require_operator`) para administrar cuentas en `/crew-management` (`GET /api/v1/crew`, `POST /api/v1/crew`, `PATCH /api/v1/crew/{crew_id}`): crear tripulantes nuevos, editar datos, restablecer PIN, activar/desactivar cuentas, desbloquear perfiles bloqueados, recalcular baselines y avanzar la etapa de misión (`LAUNCH -> MISSION -> RETURN`).
  * El backend impide desactivar o cambiar el rol del último `OPERATOR` activo (`_guard_last_operator`).
* **`PHYSICIAN` (`ID-03` — Amara Okafor):**
  * Único rol habilitado (`require_physician` y `ensure_crew_access`) para consultar registros clínicos y alertas de otros tripulantes además de los propios.

***

## 3. Reglas Técnicas de Autenticación y Seguridad

* **Hashing de PIN:** `hash_pin()` / `verify_pin()` en `wakax-nasa-challenge-2026/backend/app/auth_utils.py`. Usa `Argon2id` (`argon2-cffi`) si está disponible, o `scrypt` de biblioteca estándar (`scrypt$<salt>$<hex>`). En la base `spacescan.db` actual los hashes usan `scrypt`.
* **Bloqueo por intentos fallidos:** `MAX_FAILED_ATTEMPTS = 5` intentos incorrectos consecutivos bloquean la cuenta durante `LOCKOUT_MINUTES = 5` minutos (HTTP `423 Locked`), o hasta que un `OPERATOR` la desbloquee vía `PATCH /api/v1/crew/{crew_id}` (`unlock_account: true`).
* **Sesión JWT:** Token `HS256` con vigencia de **480 minutos (8 horas)** (`JWT_EXPIRE_MINUTES = 480`), guardado en el navegador únicamente en `sessionStorage` bajo la clave `spacescan.session`.
* **Sincronización remota de Control a Tierra:** El endpoint `POST /api/v1/crew/ground-sync` no usa PIN de usuario; exige firma `HMAC-SHA256` en el header `X-Ground-Signature` generada con `GROUND_LINK_KEY` (`SPACESCAN_GROUND_LINK_KEY` o `wakax-nasa-challenge-2026/backend/storage/ground_link.key`).

***

## 4. Torre de Control Interna (`docs/miWork/`)

El dashboard interno del equipo en `docs/miWork/` (`Puerto 8000`) **no tiene contraseñas ni autenticación**. Utiliza únicamente un selector visual de integrante (`Wilson`, `Wilmer`, `Carlos`, `Steve`, `Sandra`, `Foco (Poco)` o nombre personalizado) persistido localmente en `localStorage` (`scan_space_active_user`).
