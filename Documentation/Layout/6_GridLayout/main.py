from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout

# class GridLayoutExample(GridLayout):
#     pass

class BoxLayoutExample(BoxLayout):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()

'''
    Usamos 2 formas de declación:
        1.- La que llevamos haciendo todo este tiempo
            - main.py
                class GridLayoutExample(GridLayout):
                    pass
            - Thelag.kv
                GridLayoutExample:

        2.- Solo declarndo en archivo.kv
            GridLayoutExample:
            <GridLayoutExample@GridLayout>:
                Button:.....
'''