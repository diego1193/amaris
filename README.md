# Prueba tecnica AMARIS - Diego Cabrera 📋

> En este repositorio podrá encontrar un pequeñp backend en django y dos archivos .py en el archivo **punto_1.py** se encuntra la solución del primer punto de la prueba y el archivo **punto_3.py** se encuntra la solución del primer punto de la prueba.

## Requerimientos 📔
* [Python](https://www.python.org/) (realizado en python 3.9.14)
* [Django](https://github.com/django/django)
* [.EVN](https://github.com/theskumar/python-dotenv)
* [PyTest](https://docs.pytest.org/en/6.2.x/getting-started.html)

## Intalación del entorno y paquetes 🛠️

Primero tendremos que dirigirnos a anaconda prompt (debes tener instalado anaconda), lo puedes buscar en tu buscado de Windows (si está instalado), una vez estemos en la consola de anaconda, procederemos instalar el entorno virtual, empezaremos con escribir:
```
python -m -venv (nombre del entorno)
```

Luego tendremos que clonar el proyecto:
```
git clone git@github.com:diego1193/amaris.git
```
Una vez clonado el proyecto, nos dirigimos a la ruta mediante la consola de anaconda y una vez allí, podremos encontrar el archivo requirements.txt; procederemos a instalarlo:
```
pip install -r requirements.txt
```

## Solucion punto 1, prueba tecnica 🚀

Ya descargado el repositorio, procederemos a abrir el archivo con Visual Studio Code o nuestro editor de codigo preferido; allí encontraremos un archivo llamado **punto_1**, ahora procederemos a ejecutar cada uno de estos archivos (para poder ejecutarlos debemos dirigirnos a la carpeta **amaris** mediante consola).

#### Solución primara parte de la prueba 📝

En consola escribimos:
```
python punto_1.py
```
Y allí nos pide que ingresemos los nombres de las personas separadas por coma sin espacios, le damos enter y aperece la solución del primer punto.

#### Solución a la tercera parte de la prueba 📝

En consola escribimos:
```
python punto_3.py
```
Y allí nos que ingresemos las dos cadenas de texto, le damos enter y aperece la solución del tercer punto punto.

## Solucion parte 2, prueba tecnica 📖

### Arquitectura my_swapi ⚙️

- amaris:
    - app:
        - admin.py
        - apps.py
        - models.py
        - schema.py
        - tests.py
        - utils.py
        - views.py
    - amaris: **_(Archivos principales y configuraciones de la aplicación)_**
        - schema.py
        - settings.py
        - urls.py
        - wsgi.py
    - db.sqlite3 
    - manage.py
    - pytest.ini **_(Configuración para pruebas unitarias)_**
    - requirements.txt
***
### Ejecutando y probando aplicación 🚀

* ### Ejecutando migraciones y cargando registros a la base de datos

Para poder ejecutar el proyecto debemos dirigirnos mediante consola a la carpeta **amaris**, por consiguiente debemos escribir:
```
python manage.py makemigrations
```
```
python manage.py migrate
```

* #### PyTest

Ahora escribimos lo siguiente:
```
pytest
```
Esto lo hacemos para generar las pruebas unitarias con herramienta **_PyTest_** y poder estar seguros que nuestro proyecto esta corriendo correctamente antes de salir a producción.
#### Ejemplo:
![ScreenShot](/images/pytest1.jpg)

* #### Ejecutando proyecto
Para correr nuestro proyecto:
```
python manage.py runserver
```
Una vez estemos corriendo el servidor, podemos ir a postman o a nuestro navegador web y colocar la siguiente URL
```
http://127.0.0.1:80O0/pockemon/(escribir id del pokemon)/
```
#### ejemplo
![ScreenShot](/images/postman1.jpg)


## **__Eso es todo, muchas gracias__**. 🧑‍💻
