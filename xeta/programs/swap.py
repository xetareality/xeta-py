from xeta.modules import transaction, pool
from xeta.config import config
from xeta.library import models
import json


class Swap():
    """
    Swap pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, tx):
        """
        Transfer to swap pool
        """
        models.required_fields(tx, ['amount', 'token'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': tx['token'],
            'amount': tx['amount'],
            'function': 'swap.transfer',
        }})

    def deposit(self, tx, expires=None, unlocks=None):
        """
        Deposit to swap pool
        """
        models.required_fields(tx, ['amount', 'token'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': tx['token'],
            'amount': tx['amount'],
            'function': 'swap.deposit',
            'message': json.dumps({'expires': expires, 'unlocks': unlocks}) if expires or unlocks else None,
        }})

    def supply(self):
        """
        Supply to swap pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'swap.supply',
        }})

    def withdraw(self, percentage=1.0):
        """
        Withdraw from swap pool
        """
        assert percentage <= 1, 'input: percentage must between zero and one'

        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'swap.withdraw',
            'message': json.dumps({'percentage': percentage})
        }})