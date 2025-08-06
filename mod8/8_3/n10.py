def is_palindrome(s, i=0):
    if i >= len(s) // 2:
        return True
    return s[i] == s[-(i + 1)] and is_palindrome(s, i + 1)

print(is_palindrome('stepik'))