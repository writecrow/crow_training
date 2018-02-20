# -*- coding: utf-8 -*-
"""Passive Voice Analyser

This module opens a given text file and performs the following:
- prints sentences individually
- calculates average words per sentence
- prints any sentences determined to contain passive voice

Example:
    Run the script like this

        $ python 5_script_argument.py --file=text.txt

"""
import argparse
import os
import text_process

# Define the way we retrieve arguments sent to the script.
parser = argparse.ArgumentParser(description='Passive Voice Analyser')
parser.add_argument('--file', action="store", dest='file', default='')
args = parser.parse_args()

# Check if there is a file argument passed, and if the file exists
if args.file and os.path.isfile(args.file):
    # Open the text.
    raw = text_process.open_file(args.file)
    # Find all sentences.
    sentences = text_process.split_into_sentences(raw)
    # Find average sentence length.
    print(text_process.average_sentence_length(sentences))
    for sentence in sentences:
        # Print any sentences determined to be passive voice.
        if text_process.is_passive_sentence(sentence):
            print(sentence)
