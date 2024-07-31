import csv

country_stats = {}

with open('OlympicMedals_2020.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rank, country, gold, silver, bronze, total = row
        
        country_stats[row['Country']] = {
            'Rank': row['Rank'],
            'Gold': row['Gold'],
            'Silver': row['Silver'],
            'Bronze': row['Bronze'],
            'Total': row['Total']
        }
        print(row)
        # print(row['Cereal'], row['Calories'], row['Fat'], row['Protein'], row['Fibre'], row['Vitamin E'])
        
print(country_stats)