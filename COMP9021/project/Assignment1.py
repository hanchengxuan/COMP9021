# COMP9021 21T3
# Assignment 1 *** Due Monday 25 October (Week 7) @ 9.00am

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
import sys



def please_convert():
    get_input=input('How can I help you? ').split()
    if len(get_input)==3 and get_input[0]=='Please' and get_input[1]=='convert':
        n = get_input[2]
        if n.isdigit() and int(n)>0 and int(n)<=3999 and n.startswith('0',0)==False:
            print(f"Sure! It is {convert_int_to_roman(n)}")
        elif n.isalpha():
            print(f"Sure! It is {convert_roman_to_int(n)}")
        else:
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
    elif len(get_input)==5 and get_input[0]=='Please' and get_input[1]=='convert' and get_input[3]=='using' :
        n=get_input[2]
        n1=get_input[4]
        if n.isdigit() and int(n)>0 and n.startswith('0',0)==False and distinct_input(n1) == True:
            print(f"Sure! It is {convert_num_using(n,n1)}")
        elif n.isalpha() and distinct_input(n1) == True:
            print(f"Sure! It is {convert_alpha_using(n,n1)}")
        else:
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
    elif len(get_input)==4 and get_input[0]=='Please' and get_input[1]=='convert' and get_input[3]=='minimally':
        n=get_input[2]
        if n.isalpha():
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
        else:
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
    else:
        print("I don't get what you want, sorry mate!")
        sys.exit()

def distinct_input(alphabet):
    list1=list(alphabet)
    n=len(list1)
    for i in range(n):
        if alphabet.count(list1[i])>1:
            return False
            break
    return True

def create_char(string,int):
    a,b,c=string[::-1]
    diy_alphabet={int:['',a,a+a,a+a+a,a+b,b,b+a,b+a+a,b+a+a+a,a+c]}
    return diy_alphabet

def convert_int_to_roman(num):
    i1 = create_char("XVI", 0)
    i2 = create_char("CLX", 1)
    i3 = create_char("MDC", 2)
    i4 = create_char("__M", 3)
    list = [i1, i2, i3, i4]
    roman_alphabet = {}
    for n in list:
        roman_alphabet = {**roman_alphabet, **n}

    num1 = int(num)
    roman = []
    for k in range(4):
        if k != 0:
            roman.append(roman_alphabet[k][num1 // 10 ** k % 10])
        else:
            roman.append(roman_alphabet[0][num1 % 10])
    # roman.append(roman_alphabet[3][num1 // 1000 % 10])
    # roman.append(roman_alphabet[2][num1 // 100 % 10])
    # roman.append(roman_alphabet[1][num1 // 10 % 10])
    # roman.append(roman_alphabet[0][num1 % 10])
    s = ''
    for i in roman[::-1]:
        s += i
    return s

def convert_roman_to_int(rom):
    i1 = create_char("XVI", 0)
    i2 = create_char("CLX", 1)
    i3 = create_char("MDC", 2)
    i4 = create_char("__M", 3)
    total_list = [i1, i2, i3, i4]
    roman_alphabet = {}
    for n in total_list:
        roman_alphabet = {**roman_alphabet, **n}

    checkprev = ''
    sum2=0
    key=3
    count=0
    for i in rom:
        checkcurrent = i
        link = checkprev + checkcurrent
        count += 1
        if link in roman_alphabet[key]:
            checkprev = link
            if count == len(rom):
                index_link = roman_alphabet[key].index(link)
                sum2 += index_link * (10 ** key)
        else:
            index_prev = roman_alphabet[key].index(checkprev)
            checkprev = checkcurrent
            sum2 += index_prev * (10 ** key)
            if key==0 and count==len(rom):
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
            while checkprev not in roman_alphabet[key]:
                key -= 1
                if key < 0:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
                elif checkprev in roman_alphabet[key] and count == len(rom):
                    index_prev2 = roman_alphabet[key].index(checkprev)
                    sum2 += index_prev2 * (10 ** key)
    return sum2

def convert_num_using(num,alphabet):
    generalised_roman_alphabet = {}
    total_list = []
    count = 0
    alphabet1 = list(alphabet)
    while alphabet1 != []:
        while len(alphabet1) < 3:
            alphabet1.insert(0, '_')
        convert_list = alphabet1[-3:]
        temp_str = ''
        convert_str = temp_str.join(convert_list)
        new_alphabet = create_char(convert_str, count)
        total_list.append(new_alphabet)
        if len(alphabet1) == 3 and '_' in alphabet1:
            alphabet1 = []
        alphabet1 = alphabet1[0:-2]
        for n in total_list:
            generalised_roman_alphabet = {**generalised_roman_alphabet, **n}
        count += 1

    num1 = int(num)
    converted_num = []
    for i in range(count):
        if count != 0:
            converted_num.append(generalised_roman_alphabet[i][num1 // 10**i % 10])
        else:
            converted_num.append(generalised_roman_alphabet[0][num1 % 10])
    s = ''
    for m in converted_num[::-1]:
        s += m
    return s

def convert_alpha_using(alpha, alphabet):
    generalised_roman_alphabet = {}
    total_list = []
    count = 0
    alphabet1 = list(alphabet)
    while alphabet1 != []:
        while len(alphabet1) < 3:
            alphabet1.insert(0, '_')
        convert_list = alphabet1[-3:]
        temp_str = ''
        convert_str = temp_str.join(convert_list)
        new_alphabet = create_char(convert_str, count)
        total_list.append(new_alphabet)
        if len(alphabet1) == 3 and '_' in alphabet1:
            alphabet1 = []
        alphabet1 = alphabet1[0:-2]
        for n in total_list:
            generalised_roman_alphabet = {**generalised_roman_alphabet, **n}
        count += 1


    checkprev = ''
    sum2 = 0
    key = count-1
    count1 = 0
    while key > 0:
        for anyalpha in alpha:
            if anyalpha == generalised_roman_alphabet[key][5]:
                if alpha.count(anyalpha)>1:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
        key-=1
    key = count - 1
    for i in alpha:
        checkcurrent = i
        link = checkprev + checkcurrent
        count1 += 1
        if link in generalised_roman_alphabet[key]:
            checkprev = link
            if count1 == len(alpha):
                index_link = generalised_roman_alphabet[key].index(link)
                sum2 += index_link * (10 ** key)
        else:
            index_prev = generalised_roman_alphabet[key].index(checkprev)
            checkprev = checkcurrent
            sum2 += index_prev * (10 ** key)
            if key == 0 and count1 == len(alpha):
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
            while checkprev not in generalised_roman_alphabet[key]:
                key -= 1
                if key < 0:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
                elif checkprev in generalised_roman_alphabet[key] and count1 == len(alpha):
                    index_prev2 = generalised_roman_alphabet[key].index(checkprev)
                    sum2 += index_prev2 * (10 ** key)
    return sum2

# def generalised_alphabet(alpha):
#
# def convert_minimally(alpha):






    # EDIT AND COMPLETE THE CODE ABOVE


# DEFINE OTHER FUNCTIONS

please_convert()