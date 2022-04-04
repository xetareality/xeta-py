from xeta.modules import instruction
from xeta.library import utils


class Listing():
    """
    Listing pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, tx={}):
        """
        Transfer to listing pool
        """
        return instruction.wrap({
            'function': 'listing.transfer',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
        }, tx)

    def deposit(self, amount=None, unlocks=None, tx={}):
        """
        Deposit to listing pool
        """
        return instruction.wrap({
            'function': 'listing.deposit',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
        }, tx)

    def close(self, tx={}):
        """
        Close listing pool
        """
        return instruction.wrap({
            'function': 'listing.close',
            'pool': self.pool['address'],
        }, tx)