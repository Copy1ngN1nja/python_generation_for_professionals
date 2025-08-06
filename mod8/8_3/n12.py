def up_n_down(n):
    if n <= 0:
        print(n)
        return
    print(n)
    up_n_down(n - 5)
    print(n)

up_n_down(int(input()))