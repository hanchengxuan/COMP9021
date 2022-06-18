# COMP9021 21T3 - Rachid Hamadi
# Final Exam Question 4

'''
No point to hard code for small values of n, will be tested
only for large enough values...
'''


def pascal_triangle_line(n):
    '''
    Recall: it is the list of binomial coefficients that give the
    number of ways of choosing k objects out of n - 1 for 0 <= k < n.

    >>> pascal_triangle_line(1)
    [1]
    >>> pascal_triangle_line(2)
    [1, 1]
    >>> pascal_triangle_line(3)
    [1, 2, 1]
    >>> pascal_triangle_line(4)
    [1, 3, 3, 1]
    >>> pascal_triangle_line(5)
    [1, 4, 6, 4, 1]
    >>> pascal_triangle_line(6)
    [1, 5, 10, 10, 5, 1]
    >>> pascal_triangle_line(7)
    [1, 6, 15, 20, 15, 6, 1]
    >>> pascal_triangle_line(8)
    [1, 7, 21, 35, 35, 21, 7, 1]
    '''

    # Prompts the user for a number N and prints out the first N + 1 lines of Pascal triangle.
    pascal_triangle = [[1]]
    for i in range(1, n + 1):
        templist = [1] * (i + 1)
        if len(pascal_triangle[i - 1]) < 2:
            templist = [1, 1]
            pascal_triangle.append(templist)
        else:
            for j in range(1, i):
                templist[j] = pascal_triangle[i - 1][j] + pascal_triangle[i - 1][j - 1]
            pascal_triangle.append(templist)
    return pascal_triangle[-2]

    # REPLACE return WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
