import json
from zipfile import ZipFile

def is_correct_json(json_string):
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False

with ZipFile('data.zip', 'r') as zip_file:
    info = zip_file.infolist()
    ans = []
    for item in info:
        if item.is_dir():
            continue
        with zip_file.open(item) as json_file:
            try:
                data = json.load(json_file)
                if data['team'] == 'Arsenal':
                    ans.append((data['first_name'], data['last_name']))
            except:
                pass

ans.sort()
for person in ans:
    print(*person)