# COMP9021 21T3 - Rachid Hamadi
# Quiz 2 *** Due Friday Week 4 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Monday Week 5 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE
startcode='0' * nb_of_leading_zeroes + f'{int(code):o}'
startcode=startcode[::-1]

coordinate={'7':(-1,1),'0':(0,1),'1':(1,1),
            '6':(-1,0),'xx':(0,0),'2':(1,0),
            '5':(-1,-1),'4':(0,-1),'3':(1,-1),}

curr_status={(0,0),0}
curr_position=[(0,0)]
x_axis=0
y_axis=0
for i in startcode:
    x_axis+=coordinate[i][0]
    y_axis+=coordinate[i][1]
    if(x_axis,y_axis) in curr_position:
        curr_position.remove((x_axis,y_axis))
    else:
        curr_position.append((x_axis,y_axis))




if curr_position!=[]:
    west_line = 0  # initialise boundary
    east_line = -1
    north_line = -1
    south_line = 0

    for i in curr_position:  # find boundary
        curr_x, curr_y = i
        if west_line > curr_x:
            west_line = curr_x
        if east_line < curr_x:
            east_line = curr_x
        if north_line < curr_y:
            north_line = curr_y
        if south_line > curr_y:
            south_line = curr_y


    output = ''
    for j in range(north_line, south_line - 1, -1):
        for k in range(west_line, east_line + 1, 1):
            if (k, j) in curr_position:
                output += on
            else:
                output += off

        if south_line < j:
            output += '\n'
    print(output)