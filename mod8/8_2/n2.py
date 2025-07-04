def f(n=1):
    if n <= 100:
        print(n)
        f(n + 1)

f()