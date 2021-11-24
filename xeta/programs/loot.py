from xeta.modules import instruction
from xeta.library import utils


class Loot():
    """
    Loot pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, tx={}):
        """
        Transfer to loot pool
        """
        return instruction.wrap({
            'function': 'loot.transfer',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
        }, tx)

    def deposit(self, token, unlocks=None, expires=None, tx={}):
        """
        Deposit nft to loot pool
        """
        return instruction.wrap({
            'function': 'loot.deposit',
            'pool': self.pool['address'],
            'token': token,
            'unlocks': unlocks,
            'expires': expires,
        }, tx)

    def withdraw(self, claim, tx={}):
        """
        Withdraw nft from loot pool
        """
        return instruction.wrap({
            'function': 'loot.withdraw',
            'pool': self.pool['address'],
            'claim': claim,
        }, tx)

    def clear(self, tx={}):
        """
        Clear loot pool
        """
        return instruction.wrap({
            'function': 'loot.clear',
            'pool': self.pool['address'],
        }, tx)