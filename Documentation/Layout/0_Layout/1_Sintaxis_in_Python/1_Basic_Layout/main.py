from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class NameClass_App(App):

    # Ejemplo de muestra:
    def build(self):
        Layout = BoxLayout()
        Layout.add_widget(Button(text="A"))
        return Layout
    
NameClass_App().run()