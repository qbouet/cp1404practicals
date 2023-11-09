"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Quentin Bouet, IT@JCU
9/11/2023
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Quentin Bouet'

MILES_TO_KM = 1.60934


class MilesConvertingApp(App):
    """ MilesConvertingApp is a Kivy App for converting miles to kilometres """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Type number in the field & press Enter"
        return self.root

    def handle_calculate(self):
        """Handle calculations from the text input by updating the model from the view."""
        value = self.get_valid_miles()
        self.message = str(value * MILES_TO_KM)

    def handle_increment(self, increment):
        """Handle increments to the text input by updating the model from the view."""
        value = self.get_valid_miles()
        self.root.ids.input_number.text = str(value + increment)
        self.handle_calculate()

    def get_valid_miles(self):
        """Get valid miles (get text input from text entry widget), convert to float
        return 0 if text input is empty or invalid float"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesConvertingApp().run()
