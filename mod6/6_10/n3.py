from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    if from_left:
        for mapping in chainmap.maps:
            if key in mapping:
                return mapping[key]
    else:
        for mapping in reversed(chainmap.maps):
            if key in mapping:
                return mapping[key]
    return None

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name', False))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))