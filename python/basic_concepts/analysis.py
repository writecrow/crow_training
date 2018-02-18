import re

words = open('text.txt','r')
text = words.read()

# A very simplistic way, via regular expression
# This basically searches for a sentence marker (period, exclamation point)
# followed by a space and splits the text at that point
# This would not handle situations like "Mr. Smith"
# Compare to the much more complex https://stackoverflow.com/a/31505798
sentences = re.split(r' *[\.\?!][\'"\)\]]*\s *', text + ' ')
print(sentences)

# A very simplistic way to split text into sentences via tokenization
# token = ""
# tokens = []
# SENTENCEENDINGS = ( ".", "!", "?" )
# for i in range(0, len(text)):
#     if text[i] in SENTENCEENDINGS:
#             if len(token) > 0:
#                 tokens = tokens + [ token ]
#             tokens = tokens + [ text[i] ]
#             token = ""
#     else:
#         token = token + text[i]
# if len(token) > 0:
#     tokens = tokens + [ token ]
# print(tokens)

# Calculate average sentence length
lengths = []
for sentence in sentences:
    if len(sentence.split()) > 0:
        lengths = lengths + [len(sentence.split())]
average = sum(lengths)/len(lengths)
print(average)

# Simplistic way to find all sentences with "were * by" or "was * by"
constructions = []
for sentence in sentences:
    were = re.search(r' were\s(.*)\sby', sentence + ' ')
    was = re.search(r' was\s(.*)\sby', sentence + ' ')
    if was or were:
        constructions = constructions + [sentence]
print(constructions)
# What limitations does this method have?

# Simplistic way to find all passive voice constructions
VERBS = ['is', 'was', 'were', 'be', 'being', 'been', 'have']
passive = []
for sentence in sentences:
    words = sentence.split()
    if len(words) > 0:    
        match = bool(set(VERBS) & set(words))
        if match:
            found = False
            for word in words:
                past_tense = word[-2:] == 'ed'
                if found and past_tense:
                    passive = passive + [sentence]
                if word in VERBS:
                    found = True
                else:
                    found = False
print(passive)
# This doesn't account for irregular verbs (e.g., written)
# How would you improve the code to account for this?