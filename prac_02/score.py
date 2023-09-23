"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(process_score(score))

    random_score = random.randint(0,100)
    print(f"Random score: {random_score}")
    print(process_score(random_score))


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


main()
