def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]
    for sub_dict in nested_dicts.values():
        if isinstance(sub_dict, dict):
            value = get_value(sub_dict, key)
            if value is not None:
                return value
    return None

data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'cityName'))

data = {'first_name': 'Alyson', 'last_name': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

print(get_value(data, 'birthday'))