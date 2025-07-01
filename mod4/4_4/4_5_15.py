import json

with open('food_services.json', 'r') as json_file:
    cafes = json.load(json_file)
    district_cafes = {}
    nets = {}
    for cafe in cafes:
        district = cafe['District']
        if cafe['IsNetObject'] == 'да':
            nets[cafe['OperatingCompany']] = nets.get(cafe['OperatingCompany'], 0) + 1
        district_cafes[district] = district_cafes.get(district, 0) + 1
    max_district = max(district_cafes, key=district_cafes.get)
    max_net = max(nets, key=nets.get)
    print(f'{max_district}: {district_cafes[max_district]}')
    print(f'{max_net}: {nets[max_net]}')