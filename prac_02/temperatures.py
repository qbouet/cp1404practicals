"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def convert_celsius_to_fahrenheit():
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius():
    return 5 / 9 * (fahrenheit - 32)


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = convert_celsius_to_fahrenheit()
        print(f"Fahrenheit: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = convert_fahrenheit_to_celsius()
        print(f"Celsius: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
