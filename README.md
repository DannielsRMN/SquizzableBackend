# 🚀 Presentación de Lenguaje de Programación I - Equipo **TomCat**

Este repositorio fue creado para la presentación de avances del curso **Lenguaje de Programación I**. Aquí encontrarás documentación, código fuente y recursos relacionados con nuestro proyecto.

## 👥 Integrantes del equipo:

- 👤 **Martel Neira Danniels Rafael**
- 👤 **Caldas Sifuentes Raul**
- 👤 **Lopez Castillo Jean Andres**
- 👤 **Dionicio Orihuela Edson**
- 👤 **Palacios Presentación Jeferson**

## 📁 Estructura del repositorio

QuizAPI/
├── QuizAPI/ # Configuración principal del proyecto Django
│ ├── settings.py # Configuración general (BD, apps, etc.)
│ ├── urls.py # URLs raíz del proyecto
│ └── ...
├── api/ # Aplicación principal del proyecto
│ ├── models.py # Modelos de base de datos
│ ├── views.py # Vistas o controladores
│ ├── serializers.py # Serializadores (si usas DRF)
│ ├── middleware.py # ✅ Middleware personalizado para logging, validaciones, etc.
│ └── ...
├── imagenes/ # Carpeta para archivos multimedia (imágenes subidas)
├── db.sqlite3 # Base de datos SQLite
└── manage.py # Script de comandos para Django
