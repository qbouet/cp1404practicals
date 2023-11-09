"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Quentin Bouet, IT@JCU
9/11/2023
"""
from kivy.app import App
from kivy.lang import Builder

__author__ = 'Quentin Bouet'


class MilesConvertingApp(App):
    """ MilesConvertingApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesConvertingApp().run()
