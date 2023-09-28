# 1. Write code that asks the user for their name, then opens a file called "name.txt"
# and writes that name to it. Remember to close your file.

NAME_FILE = "name.txt"
name = input("Name: ")
out_file = open(NAME_FILE, 'w')
print(f"{name}", file=out_file)
out_file.close()

# 2. (In the same file, but as if it were a separate program)
# Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).

in_file = open(NAME_FILE, "r")
name = in_file.read()
print(f"Your name is {name}")
in_file.close()

# 3. Create a text file called numbers.txt and save it in your prac directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and
# adds them together then prints the result, which should be... 59.

NUMBERS_FILE = "numbers.txt"
out_file = open(NUMBERS_FILE, 'w')
print(f"17\n42\n400", file=out_file)
out_file.close()

in_file = open(NUMBERS_FILE, "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
sum_of_numbers = first_number + second_number
print(f"Sum of first 2 numbers is {sum_of_numbers}")
in_file.close()

# 4. Now write a fourth block of code that prints the total for all lines
# in numbers.txt or a file with any number of numbers.

NUMBERS_FILE = "numbers.txt"
sum_of_numbers = 0
with open(NUMBERS_FILE, "r") as in_file:
    for line in in_file:
        current_number = int(line)
        sum_of_numbers = sum_of_numbers + current_number
print(f"Sum of numbers is {sum_of_numbers}")
