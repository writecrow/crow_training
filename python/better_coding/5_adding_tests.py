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

output = ''

sentence1 = "This is a sentence that does not contain passive voice"
if is_passive_sentence(sentence1) != False:
  output = 'The test for sentence 1 failed'

sentence2 = "This is a sentence that is defined by passive voice"
if is_passive_sentence(sentence2) != True:
  output = 'The test for sentence 2 failed'

sentence3 = "This was created to be a sentence that is defined by passive voice"
if is_passive_sentence(sentence3) != True:
  output = 'The test for sentence 3 failed'

if output == '':
  print('All tests passed. Woohoo!')
else:
  print(output)