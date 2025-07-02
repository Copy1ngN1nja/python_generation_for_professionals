import json

filename = input()
try:
    f = open(filename, 'r')
    data = json.load(f)
    print(data)
    f.close()
except FileNotFoundError:
    print('Файл не найден')
except json.JSONDecodeError:
    print('Ошибка при десериализации')


    