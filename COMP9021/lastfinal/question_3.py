from random import seed, randrange


# Generates a dictionary with keys ranging between 0
# and some digit n, and with values in {0,..., 9}.
#
# Each digit i between 0 and n determines a sequence
# of the form k_1, k_2, k_3... such that
# - k_1 is i,
# - the dictionary maps k_1 to k_2,
# - the dictionary maps k_2 to k_3,
# - ...
# up to a digit that
# - either is not a key of the dictionary,
#   in which case the sequence stops,
# - or is a digit that has been generated already,
#   in which case the sequence would see a pattern that repeats forever.
# We want to properly display both cases.
#
# - Take {0: 6, 1: 3, 2: 6, 3: 3, 4: 0} as a first example.
#   - Starting from 4, we get a sequence of the first kind: 406
#   - Starting from 1, we get a sequence of the second type: 13.3.
# - Take {0: 3, 1: 3, 2: 0, 3: 2, 4: 4} as a second example.
#   Starting from 1, we get a sequence of the second type: 1320.320.
#
# We display all sequences for all starting digits between 0 and n,
# but vertically rather than horizontally.
# All lines have the same number of characters, so some lines can have
# trailing spaces (click far enough on a line to observe where it stops).


def f(for_seed, size, upper_bound):
    '''
    >>> f(0, 1, 1)
    The dictionary is: {0: 0}
    0
    .
    0
    .
    >>> f(0, 1, 2)
    The dictionary is: {0: 1}
    0
    1
    >>> f(0, 2, 2)
    The dictionary is: {0: 1, 1: 1}
    0 1
    1 .
    . 1
    1 .
    .  
    >>> f(0, 3, 4)
    The dictionary is: {0: 3, 1: 3, 2: 0}
    0 1 2
    3 3 0
        3
    >>> f(0, 5, 7)
    The dictionary is: {0: 6, 1: 3, 2: 6, 3: 3, 4: 0}
    0 1 2 3 4
    6 3 6 . 0
      .   3 6
      3   .  
      .      
    >>> f(0, 5, 6)
    The dictionary is: {0: 3, 1: 3, 2: 0, 3: 2, 4: 4}
    0 1 2 3 4
    3 3 0 2 .
    2 2 3 0 4
    . 0 . . .
    0 . 2 3  
    3 3 0 2  
    2 2 3 0  
    . 0 . .  
      .      
    >>> f(0, 10, 10)
    The dictionary is: {0: 6, 1: 6, 2: 0, 3: 4, 4: 8, 5: 7, 6: 6, 7: 4, 8: 7, 9: 5}
    0 1 2 3 4 5 6 7 8 9
    6 6 0 4 8 7 . 4 7 5
    . . 6 8 7 4 6 8 4 7
    6 6 . 7 . 8 . . . 4
    . . 6 . 4 .   7 8 8
        . 4 8 7   4 7 .
          8 7 4   8 4 7
          7 . 8   . . 4
          .   .       8
                      .
    '''
    if not 1 <= size <= 10 or not 1 <= upper_bound <= 10:
        return
    seed(for_seed)
    D = {i: randrange(upper_bound) for i in range(size)}
    print('The dictionary is:', D)
    # INSERT YOUR CODE HERE
    if not 1 <= size <= 10 or not 1 <= upper_bound <= 10:
        return
    seed(for_seed)
    L = []
    D = {i: randrange(upper_bound) for i in range(size)}
    print('The dictionary is:', D)
    first = []
    for i in range(for_seed, size):
        first.append(str(i))
    print(' '.join(first))
    # while True:
    this = []
    for i in range(for_seed, size):
        a = D[int(first[i])]
        this.append(str(a))
    print(' '.join(this))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
