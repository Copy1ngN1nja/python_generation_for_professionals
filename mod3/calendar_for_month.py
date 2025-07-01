import calendar

year, month = input().split()
year = int(year)
month = list(calendar.month_abbr).index(month)

print(calendar.month(year, month))