from xeta.modules import instruction
from xeta.library import utils


class Lock():
    """
    Lock pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, unlocks=None, expires=None, address=None, tx={}):
        """
        Transfer to lock pool
        """
        return instruction.wrap({
            'function': 'lock.transfer',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
            'expires': expires,
            'address': address,
        }, tx)

    def claim(self, claim, tx={}):
        """
        Claim from lock pool
        """
        return instruction.wrap({
            'function': 'lock.claim',
            'pool': self.pool['address'],
            'claim': claim,
        }, tx)