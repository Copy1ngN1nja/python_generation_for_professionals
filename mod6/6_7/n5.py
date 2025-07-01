from collections import Counter

with open('pythonzen.txt', 'r') as input_file:
    text = input_file.read()

text = text.lower()
counter_letters = Counter(c for c in text if c.isalpha())
for letter, count in sorted(counter_letters.items(), key=lambda x: x[0]):
    print(f'{letter}: {count}')