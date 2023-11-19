"""
CP1404/CP5632 Practical
Silver Service Taxi Class (child of Taxi Class)
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes Silver Service."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with Silver Service."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the silver service taxi trip."""
        return super().get_fare() + self.flagfall
