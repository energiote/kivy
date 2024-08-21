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
        self.orientation = "lr-bt"
        self.padding = (dp(20),dp(20),dp(20),dp(20))
        self.spacing = dp(20), dp(20)
        for i in range(1,100+1):
            size = dp(100)
            b = Button(text=str(i), size_hint=(None, None), size=(size,size))
            self.add_widget(b)

class TheLabApp(App):
    pass

TheLabApp().run()