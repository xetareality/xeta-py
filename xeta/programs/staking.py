from xeta.modules import instruction, pool
from xeta.library.config import config
from xeta.library import models, utils
import json
import time


def create(**values):
    """
    Create staking pool
    """
    models.required_fields(values, ['token'])
    models.valid_formats(values, models.POOL)
    return pool.create(**{**values, **{'program': 'staking'}})

class Staking():
    """
    Staking pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, unlocks=None, expires=None, submit=True):
        """
        Transfer to staking pool
        """
        assert unlocks and unlocks > time.time()*1000+24*60*60*1000, 'validation: below minimum time'

        return instruction.wrap({
            'function': 'staking.transfer',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
            'expires': expires,
        }, submit)

    def claim(self, claim, submit=True):
        """
        Claim from staking pool
        """
        return instruction.wrap({
            'function': 'staking.claim',
            'pool': self.pool['address'],
            'claim': claim,
        }, submit)

    def deposit(self, amount, unlocks=None, expires=None, submit=True):
        """
        Deposit to staking pool
        """
        return instruction.wrap({
            'function': 'staking.deposit',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
            'expires': expires,
        }, submit)

    def withdraw(self, claim, submit=True):
        """
        Withdraw from staking pool
        """
        return instruction.wrap({
            'function': 'staking.withdraw',
            'pool': self.pool['address'],
            'claim': claim,
        }, submit)