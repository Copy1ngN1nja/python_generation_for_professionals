import csv

with open('prices.csv', 'r') as input_file:
    dict_reader = csv.DictReader(input_file, delimiter=';')
    mini_name = ''
    mini_shop = ''
    mini_price = float('inf')
    for d in dict_reader:
        for item, cost in list(d.items())[1:]:
            if int(cost) < mini_price or (int(cost) == mini_price and item < mini_name) or \
                (int(cost) == mini_price and item == mini_name and d['Магазин'] < mini_shop):
                mini_price = int(cost)
                mini_name = item
                mini_shop = d['Магазин']
                
    print(f'{mini_name}: {mini_shop}')