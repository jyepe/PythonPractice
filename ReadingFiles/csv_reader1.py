import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='', mode='r') as countries_data:
    country_reader = csv.reader(countries_data, delimiter='|', newline='')
    for row in country_reader:
        print(row)