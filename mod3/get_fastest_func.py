import time

def get_the_fastest_func(funcs, arg):
    fastest_func = None
    fastest_time = float('inf')

    for func in funcs:
        start_time = time.monotonic()
        func(arg)
        end_time = time.monotonic()
        elapsed_time = end_time - start_time
        if elapsed_time < fastest_time:
            fastest_time = elapsed_time
            fastest_func = func
    
    return fastest_func


