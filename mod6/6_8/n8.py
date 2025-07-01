from collections import Counter

def scrabble(symbols, word):
    counter_symbols = Counter(symbols.lower())
    counter_word = Counter(word.lower())
    return counter_word <= counter_symbols

print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
print(scrabble('begk', 'beegeek'))
print(scrabble('beegeek', 'beegeek'))