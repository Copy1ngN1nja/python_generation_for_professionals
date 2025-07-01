from collections import Counter

counter = Counter(input().split(','))

for word, count in sorted(counter.items(), key=lambda x: x[0]):
    print(f'{word}: {count}')