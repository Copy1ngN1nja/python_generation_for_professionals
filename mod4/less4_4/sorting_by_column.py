import csv

with open('deniro.csv', mode='r') as file:
    column_number = int(input()) - 1
    csv_reader = csv.reader(file, delimiter=',')
    list_csv_reader = list(csv_reader)
    list_csv_reader.sort(key=lambda x: int(x[column_number]) if x[column_number].isdigit() else x[column_number])
    for row in list_csv_reader:
        print(','.join(row))