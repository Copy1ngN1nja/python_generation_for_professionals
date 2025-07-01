def same_parity(numbers):
    if not numbers:
        return []
    return list(filter(lambda x: x % 2 == numbers[0] % 2, numbers))

print(same_parity([]))
print(same_parity([6, 0, 67, -7, 10, -20]))
print(same_parity([-7, 0, 67, -9, 70, -29, 90]))