def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

def filter_anagrams(target_word, words):
    return list(filter(lambda word: is_anagram(target_word, word), words))