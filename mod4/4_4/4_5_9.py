import json

with open('people.json', 'r') as input_file, open('updated_people.json', 'w') as output_file:
    data = json.load(input_file)
    for person in data:
        for key, value in person.items():
            for i in range(len(data)):
                if key not in data[i]:
                    data[i][key] = None
    json.dump(data, output_file, indent=3)