"""Programming Language Class"""


class ProgrammingLanguage:
    """Programming Language Class"""
    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a Programming Language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, first appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language typing is dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False
