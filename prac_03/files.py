"""
CP1404/CP5632 - Practical - Suggested Solution
Quick file opening/writing/reading exercises
"""

# 1. Write code that asks the user for their name, then opens a file called "name.txt"
# and writes that name to it. Remember to close your file.

name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2. (In the same file, but as if it were a separate program)
# Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).

in_file = open("name.txt", "r")
name = in_file.read().strip()  # use .strip() in case user types in a space
in_file.close()
print(f"Your name is {name}")


# 3. Create a text file called numbers.txt and save it in your prac directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and
# adds them together then prints the result, which should be... 59.

in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
total = number_1 + number_2
print(f"Sum of the first 2 numbers is {total}")


# 4. Now write a fourth block of code that prints the total for all lines
# in numbers.txt or a file with any number of numbers.

total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(f"Sum of all numbers is {total}")
