 E-Commerce Básico con Django

Una aplicación web de comercio electrónico básica desarrollada con Django que permite gestionar productos y visualizarlos en una interfaz amigable.

## Características

- Catálogo de productos con imágenes
- Panel de administración para gestionar productos
- Interfaz responsiva usando Bootstrap
- Detalles de productos
- Sistema de categorías

## Requisitos

- Python 3.8+
- Django 4.2+
- Pillow

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/django-ecommerce-basic.git
   cd django-ecommerce-basic
   ```

2. Crear y activar el entorno virtual:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Realizar las migraciones:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Crear un superusuario:

   ```bash
   python manage.py createsuperuser
   ```

6. Iniciar el servidor:

   ```bash
   python manage.py runserver
   ```

## Uso

1. Acceder al panel de administración en `/admin`.
2. Iniciar sesión con el superusuario creado.
3. Comenzar a añadir productos y categorías.
4. Visitar la página principal para ver el catálogo de productos.

## Estructura del Proyecto

```
django-ecommerce-basic/
├── ecommerce/           # Proyecto principal
├── products/           # Aplicación de productos
├── static/            # Archivos estáticos
├── media/             # Imágenes subidas
└── templates/         # Plantillas HTML
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
