from xeta.modules import transaction, pool
from xeta.config import config
from xeta.library import models


def create(values):
    """
    Create loot pool
    """
    models.required_fields(values, ['token'])
    models.valid_formats(values, models.POOL)
    return pool.create({**values, **{'program': 'loot'}})

class Loot():
    """
    Loot pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, tx):
        """
        Transfer to loot pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': self.pool['token'],
            'amount': tx['amount'],
            'function': 'loot.transfer',
        }})

    def deposit(self, tx):
        """
        Deposit nft to loot pool
        """
        models.required_fields(tx, ['token'])
        models.valid_formats(tx, models.TRANSACTION)

        assert tx.get('amount') in [None, 1], 'validation: amount must be empty or one'

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': tx['token'],
            'amount': 1,
            'function': 'loot.deposit',
        }})

    def withdraw(self, tx):
        """
        Withdraw nft from loot pool
        """
        models.required_fields(tx, ['token'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'token': tx['token'],
            'function': 'loot.withdraw',
        }})

    def clear(self):
        """
        Clear loot pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'loot.clear',
        }})