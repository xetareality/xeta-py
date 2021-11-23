from xeta.modules import instruction, resource
from xeta.library import models, utils, hashed
from xeta.library.config import config


def create(to, token, amount, fromAddress=None, message=None, tx={}):
    """
    Create transfer
    """
    return instruction.wrap({
        'function': 'transfer.create',
        'to': to,
        'token': token,
        'amount': utils.amount(amount),
        'from': fromAddress,
        'message': message,
    }, tx)

def read(hash, args={}):
    """
    Read transfer by hash
    """
    return resource.read(**{**{
        'type': 'transfer',
        'key': hash,
    }, **args})

def list(hashes, args={}):
    """
    List transfers by hashes
    """
    return resource.list(**{**{
        'type': 'transfer',
        'keys': hashes,
    }, **args})

def scanSenderCreated(sender, created=None, hash=None, args={}):
    """
    Scan transfers by sender, sort by created
    """
    return resource.scan(**{**{
        'type': 'transfer',
        'index': 'sender',
        'indexValue': sender,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanFromCreated(fromAddress, created=None, hash=None, args={}):
    """
    Scan transfers by from, sort by created
    """
    return resource.scan(**{**{
        'type': 'transfer',
        'index': 'from',
        'indexValue': fromAddress,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanToCreated(to, created=None, hash=None, args={}):
    """
    Scan transfers by to, sort by created
    """
    return resource.scan(**{**{
        'type': 'transfer',
        'index': 'to',
        'indexValue': to,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanTokenCreated(token, created=None, hash=None, args={}):
    """
    Scan transfers by token, sort by created
    """
    return resource.scan(**{**{
        'type': 'transfer',
        'index': 'token',
        'indexValue': token,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanFromTokenCreated(fromAddress, token, created=None, hash=None, args={}):
    """
    Scan transfers by fromToken, sort by created
    """
    return resource.scan(**{**{
        'type': 'transfer',
        'index': 'fromToken',
        'indexValue': hashed.values([fromAddress, token])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanToTokenCreated(to, token, created=None, hash=None, args={}):
    """
    Scan transfers by toToken, sort by created
    """
    return resource.scan(**{**{
        'type': 'transfer',
        'index': 'toToken',
        'indexValue': hashed.values([to, token])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})