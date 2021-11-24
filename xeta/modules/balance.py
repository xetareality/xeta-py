from xeta.modules import instruction, resource
from xeta.library import models, utils, hashed
from xeta.library.config import config


def read(hash, args={}):
    """
    Read balance by hash
    """
    return resource.read(**{**{
        'type': 'balance',
        'key': hash,
    }, **args})

def readAddressToken(address, token, args={}):
    """
    Read balance by address and token
    """
    return resource.read(**{**{
        'type': 'balance',
        'key': hashed.balance({'address': address, 'token': token}),
    }, **args})

def list(hashes, args={}):
    """
    List balances by hashes
    """
    return resource.list(**{**{
        'type': 'balance',
        'keys': hashes,
    }, **args})

def scanAddressAmount(address, amount=None, hash=None, args={}):
    """
    Scan balances by address, sort by amount
    """
    return resource.scan(**{**{
        'type': 'balance',
        'index': 'address',
        'indexValue': address,
        'sort': 'amount',
        'sortValue': amount,
        'keyValue': hash,
    }, **args})

def scanTokenAmount(token, amount=None, hash=None, args={}):
    """
    Scan balances by token, sort by amount
    """
    return resource.scan(**{**{
        'type': 'balance',
        'index': 'token',
        'indexValue': token,
        'sort': 'amount',
        'sortValue': amount,
        'keyValue': hash,
    }, **args})