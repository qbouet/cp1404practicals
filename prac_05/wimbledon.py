"""
CP1404Practical
Wimbledon Program
"""

FILE_NAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Read csv file and display details about Wimbledon champions and countries."""
    records = get_records(FILE_NAME)
    champion_to_win, countries = process_records(records)
    display_results(champion_to_win, countries)


def display_results(champion_to_win, countries):
    """Display champions and countries"""
    print("Wimbledon Champions: ")
    for champion, number_of_wins in champion_to_win.items():
        print(champion, number_of_wins)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def process_records(records):
    """Create dictionary of champions to wins and set of countries from records."""
    countries = set()
    champions = []
    champion_to_win = {}
    for record in records:
        champion = record[CHAMPION_INDEX]
        champions.append(champion)
        country = record[COUNTRY_INDEX]
        countries.add(country)
    for champion in champions:
        number_of_wins = champions.count(champion)
        champion_to_win[champion] = number_of_wins
    return champion_to_win, countries


def get_records(file_name):
    """Get records from file in list of lists form."""
    records = []
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # ignore header
        for line in in_file:
            parts = line.strip().split(',')
            records.append(parts)

    return records


main()
