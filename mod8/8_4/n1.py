def recursive_sum(a):
    res = 0
    for elem in a:
        if isinstance(elem, list):
            res += recursive_sum(elem)
        else:
            res += elem
    return res

my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))

my_list = []

print(recursive_sum(my_list))