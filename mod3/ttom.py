import calendar
from datetime import datetime


year = int(input())

for month in range(1, 13):
    month_cal = calendar.monthcalendar(year, month)
    ttom = 0
    if month_cal[0][3]:
        ttom += month_cal[2][3]
    else:
        ttom = month_cal[3][3]
    print(f'{ttom:02d}.{month:02d}.{year:04d}')