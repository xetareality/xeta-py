from xeta.library import hashing, models, crypto
from xeta.config import config
import requests
import json
import time


def template():
    """
    Template transaction
    """
    return {
        'sender': config['public_key'],
        'from': config['public_key'],
        'to': config['factory_address'],
        'token': config['xeta_address'],
        'nonce': int(time.time())*1000,
        'amount': 0}

def create(tx):
    """
    Create transaction
    """
    tx = {k: v for k, v in tx.items() if v is not None}
    models.required_fields(tx, ['to', 'amount'])
    models.exclusive_fields(tx, ['sender', 'token', 'from', 'to', 'amount', 'nonce', 'message', 'function', 'delegate'])
    models.valid_formats(tx, models.TRANSACTION)

    tx = {**template(), **tx}

    if tx['to'] == tx['from'] and tx.get('function') != 'transaction.sponsor': raise Exception('to and from cannot be equal')
    if tx.get('function') and tx['function'] != tx['function'].lower(): raise Exception('invalid function')
    tx['signature'] = crypto.sign(hashing.hash_transaction(tx), config['private_key'])

    r = requests.request(
        method='POST',
        url=config['network']+'/transaction',
        json=tx)

    if r.status_code == 400: raise Exception(r.text)
    elif r.status_code != 200: raise Exception('request: invalid request')
    
    try: result = r.json()
    except: raise Exception('request: invalid request')

    if result.get('error'): raise Exception(result['error'])
    return result

def batch_ft(txns, tx):
    """
    Batch create FTs
    Only possible for simple transfers to non-pools
    """
    models.required_fields(tx, ['amount', 'token'])
    models.valid_formats(tx, models.TRANSACTION)

    for t in txns:
        models.required_fields(t, ['to', 'amount'])
        models.exclusive_fields(t, ['to', 'amount'])
        models.valid_formats(t, models.TRANSACTION)

    assert len(txns) == len(set([t['to'] for t in txns])), 'validation: contains duplicate recipients'
    assert all([t['amount'] > 0 for t in txns]), 'validation: amounts must be positive'
    assert tx['amount'] == sum([t['amount'] for t in txns]), 'validation: inconsistent amounts'

    result = create({**template(), **tx, **{
        'function': 'transaction.batch',
        'message': json.dumps(txns),
    }})

    try: result['data'] = [models.parse_values(r, models.TRANSACTION) for r in result['data']]
    except: pass

    return models.parse_values(result, models.TRANSACTION) 

def batch_nft(txns):
    """
    Batch create NFTs
    """
    tx = template() # For static nonce

    for t in txns:
        models.required_fields(t, ['to', 'token'])
        models.exclusive_fields(t, ['to', 'token'])
        models.valid_formats(t, models.TRANSACTION)
        t['signature'] = crypto.sign(hashing.hash_transaction({**{'sender': tx['sender'], 'from': tx['from'], 'amount': tx['amount'], 'nonce': tx['nonce']}, **t}), config['private_key'])

    result = create({**tx, **{
        'function': 'transaction.batch',
        'message': json.dumps(txns),
    }})

    try: result['data'] = [models.parse_values(r, models.TRANSACTION) for r in result['data']]
    except: pass

    return models.parse_values(result, models.TRANSACTION)

def sponsor(tx):
    """
    Sponsor xeta for delegated transfers
    """
    models.required_fields(tx, ['to', 'amount'])
    models.exclusive_fields(tx, ['from', 'to', 'amount', 'nonce'])
    models.valid_formats(tx, models.TRANSACTION)

    result = create({**template(), **tx, **{
        'to': tx['to'],
        'amount': tx['amount'],
        'function': 'transaction.sponsor',
    }})

    return models.parse_values(result, models.TRANSACTION)

def get(signature):
    """
    Get transaction by signature
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/transaction',
        params={'signature': signature})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: result = r.json()
    except: raise Exception('request: invalid request')

    return models.parse_values(result, models.TRANSACTION)

def batchGet(signatures):
    """
    Batch get transactions by signature
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/transactions',
        params={'signatures': ','.join(signatures)})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.TRANSACTION) for r in results]

def poll(signature, interval=0.5, timeout=5):
    """
    Poll periodically, to receive confirmation response
    """
    t = time.time()
    tx = {}

    while time.time() < t+timeout:
        r = requests.request(
            method='GET',
            url=config['interface']+'/transaction',
            params={'signature': signature})

        if r.status_code == 400: raise Exception(r.text)
        elif r.status_code != 200: raise Exception('request: invalid request')

        try: return models.parse_values(r.json(), models.TRANSACTION)
        except: pass

def scanByFrom(from_address, signature=None, created=None, sort='DESC', limit=25):
    """
    Scan transactions by from
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/transactions',
        params={'from': from_address, 'signature': signature, 'created': created, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.TRANSACTION) for r in results]

def scanByTo(to, signature=None, created=None, sort='DESC', limit=25):
    """
    Scan transactions by to
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/transactions',
        params={'to': to, 'signature': signature, 'created': created, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.TRANSACTION) for r in results]

def scanBySender(sender, signature=None, created=None, sort='DESC', limit=25):
    """
    Scan transactions by sender
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/transactions',
        params={'sender': sender, 'signature': signature, 'created': created, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.TRANSACTION) for r in results]

def scanByToken(token, signature=None, created=None, sort='DESC', limit=25):
    """
    Scan transactions by token
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/transactions',
        params={'token': token, 'signature': signature, 'created': created, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.TRANSACTION) for r in results]

def scanByPeriod(period, signature=None, created=None, sort='DESC', limit=25):
    """
    Scan transactions by period
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/transactions',
        params={'period': period, 'signature': signature, 'created': created, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.TRANSACTION) for r in results]

def scanByFromToken(from_address, token, signature=None, created=None, sort='DESC', limit=25):
    """
    Scan transactions by from and token
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/transactions',
        params={'from': from_address, 'token': token, 'signature': signature, 'created': created, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.TRANSACTION) for r in results]

def scanByToToken(to, token, signature=None, created=None, sort='DESC', limit=25):
    """
    Scan transactions by to and token
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/transactions',
        params={'to': to, 'token': token, 'signature': signature, 'created': created, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.TRANSACTION) for r in results]