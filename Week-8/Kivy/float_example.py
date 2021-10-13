import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout  # an alternative layout to widget that automatically scales


class FloatingApp(App):  # creates the widget object

    def build(self):
        return FloatLayout()


flApp = FloatingApp()
flApp.run()
