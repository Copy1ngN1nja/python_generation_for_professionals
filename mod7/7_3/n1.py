months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
try:
    month = int(input())
    print(months[month])
except ValueError:
    print('Введено некорректное значение')
except KeyError:
    print('Введено число из недопустимого диапазона')