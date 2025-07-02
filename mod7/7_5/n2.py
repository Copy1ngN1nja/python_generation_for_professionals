class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(password):
    if len(password) < 9:
        raise LengthError()
    if not any(char.isalpha() for char in password):
        raise LetterError()
    if not any(char.isupper() for char in password):
        raise LetterError()
    if not any(char.islower() for char in password):
        raise LetterError()
    if not any(char.isdigit() for char in password):
        raise DigitError()
    return True


try:
    print(is_good_password('Short7'))
except Exception as err:
    print(type(err))

print(is_good_password('еПQSНгиfУЙ70qE'))

try:
    print(is_good_password('41157081231232'))
except Exception as err:
    print(type(err))