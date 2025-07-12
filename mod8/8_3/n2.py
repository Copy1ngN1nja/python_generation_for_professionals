def sumi(n):
    if n == 0:
        return 0
    return n % 10 + sumi(n // 10)

n = int(input())
print(sumi(n))

