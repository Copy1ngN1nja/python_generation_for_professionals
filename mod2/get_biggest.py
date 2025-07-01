from functools import cmp_to_key


def cmp(a, b):
    a = str(a)
    b = str(b)
    if a + b > b + a:
        return 1
    elif a + b < b + a:
        return -1
    else:
        return 0


def get_biggest(numbers):
    if not numbers:
        return -1
    numbers.sort(key=cmp_to_key(cmp), reverse=True)
    return int(''.join(map(str, numbers)))


print(get_biggest([1, 2, 3]))
print(get_biggest([61, 228, 9, 3, 11]))
print(get_biggest([7, 71, 72]))
print(get_biggest([]))