from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
all_prices = ChainMap(bread, meat, sauce, vegetables, toppings)

order = Counter(input().split(','))

total_cost = 0
max_len = max(len(ingredient) for ingredient in order)
max_cnt = max(len(str(quantity)) for quantity in order.values())
for ingredient, quantity in sorted(order.items(), key=lambda x: x[0]):
    cost = all_prices[ingredient] * quantity
    total_cost += cost
    print(f'{ingredient:<{max_len}} x {quantity}')
final_s = f'ИТОГ: {total_cost}р'
print('-' * max(max_len + 3 + max_cnt, len(final_s)))
print(final_s)