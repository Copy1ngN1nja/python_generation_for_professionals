def spell(*words):
    d = {}
    for word in words:
        word = word.lower()
        d[word[0]] = max(d.get(word[0], 0), len(word))
    return d

words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))
print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))