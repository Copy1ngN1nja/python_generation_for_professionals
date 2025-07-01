from collections import defaultdict

def flip_dict(d):
    flipped = defaultdict(list)
    for key, values in d.items():
        for value in values:
            flipped[value].append(key)
    return flipped


data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')