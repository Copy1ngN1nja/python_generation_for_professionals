from collections import Counter

counter = Counter(map(int, input().split()))
n = int(input())
sumi = 0
for _ in range(n):
    grade, price = map(int, input().split())
    if counter[grade] > 0:
        counter[grade] -= 1
        sumi += price
print(sumi)