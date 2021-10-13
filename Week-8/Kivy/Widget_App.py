import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class CustomWidget(Widget):  # creates the widget object
    pass  # just a place holder


class CustomWidgetApp(App):

    def build(self):
        wid = Widget()

        butt = Button(text="A Button")

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(butt)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root


if __name__ == '__main__':
    CustomWidgetApp().run()
