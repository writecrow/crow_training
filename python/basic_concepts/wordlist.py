#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

original = "The quick brown fox jumped over the lazy gray dog."
stopwords = ('a', 'the', 'over')
alphanumeric = re.sub(r'\W+', ' ', original)
# Remove spaces from start & end, lowercase, then put all words in a list
words = alphanumeric.strip().lower().split(' ')
nonStopwords = []
frequency = {}
for word in words:
    frequency.setdefault(word, 0)
    frequency[word] += 1
    if word not in stopwords:
        nonStopwords.append(word)
print("Total words:", len(words))
print(frequency)
print("Non stopwords:", len(nonStopwords))
print(nonStopwords)
