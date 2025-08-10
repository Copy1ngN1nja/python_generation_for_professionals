def get_key(x):
    if x.isalpha() and x.islower():
        k = 0
    elif x.isalpha() and x.isupper():
        k = 1
    elif int(x) % 2 == 1:
        k = 2
    else:
        k = 3
    return (k, x)
        
s = input()
print(''.join(sorted(s, key=get_key)))