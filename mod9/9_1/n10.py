def zip_longest(*iterables, fill=None):
    max_length = max(len(it) for it in iterables)
    result = []
    for i in range(max_length):
        current = []
        for it in iterables:
            if i < len(it):
                current.append(it[i])
            else:
                current.append(fill)
        result.append(tuple(current))
    return result


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
print(zip_longest(*data))