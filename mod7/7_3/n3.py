filename = input()
try:
    f = open(filename, 'r')
    s = f.read()
    print(s)
    f.close()
except FileNotFoundError:
    print('Файл не найден')