#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# DESCRIPTION: This script opens the file text.txt, splits it into
# sentences, calcalates average sentence length, and flags each
# instance of passive voice.
#
# Usage example:
#    python3 3_using_imports.py
#

import text_process

raw = text_process.open_file('text.txt')
sentences = text_process.split_into_sentences(raw)
print(text_process.average_sentence_length(sentences))
for sentence in sentences:
    if text_process.is_passive_sentence(sentence):
        print(sentence)
