import csv

with open('titanic.csv', 'r') as file:
    dict_reader = csv.DictReader(file, delimiter=';')
    survived_less_than_18 = []
    for d in dict_reader:
        if d['survived'] == '1' and float(d['age']) < 18:
            survived_less_than_18.append(d)
    for d in sorted(survived_less_than_18, key=lambda x: x['sex'] == 'female'):
        print(d['name'])