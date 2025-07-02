from collections import Counter
import csv
import json

with open('quarter1.csv', 'r') as q1, open('quarter2.csv', 'r') as q2, open('quarter3.csv', 'r') as q3, open('quarter4.csv', 'r') as q4:
    data = Counter()
    for file in (q1, q2, q3, q4):
        reader = csv.reader(file, delimiter=',')
        reader.__next__()
        for row in reader:
            for i in range(1, len(row)):
                data[row[0]] += int(row[i])

with open('prices.json', 'r') as f:
    sumi = 0
    prices = json.load(f)
    for key, value in data.items():
        sumi += value * prices[key]
    print(sumi)