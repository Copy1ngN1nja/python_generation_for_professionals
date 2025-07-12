def is_power(base):
    if base == 1:
        return True
    if base % 2 == 0:
        return is_power(base // 2)
    return False


print(is_power(512))
print(is_power(15))