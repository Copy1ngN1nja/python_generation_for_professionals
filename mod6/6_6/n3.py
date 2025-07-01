from collections import OrderedDict

def custom_sort(data, by_values=False):
    if by_values:
        sorted_items = sorted(data.items(), key=lambda item: item[1])
    else:
        sorted_items = sorted(data.items(), key=lambda item: item[0])
    data.clear()
    data.update(sorted_items)

data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)