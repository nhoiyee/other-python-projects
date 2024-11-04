import random_string
import guess_result
import get_guess
def play(num_digits, num_guesses):
    '''
    Generate a random string with num_digits digits.
    The player has num_guesses guesses to guess the random 
    string. After each guess, the player is told how many 
    digits in the guess are in the correct place, and how 
    many digits exist but are in the wrong place.
    '''
    answer = random_string(num_digits)
    print('I generated a random {}-digit number.'.format(num_digits))
    print('You have {} guesses to guess the number.'.format(num_guesses))
    for i in range(num_guesses):
        guess = get_guess(num_digits)
        result = guess_result(guess, answer)
        print('Correct: {}, Misplaced: {}'.format(result[0], result[1]))
        if guess == answer:
            print('You win!')
            return
    print('You lose! The correct answer was {}.'.format(answer))
