PUNCTUATION = '.,;:!?'

def split(sentence):
  return [s.strip(PUNCTUATION).lower() for s in sentence.split()]

def last(sentence):
  return split(sentence)[-1]

