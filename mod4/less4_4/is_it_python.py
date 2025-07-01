from datetime import date, datetime
import sys


def is_increasing(dates):
    for i in range(1, len(dates)):
        if dates[i] <= dates[i - 1]:
            return False
    return True

lines = [line.strip() for line in sys.stdin if line.strip()]
dates = []
for line in lines:
    dates.append(datetime.strptime(line, '%d.%m.%Y').date())

if is_increasing(dates):
    print('ASC')
elif is_increasing(dates[::-1]):
    print('DESC')
else:
    print('MIX')