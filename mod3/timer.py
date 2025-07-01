from datetime import timedelta, datetime, time, date

time = datetime.strptime(input(), '%H:%M:%S').time()
delta = timedelta(seconds=int(input()))

print((datetime.combine(date.today(), time) + delta).time())