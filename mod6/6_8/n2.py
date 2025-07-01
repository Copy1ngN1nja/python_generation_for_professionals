from collections import Counter

counter = Counter(input().lower().split())
ans = []
least_common = counter.most_common()[::-1]
ans.append(least_common[0][0])
i = 1
while i < len(least_common) and least_common[i][1] == least_common[0][1]:
    ans.append(least_common[i][0])
    i += 1
print(*sorted(ans), sep=', ')