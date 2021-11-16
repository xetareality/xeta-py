from xeta.modules import transaction
from xeta.library import models, utils
from xeta.library.config import config
import json
import time


def update(token, spender, amount, raw=False):
    """
    Update allowance for spender address
    """
    instruction = utils.strip({
        'function': 'allowance.update',
        'token': token,
        'spender': spender,
        'amount': utils.amount(amount),
    })

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})

def get(address, token, spender, extended=None):
    """
    Get allowance by address, token and spender
    """
    return models.parse_values(utils.request(
        method='GET',
        url=config['interface']+'/allowance',
        params=utils.strip({'address': address, 'token': token, 'spender': spender, 'extended': extended})
    ), models.ALLOWANCE)

def getByHash(hash, extended=None):
    """
    Get allowance by hash
    """
    return models.parse_values(utils.request(
        method='GET',
        url=config['interface']+'/allowance',
        params=utils.strip({'hash': hash, 'extended': extended})
    ), models.ALLOWANCE)

def scanByAddress(address, hash=None, created=None, sort='DESC', limit=25, extended=None):
    """
    Scan allowances by address
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/allowances',
        params=utils.strip({'address': address, 'hash': hash, 'created': created, 'sort': sort, 'limit': limit, 'extended': extended}))

    return [models.parse_values(r, models.ALLOWANCE) for r in results]

def scanBySpender(spender, hash=None, created=None, sort='DESC', limit=25, extended=None):
    """
    Scan allowances by spender
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/allowances',
        params=utils.strip({'spender': spender, 'hash': hash, 'created': created, 'sort': sort, 'limit': limit, 'extended': extended}))

    return [models.parse_values(r, models.ALLOWANCE) for r in results]