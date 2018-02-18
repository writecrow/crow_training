import re

def open_file(filename):
  text = open(filename,'r')
  return text.read()

def split_into_sentences(raw):
  return re.split(r' *[\.\?!][\'"\)\]]*', raw + ' ')

def average_sentence_length(sentences):
  lengths = []
  for sentence in sentences:
    if len(sentence.split()) > 0:
      lengths = lengths + [len(sentence.split())]
  return sum(lengths)/len(lengths)
  
def is_passive_sentence(sentence):
  VERBS = ['is', 'was', 'were', 'be', 'being', 'been', 'have']
  passive = False
  words = sentence.split()
  if len(words) > 0:
    match = bool(set(VERBS) & set(words))
    if match:
      verb = False
      for word in words:
        past_tense = word[-2:] == 'ed'
        if verb and past_tense:
          passive = True
          break
        elif word in VERBS:
          verb = True
        else:
          verb = False
  return passive