PUNCTUATION = '.,;:!?'

def split_into_words(sentence):
  return [s.strip(PUNCTUATION).lower() for s in sentence.split()]

def last_word(sentence):
  return split_into_words(sentence)[-1]

