def hash_as_key(arr):
    my_dict = {}
    for item in arr:
        key = hash(item)
        if key not in my_dict:
            my_dict[key] = item
        else:
            if not isinstance(my_dict[key], list):
                my_dict[key] = [my_dict[key]]
            my_dict[key].append(item)
    return my_dict

data = [1, 2, 3, 4, 5, 5]

print(hash_as_key(data))

data = [-1, -2, -3, -4, -5]

print(hash_as_key(data))

data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

print(hash_as_key(data))