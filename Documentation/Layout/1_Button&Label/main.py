from kivy.app import App
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()

'''
Notas:
    - El eje de coordenadas empieza desde el x0 y y0 abajo a la izquierda.
    - Responsive:
        - En el archivo TheLab.py 
            - si usamos ej: size: 40, 40
                - Serán 40 pixeles
            - Pero si usamos ej: size: "40dp","40dp"
                - Se adapta a cualquier pantalla
                - dp: density independant pixels
'''