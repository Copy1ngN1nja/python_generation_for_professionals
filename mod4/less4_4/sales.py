import csv

with open('sales.csv', mode='r') as file:
    csv_reader = csv.reader(file, delimiter=';')
    for row in list(csv_reader)[1:]:
        if int(row[1]) > int(row[2]):
            print(row[0])


