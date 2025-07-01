import calendar

year, month, day = map(int, input().split('-'))
weekday = calendar.weekday(year, month, day)
print(calendar.day_name[weekday])  # Output the name of the day of the week