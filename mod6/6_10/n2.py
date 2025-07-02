from collections import ChainMap

def deep_update(chainmap, key, value):
    flag = False
    for mapping in chainmap.maps:
        if key in mapping:
            mapping[key] = value
            flag = True
    if not flag:
        chainmap[key] = value
    return None

chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')

print(chainmap)

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)