import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.widget import Widget


class CustomWidget(Widget):  # creates the widget object
    pass  # just a place holder


class CustomWidgetApp(App):
    def build(self):
        return CustomWidget()


customWidget = CustomWidgetApp()
customWidget.run()
