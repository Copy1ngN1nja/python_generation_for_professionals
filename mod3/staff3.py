from datetime import datetime, timedelta, date

cur_date = datetime.strptime(input(), '%d.%m.%Y').date()
n = int(input())
staff = []
for _ in range(n):
    name, surname, date_of_birth = input().split()
    date_of_birth = datetime.strptime(date_of_birth, '%d.%m.%Y').date()
    staff.append((date_of_birth, name, surname))

name_of_youngest = ''
date_of_youngest = date(1, 1, 1)
for date_of_birth, name, surname in staff:
    if (timedelta(days=1) <= date_of_birth.replace(year=cur_date.year) - cur_date <= timedelta(days=7) or \
        timedelta(days=1) <= date_of_birth.replace(year=cur_date.year - 1) - cur_date <= timedelta(days=7) or \
        timedelta(days=1) <= date_of_birth.replace(year=cur_date.year + 1) - cur_date <= timedelta(days=7)) and \
        date_of_birth > date_of_youngest:
        date_of_youngest = date_of_birth
        name_of_youngest = f'{name} {surname}'

if name_of_youngest:
    print(name_of_youngest)
else:
    print('Дни рождения не планируются')
