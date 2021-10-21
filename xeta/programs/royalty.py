from xeta.modules import transaction, pool
from xeta.config import config
from xeta.library import models
import json


def create(values):
    """
    Create royalty pool
    """
    models.required_fields(values, ['token'])
    models.valid_formats(values, models.POOL)
    return pool.create({**values, **{'program': 'royalty'}})

class Royalty():
    """
    Royalty pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self):
        """
        Transfer to royalty pool
        """
        return self.claim()

    def claim(self, tx):
        """
        Claim from royalty pool
        """
        models.required_fields(tx, ['token'])

        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'token': tx['token'],
            'function': 'royalty.claim',
        }})

    def deposit(self, tx, expires=None, unlocks=None):
        """
        Deposit to royalty pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': self.pool['token'],
            'amount': tx['amount'],
            'function': 'royalty.deposit',
            'message': json.dumps({'expires': expires, 'unlocks': unlocks}) if expires or unlocks else None,
        }})

    def withdraw(self):
        """
        Withdraw from royalty pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'royalty.withdraw',
        }})

    def close(self):
        """
        Close royalty pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'royalty.close',
        }})