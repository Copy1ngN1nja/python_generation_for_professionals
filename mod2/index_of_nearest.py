def index_of_nearest(array, value):
    idx = -1
    for i in range(len(array)):
        if abs(array[i] - value) < abs(array[idx] - value) or idx == -1:
            idx = i
    return idx

print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))