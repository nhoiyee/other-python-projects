import random
def random_string(length):
    '''
    length is an integer.
    
    Return a string of the given length, where each character
    is a digit from 0 to 9, and with no repeated digits.
    '''
    # create a list of digits
    digits = list(range(10))
    # shuffle the digits
    random.shuffle(digits)
    # return the first length digits as a string
    return ''.join(str(digit) for digit in digits[:length])
   