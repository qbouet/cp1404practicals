"""
CP1404 Practical
Guitar Test Program
"""

from guitar import Guitar

first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
second_guitar = Guitar("Another Guitar", 2013, 49.99)

print(first_guitar)
print(second_guitar)

print(f"{first_guitar.name} get_age() - Expected 100. Got {first_guitar.get_age()}")
print(f"{second_guitar.name} get_age() - Expected 9. Got {second_guitar.get_age()}")
print(f"{first_guitar.name} is_vintage() - Expected True. Got {first_guitar.is_vintage()}")
print(f"{second_guitar.name} is_vintage() - Expected False. Got {second_guitar.is_vintage()}")

