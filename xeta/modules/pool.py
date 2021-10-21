from xeta.programs import auction, launch, lock, loot, lottery, royalty, stake, swap, vote
from xeta.modules import transaction
from xeta.library import models
from xeta.config import config
import requests
import json
import time


def create(pool, tx):
    """
    Create pool
    """
    models.required_fields(tx, ['token'])
    models.required_fields(pool, ['program'])
    models.exclusive_fields(pool, ['program', 'name', 'mechanism', 'candidates', 'rate', 'percentage', 'probability', 'expires', 'answers', 'minAmount', 'maxAmount', 'minTime', 'maxTime', 'transfersLimit', 'claimsLimit', 'tokenLimit', 'xetaLimit', 'tokenTarget', 'xetaTarget'])
    models.valid_formats(pool, models.POOL)

    assert pool['program'] in ['auction', 'launch', 'lock', 'loot', 'lottery', 'royalty', 'stake', 'vote'], 'validation: invalid program'

    result = transaction.create({**transaction.template(), **tx, **{
        'token': tx['token'],
        'function': 'pool.create',
        'message': json.dumps(pool)
    }})

    try:
        pool = models.parse_values(result['data'], models.POOL)
        instance = getattr(globals()[pool['program']], pool['program'].capitalize())
        result['data'] = instance(pool)
    except: pass

    return models.parse_values(result, models.TRANSACTION)

def get(address):
    """
    Get pool by address
    Return as program instance
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/pool',
        params={'address': address})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: result = r.json()
    except: raise Exception('request: invalid request')

    pool = models.parse_values(result, models.POOL)
    instance = getattr(globals()[pool['program']], pool['program'].capitalize())

    return instance(pool)

def scanByToken(token, address=None, program=None, sort='DESC', limit=25):
    """
    Scan pools by token
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/pools',
        params={'token': token, 'address': address, 'program': program, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.POOL) for r in results]

def scanByCreator(creator, address=None, program=None, sort='DESC', limit=25):
    """
    Scan pools by creator
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/pools',
        params={'creator': creator, 'address': address, 'program': program, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.POOL) for r in results]

def scanByName(name, address=None, program=None, sort='DESC', limit=25):
    """
    Scan pools by name
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/pools',
        params={'name': name, 'address': address, 'program': program, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.POOL) for r in results]