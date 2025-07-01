from collections import namedtuple
import pickle as pkl

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as f:
    animals = pkl.load(f)
    for animal in animals:
        an_dict = animal._asdict()
        for key, value in an_dict.items():
            print(f'{key}: {value}')
        print()
