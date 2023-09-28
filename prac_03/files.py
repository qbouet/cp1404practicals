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