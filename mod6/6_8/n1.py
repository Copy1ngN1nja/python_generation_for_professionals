from collections import Counter

s = input()
counter = Counter(s.lower().split())
print(counter.most_common(1)[0][0])