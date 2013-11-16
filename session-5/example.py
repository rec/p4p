def one():
  return 'one'

def two(x):
  return 'two %s' % x

def three(name='tom', food='chips', drink='beer'):
  return '%s loves %s and %s.' % (name, food, drink)

def four(**kwds):
  return '{name} loves {food} and {drink}'.format(kwds)

def five(name, *args):
  return '%s loves %s' % (name, ' '.join(args))

def six(name, rank='toilet cleaner', *args, **kwds):
  return '%s is a %s: %s, %s' % (name, rank, args, kwds)

