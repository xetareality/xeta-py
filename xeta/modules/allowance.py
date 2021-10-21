from xeta.modules import transaction
from xeta.library import models
from xeta.config import config
import requests
import json
import time


def create(allowance, tx):
    """
    Create allowance for spender address
    """
    models.required_fields(tx, ['token'])
    models.required_fields(allowance, ['spender', 'amount'])
    models.exclusive_fields(allowance, ['spender', 'amount'])
    models.valid_formats(allowance, models.ALLOWANCE)

    result = transaction.create({**transaction.template(), **{
        'token': tx['token'],
        'function': 'allowance.create',
        'message': json.dumps(allowance)
    }, **tx})

    try: result['data'] = models.parse_values(result['data'], models.ALLOWANCE)
    except: pass

    return models.parse_values(result, models.TRANSACTION)

def batch(allowances, tx):
    """
    Batch create allowances
    """
    models.required_fields(tx, ['token'])

    for a in allowances:
        models.required_fields(a, ['spender', 'amount'])
        models.exclusive_fields(a, ['spender', 'amount'])
        models.valid_formats(a, models.ALLOWANCE)

    result = transaction.create({**transaction.template(), **{
        'token': tx['token'],
        'function': 'allowance.batch',
        'message': json.dumps(allowances)
    }})

    try: result['data'] = [models.parse_values(r, models.ALLOWANCE) for r in result['data']]
    except: pass

    return models.parse_values(result, models.TRANSACTION)

def get(address, token, spender):
    """
    Get allowance by address, token and spender
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/allowance',
        params={'address': address, 'token': token, 'spender': spender})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: result = r.json()
    except: raise Exception('request: invalid request')

    return models.parse_values(result, models.ALLOWANCE)

def getByHash(hash):
    """
    Get allowance by hash
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/allowance',
        params={'hash': hash})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: result = r.json()
    except: raise Exception('request: invalid request')

    return models.parse_values(result, models.ALLOWANCE)

def scanByAddress(address, hash=None, created=None, sort='DESC', limit=25):
    """
    Scan allowances by address
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/allowances',
        params={'address': address, 'hash': hash, 'created': created, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.ALLOWANCE) for r in results]

def scanBySpender(spender, hash=None, created=None, sort='DESC', limit=25):
    """
    Scan allowances by spender
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/allowances',
        params={'spender': spender, 'hash': hash, 'created': created, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.ALLOWANCE) for r in results]