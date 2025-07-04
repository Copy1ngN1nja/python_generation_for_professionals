def f():
    x = int(input())
    if x != 0:
        f()
    print(x)
f()