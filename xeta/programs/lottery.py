from xeta.modules import transaction, pool
from xeta.config import config
from xeta.library import models


def create(values):
    """
    Create lottery pool
    """
    models.required_fields(values, ['token', 'expires'])
    models.valid_formats(values, models.POOL)
    return pool.create({**values, **{'program': 'lottery'}})

class Lottery():
    """
    Lottery pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, tx):
        """
        Transfer to lottery pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': config['xeta_address'],
            'amount': tx['amount'],
            'function': 'lottery.transfer',
        }})

    def claim(self):
        """
        Claim from lottery pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'lottery.claim',
        }})

    def deposit(self, tx):
        """
        Deposit to lottery pool
        """
        models.required_fields(tx, ['amount'])
        models.valid_formats(tx, models.TRANSACTION)

        return transaction.create({**transaction.template(), **tx, **{
            'to': self.pool['address'],
            'token': self.pool['token'],
            'amount': tx['amount'],
            'function': 'lottery.deposit',
        }})

    def withdraw(self):
        """
        Withdraw from lottery pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'lottery.withdraw',
        }})

    def close(self):
        """
        Close lottery pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'lottery.close',
        }})

    def clear(self):
        """
        Clear lottery pool
        """
        return transaction.create({**transaction.template(), **{
            'to': self.pool['address'],
            'function': 'lottery.clear',
        }})