from collections import Counter
import sys

counter = Counter()
for line in sys.stdin:
    name, score = line.split()
    score = int(score)
    counter[name] = score

print(counter.most_common()[-2][0])