from collections import Counter

s = input()
lens = (len(word) for word in s.split())
counter = Counter(lens)
for length, count in sorted(counter.items(), key=lambda x: x[1]):
    print(f'Слов длины {length}: {count}')