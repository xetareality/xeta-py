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

    def transfer(self, tx={}):
        """
        Transfer to loot pool
        """
        return instruction.wrap({
            'function': 'loot.transfer',
            'pool': self.pool['address'],
        }, tx)

    def deposit(self, token, unlocks=None, tx={}):
        """
        Deposit nft to loot pool
        """
        return instruction.wrap({
            'function': 'loot.deposit',
            'pool': self.pool['address'],
            'token': token,
            'unlocks': unlocks,
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