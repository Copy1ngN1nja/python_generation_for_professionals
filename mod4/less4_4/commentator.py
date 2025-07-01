import sys

lines = [line.strip() for line in sys.stdin if line.strip()]
cnt = 0
for line in lines:
    if line.startswith('#'):
        cnt += 1
print(cnt)