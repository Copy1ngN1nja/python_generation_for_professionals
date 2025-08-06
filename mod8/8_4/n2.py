def linear(arr):
    res = []
    for elem in arr:
        if isinstance(elem, list):
            res.extend(linear(elem))
        else:
            res.append(elem)
    return res

my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))

my_list = [10, 20, 30, 40, 50]

print(linear(my_list))