# COMP9021 21T3 - Rachid Hamadi
# Quiz 3 *** Due Friday Week 5 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Monday Week 6 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends and
#   around parentheses and commas, is a valid word.


import sys
import time
def addlist(str,list):
    if str != '':
        list.append(str)
    str = ''
    return str,list

def is_valid(word, arity):
    j = 0
    k = 0
    replaced_word = word.replace(" ", '')

    size=len(replaced_word)
    for i in range(size):
        if replaced_word[i].isalpha() == False and replaced_word[i] not in ['(', ')', ',', '_']:
            return False
    for any_word in replaced_word:
        if any_word == '(':
            j += 1
        if any_word == ')':
            k += 1
    if j != k:
        return False
    if arity == 0 and j != 0:
        return False
    if arity != 0 and j == 0:
        return False

    test_list = []
    pop_item = ''
    signlist = ['(', ',', ')']
    for i in replaced_word:
        if i not in signlist:
            pop_item = pop_item+i
        elif i == signlist[0]:

            pop_item,test_list=addlist(pop_item,test_list)
            test_list.append(i)
        elif i == signlist[1]:
            pop_item, test_list = addlist(pop_item, test_list)
        elif i == signlist[2]:
            pop_item,test_list=addlist(pop_item,test_list)
            str1 = []
            num = arity+1
            for i in range(num):
                if test_list:
                    str1 += test_list.pop()
                else:
                    return False
            if str1[-1] != '(':
                return False
    return True



    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
time.sleep(1)
try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')
