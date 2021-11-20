from xeta.modules import instruction, pool
from xeta.library.config import config
from xeta.library import models, utils
import json


def create(**values):
    """
    Create lending pool
    """
    models.required_fields(values, ['token'])
    models.valid_formats(values, models.POOL)
    return pool.create(**{**values, **{'program': 'lending'}})

class Lending():
    """
    Lending pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, collateralization=2.5, submit=True):
        """
        Transfer to lending pool
        """
        return instruction.wrap({
            'function': 'lending.transfer',
            'pool': self.pool['address'],
            'token': self.pool['token'],
            'amount': utils.amount(amount),
            'collateralization': collateralization,
        }, submit)

    def settle(self, claim, submit=True):
        """
        Settle claim from lending pool
        """
        return instruction.wrap({
            'function': 'lending.settle',
            'pool': self.pool['address'],
            'claim': claim,
        }, submit)

    def liquidate(self, claim, submit=True):
        """
        Liquidate claim from lending pool
        """
        return instruction.wrap({
            'function': 'lending.liquidate',
            'pool': self.pool['address'],
            'token': self.pool['token'],
            'claim': claim,
        }, submit)

    def deposit(self, amount, unlocks=None, expires=None, submit=True):
        """
        Deposit to lending pool
        """
        return instruction.wrap({
            'function': 'lending.deposit',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
            'expires': expires,
        }, submit)

    def withdraw(self, claim, submit=True):
        """
        Withdraw from lending pool
        """
        return instruction.wrap({
            'function': 'lending.withdraw',
            'pool': self.pool['address'],
            'token': self.pool['token'],
            'claim': claim,
        }, submit)