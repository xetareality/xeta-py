from xeta.modules import transaction, pool
from xeta.library.config import config
from xeta.library import models, utils
import json


def create(**values):
    """
    Create lending pool
    """
    models.required_fields(values, ['token'])
    models.valid_formats(values, models.POOL)
    return pool.create(**{**values, **{'program': 'lending'}})

class Lock():
    """
    Lock pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, tx={}):
        """
        Transfer to lending pool
        """
        return transaction.create({**tx, **{
            'to': self.pool['address'],
            'token': self.pool['token'],
            'amount': amount,
            'function': 'lending.transfer',
        }})

    def claim(self, tx={}):
        """
        Claim from lending pool
        """
        return transaction.create({**tx, **{
            'to': self.pool['address'],
            'function': 'lending.claim',
        }})

    def resolve(self, tx={}):
        """
        Resolve lending pool
        """
        return transaction.create({**tx, **{
            'to': self.pool['address'],
            'function': 'lending.resolve',
        }})

    def deposit(self, amount, tx={}):
        """
        Deposit to lending pool
        """
        return transaction.create({**tx, **{
            'to': self.pool['address'],
            'token': self.pool['token'],
            'amount': amount,
            'function': 'lending.deposit',
        }})

    def withdraw(self, tx={}):
        """
        Withdraw from lending pool
        """
        return transaction.create({**tx, **{
            'to': self.pool['address'],
            'function': 'lending.withdraw',
        }})