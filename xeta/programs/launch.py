from xeta.modules import instruction, pool
from xeta.library.config import config
from xeta.library import models, utils


def create(**values):
    """
    Create launch pool
    """
    models.required_fields(values, ['token', 'expires'])
    models.valid_formats(values, models.POOL)
    return pool.create(**{**values, **{'program': 'launch'}})

class Launch():
    """
    Launch pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, submit=True):
        """
        Transfer to launch pool
        """
        return instruction.wrap({
            'function': 'launch.transfer',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
        }, submit)

    def swap(self, amount, submit=True):
        """
        Swap via launch pool
        """
        return instruction.wrap({
            'function': 'launch.swap',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
        }, submit)

    def resolve(self, submit=True):
        """
        Resolve launch pool
        """
        return instruction.wrap({
            'function': 'launch.resolve',
            'pool': self.pool['address'],
            'token': self.pool['token'],
        }, submit)

    def claim(self, claim, submit=True):
        """
        Claim from launch pool
        """
        return instruction.wrap({
            'function': 'launch.claim',
            'pool': self.pool['address'],
            'claim': claim,
        }, submit)

    def deposit(self, amount, unlocks=None, expires=None, submit=True):
        """
        Deposit to launch pool
        """
        return instruction.wrap({
            'function': 'launch.deposit',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
            'expires': expires,
        }, submit)

    def withdraw(self, claim, submit=True):
        """
        Withdraw from launch pool
        """
        return instruction.wrap({
            'function': 'launch.withdraw',
            'pool': self.pool['address'],
            'claim': claim,
        }, submit)

    def close(self, submit=True):
        """
        Close launch pool
        """
        return instruction.wrap({
            'function': 'launch.close',
            'pool': self.pool['address'],
        }, submit)