import sys

res = 0
cnt = 0
for row in sys.stdin:
    try:
        res += int(row)
    except ValueError:
        try:
            res += float(row)
        except ValueError:
            cnt += 1
print(res, cnt, sep='\n')