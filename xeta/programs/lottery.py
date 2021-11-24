from xeta.modules import instruction
from xeta.library import utils


class Lottery():
    """
    Lottery pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, tx={}):
        """
        Transfer to lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.transfer',
            'pool': self.pool['address'],
            'token': self.pool['token'],
            'amount': utils.amount(amount),
        }, tx)

    def claim(self, claim, tx={}):
        """
        Claim from lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.claim',
            'pool': self.pool['address'],
            'claim': claim,
        }, tx)

    def resolve(self, tx={}):
        """
        Resolve NFT lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.resolve',
            'pool': self.pool['address'],
        }, tx)

    def deposit(self, amount=None, unlocks=None, expires=None, tx={}):
        """
        Deposit to lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.deposit',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
            'expires': expires,
        }, tx)

    def withdraw(self, claim, tx={}):
        """
        Withdraw from lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.withdraw',
            'pool': self.pool['address'],
            'claim': claim,
        }, tx)

    def close(self, tx={}):
        """
        Close lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.close',
            'pool': self.pool['address'],
        }, tx)

    def clear(self, tx={}):
        """
        Clear lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.clear',
            'pool': self.pool['address'],
        }, tx)