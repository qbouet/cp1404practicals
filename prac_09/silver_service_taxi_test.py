"""
CP1404/CP5632 Practical
Silver Service Taxi Test
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    # Test str method
    fancy_taxi = SilverServiceTaxi("Fancy_taxi", 200, 4)
    print(fancy_taxi)

    # Test if fare is calculated correctly
    super_fancy_taxi = SilverServiceTaxi("Super_fancy_taxi", 200, 2)
    super_fancy_taxi.drive(18)
    print(super_fancy_taxi)
    print(f"Fare: ${super_fancy_taxi.get_fare()}")


main()
