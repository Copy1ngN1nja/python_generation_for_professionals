from datetime import datetime, timedelta, date


n = int(input())
staff = []
for _ in range(n):
    name, surname, date_of_birth = input().split()
    date_of_birth = datetime.strptime(date_of_birth, '%d.%m.%Y').date()
    staff.append((date_of_birth, name, surname))

dates = {}

for date_of_birth, _, _ in staff:
    dates[date_of_birth] = dates.get(date_of_birth, 0) + 1

cnts = list(dates.items())
ans = [cnts[0]]
for date_of_birth, cnt in cnts[1:]:
    if cnt > ans[0][1]:
        ans = [(date_of_birth, cnt)]
    elif cnt == ans[0][1]:
        ans.append((date_of_birth, cnt))

for date_of_birth, cnt in sorted(ans):
    print(date_of_birth.strftime('%d.%m.%Y'))