from xeta.modules import instruction, pool
from xeta.library.config import config
from xeta.library import models, utils
import json


def create(**values):
    """
    Create vote pool
    """
    models.required_fields(values, ['token'])
    models.valid_formats(values, models.POOL)
    return pool.create(**{**values, **{'program': 'vote'}})

class Vote():
    """
    Vote pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount=0, answer=None, number=None, submit=True):
        """
        Transfer to vote pool
        """
        assert (self.pool.get('candidates') and answer) or (not self.pool.get('candidates') and number), 'validation: incorrect answer'

        return instruction.wrap({
            'function': 'vote.transfer',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'answer': answer,
            'number': number,
        })

    def claim(self, claim, submit=True):
        """
        Claim from vote pool
        """
        return instruction.wrap({
            'function': 'vote.claim',
            'pool': self.pool['address'],
            'claim': claim,
        })

    def resolve(self, submit=True):
        """
        Resolve vote pool
        """
        return instruction.wrap({
            'function': 'vote.resolve',
            'pool': self.pool['address'],
        })

    def oracle(self, answer, submit=True):
        """
        Set correct answer
        """
        return instruction.wrap({
            'function': 'vote.oracle',
            'pool': self.pool['address'],
            'answer': answer,
        })