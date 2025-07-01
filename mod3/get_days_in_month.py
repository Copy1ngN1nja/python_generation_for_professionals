import calendar
from datetime import date

def get_date_range(start_date, end_date):
    res = []
    while start_date <= end_date:
        res.append(start_date)
        start_date = date.fromordinal(start_date.toordinal() + 1)
    return res

def get_days_in_month(year, month):
    month = list(calendar.month_name).index(month)
    month_days = calendar.monthrange(year, month)[1]
    start_date = date(year, month, 1)
    end_date = date(year, month, month_days)
    return list(get_date_range(start_date, end_date))

print(get_days_in_month(2021, 'December'))