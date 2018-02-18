#!/usr/bin/python3

import nltk
import os
#from nltk.tokenize import regexp_tokenize, wordpunct_tokenize, blankline_tokenize

text1 = open('text1.txt','r')
raw = text1.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
len(tokens)
print(text.collocations())