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