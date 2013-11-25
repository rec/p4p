import text

def _read_syllables(fname):
  syllables = {}
  with open(fname) as f:
    for line in f:
      line = line.strip()
      if line:
        word, count = line.split()
        count = int(count)
        assert word not in syllables
        syllables[word] = count
  return syllables

_SYLLABLES_FILE = 'syllables.txt'
_SYLLABLES = _read_syllables(_SYLLABLES_FILE)

def line_syllables(line):
  return sum(_SYLLABLES.get(w, 1) for w in text.split_into_words(line))
