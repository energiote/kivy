# Layout
>[Introduction](../../README.md) / Layout
1. [Box Layout]() 
2. [Anchor Layout]()  
3. [Grid Layout]()  
4. [Stack Layout]()  
6. [Page Layout]()

## Introducción:
En cualquier de los casos

Los nombres de los arhivos serán:
* main.py
* ProyectoApp

El eje de coordenadas empieza desde abajo a la izquierda (0,0)

## Sintaxis

* Librerias de todos los layouts:
    ```py
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.anchorlayout import AnchorLayout 
        from kivy.uix.gridlayout import GridLayout 
        from kivy.uix.stacklayout import StackLayout
        from kivy.uix.pagelayout import PageLayout 
    ```

## Inicialización:
Hablaremos de inicializar cada layout distinto, en este caso usaré BoxLayout
1. Partimos de iniciar la consola con la sintaxis básica
    ```py
        from kivy.app import App

        class NombreProyectoApp(App):
            pass

        NombreProyectoApp().run()
    ```
    * [Click aquí para probar](/0_Layout/1_basic_sintaxis.py/main.py)

En este caso pondré el box layout como ejemplo

* Sólo usando Python :
    ```py
    from kivy.app import App
    from kivy.uix.button import Button
    from kivy.uix.boxlayout import BoxLayout

    class BoxLayoutExample(BoxLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            b = Button(text="A")
            self.add_widget(b)

    class ProyectoApp(App):
        def build(self):
            return BoxLayoutExample()

    ProyectoApp().run()
    ```
* Sin usar el método build()
    ```py
    
    ```

### 1. Box Layout
1. Usando sólo 1 archivo.py
    ```py
    from kivy.app import App
    from kivy.uix.button import Button
    from kivy.uix.boxlayout import BoxLayout

    class BoxLayoutExample(BoxLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            b = Button(text="A")
            self.add_widget(b)

    class ProyectoApp(App):
        def build(self):
            return BoxLayoutExample()
    ProyectoApp().run()
    ```
2. Uso de ambos archivos= .py y .kv
    ```py
    from kivy.app import App

    class ProyectoApp(App):
        pass

    ProyectoApp().run()
    ```
    ```kv
    BoxLayout:
    ```


    * Archivo.kc
        ```
        BoxLayout:
        ```
* Hace la función de organizar los elementos en su interior.
### 2. Anchor Layout
```py
from kivy.uix.anchorlayout import AnchorLayout 
```
### 3. Grid Layout
```py
from kivy.uix.gridlayout import GridLayout 
```
### 4. Stack Layout  
```py
from kivy.uix.stacklayout import StackLayout 
```
### 5. Page Layout  
```py
from kivy.uix.pagelayout import PageLayout 
```











Se podría usar como una imagen fija en la app como
* Inicio, shop, cuenta,...


1. Importamos la librería
    * Archivo.py : 
        ```py
        from kivy.uix.anchorlayout import AnchorLayout
        ```
    * Archivo.kv :
        ```
        AnchorLayout:
        ```

2. 


Formas usar la consola:
1. Creación de un layout básico en kivy
    * La sintaxis básica en el arhivo.py
    ```kv
    # Creamos un AnchorLayout
    AnchorLayout:
        Button:
            text:"example"
    ```
2. Medios: Asignando una variable para usos futuros:
    ```kv
    AnchorLayoutExample:

    <AnchorLayoutExample@AnchorLayout>
        Button:
            text:"example"
    ```
3. Arrancando desde el archivo.py
    ```py
    class AnchorLayoutExample(AnchorLayout)
    ```
    ```kv
    AnchorLayoutExample:
        <AnchorLayoutExample>:
            Button:
                text:"example"
    ```
4. Solo desde python
    ```py
    class AnchorLayoutExample(AnchorLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            X = Button(text="example")
            self.add_widget(X)

    class TheLabApp(App):
        def build(self):
            return AnchorLayoutExample()

    ```
<hr>

Comparación entre:

+ Esto es lo mismo que
    ```py
    class TheLabApp(App):
        def build(self):
            return AnchorLayoutExample()
    ```
* Poner esto en el archivo.kv
    ```kv
    AnchorLayoutExample:
    ```

<hr>

+ Esto es lo mismo que
    ```py
    class AnchorLayoutExample(AnchorLayout):
        pass
    ```
+ Esto en el archivo kivy
    * Inicializamos con:
        ```kv
        AnchorLayoutExample:
        ```
    * Creamos la clase:
        ```kv
        <AnchorLayoutExample@AnchorLayout>
        ```


Recordatorio sintaxis básica:
```py
from kivy.app import App

class Nombre_App(App):
    pass

Nombre_App().run()
```

Con esto, y el archivo.kv creado podemos iniciar con 