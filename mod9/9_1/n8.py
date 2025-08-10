def my_pow(number):
    return sum(int(x[1]) ** x[0] for x in enumerate(str(number), start=1))

print(my_pow(139))
print(my_pow(123))
print(my_pow(0))