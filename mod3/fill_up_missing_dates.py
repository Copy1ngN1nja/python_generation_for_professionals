from datetime import date, datetime, timedelta, time

def fill_up_missing_dates(dates):
    dates = [datetime.strptime(date_str, '%d.%m.%Y').date() for date_str in dates]
    start_date = min(dates)
    end_date = max(dates)
    cur_date = start_date
    filled_dates = []
    while cur_date <= end_date:
        filled_dates.append(date.strftime(cur_date, '%d.%m.%Y'))
        cur_date += timedelta(days=1)
    return filled_dates

dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))

dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']

print(fill_up_missing_dates(dates))