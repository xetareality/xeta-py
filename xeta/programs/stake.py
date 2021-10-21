from xeta.modules import transaction, pool
from xeta.config import config
from xeta.library import models
import json
import time


def create(values):
    """
    Create stake pool
    """
    models.required_fields(values, ['token'])
    models.valid_formats(values, models.POOL)
    return pool.create({**values, **{'program': 'stake'}})

class Stake():
    """
    Stake pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, tx, expires=None, unlocks=None):
        """
        Transfer to stake pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        assert unlocks and unlocks > time.time()*1000+24*60*60*1000, 'validation: below minimum time'

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': self.pool['token'],
            'amount': tx['amount'],
            'function': 'stake.transfer',
            'message': json.dumps({'expires': expires, 'unlocks': unlocks}) if expires or unlocks else None,
        }})

    def claim(self):
        """
        Claim from stake pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'stake.claim',
        }})

    def deposit(self, tx, expires=None, unlocks=None):
        """
        Deposit to stake pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': self.pool['token'],
            'amount': tx['amount'],
            'function': 'stake.deposit',
            'message': json.dumps({'expires': expires, 'unlocks': unlocks}) if expires or unlocks else None,
        }})

    def withdraw(self):
        """
        Withdraw from stake pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'stake.withdraw',
        }})