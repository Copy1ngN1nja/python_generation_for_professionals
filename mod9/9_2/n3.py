import sys

nums = []
for line in sys.stdin:
    line = line.strip()
    nums.append(eval(line))
print(max(nums))