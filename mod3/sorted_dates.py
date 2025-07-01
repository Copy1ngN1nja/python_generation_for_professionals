from datetime import date

n = int(input())
dates = [date.fromisoformat(input()) for _ in range(n)]
dates.sort()
for d in dates:
    print(d.strftime('%d/%m/%Y'))