"""
CP1404/CP5632 Practical
Wikipedia API & Python Library program
Prompts the user for a page title or search phrase, then prints the summary of that page.
Continues doing this until the user enters blank input.
"""

import wikipedia


def main():
    """Wikipedia API & Python Library program"""
    print("Welcome to wiki search:")
    title = input(">>> ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.PageError:
            print(f"{title} does not match any pages. Try another query!")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"{title} may refer to:")
            for option in e.options:
                print("- ", option)
        title = input(">>> ")


main()
