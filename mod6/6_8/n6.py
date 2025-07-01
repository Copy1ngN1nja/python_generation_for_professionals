from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

def func_min_values():
    min_value = min(data.values())
    return [(key, value) for key, value in data.items() if value == min_value]

def func_max_values():
    max_value = max(data.values())
    return [(key, value) for key, value in data.items() if value == max_value]

data.min_values = func_min_values
data.max_values = func_max_values

print(data.max_values())
print(data.min_values())