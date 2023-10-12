"""
CP1404Practical
Hex Colours Program
"""

COLOUR_TO_HEX = {"ABSOLUTEZERO": "#0048ba",
           "ACIDGREEN": "#b0bf1a",
           "ALICEBLUE": "#f0f8ff",
           "AMARANTH": "#e52b50",
           "BABYBLUE": "#89cff0",
           "BANANAYELLOW": "#ffe135",
           "BITTERLIME": "#bfff00",
           "BITTERSWEET": "#fe6f5e",
           "BLEUDEFRANCE": "#318ce7",
           "GINGER": "#b06500"}

print(COLOUR_TO_HEX)

colour_name = input("Enter colour name: ").upper()

# "Easier to Ask Forgiveness than Permission" (EAFP) approach:
while colour_name != "":
    try:
        print(f"{colour_name:<12} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").upper()
