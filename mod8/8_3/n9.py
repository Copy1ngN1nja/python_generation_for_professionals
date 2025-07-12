mas_trib = [0] * 100000


def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2 or n == 3:
        mas_trib[n] = 1
    if mas_trib[n] == 0:
        mas_trib[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    return mas_trib[n]


print(tribonacci(7))