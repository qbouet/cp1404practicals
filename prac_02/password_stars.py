
def main():
    min_length = 4
    password = get_password(min_length)
    print_stars(password)


def print_stars(password):
    print(len(password) * '*')


def get_password(min_length):
    password = str(input("Password: "))
    while len(password) < min_length:
        print("Password must be shorter than 4 characters")
        password = str(input("Password: "))
    return password


main()

