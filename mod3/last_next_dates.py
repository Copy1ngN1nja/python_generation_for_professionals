from datetime import date, timedelta, datetime

now_date = datetime.strptime(input(), '%d.%m.%Y').date()
last_date = now_date - timedelta(days=1)
next_date = now_date + timedelta(days=1)
print(date.strftime(last_date, '%d.%m.%Y'), date.strftime(next_date, '%d.%m.%Y'), sep='\n')