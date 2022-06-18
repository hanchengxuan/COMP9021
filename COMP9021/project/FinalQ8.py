# COMP9021 21T3 - Rachid Hamadi
# Final Exam Question 8

def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.

    Conjunctions of inputs will be tested, so hard coding will not help.

    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    sumrow=set()
    sumcolumn=set()

    sumdignal=set()
    for i in square:
        sumrow.add(sum(i))
    for j in range(len(square[0])):
        column=[]
        for i in range(len(square)):
            column.append(square[i][j])
        sumcolumn.add(sum(column))
    digonals1=0
    digonals2=0
    for i in range(len(square)):

        digonals1+=square[i][i]
        digonals2+=square[i][len(square)-i-1]
    sumdignal.add(digonals1)
    sumdignal.add(digonals2)
    totalsum=set()

    for i in sumrow:
        totalsum.add(i)
    for j in sumcolumn:
        totalsum.add(j)
    for k in sumdignal:
        totalsum.add(k)
    if len(totalsum)==len(square)*2+2:
        return True
    else:
        return False
    # REPLACE return WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS


if __name__ == '__main__':
    import doctest

    doctest.testmod()
