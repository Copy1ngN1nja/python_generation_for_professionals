from collections import Counter

def print_bar_chart(data, mark):
    if isinstance(data, str):
        data = Counter(data)
    else:
        data = Counter(data)
    max_len = max(len(key) for key in data.keys())
    for key, value in sorted(data.items(), key=lambda x: x[1], reverse=True):
        print(f'{key:<{max_len}} |{mark * value}')

print_bar_chart('beegeek', '+')

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']

print_bar_chart(languages, '#')