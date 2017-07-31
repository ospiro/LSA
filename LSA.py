import numpy as np
import sys
import codecs
from nltk import sent_tokenize,corpus
term_count = 1000
word_count = 1000
words = corpus.gutenberg.words('austen-emma.txt')
sentences = corpus.gutenberg.sents('austen-emma.txt')
print len(sentences)
print len(words)
#with codecs.open("fiveacre.txt",'r','utf-8-sig') as f:
#    sentences = sent_tokenize(f.read())[:term_count]
#    f.seek(0)
#    words = list(set(f.read().split()))
#for s in sentences:
#    if "women" in s:
#        print 'SENT:',s + '\n'
def create_row(w):
    row_vec = [0]*term_count
    for i in xrange(term_count):
       if w in sentences[i]:#.split():# or w in sentences[max(0,i-1)] or w in sentences[min(term_count-1,i+1)]:
            row_vec[i] = 1
    return row_vec
matrix = np.array(map)
np.save("counts",matrix)
#matrix = np.load("counts.npy")
word1=  words.index(sys.argv[1])
word2 =  words.index(sys.argv[2])
print np.sum((matrix[word1,:] + matrix[word2,:])==2)
freq1 = matrix[word1,:]/np.linalg.norm(matrix[word1,:])
freq2 = matrix[word2,:]/np.linalg.norm(matrix[word2,:])
print np.dot(freq1,freq2)
