from collections import Counter
import csv

with open('name_log.csv', 'r') as input_file:
    reader = csv.DictReader(input_file)
    counter = Counter(row['email'] for row in reader)
    for email, count in sorted(counter.items(), key=lambda x: x[0]):
        print(f'{email}: {count}')