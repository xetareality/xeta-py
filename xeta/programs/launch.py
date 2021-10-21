from xeta.modules import transaction, pool
from xeta.config import config
from xeta.library import models


def create(values):
    """
    Create launch pool
    """
    models.required_fields(values, ['token', 'expires'])
    models.valid_formats(values, models.POOL)
    return pool.create({**values, **{'program': 'launch'}})

class Launch():
    """
    Launch pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, tx):
        """
        Transfer to launch pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': config['xeta_address'],
            'amount': tx['amount'],
            'function': 'launch.transfer',
        }})

    def swap(self, tx):
        """
        Swap via launch pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': config['xeta_address'],
            'amount': tx['amount'],
            'function': 'launch.swap',
        }})

    def resolve(self):
        """
        Resolve launch pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'launch.resolve',
        }})

    def claim(self):
        """
        Claim from launch pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'launch.claim',
        }})

    def deposit(self, tx):
        """
        Deposit to launch pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': self.pool['token'],
            'amount': tx['amount'],
            'function': 'launch.deposit',
        }})

    def withdraw(self):
        """
        Withdraw from launch pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'launch.withdraw',
        }})

    def close(self):
        """
        Close launch pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'launch.close',
        }})