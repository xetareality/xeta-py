from xeta.modules import instruction
from xeta.library import utils


class Lending():
    """
    Lending pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, collateralization, tx={}):
        """
        Transfer to lending pool
        """
        return instruction.wrap({
            'function': 'lending.transfer',
            'pool': self.pool['address'],
            'token': self.pool['token'],
            'amount': utils.amount(amount),
            'collateralization': collateralization,
        }, tx)

    def settle(self, claim, tx={}):
        """
        Settle claim from lending pool
        """
        return instruction.wrap({
            'function': 'lending.settle',
            'pool': self.pool['address'],
            'claim': claim,
        }, tx)

    def liquidate(self, claim, tx={}):
        """
        Liquidate claim from lending pool
        """
        return instruction.wrap({
            'function': 'lending.liquidate',
            'pool': self.pool['address'],
            'token': self.pool['token'],
            'claim': claim,
        }, tx)

    def deposit(self, amount, unlocks=None, tx={}):
        """
        Deposit to lending pool
        """
        return instruction.wrap({
            'function': 'lending.deposit',
            'pool': self.pool['address'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
        }, tx)

    def withdraw(self, claim, percentage=1, tx={}):
        """
        Withdraw from lending pool
        """
        return instruction.wrap({
            'function': 'lending.withdraw',
            'pool': self.pool['address'],
            'token': self.pool['token'],
            'claim': claim,
            'percentage': percentage,
        }, tx)