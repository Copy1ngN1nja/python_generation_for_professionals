from datetime import date, datetime, time

with open('diary.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]
    dates = {}
    cur = ''
    for line in lines:
        try:
            entry_dt = datetime.strptime(line, '%d.%m.%Y; %H:%M')
            dates[entry_dt] = []
            cur = entry_dt
        except ValueError:
            if line != '':
                dates[cur].append(line)
    for dt, entries in sorted(dates.items()):
        print(f'{dt.strftime('%d.%m.%Y; %H:%M')}')
        for entry in entries:
            print(entry)
        print()