import random
import math
from kivy.app import  App
from kivy.uix.widget import Widget
class card(Widget):
    pass
class solitaire(Widget):
    def on_touch_down(self, touch):
        print(touch)

class Game(App):
    def build(self):
        return solitaire()


if __name__ == '__main__':
    Game().run()
