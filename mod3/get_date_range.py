from datetime import date

def get_date_range(start_date, end_date):
    res = []
    while start_date <= end_date:
        res.append(start_date)
        start_date = date.fromordinal(start_date.toordinal() + 1)
    return res
        


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)

print(get_date_range(date1, date2))