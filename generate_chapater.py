import os
import re
import sys
#coding:utf-8

def get_words(file, known_words):
    with open (file) as f:
        i = 0
        words_box=[]
        for line in f:                           
            words = [w for w in nltk.regexp_tokenize(line, '[A-Za-z\']+') if not "'" in w]
            words_box.extend(merge(words, known_words))
            if i % 100 == 0:
                print "line %d done..." % i
            i += 1
    return OrderedCounter(words_box)  



if __name__=='__main__':
    """ 
    Usage: 
    """
    inbook = sys.argv[1]
    with open(inbook) as f:
        i = 1
        for line in f:
            if line.find("= = =") != -1:
                print("\n\n==============================")
                print("Chapter {}".format(i))
                i += 1
            else:
                print line.strip()
