from collections import Counter

def count_occurences(word, words):
    words_counter = Counter(words.lower().split())
    return words_counter[word.lower()]

word = 'python'
words = 'Python Conferences python training python events'

print(count_occurences(word, words))

word = 'Java'
words = 'Python C++ C# JavaScript Go Assembler'

print(count_occurences(word, words))

word = 'Se'
words = 'se sdsf sds SE sdfsdg Se dhgf gfd asd se'

print(count_occurences(word, words))