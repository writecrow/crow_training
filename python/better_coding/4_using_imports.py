from passive_voice_functions import open_file
from passive_voice_functions import split_into_sentences
from passive_voice_functions import average_sentence_length
from passive_voice_functions import is_passive_sentence

# The following is the only code we really need to think about now.
raw = open_file('text.txt')
sentences = split_into_sentences(raw)
print(average_sentence_length(sentences))
for sentence in sentences:
    if is_passive_sentence(sentence) == True:
        print(sentence)
