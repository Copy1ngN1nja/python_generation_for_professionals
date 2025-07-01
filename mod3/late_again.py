from datetime import datetime, timedelta, date, time

dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')

if dt.weekday() < 5:
    if time(hour=9, minute=0) <= dt.time() < time(hour=21, minute=0):
        print(int((dt.replace(hour=21, minute=0) - dt).total_seconds() // 60))
    else:
        print('Магазин не работает')
else:
    if time(hour=10, minute=0) <= dt.time() < time(hour=18, minute=0):
        print(int((dt.replace(hour=18, minute=0) - dt).total_seconds() // 60))
    else:
        print('Магазин не работает')
        