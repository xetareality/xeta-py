from xeta.modules import transaction, pool
from xeta.config import config
from xeta.library import models
import json


def create(values):
    """
    Create vote pool
    """
    models.required_fields(values, ['token'])
    models.valid_formats(values, models.POOL)
    return pool.create({**values, **{'program': 'vote'}})

class Vote():
    """
    Vote pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, tx, answer=None, number=None):
        """
        Transfer to vote pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        assert (self.pool.get('candidates') and answer) or (not self.pool.get('candidates') and number), 'validation: incorrect answer'

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': self.pool['token'],
            'amount': tx['amount'],
            'function': 'vote.transfer',
            'message': json.dumps({'answer': answer}) if answer else json.dumps({'number': number}),
        }})

    def claim(self):
        """
        Claim from vote pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'vote.claim',
        }})

    def resolve(self):
        """
        Resolve vote pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'vote.resolve',
        }})