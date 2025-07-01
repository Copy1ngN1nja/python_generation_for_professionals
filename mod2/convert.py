def convert(s):
    if sum(map(lambda x: x.isupper(), s)) > sum(map(lambda x: x.islower(), s)):
        return s.upper()
    else:
        return s.lower()
    

print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))