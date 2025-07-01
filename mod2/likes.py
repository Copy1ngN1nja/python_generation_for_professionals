def likes(likers):
    if not likers:
        return 'Никто не оценил данную запись'
    elif len(likers) == 1:
        return f'{likers[0]} оценил(а) данную запись'
    elif len(likers) == 2:
        return f'{likers[0]} и {likers[1]} оценили данную запись'
    elif len(likers) == 3:
        return f'{likers[0]}, {likers[1]} и {likers[2]} оценили данную запись'
    else:
        return f'{likers[0]}, {likers[1]} и {len(likers) - 2} других оценили данную запись'
    
print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))