def triangle(n):
    if n > 0:
        print('*' * n)
        triangle(n - 1)

triangle(3)