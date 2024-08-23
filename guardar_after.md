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



