import csv

country_stats = {}

with open('OlympicMedals_2020.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    header = file.readline().strip() # Skip the header
    print(header)
    for row in reader:
        rank, country, gold, silver, bronze, total = row
        country_stats[country] = {
            'rank': rank,
            'gold': gold,
            'silver': silver,
            'bronze': bronze,
            'total': total
        }
        print(row)
