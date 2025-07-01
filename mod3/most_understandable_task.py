from datetime import datetime, timedelta, date, time

start_date = datetime.strptime(input(), '%d.%m.%Y')
end_date = datetime.strptime(input(), '%d.%m.%Y')

# ищем старт
while (start_date.month + start_date.day) % 2 == 0:
    start_date += timedelta(days=1)

cur = start_date

while cur <= end_date:
    if cur.weekday() not in [0, 3]:
        print(cur.strftime('%d.%m.%Y'))
    cur += timedelta(days=3)


 