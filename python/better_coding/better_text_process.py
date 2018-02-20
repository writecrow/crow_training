#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# DESCRIPTION: Helper file that includes functions to
# open a file,
# splits it into sentences,
# calculate average sentence length,
# and flag each instance of passive voice.
#
# Usage example:
#    import better_text_process
#
#    better_text_process.split_into_sentences(raw)

import re


def open_file(filename: str):
    """ Simple function to open a file """
    text = open(filename, 'r')
    return text.read()


def split_into_sentences(raw: str):
    # Split a given string of text at period, question mark,
    # or exclamation point.
    return re.split(r' *[\.\?!][\'"\)\]]*', raw + ' ')


def average_sentence_length(sentences: list):
    # Calculate average sentence length
    # (total words divided by number of sentences)
    lengths = []
    for sentence in sentences:
        if len(sentence.split()) > 0:
            lengths = lengths + [len(sentence.split())]
    return sum(lengths)/len(lengths)


def get_irregular_verbs():
    verbs = []
    for line in open("irregular_passive.txt", "r").readlines():
        line = line.replace("\r", "")
        line = line.replace("\n", "")
        verbs.append(line)
    return verbs


def is_passive_sentence(sentence: str):
    """ Passive Voice Analysis """
    # 1. Define verbs that are used in passive voice constructions.
    VERBS = ['is', 'was', 'were', 'be', 'being', 'been', 'have']
    passive = False
    words = sentence.split()
    if len(words) > 0:
        IRREGULAR = get_irregular_verbs()
        # Perform a simple check if the sentence contains a passive verb.
        # If it doesn't, there's no reason to check further.
        match = bool(set(VERBS) & set(words))
        if match:
            verb = False
            # 3. Move sequentially through each of the words in the sentence.
            # We record if a word is a passive verb, and then check if the
            # subsequent word is in past tense.
            for word in words:
                past_tense = word[-2:] == 'ed' or bool(word in set(IRREGULAR))
                if verb and past_tense:
                    passive = True
                    break
                elif word in VERBS:
                    verb = True
                else:
                    verb = False
    # Return True or False
    return passive
