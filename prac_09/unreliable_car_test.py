"""
CP1404/CP5632 Practical
Unreliable Car Test
"""

from unreliable_car import UnreliableCar


def main():
    # Create 2 cars with contrasting reliability
    bad_car = UnreliableCar("Bad car", 100, 30)
    good_car = UnreliableCar("Good car", 100, 89)

    # Drive the cars several times to compare reliability
    for i in range(15):
        print(f"{bad_car.name}  drove {bad_car.drive(i):2} km")
        print(f"{good_car.name} drove {good_car.drive(i):2} km")

    print(bad_car)
    print(good_car)


main()
