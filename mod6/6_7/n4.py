from collections import Counter

counter = Counter(input().split(','))
max_len_word = max(len(word) for word in counter)

for word, count in sorted(counter.items(), key=lambda x: x[0]):
    price = sum(ord(c) for c in word if c.isalpha())
    print(f'{word:<{max_len_word}}: {price} UC x {count} = {price * count} UC')