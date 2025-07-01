from datetime import datetime, timedelta, time, date


start_date = datetime.strptime(input(), '%d.%m.%Y').date()
cur_date = start_date
for i in range(10):
    print(date.strftime(cur_date, '%d.%m.%Y'))
    cur_date += timedelta(days=i + 2)