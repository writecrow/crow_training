import re
text = open('text.txt','r')
raw = text.read()
sentences = re.split(r' *[\.\?!][\'"\)\]]*', raw + ' ')
print(sentences)
words = []
for sentence in sentences:
    if len(sentence.split()) > 0:
        words = words + [len(sentence.split())]
average = sum(words)/len(sentences)
print(average)
VERBS = ['is', 'was', 'were', 'be', 'being', 'been', 'having']
passive = []
for sentence in sentences:
    words = sentence.split()
    if len(words) > 0:    
        match = bool(set(VERBS) & set(words))
        if match:
            previous_is_helper_verb = False
            for word in words:
                current_is_past_tense = word[-2:] == 'ed'
                if previous_is_helper_verb and current_is_past_tense:
                    passive = passive + [sentence]
                if word in VERBS:
                    previous_is_helper_verb = True
                else:
                    previous_is_helper_verb = False
print(passive)