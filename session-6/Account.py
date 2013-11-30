class Account(object):
  def __init__(self, balance=0, name='Your'):
    self.balance = balance
    self.name = name

  def deposit(self, amount):
    self.balance += amount

  def is_overdrawn(self):
    return self.balance < 0

  def __iadd__(self, amount):
    self.deposit(amount)
    return self

  def __str__(self):
    return '%s balance is %.2f' % (self.name, self.balance)

  def __repr__(self):
    return 'BankAccount(%.2f)' % self.balance

