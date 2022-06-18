# COMP9021 21T3 - Rachid Hamadi
# Final Exam Question 3

'''
You might find the ord() function useful.
'''


def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of nothing but lowercase letters.

    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwrstuvabcde')
    'rstuv'
    '''
    if not word:
        return word
    wordlist=list(word)
    result=[]
    finalresult=[]
    letter=''

    for i in range(len(wordlist)-1):
        if ord(wordlist[i])==ord(wordlist[i+1])-1:
            if wordlist[i] not in result:
                result.append(wordlist[i])
            if wordlist[i+1] not in result:
                result.append(wordlist[i+1])
            if i+1==len(wordlist)-1:
                finalresult.append(result)
        else:
            if result:
                finalresult.append(result)
            result=[]
    if not finalresult:
        finalresult.append(wordlist[0])
    maxlen=0
    for i in finalresult:
        if len(i)>maxlen:
            maxlen=len(i)
    for i in finalresult:
        if len(i)<maxlen:
            finalresult.pop(finalresult.index(i))
    for anyword in finalresult:
        if len(anyword)==maxlen:
            letter=''.join(anyword)
            return letter
    # REPLACE return WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
