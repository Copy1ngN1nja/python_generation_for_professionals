def recursive_sum(a, b):
    if a > 0:
        return 1 + recursive_sum(a - 1, b)
    elif b > 0:
        return 1 + recursive_sum(a, b - 1)
    else:
        return 0
    
print(recursive_sum(3, 5))