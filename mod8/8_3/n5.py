def get_pow(base, exp):
    if exp == 0:
        return 1
    return base * get_pow(base, exp - 1)

print(get_pow(5, 2))