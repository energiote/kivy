# Introducción de Kivy

1. Introducción
    * [Instalación](#instalación)
    * [Sintaxis](#sintaxis)
2. Documentación
    * [Layout](/Documentation/Layout/layout2.md)  
        1. [Box Layout](/Documentation/Layout/1_BoxLayout/BoxLayout.md) 
        2. [Anchor Layout](/Documentation/Layout/2_AnchorLayout/AnchorLayout.md)  
        3. [Grid Layout](/Documentation/Layout/3_GridLayout/GridLayout.md)  
        4. [Stack Layout](/Documentation/Layout/4_StackLayout/StackLayout.md)  
        6. [Page Layout](/Documentation/Layout/5_PageLayout/PageLayout.md)

    * [Widget](/Documentation/Widget/)  
    * [Canvas](/Documentation/Canvas/)  
    
<!-- 3. Galaxy
    1. Gestión de la perspectiva de los movimiento
    2. Generación del terreno, mostrar la nave espacial y gestionar las colisiones
    3. Agregar menu al juego, visualización de la puntuación, imágenes y resproducir sonidos -->

##  Instalación
>[Introducción](#introducción-de-kivy) /  Instalación

#### 1. Comprobación de versiones :
    
* Comprobamos si nuestra versión de Python es aceptada por [kivy](https://kivy.org/doc/stable/gettingstarted/installation.html)  .

#### 2. Entorno virtual :
* Instalar virutalenv : `pip install virtualenv`
* Crear un nuevo entorno : `virtualenv venv`
* Activar el entorno virtual : `.\venv\Script\activate`
    * Si da error usa : `Set-ExecutionPolicy Unrestricted -Scope CurrentUser`
* Desactivar : `deactivate`

* Otros comandos:
    * Listar los paquetes instalados en python : `pip list`
    * Guardar la lista en un documento : `pip freeze > requirement.txt`
    * Instalar los paquetes guardados en lista : `pip install -r requirement.txt`

#### 3. Instalar kivy
* `pip install kivy`

## Sintaxis
>[Introducción](#introducción-de-kivy) /   /  Sintaxis

```py
from kivy.app import App

class Nombre_App(App):
    pass

Nombre_App().run()
```

- Importamos la clase `App` del archivo kivy/app.py `from kivy.app`.
- Heredamos las variables de la clase `(App)` en nuestra nueva clase `Nombre_App`.
- La palabra clave `pass` permite las clases vacias.
- Arrancamos la clase `ProyectApp()` con la función `run()`.

### Archivo.kv

- Las clase que hemos creado será el nombre que tenga el archivo.kv, en este caso `Nombre_.kv`
- `App` de `Nombre_App` es el conector de los archivos y no aparecerá en el nombre del archivo.kv



    
