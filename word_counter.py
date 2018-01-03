import sys,re,collections,nltk
from collections import Counter, OrderedDict
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

lmtzr = WordNetLemmatizer()


class OrderedCounter(Counter, OrderedDict):
    '''Counter that remembers the order elements are first encountered'''

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


def get_known_words(file):
    stop_words = set(stopwords.words('english'))
    known_words = set()
    with open(file) as f:
        for line in f:
            known_words.add(line.strip()) 

    blacklist_words = known_words.union(stop_words)
    return blacklist_words


def get_words(file, known_words):
    with open (file) as f:
        words_box=[]
        for line in f:                           
            words = [w for w in nltk.regexp_tokenize(line, '[A-Za-z\']+') if not "'" in w]
            words_box.extend(merge(words, known_words))
    return OrderedCounter(words_box)  


def merge(words, known_words):
    new_words = []
    for word in words:
        tag = nltk.pos_tag(word_tokenize(word)) # tag is like [('bigger', 'JJR')]
        pos = get_wordnet_pos(tag[0][1])
        if pos:
            lemmatized_word = lmtzr.lemmatize(word, pos)
            if (lemmatized_word not in known_words) and (lemmatized_word.lower() not in known_words):
                new_words.append(lemmatized_word)
    return new_words


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif treebank_tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return nltk.corpus.wordnet.ADV
    else:
        return ''


def append_ext(words):
    new_words = []
    for item in words.items():
        word, count = item
        tag = nltk.pos_tag(word_tokenize(word))[0][1]
        new_words.append((word, count, tag))
    return new_words


def write_to_file(words, filename):
    f = open(filename, 'w')
    for item in words:
        for field in item:
            f.write(str(field)+',')
        f.write('\n')


if __name__=='__main__':
    """ 
    Usage: 
    python word_counter.py resources/Dune1_Chapter1.txt output/Dune_Chapter1_New_Word_Order_By_Word.txt resources/known_words_1_1230.txt WORD
    python word_counter.py resources/Dune1_Chapter1.txt output/Dune_Chapter1_New_Word_Order_By_Count.txt resources/known_words_1_1230.txt COUNT
    """
    book = sys.argv[1]
    word_count_result_file = sys.argv[2]
    known_words_file = sys.argv[3]
    order_type = sys.argv[4]
    known_words = get_known_words(known_words_file)
    print "counting..."
    words = get_words(book, known_words)
    print "writing file..."
    if order_type == "COUNT":
        write_to_file(append_ext(OrderedDict(words.most_common())), word_count_result_file)
    elif order_type == "WORD":
        write_to_file(append_ext(OrderedDict(words)), word_count_result_file)
