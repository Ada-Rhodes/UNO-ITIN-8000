'''
This will let us call the toy box .py files from a ui
'''

from toybox import dicebag  # imports the dicebag module from the toybox package
from toybox import carddeck  # imports the card deck module from the toybox package

from kivy.app import App  # creates a runnable kivy app
from kivy.uix.widget import Widget  # lets us create a kivy ui widget object (a window)
from kivy.uix.button import Button  # lets us create a kivy ui button
from kivy.uix.label import Label  # text labeled object

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle


# Create the App object to be run (can all be as a .kv file)
class ToyBoxApp(App):
    def roll_d6(self):
        