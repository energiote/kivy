# Layout
>[Introduction](/README.md) / Layout

* Introducción Layouts
    1. [Box Layout](/Documentation/Layout/1_BoxLayout/BoxLayout.md) 
    2. [Anchor Layout](/Documentation/Layout/2_AnchorLayout/AnchorLayout.md)  
    3. [Grid Layout](/Documentation/Layout/3_GridLayout/GridLayout.md)  
    4. [Stack Layout](/Documentation/Layout/4_StackLayout/StackLayout.md)  
    6. [Page Layout](/Documentation/Layout/5_PageLayout/PageLayout.md)

## Introducción Layouts

### 1. Sintaxis en python
1. Layout Básico
    <!-- Code -->
    ```py
    from kivy.app import App
    from kivy.uix.__layout import __Layout #1

    class NameClass_App(App):
        def build(self): #2
            Layout = __Layout() #3
            return Layout #4

    NameClass_App().run()
    ```
    <!-- Explanation -->
    1. De la librería de un `__layout `(minúsculas) importamos `__Layout`(Pascal Case).
    2. En nuestra clase `NameClass_App(App)` ya explicada [anteriormete](/README.md/#instalación), definimos de la clase `App` su `build()`.
    3. Pasamos la clase `__Layout` a una variable nueva `Layout`
    4. Devolvemos la variable `Layout` al `build()`
    <!-- Links -->
    Ver ejemplo: [main.py](/Documentation/Layout/0_Layout/1_Sintaxis_in_Python/1_Basic_Layout/main.py).  
    Ruta del ejemplo: `/Documentation/Layout/0_Layout/1_Sintaxis_in_Python/1_Basic_Layout`
    ***

2. Layout en clase de herencia
    <!-- Code -->
    ```py
    from kivy.app import App
    from kivy.uix.__layout import __Layout

    class Name_Layout_Class(__Layout): #1
        pass

    class NameClass_App(App):
        def build(self) 
            return Name_Layout_Class() #2

    NameClass_App().run()
    ```
    <!-- Explanation -->
    1. De la clase base`(__Layout)` heredamos sus variables en `Name_Layout_Class`.
    2. Devolvemos todos los valores de `Name_Layout_Class()` para nuestro del `build()`.  
    <!-- Links -->
    Ver ejemplo: [main.py](/Documentation/Layout/0_Layout/1_Sintaxis_in_Python/2_Class_layout/main.py)  
    Ruta del ejemplo: `/Documentation/Layout/0_Layout/1_Sintaxis_in_Python/2_Class_layout`

### 2. Sintaxis en kivy

1. main.py :
    * Incluimos la [sintaxis básica](/README.md/#instalación) para vincular los arhivos y que funcione.
    
2. NameClass_.kv :
    1. Declarar un Layout Básico
        <!-- Code -->
        ```kv
        Name_Layout:
        ```
        <!-- Explanation -->
        * Actua como el Layout Básico visto en [Sintaxis en python](#1-sintaxis-en-python).
        <!-- Links -->
        Ver ejemplo: [main.py](/Documentation/Layout/0_Layout/2_Sintaxis_in_kivy/1_Básic_Layout/main.py), [NameClass_.py](/Documentation/Layout/0_Layout/2_Sintaxis_in_kivy/1_Básic_Layout/NameClass_.kv).  
        Ruta del ejemplo: `/Documentation/Layout/0_Layout/2_Sintaxis_in_kivy/1_Básic_Layout`
        ***
    2. Crear una variable y declarar un Layout Básico
        ```kv
        Name_Layout_Class:

        <Name_Layout_Class@____Layout>:
        ```
        * Es como si fuera crear una clase`Name_Layout_Class` con los atributos del `___Layout`

        Ver ejemplo: [main.py](/Documentation/Layout/0_Layout/2_Sintaxis_in_kivy/2_Variables_Layout/main.py), [NameClass_.py](/Documentation/Layout/0_Layout/2_Sintaxis_in_kivy/2_Variables_Layout/NameClass_.kv).  
        Ruta del ejemplo: `/Documentation/Layout/0_Layout/2_Sintaxis_in_kivy/2_Variables_Layout`
        
### 3. Sintaxis en Python y kivy

* main.py
    ```py
    from kivy.uix._____layout import _____Layout #1

    class Name_Layout_Class(____Layout): #2
        pass

    class NameClass_App(App):
        pass

    NameClass_App().run()
    ```
    1. Importamos la librería
    2. Creamos la clase de herancia
* NameClass_.kv
    ```kv
    Name_Layout_Class:

    <Name_Layout_Class>:
    ```
    * Invocamos la clase como si fuera el build().
    * Escribimos dentro la clase para construir su estructura.  

    Ver ejemplo: [main.py](/Documentation/Layout/0_Layout/3_Sintaxis_in_Python&Kivy/main.py), [NameClass_.py](/Documentation/Layout/0_Layout/3_Sintaxis_in_Python&Kivy/NameClass_.kv).  
    Ruta del ejemplo: `/Documentation/Layout/0_Layout/3_Sintaxis_in_Python&Kivy`  

## 2. Importar elementos de la clase base
>[Introduction](#layout) / Layout
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