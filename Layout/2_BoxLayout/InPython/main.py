from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.button import Button, Label

from kivy.uix.boxlayout import BoxLayout

class BoxLayoutExample(BoxLayout):
    '''
        **kwargs: Internal Working of kivy
    '''
    # Recopila y expande las variables
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Orientación
        '''
        Por defecto es "horizontal"
        '''
        self.orientation = "vertical"

        # Instanciadores
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Label(text="C")

        # Ejecutadores
        '''
        El orden afecta a su posición
        '''
        self.add_widget(b2)
        self.add_widget(b1)
        self.add_widget(b3)

class TheLabApp(App):
    pass

TheLabApp().run()

