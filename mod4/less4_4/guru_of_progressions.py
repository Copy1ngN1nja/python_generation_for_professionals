import sys
from decimal import Decimal

arr = [Decimal(line.strip()) for line in sys.stdin if line.strip()]

def is_arithmetic_progression(arr):
    subs = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
    return all(sub == subs[0] for sub in subs)

def is_geometric_progression(arr):
    if any(x == 0 for x in arr):
        return False
    divs = [arr[i] / arr[i - 1] for i in range(1, len(arr))]
    return all(div == divs[0] for div in divs)

if is_arithmetic_progression(arr):
    print('Арифметическая прогрессия')
elif is_geometric_progression(arr):
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')