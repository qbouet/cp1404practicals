"""
CP1404/CP5632 Practical
State names in a dictionary
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()

# "Easier to Ask Forgiveness than Permission" (EAFP) approach:
while state_code != "":
    try:
        print(f"{state_code:<3} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# # "Look Before You Leap" (LBYL) approach:
# print(f"{state_code:<3} is {CODE_TO_NAME[state_code]}")
# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(f"{state_code:<3} is {CODE_TO_NAME[state_code]}")
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()
