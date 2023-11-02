"""
CP1404 Practical
My Guitars Program - read all the guitars and store them in a list of
Guitar objects, using Guitar class.
"""

from guitar import Guitar

FILE_NAME = 'guitars.csv'


def main():
    """Read file of guitar details, save as objects, display."""
    guitars = []
    # Open the file for reading
    in_file = open(FILE_NAME, 'r')
    # File format is like: Guitar,Year,Cost
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging
        # Construct a Guitar object using the elements
        # year should be an int and cost should be float
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        # Add the guitar we've just constructed to the list
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()

    # sort guitars by year
    guitars.sort()

    # Loop through and display all guitars (using their str method)
    for guitar in guitars:
        print(guitar)

    get_input(guitars)
    record_guitars(guitars)


def get_input(guitars):
    """Get input from user to add a new guitar"""
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


def record_guitars(guitars):
    """Record guitars to file in format: Guitar,Year,Cost"""
    out_file = open(FILE_NAME, 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


main()
