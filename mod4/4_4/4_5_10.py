import json

with open('countries.json', 'r') as input_file, open('religion.json', 'w') as output_file:
    data = json.load(input_file)
    religion_data = {}
    for country in data:
        if country['religion'] not in religion_data:
            religion_data[country['religion']] = []
        religion_data[country['religion']].append(country['country'])
    json.dump(religion_data, output_file, indent=3)