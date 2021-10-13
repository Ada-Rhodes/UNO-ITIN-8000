from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class SayHello(App):
    def build(self):
        self.window = GridLayout()  # did this have to be called window?
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)  # what do you think size hint means?
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}  # what do you think this does?

        # add an image widget
        self.window.add_widget(Image(source='uno-icon-color.png'))
        # add label widget
        self.greeting = Label(
                        text="What is your name?",  # Break up to multiple lines
                        font_size=18,
                        color='#FF0000')
        self.window.add_widget(self.greeting)
        # get text input
        self.user = TextInput(
                    multiline=False,
                    padding_y=(20, 20),
                    size_hint=(1, 0.5))
        self.window.add_widget(self.user)
        # add a button
        self.button = Button(  # What did we change
            text="Say Howdy",
            size_hint=(1,0.5),
            bold=True,
            background_color='#FF0000',
            background_normal="")  # lets play with this line
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = "Howdy " + self.user.text + "!"


if __name__ == "__main__":
    SayHello().run()
