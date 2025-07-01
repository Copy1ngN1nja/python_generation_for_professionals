import json
import sys


json_dict = json.loads(sys.stdin.read())
for key, value in json_dict.items():
    if isinstance(value, list):
        value = ', '.join(list(map(str, value)))
    print(f'{key}: {value}')