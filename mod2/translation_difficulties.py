n = int(input())
people = [set() for _ in range(n)]
for i in range(n):
    people[i] = set(input().split(', '))

common = set.intersection(*people)
if common:
    print(*sorted(common), sep=', ')
else:
    print('Сериал снять не удастся')
