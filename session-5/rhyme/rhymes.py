import text

def _read_rhyme_dictionary(fname):
  rhymes = {}
  with open(fname) as f:
    for line in f:
      line = line.strip()
      if line:
        words = set(text.split(line))
        for w in words:
          assert w not in rhymes
          rhymes[w] = words
  return rhymes

_RHYME_FILE = 'rhymes.txt'
RHYMES = _read_rhyme_dictionary(_RHYME_FILE)

def words_rhyme(w1, w2):
  return w1 in RHYMES.get(w2, [])

def lines_rhyme(l1, l2):
  return words_rhyme(text.last(l1), text.last(l2))
