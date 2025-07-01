from collections import Counter

counter = Counter(input().lower().split())
ans = []
most_common = counter.most_common()
ans.append(most_common[0][0])
i = 1
while i < len(most_common) and most_common[i][1] == most_common[0][1]:
    ans.append(most_common[i][0])
    i += 1

print(max(ans))
