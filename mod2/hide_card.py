def hide_card(card):
    card = card.replace(' ', '')
    return '*' * 12 + card[-4:]

card = '1234567890123456'

print(hide_card(card))