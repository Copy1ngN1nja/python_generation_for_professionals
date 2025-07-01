from datetime import date

def get_date_range(start_date, end_date):
    res = []
    while start_date <= end_date:
        res.append(start_date)
        start_date = date.fromordinal(start_date.toordinal() + 1)
    return res

def saturdays_between_two_dates(start_date, end_date):
    date_range = get_date_range(min(start_date, end_date), max(start_date, end_date))
    cnt_saturdays = sum(1 for d in date_range if d.weekday() == 5)
    return cnt_saturdays

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))

date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

print(saturdays_between_two_dates(date1, date2))