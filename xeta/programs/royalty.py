from xeta.modules import instruction, pool
from xeta.library.config import config
from xeta.library import models, utils
import json


def create(**values):
    """
    Create royalty pool
    """
    models.required_fields(values, ['token'])
    models.valid_formats(values, models.POOL)
    return pool.create(**{**values, **{'program': 'royalty'}})

class Royalty():
    """
    Royalty pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, token, submit=True):
        """
        Transfer to royalty pool
        """
        return instruction.wrap({
            'function': 'royalty.transfer',
            'pool': self.pool['address'],
            'token': token,
        })

    def deposit(self, amount, unlocks=None, expires=None, submit=True):
        """
        Deposit to royalty pool
        """
        return instruction.wrap({
            'function': 'royalty.deposit',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
            'expires': expires,
        })

    def withdraw(self, claim, submit=True):
        """
        Withdraw from royalty pool
        """
        return instruction.wrap({
            'function': 'royalty.withdraw',
            'pool': self.pool['address'],
            'claim': claim,
        })

    def close(self, submit=True):
        """
        Close royalty pool
        """
        return instruction.wrap({
            'function': 'royalty.close',
            'pool': self.pool['address'],
        })