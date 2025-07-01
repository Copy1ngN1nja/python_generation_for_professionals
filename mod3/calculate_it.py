import time

def calculate_it(func, *args):
    start_time = time.monotonic()
    result = func(*args)
    end_time = time.monotonic()
    elapsed_time = end_time - start_time
    return result, elapsed_time

def add(a, b, c):
    time.sleep(3)
    return a + b + c

print(calculate_it(add, 1, 2, 3))