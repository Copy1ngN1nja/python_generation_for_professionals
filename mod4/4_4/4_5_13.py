import json
from datetime import datetime, time

def cmp_pool(pool):
    timetable_mon = pool['WorkingHoursSummer']['Понедельник']
    from_time, to_time = timetable_mon.split('-')
    from_time = datetime.strptime(from_time, '%H:%M').time()
    to_time = datetime.strptime(to_time, '%H:%M').time()
    does_work = (from_time <= time(10, 0) and time(12, 0) <= to_time)
    dimensions = pool['DimensionsSummer']
    length = dimensions['Length']
    width = dimensions['Width']
    return (does_work, length, width)
    


with open('pools.json', 'r') as input_file:
    data = json.load(input_file)
    best_pool = max(data, key=cmp_pool)
    print(f'{best_pool['DimensionsSummer']['Length']}x{best_pool['DimensionsSummer']['Width']}')
    print(best_pool['Address'])
