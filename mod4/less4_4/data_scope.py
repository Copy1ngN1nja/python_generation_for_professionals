import sys
from datetime import datetime, date, timedelta

mini = date.max
maxi = date.min
for line in sys.stdin:
    line = line.strip()
    d = datetime.strptime(line, '%Y-%m-%d').date()
    mini = min(mini, d)
    maxi = max(maxi, d)

data_scope = maxi - mini
print(data_scope.days)