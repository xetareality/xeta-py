from xeta.modules import transaction, pool
from xeta.config import config
from xeta.library import models
import json


def create(values):
    """
    Create lock pool
    """
    models.required_fields(values, ['token'])
    models.valid_formats(values, models.POOL)
    return pool.create({**values, **{'program': 'lock'}})

class Lock():
    """
    Lock pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, tx, expires=None, unlocks=None, address=None):
        """
        Transfer to lock pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': self.pool['token'],
            'amount': tx['amount'],
            'function': 'lock.transfer',
            'message': json.dumps({'expires': expires, 'unlocks': unlocks, 'address': address}) if expires or unlocks or address else None,
        }})

    def claim(self):
        """
        Claim from lock pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'lock.claim',
        }})