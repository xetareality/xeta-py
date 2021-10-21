from xeta.modules import transaction, pool
from xeta.config import config
from xeta.library import models


def create(values):
    """
    Create auction pool
    """
    models.required_fields(values, ['token', 'expires'])
    models.valid_formats(values, models.POOL)
    return pool.create({**values, **{'program': 'auction'}})

class Auction():
    """
    Auction pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, tx):
        """
        Transfer to auction pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': config['xeta_address'],
            'amount': tx['amount'],
            'function': 'auction.transfer',
        }})

    def deposit(self, tx):
        """
        Deposit to auction pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': self.pool['token'],
            'amount': tx['amount'],
            'function': 'auction.deposit',
        }})

    def resolve(self):
        """
        Resolve auction pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'token': config['xeta_address'],
            'amount': 0,
            'function': 'auction.resolve',
        }})

    def cancel(self):
        """
        Cancel auction pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'token': config['xeta_address'],
            'amount': 0,
            'function': 'auction.cancel',
        }})

    def close(self):
        """
        Close auction pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'token': config['xeta_address'],
            'amount': 0,
            'function': 'auction.close',
        }})