from datetime import date


def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False


ans = []
cnt = 0
while True:
    line = input()
    if line == 'end':
        break
    if is_correct(*map(int, line.split('.'))):
        ans.append('Корректная')
        cnt += 1
    else:
        ans.append('Некорректная')

for res in ans:
    print(res)
print(cnt)