import calendar

ans = []
n = int(input())
for _ in range(n):
    year = int(input())
    ans.append(calendar.isleap(year))
print(*ans, sep='\n')