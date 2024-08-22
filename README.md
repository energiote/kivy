# Introducción

1. Introducción
    * [Instalación](#instalación)
    * [Sintaxis](#sintaxis)
    * [Explicación código](#explicación-código)
2. The lab  
    * [Layout](/Documentation/Layout/layout.md)  
        * [Box Layout]()  
        * [Anchor Layout]()  
        * [Grid Layout]()  
        * [Stack Layout]()  
        * [Scroll View]()  
        * [Page Layout]()  

    * [Widget](/Documentation/Widget/)  
    * [Canvas](/Documentation/Canvas/)  
    
3. Galaxy
    1. Gestión de la perspectiva de los movimiento
    2. Generación del terreno, mostrar la nave espacial y gestionar las colisiones
    3. Agregar menu al juego, visualización de la puntuación, imágenes y resproducir sonidos
<br>
<br>
##  Instalación
>[Introducción](#introducción) /  Instalación
---



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

<br>
<br>

## Sintaxis
>[Introducción](#introducción) /  Sintaxis
<hr>

```py
from kivy.app import App

class ProyectApp(App):
    pass

ProyectApp().run()
```

1. Heredar clases:  
    - Es necesario que la clase base de nuestra aplicación herede la clase de kivy
```py
# Importamos del archivo kivy/app.py la clase App
from kivy.app import App

# ProyectApp heredará la clase de kivy/app.py
class ProyectApp(App):
    pass
```
2. Definir nuestra aplicación  
    - Es donde podemos definir las propiedades de la App
    - Puedes cambiar el nombre de tu la aplicación ***ProyectApp***
```py
class ProyectApp(App):
    pass
```
3. Arrancar la Aplicación
    - Se llama al metodo ***run()***
```py
ProyectApp().run()
```
<br>
<br>

## Explicación código
>[Introducción](#introducción) /  Explicación código
<hr>

```py
def __init__(self, **kwargs):
    super().__init__(**kwargs)
```
* `__init__` Se utiliza para inicializar un nuevo objeto de una clase  
* `self` de si mismo  
* `**kwargs` es un diccionario que contiene todos los argumentos pasados al constructor que no se especificarion de forma explícita :
    * Ej: {'ciudad': 'Madrid', 'profesion': 'Ingeniero'}
```py
def __init__(self, **kwargs):
```

```py
super().__init__(**kwargs)
```
- Codigo:
    - def __init__(self, **kwargs):
        - Empaqueta todos los argumentos de palabras clave utilizados en cualquier llamada dada a __init__ en un dict
    - super().__init__(**kwargs):
        - Los expande nuevamente en argumentos de palabras clave




    
