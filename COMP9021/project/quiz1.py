# COMP9021 21T3
# Quiz 1 *** Due Friday Week 3 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Monday Week 4 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE
process_cycles=[]
process_keys=set(keys)
def check_keys_is_cycles(k):
    if k ==process_cycles[0]:
        return 1
    else:
        return 0

def find_cycles(k1):
    k2=0
    for k1 in keys:
        k2=k1
        if k2 in process_keys:
            while k2 in process_keys:
                process_cycles.append(k2)
                process_keys.remove(k2)
                k2 = mapping[k2]
            if check_keys_is_cycles(k2) == 1:
                cycles1 = sorted(process_cycles)
                cycles.append(cycles1)
                process_cycles.clear()
            else:
                for n in process_cycles:
                    process_keys.add(n)
                process_cycles.clear()

mapping2={}
mapping3={}
length=[]
for key,value in mapping.items():
    if value in mapping2:
        mapping2[value].append(key)
    else:
        mapping2[value]=[key]

def sort_by_length():
    for key,value in mapping2.items():
      len1=len(value)
      if len1 not in length:
          length.append(len1)

sort_by_length()

length2=sorted(length)


for i in length2:
    for key,value in mapping2.items():
        key3 = []
        key3.append(key)

        for key2 in key3:
            len3 = len(mapping2[key2])

            if len3 == i:
                mapping3[key2] = mapping2[key2]

        reversed_dict_per_length[i] = mapping3
    mapping3={}

for any_key in keys:
    find_cycles(any_key)

print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)
