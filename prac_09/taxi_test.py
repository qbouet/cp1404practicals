"""
CP1404/CP5632 Practical
Taxi Test
"""
from taxi import Taxi


def main():
    """Test Taxi Class"""
    my_taxi = Taxi("Prius 1", 100)
    print(my_taxi)  # test str method

    my_taxi.drive(40)
    print(f"Name: {my_taxi.name} Fuel: {my_taxi.fuel} Price per km: ${my_taxi.price_per_km}")
    print(f"Fare: ${my_taxi.get_fare():.2f}")

    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"Name: {my_taxi.name} Fuel: {my_taxi.fuel} Price per km: ${my_taxi.price_per_km}")
    print(f"Fare: ${my_taxi.get_fare():.2f}")


main()
