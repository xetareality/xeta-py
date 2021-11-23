from xeta.modules import instruction, resource
from xeta.library import models, utils
from xeta.library.config import config

def read(address):
    """
    Read account data for an address (pool, token, balance)
    """
    result = utils.request(
        method='GET',
        url=config['interface']+'/account',
        params={'address': address})

    return {'pool': result.get('pool'), 'balance': result.get('balance'), 'token': result.get('token')}

def update(name, object=None, description=None, links=None, meta=None, tx={}):
    """
    Update (or create) account
    """
    return instruction.wrap({
        'function': 'account.update',
        'name': name,
        'object': object,
        'description': description,
        'links': links,
        'meta': meta,
    }, tx)