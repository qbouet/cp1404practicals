"""
CP1404 Week 11 Workshop - Box Layout Demo
Quentin Bouet, IT@JCU
12/11/2023
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Main program - Kivy app to demo box layout."""
    def build(self):
        """Build the Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greeting of user"""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_all(self):
        """Clear all widgets that are children of the "entries_box" layout widget."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
