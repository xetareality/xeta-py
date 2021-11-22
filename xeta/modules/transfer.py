from xeta.modules import instruction
from xeta.library import utils, hashed


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

def readHash(hash, args={}):
    """
    Read transfer by hash
    """
    return resource.read(**{**{
        'type': 'transfer',
        'key': hash,
    }, **args})

def listHashes(hashes, args={}):
    """
    List transfers by hashes
    """
    return resource.list(**{**{
        'type': 'transfer',
        'keys': hashes,
    }, **args})

def scanSenderCreated(sender, created=None, hash=None, args={}):
    """
    Scan transfers by sender, sorted by created
    """
    return resource.scan(**{**{
        'type': 'transfer',
        'index': 'sender,
        'indexValue': sender,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanFromCreated(fromAddress, created=None, hash=None, args={}):
    """
    Scan transfers by from, sorted by created
    """
    return resource.scan(**{**{
        'type': 'transfer',
        'index': 'from,
        'indexValue': fromAddress,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanToCreated(to, created=None, hash=None, args={}):
    """
    Scan transfers by to, sorted by created
    """
    return resource.scan(**{**{
        'type': 'transfer',
        'index': 'to,
        'indexValue': to,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanTokenCreated(token, created=None, hash=None, args={}):
    """
    Scan transfers by token, sorted by created
    """
    return resource.scan(**{**{
        'type': 'transfer',
        'index': 'token,
        'indexValue': token,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanFromTokenCreated(fromAddress, token, created=None, hash=None, args={}):
    """
    Scan transfers by fromToken, sorted by created
    """
    fromToken = 
    return resource.scan(**{**{
        'type': 'transfer',
        'index': 'fromToken,
        'indexValue': hashed.values([fromAddress, token])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanToTokenCreated(to, token, created=None, hash=None, args={}):
    """
    Scan transfers by toToken, sorted by created
    """
    return resource.scan(**{**{
        'type': 'transfer',
        'index': 'toToken,
        'indexValue': hashed.values([to, token])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})