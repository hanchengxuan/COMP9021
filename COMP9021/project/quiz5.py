# COMP9021 21T3 - Rachid Hamadi
# Quiz 5 *** Due Friday Week 8 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Monday Week 8 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines moved to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines moved to the right by one position, e.g.
#      111
#       111
#        111
#         111
# The size is the number of 1s in the parallelogram. In the above examples, the size is 12.

from random import seed, randrange
import sys
import time

dim = 10


def display_grid():
    for row in grid:
        print('   ', *row)


def size_of_largest_parallelogram():
    width = 0
    height = 1

    tempsizelist = []
    for i in range(1, len(grid)):
        for j in range(len(grid)):
            while grid[i][j] == 1:
                tempI=i
                width += 1
                j += 1
                if j not in range(len(grid)):
                    break
                else:
                    tempJ = j
                if width>=2:
                    i-=1
                    while i>=0 and j >= 0 and j - 1+width <=len(grid) and j+1<=len(grid):
                        testlist=[]
                        for e in grid[i][j-1:j-1+width]:
                            testlist.append(e)
                        if all(testlist):
                            if i==0:
                                height += 1
                                break
                            else:
                                height += 1
                                i -= 1
                                j += 1
                                if j==len(grid):
                                    break
                        else:
                            break
                    i = tempI
                    j = tempJ
                    if height > 1:
                        tempsize = height * width
                        tempsizelist.append(tempsize)
                    height=1
            width = 0

    for i in range(1, len(grid)):
        for j in range(len(grid)):
            while grid[i][j] == 1:
                tempI = i
                width += 1
                j+=1
                if j not in range(len(grid)):
                    break
                else:
                    tempJ = j
                if width >= 2:
                    i = tempI
                    j = tempJ
                    i -= 1
                    while i >= 0 and j >= 0 and j-width-1>=0:
                        testlist = []
                        for e in grid[i][j - width-1:j-1]:
                            testlist.append(e)
                        if all(testlist):
                            if i == 0:
                                height += 1
                                break
                            else:
                                height += 1
                                i -= 1
                                j -= 1
                                if j == 0:
                                    break
                        else:
                            break
                    i = tempI
                    j = tempJ
                    if height > 1:
                        tempsize = height * width
                        tempsizelist.append(tempsize)
                    height = 1
            width = 0

    for i in range(1, len(grid)):
        for j in range(len(grid)):
            while grid[i][j] == 1:
                tempI = i
                width += 1
                if j not in range(len(grid)):
                    break
                else:
                    tempJ = j
                if width >= 2:
                    i -= 1
                    while i >= 0 and j >= 0 and j-width>=0:
                        testlist = []
                        for e in grid[i][j - width+1:j+1]:
                            testlist.append(e)
                        if all(testlist):
                            if i == 0:
                                height += 1
                                break
                            else:
                                height += 1
                                i -= 1
                                if j == len(grid):
                                    break
                        else:
                            break
                    i = tempI
                    j = tempJ
                    if height > 1:
                        tempsize = height * width
                        tempsizelist.append(tempsize)
                    height = 1
                if j == len(grid)-1:
                    break
                else:
                    j+=1
            width = 0
    if tempsizelist:
        size = max(tempsizelist)
    else:
        return 0
    return size


    # REPLACE PASS ABOVE WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS

time.sleep(0.1)
try:

    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                               ).split()
                         )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
        for _ in range(dim)
        ]
print('Here is the grid that has been generated:')
print(grid)
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
          )
else:
    print('There is no parallelogram with horizontal sides.')