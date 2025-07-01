import csv

with open('wifi.csv', 'r') as file:
    dict_reader = csv.DictReader(file, delimiter=';')
    districts = {}
    for d in dict_reader:
        district = d['district']
        if district not in districts:
            districts[district] = 0
        districts[district] += int(d['number_of_access_points'])
    for district, count in sorted(districts.items(), key=lambda x: (-x[1], x[0])):
        print(f'{district}: {count}')