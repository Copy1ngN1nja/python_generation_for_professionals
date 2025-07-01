def choose_plural(amount, declensions):
    declension = ''
    if amount % 10 == 1 and amount % 100 != 11:
        declension = declensions[0]
    elif amount % 10 in [2, 3, 4] and not (amount % 100 in [12, 13, 14]):
        declension = declensions[1]
    else:
        declension = declensions[2]
    return str(amount) + ' ' + declension

print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))