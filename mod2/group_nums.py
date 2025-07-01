groups = {}
n = int(input())
nums = [i for i in range(1, n + 1)]

for num in nums:
    key_group = sum(int(digit) for digit in str(num))
    groups[key_group] = groups.get(key_group, 0) + 1

groups = sorted(groups.values(), reverse=True)
print(groups[0])
