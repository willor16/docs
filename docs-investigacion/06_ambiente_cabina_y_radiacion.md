# 06. Ambiente de Cabina y Radiación Espacial

> **Parámetros cubiertos:** `mis-humedad` (Humedad / Confort de Cabina) y `res-radiacion` (Radiación).

---

## 1. Rangos de Confort Ambiental en Cabina (`mis-humedad`)

* **Responsable:** Foco (Poco) (`listo: true`)
* **Fuente:** NASA — *6.0 Natural and Induced Environments Vol. 2*: https://www.nasa.gov/reference/6-0-natural-and-induced-environments-vol-2/?utm_source

| Parámetro | Temperatura | Humedad Relativa |
| :--- | :---: | :---: |
| **Zona de rendimiento citada** | `20 – 25 °C` | `30 % – 60 %` |
| **Extremos de referencia** | `18 °C` / `27 °C` | `75 %` (a `18 °C`) / `25 %` (a `27 °C`) |

---

## 2. Radiación Espacial y Límites de Exposición (`res-radiacion`)

* **Responsable:** Steve (`listo: true`)
* **Fuentes:**
  * NASA — *The Human Body in Space*: https://www.nasa.gov/humans-in-space/the-human-body-in-space/
  * NASA — *About the Space Radiation Element (SRE)*: https://www.nasa.gov/reference/about-the-space-radiation-element/
  * NASA — *OCHMO-TB-020: Radiation Protection*: https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-020-radiation-protection.pdf

### Riesgos y Mitigación
* La exposición a radiación espacial incrementa la probabilidad de desarrollar **cáncer**, **cardiopatías** y **cataratas**.
* **Puntos clave de protección:** **blindaje** y **monitoreo continuo de la radiación**.
* **Space Radiation Element (SRE):** Programa de NASA enfocado en desarrollar la base de conocimiento para predecir y gestionar los riesgos de la radiación del espacio profundo sobre la salud humana.

### Estándares de Referencia de Dosis

| Categoría de Exposición | Dosis de Referencia |
| :--- | :---: |
| **Radiación natural de fondo** *(cualquier persona)* | `2.4 – 3.0 mSv` |
| **Límite para el público general** *(fuentes artificiales)* | `1 mSv / año` |
| **Trabajador ocupacional** *(radiólogos, planta nuclear)* | `20 mSv / año` |
