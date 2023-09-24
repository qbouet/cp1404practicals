def main():
    MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars (this should print as many stars as the score)
(Q)uit"""

    # Ask for valid score
    score = get_valid_score()

    # Get choice
    print(MENU)
    choice = input(">>> ").upper()

    # Process choice
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(process_score(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    score = float(input("Enter score (must be 0-100 inclusive): "))
    while process_score(score) == "Invalid score":
        score = float(input("Enter score (must be 0-100 inclusive): "))
    return score


def process_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Pass"
        else:
            return "Bad"


def print_stars(score):
    print(int(score) * '*')


main()
