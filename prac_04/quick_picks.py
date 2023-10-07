"""
CP1404 Practical
Write a program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output.
Each line consists of 6 random numbers between 1 and 45.
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick picks program"""
    # Use exception-based error checking to check if input is invalid
    is_valid_input = False
    while not is_valid_input:
        try:
            number_of_quick_picks = int(input("How many quick picks? "))
            if number_of_quick_picks < 0:
                print("Number of quick picks cannot be less than 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")

    # Process number of quick picks
    for i in range(number_of_quick_picks):
        # Create a list of 6 random integers
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        # Print the quick pick in the desired format using join method and list comprehension
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
