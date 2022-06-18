# COMP9021 21T3 - Rachid Hamadi
# Quiz 6 *** Due Friday Week 9 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Monday Week 10 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).
# Neighbours are only considered vertically or horizontally (not diagonally).


from random import seed, randrange
import sys


dim = 10
movelist = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def display_grid():
    for row in grid:
        print('   ', *row)


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.
def colour_shapes():
    colour=[]

    countshape=2
    colour.append(countshape)
    for i in range(dim):
        for j in range(dim):
            if grid[i][j]==1:
                shapelist = []
                find_shape(i,j,shapelist)
                for i,j in shapelist:
                    grid[i][j]=countshape
                colour.pop()
                countshape+=1
                colour.append(countshape)
    nb_of_shapes=countshape-2
    return nb_of_shapes




    # Replace pass above with your code


def max_number_of_spikes(nb_of_shapes):
    spikelist=[]
    templist = []

    for shape in range(2, nb_of_shapes + 3):
        for i in range(dim):
            for j in range(dim):
                if grid[i][j] == shape:
                    templist.append((i, j))
        spike=find_neighbor(shape,templist)
        spikelist.append(spike)
        templist = []

    maxspike=max(spikelist)
    return maxspike


    # Replace pass above with your code
def find_neighbor(shape,templist):
    spike = 0

    for dot in templist:
        tempi, tempj = dot
        neighborlist=[]
        for a, b in movelist:
            if 0 <= tempi + a < dim and 0 <= tempj + b < dim and grid[tempi + a][tempj + b] == shape:
                neighborlist.append((tempi+a,tempj+b))
        if len(neighborlist) == 1:
            spike += 1
    if len(templist)==1:
        spike+=1
    return spike

# Possibly define other functions here
def find_shape(i,j,shapelist):

    if 0<=i<dim and 0<=j<dim:
        shapelist.append((i,j))
        for a,b in movelist:
            if 0<=i+a<dim and 0<=j+b<dim and (i+a,j+b) not in shapelist and grid[i+a][j+b]==1:
                find_shape(i+a,j+b,shapelist)
    else:

        return shapelist

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
display_grid()
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )




