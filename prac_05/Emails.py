"""
CP1404Practical
Emails Program
"""


def main():
    """Create dictionary of emails-to-names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        answer = input(f"Is your name {name}? (Y/n)")
        if answer.upper() != "Y" and answer != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    print(email_to_name)
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract name from email address."""
    prefix = email.split("@")[0]
    parts = prefix.title().split(".")
    name = " ".join(f"{part}"for part in parts)
    return name


main()
