"""
CP1404/CP5632 Practical
Taxi Simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Taxi Simulator"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    # Reset variables
    total_bill = 0
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    # Process choice
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_index = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_index]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you {fare:.2f}")
                total_bill += fare
        else:
            print("Invalid choice")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    # Display final states of taxis
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display numbered taxis"""
    number = 0
    for taxi in taxis:
        print(f"{number} - {taxi}")
        number += 1


main()


