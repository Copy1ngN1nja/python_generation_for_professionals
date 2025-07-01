from datetime import date, timedelta, datetime

def num_of_sundays(year):
    first_day = date(year, 1, 1)
    last_day = date(year, 12, 31)

    sundays_count = 0
    cur = first_day
    while cur <= last_day:
        if cur.weekday() == 6:
            sundays_count += 1
        cur += timedelta(days=1)
    return sundays_count

print(num_of_sundays(2021))
year = 2000
print(num_of_sundays(year))
print(num_of_sundays(768))