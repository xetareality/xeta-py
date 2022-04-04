from xeta.modules import instruction
from xeta.library import utils


class Royalty():
    """
    Royalty pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, token, tx={}):
        """
        Claim from royalty pool
        """
        return self.claim(token, tx)

    def claim(self, token, tx={}):
        """
        Claim from royalty pool
        """
        return instruction.wrap({
            'function': 'royalty.claim',
            'pool': self.pool['address'],
            'token': token,
        }, tx)

    def deposit(self, amount, unlocks=None, tx={}):
        """
        Deposit to royalty pool
        """
        return instruction.wrap({
            'function': 'royalty.deposit',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
        }, tx)

    def withdraw(self, claim, tx={}):
        """
        Withdraw from royalty pool
        """
        return instruction.wrap({
            'function': 'royalty.withdraw',
            'pool': self.pool['address'],
            'claim': claim,
        }, tx)

    def close(self, tx={}):
        """
        Close royalty pool
        """
        return instruction.wrap({
            'function': 'royalty.close',
            'pool': self.pool['address'],
        }, tx)