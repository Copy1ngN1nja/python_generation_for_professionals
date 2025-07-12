def get_fast_pow(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        half_pow = get_fast_pow(base, exp // 2)
        return half_pow * half_pow
    else:
        return base * get_fast_pow(base, exp - 1)
    
print(get_fast_pow(5, 2))