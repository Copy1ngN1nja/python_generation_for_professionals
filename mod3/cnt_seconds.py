from datetime import timedelta, time, datetime

time = datetime.strptime(input(), '%H:%M:%S').time()
delta = timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

seconds = delta.total_seconds()
print(int(seconds))