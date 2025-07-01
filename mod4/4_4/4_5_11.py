import csv, json

with open('playgrounds.csv', 'r') as input_file, open('addresses.json', 'w') as output_file:
    reader = csv.DictReader(input_file, delimiter=';')
    address_data = {}
    
    for row in reader:
        adm_area = row['AdmArea']
        if adm_area not in address_data:
            address_data[adm_area] = {}
        district = row['District']
        if district not in address_data[adm_area]:
            address_data[adm_area][district] = []
        address_data[adm_area][district].append(row['Address'])
    json.dump(address_data, output_file, indent=3, ensure_ascii=False)