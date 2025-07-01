list_vow = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

def similar_words(word1, word2):
    for i in range(len(word1)):
        if word1[i] in list_vow and (i > len(word2) - 1 or word2[i] not in list_vow):
            return False
    for i in range(len(word2)):
        if word2[i] in list_vow and (i > len(word1) - 1 or word1[i] not in list_vow):
            return False
    return True

original_word = input()
candidate_words = [input() for _ in range(int(input()))]
# print()
candidate_word = [word for word in candidate_words if similar_words(original_word, word)]
if candidate_word:
    print(*candidate_word, sep='\n')
    