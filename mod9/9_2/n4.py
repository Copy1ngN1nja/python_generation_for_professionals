func = input()
a, b = map(int, input().split())

values = []
for x in range(a, b + 1):
    values.append(eval(func))

print(f'Минимальное значение функции {func} на отрезке [{a}; {b}] равно {min(values)}')
print(f'Максимальное значение функции {func} на отрезке [{a}; {b}] равно {max(values)}')