from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Calculator(App):
    # First Define Your Layouts
    main_layout = GridLayout()
    display_layout = BoxLayout()

    # Next Define Functions

    # Finally Define Your Build


# Create run line
if __name__ == "__main__":
    Calculator().run()