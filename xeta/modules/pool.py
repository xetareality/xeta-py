from xeta.programs import auction, launch, lending, lock, loot, lottery, royalty, staking, swap, vote
from xeta.modules import transaction
from xeta.library import models, utils
from xeta.library.config import config
import json
import time


def create(token, program, name=None, mechanism=None, candidates=None, rate=None, percentage=None, probability=None, expires=None, answers=None, meta=None, minAmount=None, maxAmount=None, minTime=None, maxTime=None, transfersLimit=None, claimsLimit=None, tokenLimit=None, xetaLimit=None, tokenTarget=None, xetaTarget=None, raw=False):
    """
    Create pool
    """
    assert program in ['auction', 'launch', 'lending', 'lock', 'loot', 'lottery', 'royalty', 'staking', 'vote'], 'validation: invalid program'

    instruction = utils.strip({
        'function': 'pool.create',
        'token': token,
        'program': program,
        'name': name,
        'mechanism': mechanism,
        'candidates': candidates,
        'rate': rate,
        'percentage': percentage,
        'probability': probability,
        'expires': expires,
        'answers': answers,
        'meta': meta,
        'minAmount': minAmount,
        'maxAmount': maxAmount,
        'minTime': minTime,
        'maxTime': maxTime,
        'transfersLimit': transfersLimit,
        'claimsLimit': claimsLimit,
        'tokenLimit': tokenLimit,
        'xetaLimit': xetaLimit,
        'tokenTarget': tokenTarget,
        'xetaTarget': xetaTarget,
    })

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})

def get(address, extended=None):
    """
    Get pool by address
    """
    return models.parse_values(utils.request(
        method='GET',
        url=config['interface']+'/pool',
        params=utils.strip({'address': address, 'extended': extended})
    ), models.POOL)

def batchGet(addresses, extended=None):
    """
    Batch get pools by addresses
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/pools',
        params=utils.strip({'addresses': ','.join(addresses), 'extended': extended}))

    return [models.parse_values(r, models.POOL) for r in results]

def instance(address, extended=None):
    """
    Get pool by address
    Return as program instance
    """
    result = utils.request(
        method='GET',
        url=config['interface']+'/pool',
        params=utils.strip({'address': address, 'extended': extended}))

    pool = models.parse_values(result, models.POOL)
    instance = getattr(globals()[pool['program']], pool['program'].capitalize())
    return instance(pool)

def scanByToken(token, address=None, program=None, sort='DESC', limit=25, extended=None):
    """
    Scan pools by token
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/pools',
        params=utils.strip({'token': token, 'address': address, 'program': program, 'sort': sort, 'limit': limit, 'extended': extended}))

    return [models.parse_values(r, models.POOL) for r in results]

def scanByCreator(creator, address=None, program=None, sort='DESC', limit=25, extended=None):
    """
    Scan pools by creator
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/pools',
        params=utils.strip({'creator': creator, 'address': address, 'program': program, 'sort': sort, 'limit': limit, 'extended': extended}))

    return [models.parse_values(r, models.POOL) for r in results]

def scanByName(name, address=None, program=None, sort='DESC', limit=25, extended=None):
    """
    Scan pools by name
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/pools',
        params=utils.strip({'name': name, 'address': address, 'program': program, 'sort': sort, 'limit': limit, 'extended': extended}))

    return [models.parse_values(r, models.POOL) for r in results]