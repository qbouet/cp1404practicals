"""
CP1404Practical
Wimbledon Program
"""

FILE_NAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    countries = set()
    champions = []
    champion_to_win = {}
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # ignore header
        for line in in_file:
            parts = line.strip().split(',')
            champion = parts[2]
            champions.append(champion)
            country = parts[1]
            countries.add(country)

    for champion in champions:
        number_of_wins = champions.count(champion)
        champion_to_win[champion] = number_of_wins

    for champion, number_of_wins in champion_to_win.items():
        print(f"{champion} {number_of_wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
