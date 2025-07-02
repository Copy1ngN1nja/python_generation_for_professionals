from collections import ChainMap

def get_all_values(chainmap, key):
    res = set()
    for mapping in chainmap.maps:
        if key in mapping:
            res.add(mapping[key])
    return res

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')

print(*sorted(result))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')

print(result)