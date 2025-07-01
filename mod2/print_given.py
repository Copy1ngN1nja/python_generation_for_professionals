def print_given(*args, **kwargs):
    for arg in args:
        print(arg, type(arg))
    for key, value in sorted(kwargs.items()):
        print(key, value, type(value))

print_given(1, [1, 2, 3], 'three', two=2)
print_given('apple', 'cherry', 'watermelon')
print_given(b=2, d=4, c=3, a=1)
print_given()