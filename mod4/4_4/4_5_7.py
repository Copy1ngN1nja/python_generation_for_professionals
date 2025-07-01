import json

with open('data.json', 'r') as input_file, open('updated_data.json', 'w') as output_file:
    data = json.load(input_file)
    new_data = []
    for i in range(len(data)):
        if isinstance(data[i], str):
            new_data.append(data[i] + '!')
        elif isinstance(data[i], bool):
            new_data.append(not data[i])
        elif isinstance(data[i], int):
            new_data.append(data[i] + 1)
        elif isinstance(data[i], list):
            new_data.append(data[i] * 2)
        elif isinstance(data[i], dict):
            data[i]['newkey'] = None
            new_data.append(data[i])
    json.dump(new_data, output_file, indent=3)

    
            
