import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.button import Label


class HelloKivy(App):  # create a Kivy app object called HelloKivy

    def build(self):
        return Label(text="Hello Kivy")  # Prints hello kivy in the kivy object as a label


helloKivy = HelloKivy()  # create an object pointing to the app
helloKivy.run()  # run the app
