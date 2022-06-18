from random import seed, shuffle


# Generates a list L consisting of all integers
# between 0 and nb_of_elements - 1, in some random order.
#
# Consider the following lists with at least 2 elements:
# - the members of L from L's smallest element
#   to L's largest element,
#   read from left to right if the former occurs before the latter in L,
#   read from right to left if the former occurs after the latter in L;
# - the members of L from L's second smallest element
#   to L's second largest element,
#   read from left to right if the former occurs before the latter in L,
#   read from right to left if the former occurs after the latter in L;
# - the members of L from L's third smallest element
#   to L's third largest element,
#   read from left to right if the former occurs before the latter in L,
#   read from right to left if the former occurs after the latter in L.
#
# Outputs those lists preceded with some text, that explains the order
# in which they are output.
#
# Note that <BLANKLINE> is doctest's way to express that your code
# should produce a blank line; do not let your code print out <BLANKLINE>...
#
# You can assume that the function is called with integers as arguments.


def f(arg_for_seed, nb_of_elements):
    '''
    >>> f(0, 1)
    Here is L: [0]
    Sequences will appear from shortest to longest.
    >>> f(0, 2)
    Here is L: [0, 1]
    Sequences will appear from shortest to longest.
    Ordered from smallest to largest sum,
    and for a given sum from smallest to largest first element,
    there are sequences of length 2, namely:
        [0, 1] (sum is 1)
    >>> f(0, 3)
    Here is L: [0, 2, 1]
    Sequences will appear from shortest to longest.
    Ordered from smallest to largest sum,
    and for a given sum from smallest to largest first element,
    there are sequences of length 2, namely:
        [0, 2] (sum is 2)
    >>> f(0, 4)
    Here is L: [2, 0, 1, 3]
    Sequences will appear from shortest to longest.
    Ordered from smallest to largest sum,
    and for a given sum from smallest to largest first element,
    there are sequences of length 3, namely:
        [1, 0, 2] (sum is 3)
        [0, 1, 3] (sum is 4)
    >>> f(0, 5)
    Here is L: [2, 1, 0, 4, 3]
    Sequences will appear from shortest to longest.
    Ordered from smallest to largest sum,
    and for a given sum from smallest to largest first element,
    there are sequences of length 2, namely:
        [0, 4] (sum is 4)
    <BLANKLINE>
    Ordered from smallest to largest sum,
    and for a given sum from smallest to largest first element,
    there are sequences of length 4, namely:
        [1, 0, 4, 3] (sum is 8)
    >>> f(0, 6)
    Here is L: [4, 2, 1, 0, 5, 3]
    Sequences will appear from shortest to longest.
    Ordered from smallest to largest sum,
    and for a given sum from smallest to largest first element,
    there are sequences of length 2, namely:
        [0, 5] (sum is 5)
    <BLANKLINE>
    Ordered from smallest to largest sum,
    and for a given sum from smallest to largest first element,
    there are sequences of length 3, namely:
        [1, 2, 4] (sum is 7)
    <BLANKLINE>
    Ordered from smallest to largest sum,
    and for a given sum from smallest to largest first element,
    there are sequences of length 5, namely:
        [2, 1, 0, 5, 3] (sum is 11)
    >>> f(0, 12)
    Here is L: [1, 9, 8, 5, 10, 2, 3, 7, 4, 0, 11, 6]
    Sequences will appear from shortest to longest.
    Ordered from smallest to largest sum,
    and for a given sum from smallest to largest first element,
    there are sequences of length 2, namely:
        [0, 11] (sum is 11)
        [4, 7] (sum is 11)
    <BLANKLINE>
    Ordered from smallest to largest sum,
    and for a given sum from smallest to largest first element,
    there are sequences of length 5, namely:
        [3, 2, 10, 5, 8] (sum is 28)
        [1, 9, 8, 5, 10] (sum is 33)
        [2, 10, 5, 8, 9] (sum is 34)
    <BLANKLINE>
    Ordered from smallest to largest sum,
    and for a given sum from smallest to largest first element,
    there are sequences of length 9, namely:
        [5, 10, 2, 3, 7, 4, 0, 11, 6] (sum is 48)
    '''
    if nb_of_elements < 1:
        return
    L = list(range(nb_of_elements))
    seed(arg_for_seed)
    shuffle(L)
    print('Here is L:', L)
    # INSERT YOUR CODE HERE
    print('Sequences will appear from shortest to longest.')
    X = L[::-1]
    k = set(L)
    lth = set()
    final = []
    if len(L) > 1:
        while k:
            a = min(k)
            b = max(k)
            if L.index(a)<L.index(b):
                this = L[L.index(a):L.index(b) + 1]
            elif L.index(a)>L.index(b):
                this = L[L.index(b):L.index(a) + 1][::-1]
            if len(this) > 1:
                final.append((len(this), this))
                lth.add(len(this))
                this = []
            if a == b:
                k.remove(a)
            else:
                k.remove(a)
                k.remove(b)
        pgs = []
        for i in range(len(L)+1):

            if i in lth:
                pgs = []
                print(f'Ordered from smallest to largest sum,')
                print('and for a given sum from smallest to largest first element,')
                print(f'there are sequences of length {i}, namely:')
                for j in final:
                    if j[0] == i:
                        pgs.append(j[1])
                pgs = sorted(pgs, key=lambda x: sum(x))
                for lt in pgs:
                    print('   ', lt, f'(sum is {sum(lt)})')
            if i > 1:
                if i+1 in lth and pgs:
                    print()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
