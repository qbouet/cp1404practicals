"""
CP1404 Practical
My Guitars Program - read all the guitars and store them in a list of
Guitar objects, using Guitar class.
"""

from guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display."""
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
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


main()
