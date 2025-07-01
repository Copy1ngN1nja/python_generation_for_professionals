import sys

heights = [int(line.strip()) for line in sys.stdin]
if len(heights) == 0:
    print('нет учеников')
else:
    print(f'Рост самого низкого ученика: {min(heights)}')
    print(f'Рост самого высокого ученика: {max(heights)}')
    print(f'Средний рост: {sum(heights) / len(heights)}')