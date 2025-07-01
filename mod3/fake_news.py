from datetime import datetime, timedelta


def choose_plural(amount, declensions):
    declension = ''
    if amount % 10 == 1 and amount % 100 != 11:
        declension = declensions[0]
    elif amount % 10 in [2, 3, 4] and not (amount % 100 in [12, 13, 14]):
        declension = declensions[1]
    else:
        declension = declensions[2]
    return str(amount) + ' ' + declension

day_declensions = ['день', 'дня', 'дней']
hour_declensions = ['час', 'часа', 'часов']
minute_declensions = ['минута', 'минуты', 'минут']
time_drop = datetime(2022, 11, 8, 12, 0)

dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')

rest = time_drop - dt
hours = rest.seconds // 3600
minutes = rest.seconds % 3600 // 60

if rest <= timedelta(0):
    print('Курс уже вышел!')
elif rest.days > 0:
    days_str = choose_plural(rest.days, day_declensions)
    if hours > 0:
        hours_str = choose_plural(hours, hour_declensions)
        print('До выхода курса осталось: ' + days_str + ' и ' + hours_str)
    else:
        print('До выхода курса осталось: ' + days_str)
elif hours > 0:
    hours_str = choose_plural(hours, hour_declensions)
    if minutes > 0:
        minutes_str = choose_plural(minutes, minute_declensions)
        print('До выхода курса осталось: ' + hours_str + ' и ' + minutes_str)
    else:
        print('До выхода курса осталось: ' + hours_str)
elif minutes > 0:
    minutes_str = choose_plural(minutes, minute_declensions)
    print('До выхода курса осталось: ' + minutes_str)
