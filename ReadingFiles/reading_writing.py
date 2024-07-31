import csv

with open('OlympicMedals_2020.csv', 'r', encoding='utf-8', newline='') as input_file,\
    open('medals_dict.csv', 'w', encoding='utf-8', newline='') as output_file:
    
    print('importing csv', file=output_file)
    print(file=output_file)
    print('medals_table = {', file=output_file)
    
    reader = csv.DictReader(input_file)
    
    # for row in reader:
        