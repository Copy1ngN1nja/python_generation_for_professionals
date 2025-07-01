from datetime import date


def print_good_dates(dates):
    res = []
    for d in sorted(dates):
        if d.year == 1992 and d.month + d.day == 29:
            print(d.strftime('%B %d, %Y'))


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)
dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
print_good_dates(dates)