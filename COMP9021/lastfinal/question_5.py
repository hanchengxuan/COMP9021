
# We explain the task with an example.
#
# Consider the following sequence of integers: 1, 2, 3, 2, 2.
# Here are all permutations of this sequence:
# - 1, 2, 3, 2, 2, starting at index 0
# - 2, 3, 2, 2, 1, starting at index 1
# - 3, 2, 2, 1, 2, starting at index 2
# - 2, 2, 1, 2, 3, starting at index 3
# - 2, 1, 2, 3, 2, starting at index 4
# For each of those permutations, we try and split it in 2 nonempty parts
# so that the sum of the numbers on the left is equal to the sum of the
# numbers on the right.
# - It is not possible with the permutation that starts at index 0.
# - It is possible with the permutation that starts at index 1:
#   2 + 3 = 2 + 2 + 1
#   yielding a solution with 2 terms on the left
#   and 3 terms on the right of the equality.
# - It is possible with the permutation that starts at index 2:
#   3 + 2 = 2 + 1 + 2
#   yielding a solution with 2 terms on the left
#   and 3 terms on the right of the equality.
# - It is possible with the permutation that starts at index 3:
#   2 + 2 + 1 = 2 + 3
#   yielding a solution with 3 terms on the left
#   and 2 terms on the right of the equality.
# - It is possible with the permutation that starts at index 4:
#   2 + 1 + 2 = 3 + 2
#   yielding a solution with 3 terms on the left
#   and 2 terms on the right of the equality.
# For all solutions, the sum is 5.
#
# We want to report whether there is a solution, and in case there is,
# say what is the leftmost permutation that yields a solution
# (so what is the minimal i for which the permutation that starts at
# index i yields a solution), and how many terms it has on the left
# and on the right of the equality.
#
# Do not ask for how large the sequence can be, just do your best.
# For the sample tests, the function should return within a fraction
# of a second. If you think well, it can be pushed way further.
#
# You can assume that the function is provided with nothing but integers
# as arguments.


def f(*numbers):
    '''
    >>> f(1, 2)
    There is no solution.
    >>> f(1, 1, 1)
    There is no solution.
    >>> f(1, 1)
    There is a solution, with a sum of 1.
    The leftmost permutation that yields a solution starts at index 0.
    If has 1 term on the left and 1 term on the right of the equality.
    >>> f(1, 1, 1, 1)
    There is a solution, with a sum of 2.
    The leftmost permutation that yields a solution starts at index 0.
    If has 2 terms on the left and 2 terms on the right of the equality.
    >>> f(1, 1, 1, 3)
    There is a solution, with a sum of 3.
    The leftmost permutation that yields a solution starts at index 0.
    If has 3 terms on the left and 1 term on the right of the equality.
    >>> f(1, 1, 3, 1)
    There is a solution, with a sum of 3.
    The leftmost permutation that yields a solution starts at index 2.
    If has 1 term on the left and 3 terms on the right of the equality.
    >>> f(1, 3, 1, 1)
    There is a solution, with a sum of 3.
    The leftmost permutation that yields a solution starts at index 1.
    If has 1 term on the left and 3 terms on the right of the equality.
    >>> f(3, 1, 1, 1)
    There is a solution, with a sum of 3.
    The leftmost permutation that yields a solution starts at index 0.
    If has 1 term on the left and 3 terms on the right of the equality.
    >>> f(1, 2, 3, 2, 2)
    There is a solution, with a sum of 5.
    The leftmost permutation that yields a solution starts at index 1.
    If has 2 terms on the left and 3 terms on the right of the equality.
    >>> f(*((1,) * 10_000))
    There is a solution, with a sum of 5000.
    The leftmost permutation that yields a solution starts at index 0.
    If has 5000 terms on the left and 5000 terms on the right of the equality.
    >>> f(*((1,) * 1_000 + (2_000,) + (1,) * 1_000))
    There is a solution, with a sum of 2000.
    The leftmost permutation that yields a solution starts at index 1000.
    If has 1 term on the left and 2000 terms on the right of the equality.
    '''
    if len(numbers) < 2:
        return
    # INSERT YOUR CODE HERE
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
