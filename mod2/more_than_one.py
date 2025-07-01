a = list(map(int, input().split()))
res = []
for x in a:
    if x not in res and a.count(x) > 1:
        res.append(x)
if res:
    print(*sorted(res))