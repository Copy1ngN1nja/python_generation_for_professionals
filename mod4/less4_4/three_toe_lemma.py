import sys

lines = [int(line.strip()) for line in sys.stdin]
if len(lines) % 2 == lines[-1] % 2:
    print('Дима')
else:
    print('Анри')