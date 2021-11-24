from xeta.modules import instruction
from xeta.library import utils
import time

class Staking():
    """
    Staking pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, unlocks=None, expires=None, tx={}):
        """
        Transfer to staking pool
        """
        assert unlocks and unlocks > time.time()*1000+24*60*60*1000, 'invalid:time'

        return instruction.wrap({
            'function': 'staking.transfer',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
            'expires': expires,
        }, tx)

    def claim(self, claim, tx={}):
        """
        Claim from staking pool
        """
        return instruction.wrap({
            'function': 'staking.claim',
            'pool': self.pool['address'],
            'claim': claim,
        }, tx)

    def deposit(self, amount, unlocks=None, expires=None, tx={}):
        """
        Deposit to staking pool
        """
        return instruction.wrap({
            'function': 'staking.deposit',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
            'expires': expires,
        }, tx)

    def withdraw(self, claim, tx={}):
        """
        Withdraw from staking pool
        """
        return instruction.wrap({
            'function': 'staking.withdraw',
            'pool': self.pool['address'],
            'claim': claim,
        }, tx)