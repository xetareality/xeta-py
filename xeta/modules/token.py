from xeta.modules import transaction
from xeta.library import models
from xeta.config import config
import requests
import json
import time


def create(token, tx={}):
    """
    Create token
    """
    models.required_fields(token, ['name'])
    models.exclusive_fields(token, ['name', 'supply', 'ticker', 'reserve', 'description', 'links', 'object', 'meta', 'icon', 'mime'])
    models.valid_formats(token, models.TOKEN)

    assert token.get('supply') != 0, 'validation: supply cannot be 0'
    assert token.get('supply') in [None, 1] or token.get('ticker'), 'validation: fungible tokens require a ticker'

    result = transaction.create({**transaction.template(), **tx, **{
        'function': 'token.create',
        'message': json.dumps(token)
    }})

    try: result['data'] = models.parse_values(result['data'], models.TOKEN)
    except: pass

    return models.parse_values(result, models.TRANSACTION)

def update(token, tx):
    """
    Update specified values of an token
    """
    models.exclusive_fields(token, ['description', 'links', 'meta', 'icon'])
    models.required_fields(tx, ['token'])
    models.valid_formats(token, models.TOKEN)
    models.valid_formats(tx, models.TRANSACTION)

    result = transaction.create({**transaction.template(), **tx, **{
        'function': 'token.update',
        'message': json.dumps(token)
    }})

    try: result['data'] = models.parse_values(result['data'], models.TOKEN)
    except: pass

    return models.parse_values(result, models.TRANSACTION)

def mint(token, tx):
    """
    Mint from reserve
    """
    models.exclusive_fields(token, ['amount'])
    models.required_fields(tx, ['token'])
    models.valid_formats(tx, models.TRANSACTION)

    result = transaction.create({**transaction.template(), **tx, **{
        'function': 'token.mint',
        'message': json.dumps(token)
    }})

    try: result['data'] = models.parse_values(result['data'], models.TRANSACTION)
    except: pass

    return models.parse_values(result, models.TRANSACTION)

def batch(tokens):
    """
    Batch create NFTs
    Fungible tokens cannot be created in batch due to swap pool creation
    """
    assert len(tokens) <= 40, 'input: batch exceeds maximum items'
    assert all([t.get('supply') in [None, 1] for t in tokens]), 'validation: function only supports non-fungible tokens'

    for a in tokens:
        models.required_fields(a, ['name'])
        models.exclusive_fields(a, ['name', 'supply', 'ticker', 'description', 'links', 'object', 'meta', 'icon', 'mime'])
        models.valid_formats(a, models.TOKEN)

    result = transaction.create({**transaction.template(), **{
        'function': 'token.batch',
        'message': json.dumps(tokens)
    }})

    try: result['data'] =[models.parse_values(r, models.TOKEN) for r in result['data']]
    except: pass

    return models.parse_values(result, models.TRANSACTION)

def get(address):
    """
    Get token by address
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/token',
        params={'address': address})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: result = r.json()
    except: raise Exception('request: invalid request')

    return models.parse_values(result, models.TOKEN)

def batchGet(addresses):
    """
    Batch get tokens by addresses
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/tokens',
        params={'addresses': ','.join(addresses)})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByCreator(creator, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by creator
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/tokens',
        params={'creator': creator, 'address': address, 'created': created, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByTicker(ticker, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by ticker
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/tokens',
        params={'ticker': ticker, 'address': address, 'created': created, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByName(name, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by name
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/tokens',
        params={'name': name, 'address': address, 'created': created, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.TOKEN) for r in results]