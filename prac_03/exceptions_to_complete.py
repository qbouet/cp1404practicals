"""
CP1404/CP5632 - Practical
Try & except exercise
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
# PyCharm will probably give you a warning that result "may be undefined". This is safe to ignore.
print("Valid result is:", result)
