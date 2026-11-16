# Manual Rápido de Despliegue — SpaceScan

Resumen operativo de la configuración en producción para **SpaceScan** (`wakax-nasa-challenge-2026`).

---

## 1. Arquitectura en Producción

| Componente | Hosting / Servicio | URL / Puerto | Origen de Build |
| :--- | :--- | :--- | :--- |
| **Frontend (SPA estática)** | GitHub Pages (`main`) | `https://spacescan.me` | `.github/workflows/deploy-pages.yml` (`frontend/public/CNAME`) |
| **Reverse Proxy + TLS** | Caddy (`caddy:2-alpine`) en EC2 | `80/tcp`, `443/tcp`, `443/udp` | `deploy/Caddyfile` (`flush_interval -1` para SSE) |
| **Backend API (FastAPI + SQLite)** | Docker en AWS EC2 (`--workers 1`) | `127.0.0.1:8080` -> `https://api.spacescan.me` | `ghcr.io/willor16/wakax-nasa-challenge-2026-api:latest` |

---

## 2. DNS (`spacescan.me`)

| Tipo | Host | Valor | Uso |
| :--- | :--- | :--- | :--- |
| `A` | `@` | `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` | GitHub Pages (`spacescan.me`) |
| `CNAME` | `www` | `spacescan.me.` | Subdominio `www` |
| `A` | `api` | `18.223.54.184` | Elastic IP de la EC2 |

---

## 3. AWS EC2 y Security Group

* **SO:** Ubuntu 24.04.5 LTS (`x86_64`), `1.9 GiB` RAM, disco EBS `19 GB` (sin EFS/FSx/S3: SQLite requiere disco local EBS).
* **Elastic IP:** `18.223.54.184`
* **Usuario SSH:** `ubuntu` (llave local `wakax-nasa-challenge.pem` con `chmod 400`).
* **Reglas de entrada (Inbound Security Group):**
  * `22/tcp`: SSH (necesario también para runners de GitHub Actions durante el deploy).
  * `80/tcp` (`0.0.0.0/0`): validación Let's Encrypt y redirección a HTTPS.
  * `443/tcp` y `443/udp` (`0.0.0.0/0`): tráfico HTTPS, SSE y HTTP/3.

---

## 4. Configuración Aplicada en la EC2

1. **Swap (2 GiB):** `/swapfile` montado en `/etc/fstab` con `vm.swappiness=10` en `/etc/sysctl.d/99-swappiness.conf`.
2. **Docker y Compose:** instalados con `https://get.docker.com`; usuario `ubuntu` agregado al grupo `docker`.
3. **Proyecto y variables (`~/spacescan`):**
   * Clonado de `https://github.com/willor16/wakax-nasa-challenge-2026.git` (rama `main`).
   * `.env` copiado de `.env.example`:
     ```env
     API_DOMAIN=api.spacescan.me
     SPACESCAN_CORS_ORIGINS=https://spacescan.me,https://www.spacescan.me
     ```
4. **Persistencia (volúmenes Docker):**
   * `spacescan_storage` -> `/app/storage` (SQLite `spacescan.db`, audios y llaves de sesión).
   * `caddy_data` y `caddy_config` -> certificados TLS de Let's Encrypt.

---

## 5. CI/CD con GitHub Actions (Enfoque B: GHCR -> EC2)

* **Frontend (`.github/workflows/deploy-pages.yml`):** en cada `push` a `main` compila la SPA con `NUXT_PUBLIC_API_BASE=https://api.spacescan.me` y publica en GitHub Pages.
* **Backend (`.github/workflows/deploy-backend.yml`):** en `push` a `main` (cambios en `backend/**`, `deploy/**`, `docker-compose.ec2.yml` o el propio workflow) o ejecución manual (`workflow_dispatch`):
  1. Construye y sube la imagen a `ghcr.io/willor16/wakax-nasa-challenge-2026-api:latest`.
  2. Entra por SSH (`ssh -T ... "bash -s"` para evitar que `~/.bash_logout` devuelva error sin TTY), actualiza `main`, ejecuta `docker compose -f docker-compose.ec2.yml pull api`, `up -d --no-build`, `docker image prune -f` y verifica `http://127.0.0.1:8080/api/v1/health`.

### Secrets requeridos en GitHub
Ruta: **Settings -> Secrets and variables -> Actions -> Secrets**
* `EC2_HOST`: `18.223.54.184`
* `EC2_USER`: `ubuntu`
* `EC2_SSH_KEY`: contenido completo de la llave privada `.pem`

---

## 6. Comandos de Verificación y Operación

```bash
# Verificar frontend y backend desde fuera
curl -sSI https://spacescan.me/
curl -fsS https://api.spacescan.me/api/v1/health

# Conectarse a la EC2
ssh -i wakax-nasa-challenge.pem ubuntu@18.223.54.184

# Dentro de la EC2 (~/spacescan)
docker compose -f docker-compose.ec2.yml ps
docker compose -f docker-compose.ec2.yml logs -f api caddy
docker compose -f docker-compose.ec2.yml restart api
```
