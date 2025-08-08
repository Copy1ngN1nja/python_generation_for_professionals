def convert(x):
    if x >= 0:
        return (bin(x)[2:], oct(x)[2:], hex(x)[2:].upper())
    else:
        return ('-' + bin(-x)[2:], '-' + oct(-x)[2:], '-' + hex(-x)[2:].upper())

print(convert(15))
print(convert(-24))
print(convert(1))