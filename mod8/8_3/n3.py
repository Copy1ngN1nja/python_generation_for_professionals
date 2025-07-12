def number_of_frogs(year, cnt=77):
    if year == 1:
        return cnt
    else:
        return number_of_frogs(year - 1, 3 * (cnt - 30))


print(number_of_frogs(2))