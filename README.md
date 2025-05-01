# 🍔 Automatización de Reportes de Apps de Delivery para Restaurantes

Este proyecto permite automatizar la descarga de reportes desde plataformas de delivery como **Uber Eats**, **Didi Food** y **Rappi**, ideal para restaurantes, franquicias o equipos contables que manejan múltiples cuentas. Usando bots personalizados y una interfaz gráfica intuitiva, esta herramienta reduce tareas repetitivas y mejora la eficiencia operativa.

---

## 🚀 ¿Qué hace esta app?

- Automatiza el login y descarga de reportes de Uber, Didi y Rappi.
- Permite seleccionar la fecha desde una interfaz gráfica simple.
- Ejecuta los bots de forma individual o simultánea.
- Lee credenciales desde un archivo Excel centralizado.
- Ideal para ejecutarse manualmente o de forma programada (tareas automáticas diarias).

---

## 🧰 Tecnologías utilizadas

- **Python 3.12**
- **Tkinter** – Para la interfaz gráfica.
- **Selenium** – Para la automatización web.
- **Pandas** – Para leer y procesar archivos Excel.
- **openpyxl** – Para soporte de archivos `.xlsx`.
- **ChromeDriver** – Para automatizar Chrome.

---

## 🗂️ Estructura del proyecto

automation/ ├── App.py # Script principal con la interfaz gráfica ├── bot_uber.py # Bot para automatizar Uber Eats ├── bot_didi.py # Bot para automatizar Didi Food ├── bot_rappi.py # Bot para automatizar Rappi ├── functions.py # Funciones comunes (leer Excel, helpers, etc.) ├── credentials/ │ └── credenciales.xlsx # Archivo con las credenciales de acceso


---

## 🧪 Cómo correr el proyecto

1. Cloná este repositorio o descargá los archivos.

2. Colocá tus credenciales en el archivo:

   - `automation/credentials/credenciales.xlsx`
   - Estructura: una hoja por app (`Uber`, `Didi`, `Rappi`) con columnas como `usuario`, `contraseña`, `sucursal`.

3. Instala las dependencias necesarias:

   En tu terminal:

   ```bash
   pip install -r requirements.txt


Ejecutá la app:

bash
Copy
Edit
python automation/App.py
📅 Ejecución automática
Podés programar este script para que se ejecute todos los días usando el Programador de Tareas de Windows (taskschd.msc) y así descargar los reportes de forma desatendida.

🔌 Integración con otros sistemas
Los archivos descargados pueden ser consumidos por sistemas como Power BI, Excel, Google Sheets o incluso sistemas POS como Aloha.

Es fácilmente adaptable para agregar nuevas plataformas de delivery o integraciones contables (por ejemplo, cálculo de comisiones o conciliaciones).

📦 Requisitos
Creá un archivo requirements.txt con el siguiente contenido (ya incluido en el repo):

nginx
Copy
Edit
selenium
pandas
openpyxl
tk
✨ Próximas funcionalidades
Integración con dashboards de Power BI para visualizar ventas por sucursal.

Consola web para gestión remota de bots.

Reportes automáticos por correo electrónico.

Comparativa entre plataformas.

🤝 Contribuciones
¿Querés agregar nuevas plataformas o funcionalidades? ¡Forkeá el repo y mandá tu PR!

Desarrollado con ❤️ para simplificar procesos repetitivos en gastronomía.
