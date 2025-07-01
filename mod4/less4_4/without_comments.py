import sys

lines = [line for line in sys.stdin]
new_lines = []
for line in lines:
    if not line.strip().startswith('#'):
        new_lines.append(line)
print(''.join(new_lines))