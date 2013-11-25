import rhymes
import syllables

_POEM_TYPES = {
  'limerick':  {
     'rhymes': (
       (0, 1),
       (2, 3),
       (1, 4),
      ),

      'syllables': (
        (8, 11),
        (8, 11),
        (5, 7),
        (5, 7),
        (8, 11),
      ),
    },

  'sonnet': {
    'rhymes': (
      (0, 2),
      (1, 3),
      (4, 6),
      (5, 7),
      (8, 10),
      (9, 11),
      (12, 13),
    ),

    'syllables': (
      (10, 10),
      (10, 10),
      (10, 10),
      (10, 10),
      (10, 10),
      (10, 10),
      (10, 10),
      (10, 10),
      (10, 10),
      (10, 10),
      (10, 10),
      (10, 10),
      (10, 10),
      (10, 10),
    ),
  },
}

def is_poem_type(poem, poem_type):
  rule = _POEM_TYPES[poem_type]
  if len(poem) != len(rule['syllables']):
    return 'Poem has %d lines, not %d' % (
      len(poem), len(rule['syllables']))

  for line1, line2 in rule['rhymes']:
    if not rhymes.lines_rhyme(poem[line1], poem[line2]):
      return "Lines %d and %d don't rhyme" % (line1, line2)

  for line_number, bounds in enumerate(rule['syllables']):
    least, most = bounds
    syllable_count = syllables.line_syllables(poem[line_number])
    if syllable_count < least:
      return 'Line %d has %d syllables, which is less than %d' % (
        line_number, syllable_count, least)

    if syllable_count > most:
      return 'Line %d has %d syllables, which is greater than %d' % (
        line_number, syllable_count, most)




