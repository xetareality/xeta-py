from xeta.modules import instruction, pool
from xeta.library.config import config
from xeta.library import models, utils
import json


class Swap():
    """
    Swap pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, token, amount, submit=True):
        """
        Transfer to swap pool
        """
        return instruction.wrap({
            'function': 'swap.transfer',
            'pool': self.pool['address'],
            'token': token,
            'amount': utils.amount(amount),
        })

    def deposit(self, tokenAmount, xetaAmount, unlocks=None, expires=None, submit=True):
        """
        Deposit to swap pool
        """
        return instruction.wrap({
            'function': 'swap.deposit',
            'pool': self.pool['address'],
            'tokenAmount': utils.amount(tokenAmount),
            'xetaAmount': utils.amount(xetaAmount),
            'unlocks': unlocks,
            'expires': expires,
        })

    def withdraw(self, claim, percentage=1, submit=True):
        """
        Withdraw from swap pool
        """
        assert percentage <= 1, 'input: percentage must between zero and one'

        return instruction.wrap({
            'function': 'swap.withdraw',
            'pool': self.pool['address'],
            'claim': claim,
            'percentage': percentage,
        })