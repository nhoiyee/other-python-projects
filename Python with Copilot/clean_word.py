import string
def clean_word(word):
    '''
word is a string.

Return a version of word in which all letters have been
converted to lowercase, and punctuation characters have been
stripped from both ends. Inner punctuation is left untouched.
   
>>> clean_word('Pearl!')
'pearl'
>>> clean_word('card-board')
'card-board'
'''
    word = word.strip(string.punctuation)
    return word.lower()



  