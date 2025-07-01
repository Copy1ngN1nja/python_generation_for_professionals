from datetime import date

def get_min_max(dates):
    if not dates:
        return ()
    min_date = min(dates)
    max_date = max(dates)
    return (min_date, max_date)


dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]

print(get_min_max(dates))

print(get_min_max([]))