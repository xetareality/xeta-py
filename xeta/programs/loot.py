from xeta.modules import instruction, pool
from xeta.library.config import config
from xeta.library import models, utils


def create(**values):
    """
    Create loot pool
    """
    models.required_fields(values, ['token'])
    models.valid_formats(values, models.POOL)
    return pool.create(**{**values, **{'program': 'loot'}})

class Loot():
    """
    Loot pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, submit=True):
        """
        Transfer to loot pool
        """
        return instruction.wrap({
            'function': 'loot.transfer',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
        })

    def deposit(self, token, unlocks=None, expires=None, submit=True):
        """
        Deposit nft to loot pool
        """
        return instruction.wrap({
            'function': 'loot.deposit',
            'pool': self.pool['address'],
            'token': token,
            'unlocks': unlocks,
            'expires': expires,
        })

    def withdraw(self, claim, submit=True):
        """
        Withdraw nft from loot pool
        """
        return instruction.wrap({
            'function': 'loot.withdraw',
            'pool': self.pool['address'],
            'claim': claim,
        })

    def clear(self, submit=True):
        """
        Clear loot pool
        """
        return instruction.wrap({
            'function': 'loot.clear',
            'pool': self.pool['address'],
        })