from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Name_Layout_Class(BoxLayout):
    
    # Ejemplo de muestra
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        X = Button(text="example")
        self.add_widget(X)

class NameClass_App(App):
    def build(self):
        return Name_Layout_Class()

NameClass_App().run()