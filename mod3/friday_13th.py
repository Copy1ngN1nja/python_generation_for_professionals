from datetime import datetime, timedelta, date

start_date = date(1, 1, 1)
end_date = date(9999, 12, 31)

cnt = [0] * 7
cur = start_date

while cur < end_date:
    if cur.day == 13:
        cnt[cur.weekday()] += 1
    cur += timedelta(days=1)
    # print(cur, cnt)

print(*cnt)