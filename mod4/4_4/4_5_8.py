import json

d = {}

with open('data1.json', 'r') as input_file:
    d = json.load(input_file)

with open('data2.json', 'r') as input_file:
    temp_d = json.load(input_file)
    for key, value in temp_d.items():
        d[key] = value

with open('data_merge.json', 'w') as output_file:
    json.dump(d, output_file, indent=3)