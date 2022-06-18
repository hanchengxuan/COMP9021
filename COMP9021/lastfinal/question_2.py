
# Takes two strings (words) as arguments and checks
# that both consist of nothing but uppercase letters.
#
# If that is the case,
# - displays the first word horizontally,
# - displays the second word vertically,
# - displays 0 at the intersection of a row and a column
#   where the letters are different,
# - displays i at the intersection of a row and a column
#   where the letters are the same and this happens for
#   the i-th time,
#   - processing the first row from left to right,
#   - processing the second row from right to left,
#   - processing the third row from left to right,
#   - processing the fourth row from right to left,
#   - ...
# The number of digits in the maximum number i determines
# the width of columns as shown in the sample tests.
#
# You can assume that both arguments are strings.


def f(word_1, word_2):
    '''
    >>> f('AB', 'C2D')
    Both arguments should consist of nothing but uppercase letters.
    >>> f('Aa', 'BB')
    Both arguments should consist of nothing but uppercase letters.
    >>> f('AB', '')
    >>> f('AB', 'CD')
      A B
    C 0 0
    D 0 0
    >>> f('AA', 'A')
      A A
    A 1 2
    >>> f('AAA', 'AAAA')
       A  A  A
    A  1  2  3
    A  6  5  4
    A  7  8  9
    A 12 11 10
    >>> f('AAAAAAAAAAAAAAA', 'AAAAAAAA')
        A   A   A   A   A   A   A   A   A   A   A   A   A   A   A
    A   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
    A  30  29  28  27  26  25  24  23  22  21  20  19  18  17  16
    A  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45
    A  60  59  58  57  56  55  54  53  52  51  50  49  48  47  46
    A  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75
    A  90  89  88  87  86  85  84  83  82  81  80  79  78  77  76
    A  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105
    A 120 119 118 117 116 115 114 113 112 111 110 109 108 107 106
    >>> f('ABC', 'BCD')
      A B C
    B 0 1 0
    C 0 0 2
    D 0 0 0
    >>> f('ABBC', 'BCDECB')
      A B B C
    B 0 1 2 0
    C 0 0 0 3
    D 0 0 0 0
    E 0 0 0 0
    C 0 0 0 4
    B 0 6 5 0
    >>> f('ABABCDCD', 'ABDEABDE')
       A  B  A  B  C  D  C  D
    A  1  0  2  0  0  0  0  0
    B  0  4  0  3  0  0  0  0
    D  0  0  0  0  0  5  0  6
    E  0  0  0  0  0  0  0  0
    A  7  0  8  0  0  0  0  0
    B  0 10  0  9  0  0  0  0
    D  0  0  0  0  0 11  0 12
    E  0  0  0  0  0  0  0  0
    '''
    # INSERT YOUR CODE HERE        
    cdt = False
    if word_2 and word_1:
        for i in word_1:
            if 65 <= ord(i) <= 90:
                pass
            else:
                cdt = True
        for i in word_2:
            if 65 <= ord(i) <= 90:
                pass
            else:
                cdt = True
        if cdt:
            print('Both arguments should consist of nothing but uppercase letters.')
        else:
            a = list(word_1)
            b = list(word_2)
            c = 0
            final = []
            for i in b:
                for j in a:
                    if i == j:
                        c += 1
            sp = len(str(c))
            print(' ', end='')
            for i in a:
                print(' ' * sp + i, end='')
            print('\n', end='')
            d = 0
            for i in range(len(b)):
                print(b[i][0], end='')
                if i in range(0, len(b), 2):
                    for j in a:
                        if b[i] == j:
                            d += 1
                            ned = sp + 1 - len(str(d))
                            print(' ' * ned + str(d), end='')
                        else:
                            print(' ' * sp + '0', end='')
                else:
                    s = ''
                    for j in a[::-1]:
                        if b[i] == j:
                            d += 1
                            ned = sp + 1 - len(str(d))
                            s = ' ' * ned + str(d) + s
                        else:
                            s = ' ' * sp + '0' + s
                    print(s, end='')
                print('\n', end='')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
