#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# DESCRIPTION: This script opens the file text.txt, splits it into
# sentences, calcalates average sentence length, and flags each
# instance of passive voice.
#
# Usage example:
#    python3 1_with_comments.py
#

import re

text = open('text.txt', 'r')
raw = text.read()
# The following regular expression splits the text at period,
# question mark, or exclamation point. It is a simplistic
# sentence splitter that doesn't handle many scenarios.
sentences = re.split(r' *[\.\?!][\'"\)\]]*', raw + ' ')
print(sentences)
words = []
for sentence in sentences:
    if len(sentence.split()) > 0:
        # A simple word counter; adds wordcount of each sentence
        words = words + [len(sentence.split())]
# Average sentence length = total word count/sentence count
average = sum(words)/len(sentences)
print(average)
# Define a list of helper verbs used to construct passive voice.
VERBS = ['is', 'was', 'were', 'be', 'being', 'been', 'have']
passive = []
# Loop through each sentence
for sentence in sentences:
    words = sentence.split()
    if len(words) > 0:
        # First check if the helper verb is in the sentence.
        # If not, no reason to probe further.
        match = bool(set(VERBS) & set(words))
        if match:
            previous_is_helper_verb = False
            # Loop through each word in the sentence,
            # logging if a words is a helper verb in the
            # variable previous_is_helper_verb
            for word in words:
                # Simple check to see if current word is past tense
                current_is_past_tense = word[-2:] == 'ed'
                # The below statement evaluates whether there is passive voice
                if previous_is_helper_verb and current_is_past_tense:
                    passive = passive + [sentence]
                if word in VERBS:
                    previous_is_helper_verb = True
                else:
                    previous_is_helper_verb = False
print(passive)
