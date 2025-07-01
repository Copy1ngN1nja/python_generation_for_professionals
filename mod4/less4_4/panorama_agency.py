import sys

categories = {}

lines = [line.strip() for line in sys.stdin]

for line in lines[:-1]:
    news, category, rate = line.split(' / ')
    rate = float(rate)
    if category not in categories:
        categories[category] = []
    categories[category].append((rate, news))


desired_category = lines[-1]
for rate, news in sorted(categories.get(desired_category, [])):
    print(news)