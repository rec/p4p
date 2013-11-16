import text

def _read_rhymes(fname):
  rhymes = []
  with open(fname) as f:
    for line in f:
      line = line.strip()
      if line:
        rhymes.append(set(text.split(line)))
  return rhymes

_RHYME_FILE = 'rhymes.txt'
RHYMES = _read_rhymes(_RHYME_FILE)

def words_rhyme(w1, w2):
  for rhyme_set in RHYMES:
    if w1 in rhyme_set:
      return w2 in rhyme_set
    elif w2 in rhyme_set:
      return False
  return False

def lines_rhyme(l1, l2):
  return words_rhyme(text.last(l1), text.last(l2))
