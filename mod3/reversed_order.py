import sys

ans = []
for line in sys.stdin:
    line = line.strip()
    ans.append(line[::-1])
print(*ans, sep='\n')