n = int(input())
d = {}
for _ in range(n):
    name, _ = input().split('@')
    idx = -1
    for i, c in enumerate(name):
        if c.isdigit():
            idx = i
            break
    digit = 0
    if idx != -1:
        digit = int(name[idx:])
        name = name[:idx]
    if name not in d:
        d[name] = set(i for i in range(1000))
    d[name].discard(digit)

m = int(input())
ans = []
for _ in range(m):
    name = input()
    if name not in d:
        d[name] = set(i for i in range(1000))
    min_digit = min(d[name])

    d[name].discard(min_digit)
    if min_digit == 0:
        res = name + '@beegeek.bzz'
    else:
        res = name + str(min_digit) + '@beegeek.bzz'
    ans.append(res)
    
print(*ans, sep='\n')