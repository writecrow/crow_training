#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk
import os
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import BlanklineTokenizer
from nltk.tokenize import regexp_tokenize, wordpunct_tokenize
from nltk.tokenize import blankline_tokenize

words = open('text1.txt', 'r')
text = words.read()

# Example 1
# Standard tokenization of a text using word_tokenize()
tokens = nltk.word_tokenize(text)
print(tokens)

# Example 2
# A simple sentence tokenizer. Uses the regular expression '.(s+|$)',
# which means, look for a period, followed by a space,
# and use that as the delimiter.
tokens = nltk.regexp_tokenize(text, pattern=r'\.(\s+|$)', gaps=True)
# print(*tokens, sep='\n')

# Example 3
# A slightly smarter sentence tokenizer. The regular expression used means
# 'Look for a period, exclamation point, question mark, or semicolon,
# followed by a space, and use that as the delimiter.'
tokens = nltk.regexp_tokenize(text, pattern=r'[\.!?;](\s+|$)', gaps=True)
# print(*tokens, sep='\n')

# Example 4
# Split text with spaces only, preserving punctuation:
tokenizer = RegexpTokenizer(r'\s+', gaps=True)
tokens = tokenizer.tokenize(text)
# print(*tokens, sep='\n')

# Example 5
# Retrieve all capitalized words using a regular expression
capword_tokenizer = RegexpTokenizer(r'[A-Z]\w+')
tokens = capword_tokenizer.tokenize(text)
# print(*tokens, sep='\n')

# Example 6
# Example 4: Chunk text by paragraph breaks"
tokens = BlanklineTokenizer().tokenize(text)
# print(tokens)
