from xeta.modules import instruction, resource
from xeta.library import models, utils, hashed
from xeta.library.config import config


def update(spender, token, amount, tx={}):
    """
    Update allowance for spender address
    """
    return instruction.wrap({
        'function': 'allowance.update',
        'spender': spender,
        'token': token,
        'amount': utils.amount(amount),
    }, tx)

def read(hash, args={}):
    """
    Read allowance by hash
    """
    return resource.read(**{**{
        'type': 'allowance',
        'key': hash,
    }, **args})

def list(hashes, args={}):
    """
    List allowances by hashes
    """
    return resource.list(**{**{
        'type': 'allowance',
        'keys': hashes,
    }, **args})

def readAddressSpenderToken(address, spender, token, args={}):
    """
    Read allowance by address, spender, and token
    """
    return resource.read(**{**{
        'type': 'allowance',
        'key': hashed.allowance({'address': address, 'spender': spender, 'token': token}),
    }, **args})

def list(hashes, args={}):
    """
    List allowances by hashes
    """
    return resource.list(**{**{
        'type': 'allowance',
        'keys': hashes,
    }, **args})

def scanAddressCreated(address, created=None, hash=None, args={}):
    """
    Scan allowances by address, sort by created
    """
    return resource.scan(**{**{
        'type': 'allowance',
        'index': 'address',
        'indexValue': address,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanSpenderCreated(spender, created=None, hash=None, args={}):
    """
    Scan allowances by spender, sort by created
    """
    return resource.scan(**{**{
        'type': 'allowance',
        'index': 'spender',
        'indexValue': spender,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})