def get_id(names, name):
    def check_name(name):
        return name[0].isupper() and all(c.isalpha() and c.islower() for c in name[1:])

    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    if not check_name(name):
        raise ValueError('Имя не является корректным')
    return len(names) + 1
    

names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'

print(get_id(names, name))

names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'Ruslan1337'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)