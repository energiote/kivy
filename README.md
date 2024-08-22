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

##  Instalación
>[Introducción](#introducción) /  Instalación

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
>[Introducción](#introducción) /  Sintaxis
```py
from kivy.app import App

class Nombre_App(App):
    pass

ProyectApp().run()
```

- Importamos la clase `App` del archivo kivy/app.py `from kivy.app`.
- Heredamos las variables de la clase `(App)` en nuestra nueva clase `Nombre_App`.
- La palabra clave `pass` permite las clases vacias.
- Arrancamos la clase `ProyectApp()` con la función `run()`.

    ![Black Console](/imgs/introducción/black_console_2.png)

## Explicación código
>[Introducción](#introducción) /  Explicación código

### Uso de la clase base
```py
# También se puede utilizar AnchorLayout, GridLayout, StackLayout,..
from kivy.uix.boxlayout import BoxLayout

    class Nombre_clase_layout(BoxLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
```
- Llamamos al arhivo kivy/uix/boxlayout.py e importamos `BoxLayout`.
- Creamos un subclase `Nombre_clase_layout` al que heredaremos las variables de la clase base`(BoxLayout)`.
- Definimos las variables de instancia con `__init__`:
    - `self` se utliza como primer parámetro en las variables de instancia`__init__` de la clase. Permite el acceso a las varibles de la clase.
    - `**kwargs` son los argumentos que no se especificaron de forma explicita.
        ```py
        class Persona:
            def __init__(self, nombre, **kwargs):
                self.nombre = nombre
                self.otros_datos = kwargs

        p = Persona(nombre="Sergio", edad="26", profesión= "programador")
        print("self.nombre: ",p.nombre)
        print("kwargs: ",p.otros_datos) 
        ```
    - Resultado :
        ```
        self.nombre:  Sergio
        kwargs:  {'edad': '26', 'profesión': 'programador'}
        ```
- `super()` es una función que llama al método de la clase base`(BoxLayout)` para acceder a sus atributos de instancia mediante `.__init__` y a todos sus argumentos con `(**kwargs)`.




    
