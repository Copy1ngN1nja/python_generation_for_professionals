from datetime import datetime, timedelta, time

start_time = datetime.strptime(input(), '%H:%M').time()
end_time = datetime.strptime(input(), '%H:%M').time()
time_class = timedelta(minutes=45)
time_rest = timedelta(minutes=10)

cur = datetime.combine(datetime.today(), start_time) + time_class
while cur.time() <= end_time:
    print(f'{(cur - time_class).strftime('%H:%M')} - {cur.strftime('%H:%M')}')
    cur += time_class + time_rest