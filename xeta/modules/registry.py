from xeta.modules import instruction, resource
from xeta.library import models, utils
from xeta.library.config import config


def read(hash, args={}):
    """
    Read object by hash
    """
    return resource.read(**{**{
        'type': 'object',
        'key': hash,
    }, **args})

def list(hashes, args={}):
    """
    List objects by hashes
    """
    return resource.list(**{**{
        'type': 'object',
        'keys': hashes,
    }, **args})

def scanContentCreated(content, created=None, token=None, args={}):
    """
    Scan objects by content, sort by created
    """
    return resource.scan(**{**{
        'type': 'object',
        'index': 'content',
        'indexValue': content,
        'sort': 'created',
        'sortValue': created,
        'keyValue': token,
    }, **args})

def scanFingerprintCreated(fingerprint, created=None, token=None, args={}):
    """
    Scan objects by fingerprint, sort by created
    """
    return resource.scan(**{**{
        'type': 'object',
        'index': 'fingerprint',
        'indexValue': fingerprint,
        'sort': 'created',
        'sortValue': created,
        'keyValue': token,
    }, **args})

def scanClusterCreated(cluster, created=None, token=None, args={}):
    """
    Scan objects by cluster, sort by created
    """
    return resource.scan(**{**{
        'type': 'object',
        'index': 'cluster',
        'indexValue': cluster,
        'sort': 'created',
        'sortValue': created,
        'keyValue': token,
    }, **args})