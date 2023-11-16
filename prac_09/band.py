"""
CP1404/CP5632 Practical
Band Class
"""

class Band:
    """Band class for storing details of a band."""

    def __init__(self, name=""):
        """Initialise a Band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join([str(musician) for musician in self.musicians])})"

    def __repr__(self):
        """Return a string representation of a Band."""
        return str(self)

    def add(self, musician):
        """Add a musician to band"""
        self.musicians.append(musician)

    def play(self):
        """Play band."""
        return '\n'.join([musician.play() for musician in self.musicians])


