# COMP9021 21T3 - Rachid Hamadi
# Final Exam Question 6

def statistics(filename):
    '''
    A text file, stored in the working directory, consists of sentences.
    A sentence consists of words, possibly directly followed by a comma,
    except for the last word which is directly followed by a full stop.
    Words are separated by spaces.

    >>> statistics('text_file_1.txt')
    There are 2 sentence(s).
    The shortest sentence has 31 word(s).
    The longest sentence has 34 word(s).
    The shortest word has 1 character(s).
    The longest word has 9 character(s).
    >>> statistics('text_file_2.txt')
    There are 4 sentence(s).
    The shortest sentence has 6 word(s).
    The longest sentence has 34 word(s).
    The shortest word has 1 character(s).
    The longest word has 12 character(s).
    >>> statistics('text_file_3.txt')
    There are 1 sentence(s).
    The shortest sentence has 30 word(s).
    The longest sentence has 30 word(s).
    The shortest word has 1 character(s).
    The longest word has 12 character(s).
    '''

    nb_of_sentences = 0
    length_of_shortest_word = 0
    length_of_longest_word = 0
    min_nb_of_words_in_sentences = 0
    max_nb_of_words_in_sentences = 0
    sentencelist=[]
    wordlist=[]
    allword=[]
    totalwordlist=[]
    sentenceword=[]
    count=0


    with open(filename) as file:
        data=file.read()
        data=data.rstrip()
        for i in data:
            if i=='.':
                nb_of_sentences+=1
        for i in data:
            if i!=',' and i!='\n' and i!=' ' and i!='.':
                wordlist.append(i)
            else:
                if wordlist:
                    allword.append(wordlist)
                    totalwordlist.append(wordlist)
                wordlist=[]
                if i=='.':
                    sentenceword.append(totalwordlist)
                    totalwordlist=[]
        min_nb_of_words_in_sentences = len(sentenceword[0])
        for anysentence in sentenceword:
            if len(anysentence)>max_nb_of_words_in_sentences:
                max_nb_of_words_in_sentences=len(anysentence)
            if len(anysentence)<min_nb_of_words_in_sentences:
                min_nb_of_words_in_sentences=len(anysentence)
        length_of_shortest_word=len(allword[0])
        for anyword in allword:
            if len(anyword)>length_of_longest_word:
                length_of_longest_word=len(anyword)
            if len(anyword)<length_of_shortest_word:
                length_of_shortest_word=len(anyword)


        # REPLACE pass ABOVE WITH YOUR CODE

    print('There are', nb_of_sentences, 'sentence(s).')
    print('The shortest sentence has', min_nb_of_words_in_sentences, 'word(s).')
    print('The longest sentence has', max_nb_of_words_in_sentences, 'word(s).')
    print('The shortest word has', length_of_shortest_word, 'character(s).')
    print('The longest word has', length_of_longest_word, 'character(s).')


if __name__ == '__main__':
    import doctest

    doctest.testmod()
