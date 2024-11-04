
def get_guess(length):
    '''
length is an integer.
 
Keep asking the player to enter a string where each character 
is a digit from 0 to 9, until they enter a valid guess.
A valid guess has the given length and has no repeated digits.
'''
    # loop until the player enters a valid guess
    while True:
        # get the player's guess
        guess = input(f'Enter a {length}-digit guess: ')
        # check if the guess has the given length
        if len(guess) != length:
            print(f'Your guess must be {length} digits long.')
            continue
        # check if the guess has no repeated digits
        if len(set(guess)) != length:
            print('Your guess must have no repeated digits.')
            continue
        # return the valid guess
        return guess