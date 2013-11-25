def zero():
  return 'zero'


def one(x):
  return 'one %s' % x


def two_1(x, y):
  return 'two_1 %s %s' % (x, y)

def two_2(*args):
  x, y = args
  return 'two_2 %s %s' % (x, y)

def two_3(*args):
  return 'two_3 %s %s' % args

def two_4(*args):
  return 'two_ %s' % args

def two_5(*args):
  return 'two_5 %s' % list(args)


def three_1(*args):
  return ' '.join(args)

def three_2(first, *args):
  return 'first is: %s.  args are: %s' % (first, ' '.join(args))

def three_2(first, second, *args):
  return 'first: %s. second: %s. args: %s' % (first, second ' '.join(args))


def three(name='tom', food='chips', drink='beer'):
  return '%s loves %s and %s.' % (name, food, drink)

def three2(name, food, drink='beer'):
  return '%s loves %s and %s.' % (name, food, drink)


def four(**kwds):
  return '{name} loves {food} and {drink}'.format(kwds)

def five(name, *args):
  return '%s loves %s' % (name, ' '.join(args))

def six(name, rank='toilet cleaner', *args, **kwds):
  return '%s is a %s: %s, %s' % (name, rank, args, kwds)

