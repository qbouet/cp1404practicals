# 1. Write code that asks the user for their name, then opens a file called "name.txt"
# and writes that name to it. Remember to close your file.

NAME_FILE = "name.txt"
name = input("Name: ")
out_file = open(NAME_FILE, 'w')
print(f"{name}", file=out_file)
out_file.close()
