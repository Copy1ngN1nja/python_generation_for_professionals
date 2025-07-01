import calendar
from datetime import date

def get_all_mondays(year):
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    mondays = []
    while calendar.weekday(start_date.year, start_date.month, start_date.day) != 0:
        start_date = date.fromordinal(start_date.toordinal() + 1)
    cur_date = start_date
    while cur_date <= end_date:
        mondays.append(cur_date)
        cur_date = date.fromordinal(cur_date.toordinal() + 7)
    return mondays


print(get_all_mondays(2021)[:10])
