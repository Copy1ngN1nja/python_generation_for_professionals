def range_sum(lst, start, end):
    if start > end:
        return 0
    return lst[start] + range_sum(lst, start + 1, end)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))