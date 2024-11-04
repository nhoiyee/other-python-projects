def num_points(word): 
    """ 
    Each letter is worth the following points: 
    a, e, i, o, u, l, n, s, t, r: 1 point 
    d, g: 2 points 
    b, c, m, p: 3 points 
    f, h, v, w, y: 4 points 
    k: 5 points 
    j, x: 8 points 
    q, z: 10 points 

    word is a word consisting of lowercase characters. 
    Return the sum of points for each letter in word. 
    """
    # create a dictionary of points for each letter
    points = {'a': 1, 'b': 3, 'c': 3, 'd': 2,
            'e': 1, 'f': 4, 'g': 2, 'h': 4,
            'i': 1, 'j': 8, 'k': 5, 'l': 1,
            'm': 3, 'n': 1, 'o': 1, 'p': 3,
            'q': 10, 'r': 1, 's': 1, 't': 1,
            'u': 1, 'v': 4, 'w': 4, 'x': 8,
            'y': 4, 'z': 10}
    # initialize the total points to 0
    total = 0
    # loop through each letter in the word
    for letter in word:
        # add the points for the letter to the total
        total += points[letter]
    # return the total points
    return total

def best_word(word_list):
    """
    word_list is a list of words.
        
    Return the word worth the most points.
    """
    # initialize the best word and the max points to 0
    best = ''
    max_points = 0
    # loop through each word in the word list
    for word in word_list:
        # calculate the points for the word
        points = num_points(word)
        # check if the word is worth more points than the best word
        if points > max_points:
            # update the best word and max points
            best = word
            max_points = points
    # return the best word
    return best

best_word(['zap', 'pack', 'quack'])  
#'quack'