"""
CP1404 Practical
Guitars Program
This program should use a list to store all the user's guitars
(keep inputting until they enter a blank name), then print their details.
"""

from guitar import Guitar


def main():
    """Guitar program (using Guitar class)."""
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    print()
    print("... snip ...")
    print()
    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            # do something with i (the index) and guitar (the element)
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
