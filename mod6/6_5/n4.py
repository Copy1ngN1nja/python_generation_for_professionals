from collections import defaultdict

def wins(matches):
    my_dict = defaultdict(set)

    for winner, loser in matches:
        my_dict[winner].add(loser)

    return my_dict


result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))