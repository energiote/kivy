from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

class Name_Layout_Class(BoxLayout):

    # Ejemplo de muestra
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b = Button(text="A")
        self.add_widget(b)

class NameClass_App(App):
    pass

NameClass_App().run()