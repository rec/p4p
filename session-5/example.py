def zero():
  return 'zero'


def one(x):
  return 'one %s' % x


def two_a(x, y):
  return 'two_a %s %s' % (x, y)

def two_b(*args):
  x, y = args
  return 'two_b %s %s' % (x, y)

def two_c(*args):
  return 'two_c %s %s' % args

def two_d(*args):
  return 'two_d %s' % args

def two_e(*args):
  return 'two_e %s' % list(args)


def three_a(*args):
  return ' '.join(args)

def three_b(first, *args):
  return 'first is: %s.  args are: %s' % (first, ' '.join(args))

def three_c(first, second, *args):
  return 'first: %s. second: %s. args: %s' % (first, second ' '.join(args))


def four_a(name='tom', food='chips', drink='beer'):
  return 'four_a: %s loves %s and %s.' % (name, food, drink)

def four_b(name, food, drink='beer'):
  return 'found_b: %s loves %s and %s.' % (name, food, drink)


def five_a(**kwds):
  return kwds

def five_b(**kwds):
  return '{name} loves {food} and {drink}'.format(kwds)


def six(name, rank='toilet cleaner', *args, **kwds):
  return '%s is a %s: %s, %s' % (name, rank, args, kwds)

