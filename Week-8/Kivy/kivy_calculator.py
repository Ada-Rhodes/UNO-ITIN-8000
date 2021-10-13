import kivy
kivy.require("2.0.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGridLayout(GridLayout):  # creates a callable gridlayout object tha can be built

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()  # will return the build calc gridlayout


calcApp = CalculatorApp()
calcApp.run()
