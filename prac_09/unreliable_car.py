"""
CP1404/CP5632 Practical
Unreliable Car Class (child of Car Class)
"""
from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability: float):
        """Initialise a Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability."""
        return f"{super().__str__()}, reliability={self.reliability}"

    def drive(self, distance):
        """Drive like a Car but only drive if a randomly generated number
        is less than the car's reliability."""
        if self.reliability <= randint(0, 100):
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
