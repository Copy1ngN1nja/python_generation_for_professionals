from collections import Counter

vegetables = Counter({'cabbage': 10, 'pepper': 'seven', 'pumpkin': 'four'})

vegetables.update({'cabbage': 5, 'pepper': 'two'})

print(vegetables['pepper'])
print(vegetables['cabbage'])