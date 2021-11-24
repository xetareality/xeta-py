from xeta.modules import instruction
from xeta.library import utils


class Vote():
    """
    Vote pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount=0, answer=None, number=None, tx={}):
        """
        Transfer to vote pool
        """
        assert (self.pool.get('candidates') and answer) or (not self.pool.get('candidates') and number), 'answer:invalid'

        return instruction.wrap({
            'function': 'vote.transfer',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'answer': answer,
            'number': number,
        }, tx)

    def claim(self, claim, tx={}):
        """
        Claim from vote pool
        """
        return instruction.wrap({
            'function': 'vote.claim',
            'pool': self.pool['address'],
            'claim': claim,
        }, tx)

    def resolve(self, tx={}):
        """
        Resolve vote pool
        """
        return instruction.wrap({
            'function': 'vote.resolve',
            'pool': self.pool['address'],
        }, tx)

    def oracle(self, answer, tx={}):
        """
        Set accepted answer
        """
        return instruction.wrap({
            'function': 'vote.oracle',
            'pool': self.pool['address'],
            'answer': answer,
        }, tx)