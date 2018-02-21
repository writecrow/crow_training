#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This demonstrates retrieving text from a remote URL using the `urllib` library
In this case, we request the writecrow.org homepage.
'''

import nltk
import os

text1 = open('text1.txt', 'r')
raw = text1.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
len(tokens)
print(text.collocations())
