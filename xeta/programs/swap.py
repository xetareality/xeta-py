from xeta.modules import instruction
from xeta.library import utils


class Swap():
    """
    Swap pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, token, amount, tx={}):
        """
        Transfer to swap pool
        """
        return instruction.wrap({
            'function': 'swap.transfer',
            'pool': self.pool['address'],
            'token': token,
            'amount': utils.amount(amount),
        }, tx)

    def deposit(self, tokenAmount, xetaAmount, unlocks=None, expires=None, tx={}):
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
        }, tx)

    def withdraw(self, claim, percentage=1, tx={}):
        """
        Withdraw from swap pool
        """
        assert percentage <= 1, 'percentage:invalid'

        return instruction.wrap({
            'function': 'swap.withdraw',
            'pool': self.pool['address'],
            'claim': claim,
            'percentage': percentage,
        }, tx)