import json

def is_correct_json(json_string):
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False
    
data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

print(is_correct_json(data))

print(is_correct_json('number = 17'))