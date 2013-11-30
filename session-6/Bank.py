from __future__ import absolute_import, division, print_function, unicode_literals

import Account

class BankAccount(Account.Account):
  def __init__(self, bank, amount=0, name='My'):
    super(BankAccount, self).__init__(amount, name)
    self.bank = bank
    self.bank += amount

  def deposit(self, amount):
    super(BankAccount, self).deposit(amount)
    self.bank.deposit(amount)


class Bank(Account.Account):
  def make_account(self, amount=0, name='Your'):
    return BankAccount(self, amount, name)
