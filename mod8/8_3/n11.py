def to_binary(n, result=''):
    if n == 0:
        if result == '':
            return '0'
        return result[::-1]
    return to_binary(n // 2, result + str(n % 2))

print(to_binary(15))
print(to_binary(0))
print(to_binary(1))