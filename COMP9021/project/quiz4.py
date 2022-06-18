# COMP9021 21T3 - Rachid Hamadi
# Quiz 4 *** Due Friday Week 7 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Monday Week 8 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a strictly positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys
import time


def encode(list_of_integers):
    decimal_num = 0
    encodelist = []
    str = '0'
    joinnum = ''
    finalnum = 0
    temp = []
    str1 = ''
    for i in list_of_integers:
        decimal_num = bin(i)[2:]
        encodelist.append(decimal_num)
    for element in encodelist:
        for j in element:
            k = j + j
            j = k
            str1 += j
        temp.append(str1)
        str1 = ''
    joinnum = str.join(temp)
    finalnum = int(joinnum, 2)
    return finalnum

def decode(integer):
    finalbinlist = []
    str2 = ''
    count = 0
    decodelist = list(bin(integer)[2:])
    while count < len(decodelist):
        if count + 1 <= len(decodelist) and len(decodelist) != 1:
            if decodelist[count] == decodelist[count + 1]:
                str2 += decodelist[count]
                count += 2
            elif decodelist[count] == '0':
                finalbinlist.append(int(str2, 2))
                str2 = ''
                count += 1
            else:
                return None
                break
        else:
            return None
    finalbinlist.append(int(str2, 2))
    return finalbinlist


time.sleep(1)
# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))