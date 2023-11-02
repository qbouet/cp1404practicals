"""Guitar Class"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Guitar Class"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get age of Guitar based on the CURRENT_YEAR."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if Guitar is considered vintage or not based on VINTAGE_AGE."""
        return self.get_age() >= VINTAGE_AGE

