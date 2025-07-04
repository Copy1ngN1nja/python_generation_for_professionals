def pes(n=16, x=1):
    print(' ' * (x - 1) * 2 + str(x) * n)
    if x < 4:
        pes(n - 4, x + 1)
        print(' ' * (x - 1) * 2 + str(x) * n)

pes()