from datetime import datetime, timedelta, time, date

dates = [datetime.strptime(date_str, '%d.%m.%Y').date() for date_str in input().split()]

ans = []
for i in range(len(dates) - 1):
    ans.append((abs(dates[i + 1] - dates[i])).days)

print(ans)