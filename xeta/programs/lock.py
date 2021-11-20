from xeta.modules import instruction, pool
from xeta.library.config import config
from xeta.library import models, utils
import json


def create(**values):
    """
    Create lock pool
    """
    models.required_fields(values, ['token'])
    models.valid_formats(values, models.POOL)
    return pool.create(**{**values, **{'program': 'lock'}})

class Lock():
    """
    Lock pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, unlocks=None, expires=None, address=None, submit=True):
        """
        Transfer to lock pool
        """
        return instruction.wrap({
            'function': 'lock.transfer',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
            'expires': expires,
            'address': address,
        }, submit)

    def claim(self, claim, submit=True):
        """
        Claim from lock pool
        """
        return instruction.wrap({
            'function': 'lock.claim',
            'pool': self.pool['address'],
            'claim': claim,
        }, submit)