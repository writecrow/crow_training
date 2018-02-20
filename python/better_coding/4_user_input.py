#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# DESCRIPTION: This script opens a file provided by the user,
# splits it into sentences, calcalates average sentence length,
# and flags each instance of passive voice.
#
# Usage example:
#    python3 4_user_input.py
#

import text_process

print("This script identifies passive voice sentences in a given text file.")
filename = input("Provide a filename to analyse:  ")
raw = text_process.open_file(filename)
sentences = text_process.split_into_sentences(raw)
print(text_process.average_sentence_length(sentences))
for sentence in sentences:
    if text_process.is_passive_sentence(sentence):
        print(sentence)
