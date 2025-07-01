# d1d2d
# d12d
# d121d
# d212d

dto1, dto2, other = int(input()), int(input()), int(input())
print(min(
    dto1 + dto1 + dto2 + dto2,
    dto1 + other + dto2,
    dto1 + other + other + dto1,
    dto2 + other + other + dto2,
))
