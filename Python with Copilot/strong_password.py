def is_strong_password(password):
    """
A strong password has at least one uppercase character,
at least one number, and at least one punctuation.
 
Return True if the password is a strong password, False if not.
"""
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    return True


