import text_process

raw = text_process.open_file('text.txt')
sentences = text_process.split_into_sentences(raw)
print(text_process.average_sentence_length(sentences))
for sentence in sentences:
    if text_process.is_passive_sentence(sentence) == True:
        print(sentence)
