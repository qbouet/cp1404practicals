"""CP1404/CP5632 Practical
Program that prompts the user for 5 numbers and then stores each of these in a list called numbers
"""

# Part 1.
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[4]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/len(numbers)}")
