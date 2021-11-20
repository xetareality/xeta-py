from xeta.modules import instruction, pool
from xeta.library.config import config
from xeta.library import models, utils


def create(**values):
    """
    Create lottery pool
    """
    models.required_fields(values, ['token', 'expires'])
    models.valid_formats(values, models.POOL)
    return pool.create(**{**values, **{'program': 'lottery'}})

class Lottery():
    """
    Lottery pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, submit=True):
        """
        Transfer to lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.transfer',
            'pool': self.pool['address'],
            'token': self.pool['token'],
            'amount': utils.amount(amount),
        })

    def claim(self, claim, submit=True):
        """
        Claim from lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.claim',
            'pool': self.pool['address'],
            'claim': claim,
        })

    def resolve(self, submit=True):
        """
        Resolve NFT lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.resolve',
            'pool': self.pool['address'],
        })

    def deposit(self, amount=None, unlocks=None, expires=None, submit=True):
        """
        Deposit to lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.deposit',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
            'expires': expires,
        })

    def withdraw(self, claim, submit=True):
        """
        Withdraw from lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.withdraw',
            'pool': self.pool['address'],
            'claim': claim,
        })

    def close(self, submit=True):
        """
        Close lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.close',
            'pool': self.pool['address'],
        })

    def clear(self, submit=True):
        """
        Clear lottery pool
        """
        return instruction.wrap({
            'function': 'lottery.clear',
            'pool': self.pool['address'],
        })