## Crow Training Materials
This is a general-purpose repository for learning the central concepts and main tools used by the Corpus and Repository of Writing team for text processing.

### Command Line
This directory includes example scripts written in `bash`, primarily demonstrating how scripts written in various computer programming languages can be chained together to perform a series of steps on given texts.

### Python
1. `basic_concepts` includes scripts that use the simplest python commands to open a given text file, tokenize the words, and perform computational analysis like identifying average sentence length and finding sentences containing passive voice.
2. `better_coding` builds on many of the other lessons in this section to introduce ways to make your code:
* more readable through use of comments and adherence to PEP8 standards
* more re-usable through use of functions and imports
* more user-friendly by using parameters instead of hardcoded values
* more reliable by integrating tests
3. `conversion` focuses on methods to manipulating text input, including:
* conversion from Word or PDF formats to plaintext
* conversion into UTF-8 format
4. `natural_language_toolkit` includes code snippets that illustrate using the Natural Language Toolkit ([https://nltk.org](https://nltk.org)), including:
* tokenization
* text cleaning
* collocations
5. `regex` provides sample code snippets for various methods of complex parsing of texts, including:
* Finding a "header" value in markup like `<Program: XXX>`
* Finding all header values and putting into a manipulable list
* Finding all matches of phrases like "were xxx by" or "was xxx by"
6. `remote_data` demonstrates basic methods for retrieving content from non-local files

## Sandbox
This is a directory to be used for simply trying out coding ideas, and using Git in order
to keep track of that code. One of the team scaffolding assignments is to create an issue
in this repository, create a branch that adds a file to this "Sandbox" directory, and open
that as a "pull request" for team review.