from datetime import datetime, timedelta, date


n = int(input())
staff = []
for _ in range(n):
    name, surname, date_of_birth = input().split()
    date_of_birth = datetime.strptime(date_of_birth, '%d.%m.%Y').date()
    staff.append((date_of_birth, name, surname))

oldest_staff = staff[0]
cnt = 1
for i in range(1, len(staff)):
    if staff[i][0] < oldest_staff[0]:
        oldest_staff = staff[i]
        cnt = 1
    elif staff[i][0] == oldest_staff[0]:
        cnt += 1

if cnt == 1:
    print(f'{oldest_staff[0].strftime('%d.%m.%Y')} {oldest_staff[1]} {oldest_staff[2]}')
else:
    print(f'{oldest_staff[0].strftime("%d.%m.%Y")} {cnt}')