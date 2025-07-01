import json

with open('food_services.json', 'r') as json_file:
    food_services = json.load(json_file)
    max_types = {}
    for restaurant in food_services:
        restaurant_type = restaurant['TypeObject']
        if restaurant_type not in max_types:
            max_types[restaurant_type] = {
                'SeatsCount': 0,
                'Name': ''
            }
        if restaurant['SeatsCount'] > max_types[restaurant_type]['SeatsCount']:
            max_types[restaurant_type]['SeatsCount'] = restaurant['SeatsCount']
            max_types[restaurant_type]['Name'] = restaurant['Name']
    for restaurant_type, data in sorted(max_types.items(), key=lambda x: x[0]):
        print(f'{restaurant_type}: {data["Name"]}, {data["SeatsCount"]}')