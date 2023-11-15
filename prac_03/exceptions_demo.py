"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # Check if the denominator is zero and keep asking for new denominator
    while denominator == 0:
        print("Denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# This last except is no longer needed as error checking has been added to avoid a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. When will a ValueError occur?
# A ValueError will occur when the user tries to input anything that isn't a number.

# 2. When will a ZeroDivisionError occur?
# A ZeroDivisionError will occur when the user inputs a zero as the denominator.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# You could check if the denominator is equal to zero before executing the fraction.
# This can be done by doing an error checking while loop for when the denominator is equal to zero.
