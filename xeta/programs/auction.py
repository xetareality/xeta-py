from xeta.modules import instruction, pool
from xeta.library.config import config
from xeta.library import models, utils


def create(**values):
    """
    Create auction pool
    """
    models.required_fields(values, ['token', 'expires'])
    models.valid_formats(values, models.POOL)
    return pool.create(**{**values, **{'program': 'auction'}})

class Auction():
    """
    Auction pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, submit=True):
        """
        Transfer to auction pool
        """
        return instruction.wrap({
            'function': 'auction.transfer',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
        })

    def deposit(self, amount, submit=True):
        """
        Deposit to auction pool
        """
        return instruction.wrap({
            'function': 'auction.deposit',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'amount': utils.amount(amount),
        })

    def resolve(self, submit=True):
        """
        Resolve auction pool
        """
        return instruction.wrap({
            'function': 'auction.resolve',
            'pool': self.pool['address'],
        })

    def cancel(self, submit=True):
        """
        Cancel auction pool
        """
        return instruction.wrap({
            'function': 'auction.cancel',
            'pool': self.pool['address'],
        })

    def close(self, submit=True):
        """
        Close auction pool
        """
        return transaction.create({**tx, **{
            'to': self.pool['address'],
            'function': 'auction.close',
        }})

        return instruction.wrap({
            'function': 'auction.transfer',
            'pool': self.pool['address'],
        })