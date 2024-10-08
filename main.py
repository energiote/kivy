from kivy.app import App

from kivy.metrics import dp

from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

class StackLayoutExample(StackLayout):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        # self.padding = (dp(20),dp(20),dp(20),dp(20))
        # self.spacing = dp(20), dp(20)
        for i in range(1,100+1):
            size = dp(100)
            b = Button(text=str(i), size_hint=(None, None), size=(size,size))
            self.add_widget(b)

# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    #     # Orientación
    #     '''
    #     Por defecto es "horizontal"
    #     '''
    #     self.orientation = "vertical"

    #     # Instanciadores
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")

    #     # Ejecutadores
    #     '''
    #     El orden afecta a su posición
    #     '''
    #     self.add_widget(b2)
    #     self.add_widget(b1)
    #     self.add_widget(b3)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()