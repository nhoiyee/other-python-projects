def split_string(text, separators):
    '''
    text is a string of text.
    separators is a string of separator characters.
    
    Split the text into a list using any of the one-character
    separators and return the result.
    Remove spaces from beginning and end
    of a string before adding it to the list.
    Do not include empty strings in the list.
    
    >>> split_string('one*two[three', '*[')
    ['one', 'two', 'three']
    >>> split_string('A pearl! Pearl! Lustrous pearl! Rare. \
    What a nice find.', '.?!')   
    ['A pearl', 'Pearl', 'Lustrous pearl', 'Rare', \
    'What a nice find']
    '''
    words = []
    word = ''
    for char in text:
        if char not in separators:
            word += char
        else:
            if word != '':
                words.append(word.strip())
            word = ''
    if word != '':
        words.append(word.strip())
    return words

    
