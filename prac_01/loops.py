# demo
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# part a
# count in 10s from 0 to 100:
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# part b
# count down from 20 to 1:
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# part c
# print n stars. Ask the user for a number, then print that many stars (*), all on one line.
number_of_stars = int(input("number of starts: "))
for n in range(0, number_of_stars, 1):
    print('*', end='')
print()

# part d
# print n lines of increasing stars. Using the same number as above, print lines of increasing stars, starting at 1.
for n in range(0, number_of_stars + 1, 1):
    print('*' * n)
print()
