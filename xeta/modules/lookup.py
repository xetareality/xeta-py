from xeta.modules import instruction, resource
from xeta.library import models, utils
from xeta.library.config import config

def read(token, args={}):
    """
    Read lookup by token address
    """
    return resource.read(**{**{
        'type': 'lookup',
        'key': token,
    }, **args})

def list(tokens, args={}):
    """
    List lookups by token addresses
    """
    return resource.list(**{**{
        'type': 'lookup',
        'keys': tokens,
    }, **args})

def scanHashCreated(hash, created=None, token=None, args={}):
    """
    Scan tokens by hash, sort by created
    """
    return resource.scan(**{**{
        'type': 'lookup',
        'index': 'hash',
        'indexValue': hash,
        'sort': 'created',
        'sortValue': created,
        'keyValue': token,
    }, **args})

def scanFingerprintCreated(fingerprint, created=None, token=None, args={}):
    """
    Scan tokens by fingerprint, sort by created
    """
    return resource.scan(**{**{
        'type': 'lookup',
        'index': 'fingerprint',
        'indexValue': fingerprint,
        'sort': 'created',
        'sortValue': created,
        'keyValue': token,
    }, **args})

def scanClusterCreated(cluster, created=None, token=None, args={}):
    """
    Scan tokens by cluster, sort by created
    """
    return resource.scan(**{**{
        'type': 'lookup',
        'index': 'cluster',
        'indexValue': cluster,
        'sort': 'created',
        'sortValue': created,
        'keyValue': token,
    }, **args})