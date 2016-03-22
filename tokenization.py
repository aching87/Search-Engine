## functions to tokenize documents
def removePunctuation( s ):
    'remove punctuation from s'
    p = '#*&()!-_,.:;!?"\'\n'
    for symbol in p:
        s = s.replace(symbol, ' ')
    return s

def removestopwords(textWithStopWords):
    infile=open('stopwords.txt') # list of stopwords extracted from http://www.lextek.com/manuals/onix/stopwords1.html
    content=infile.read()
    stopwords=content.split()
    text = ' '.join([word for word in textWithStopWords.split() if word not in stopwords])
    return text

from nltk import PorterStemmer

def stemwords(text):
    stemmedwords=[]
    for word in text.split():
        stemmedword=PorterStemmer().stem_word(word)
        stemmedwords.append(stemmedword)
    return stemmedwords
