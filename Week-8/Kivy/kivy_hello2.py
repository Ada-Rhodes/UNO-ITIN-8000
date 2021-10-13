import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.button import Label


class HelloKivyApp(App):  # will call the .kv file HelloKivy.kv (Name-App)

    def build(self):
        return Label()


helloKivy = HelloKivyApp()

helloKivy.run()
