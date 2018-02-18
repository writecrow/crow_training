import better_text_process

output = ''

sentence1 = "This is a sentence that does not contain passive voice"
if better_text_process.is_passive_sentence(sentence1) != False:
  output = 'The test for sentence 1 failed'

sentence2 = "This is a sentence that is defined by passive voice"
if better_text_process.is_passive_sentence(sentence2) != True:
  output = 'The test for sentence 2 failed'

sentence3 = "This was created to be a sentence that is defined by passive voice"
if better_text_process.is_passive_sentence(sentence3) != True:
  output = 'The test for sentence 3 failed'

sentence3 = "The class was held captive by the great presentation."
if better_text_process.is_passive_sentence(sentence3) != True:
  output = 'The test for sentence 4 failed'  

if output == '':
  print('All tests passed. Woohoo!')
else:
  print(output)