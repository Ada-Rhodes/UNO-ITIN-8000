from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class SayHello(App):  # Create the app class
    def build(self):  # Build method
        self.window = GridLayout()  # Create a window with the grid layout
        self.window.cols = 1

        # add an image widget
        self.window.add_widget(Image(source='uno-icon-color.png'))
        # add label widget
        self.greeting = Label(text="What is your name?")  # another way of creating a widget object
        self.window.add_widget(self.greeting)  # add the widget
        # get text input
        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)  # What do these do?
        # add a button
        self.button = Button(text="Say Howdy")  # what do you notice about capitilization
        self.button.bind(on_press=self.callback)  # what do you think this does?
        self.window.add_widget(self.button)  # what does this do?

        return self.window

    def callback(self, instance):  # Does it need to be called callback?
        self.greeting.text = "Howdy " + self.user.text + "!"


if __name__ == "__main__":
    SayHello().run()