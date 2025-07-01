from datetime import date, datetime


def get_date_range(start_date, end_date):
    res = []
    while start_date <= end_date:
        res.append(start_date)
        start_date = date.fromordinal(start_date.toordinal() + 1)
    return res


def is_available_date(booked_dates, date_for_booking):
    set_of_booked_dates = set()
    for date_range in booked_dates:
        if '-' in date_range:
            start_date_str, end_date_str = date_range.split('-')
            start_date = datetime.strptime(start_date_str, '%d.%m.%Y').date()
            end_date = datetime.strptime(end_date_str, '%d.%m.%Y').date()
            for d in get_date_range(start_date, end_date):
                set_of_booked_dates.add(d)
        else:
            single_date = datetime.strptime(date_range, '%d.%m.%Y').date()
            set_of_booked_dates.add(single_date)

    if '-' in date_for_booking:
        start_date_str, end_date_str = date_for_booking.split('-')
        start_date = datetime.strptime(start_date_str, '%d.%m.%Y').date()
        end_date = datetime.strptime(end_date_str, '%d.%m.%Y').date()
        for d in get_date_range(start_date, end_date):
            if d in set_of_booked_dates:
                return False
    else:
        single_date = datetime.strptime(date_for_booking, '%d.%m.%Y').date()
        if single_date in set_of_booked_dates:
            return False
    return True
    



dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))