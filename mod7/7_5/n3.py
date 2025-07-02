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

while True:
    try:
        password = input()
        if is_good_password(password):
            print('Success!')
            break
    except PasswordError as err:
        print(err.__class__.__name__)