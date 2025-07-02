def get_weekday(day_number):
    if not isinstance(day_number, int):
        raise TypeError('Аргумент не является целым числом')
    if day_number < 1 or day_number > 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return days[day_number - 1]


print(get_weekday(1))

try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))

try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))