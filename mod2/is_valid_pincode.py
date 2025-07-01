def is_valid(code):
    return 4 <= len(code) <= 6 and code.isdigit()


print(is_valid('4367'))
print(is_valid('92134'))
print(is_valid('89abc1'))
print(is_valid('900876'))
print(is_valid('49 83'))