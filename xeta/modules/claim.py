from xeta.library import models
from xeta.config import config
import requests


def get(address, token, owner):
    """
    Get claim by address, token and owner
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/claim',
        params={'address': address, 'token': token, 'owner': owner})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: result = r.json()
    except: raise Exception('request: invalid request')

    return models.parse_values(result, models.CLAIM)

def getByHash(hash):
    """
    Get claim by hash
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/claim',
        params={'hash': hash})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: result = r.json()
    except: raise Exception('request: invalid request')

    return models.parse_values(result, models.CLAIM)

def scanByAmount(owner, hash=None, amount=None, sort='DESC', limit=25):
    """
    Scan claims by amount
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/claims',
        params={'owner': owner, 'hash': hash, 'amount': amount if amount else 1, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.CLAIM) for r in results]

def scanByCreated(owner, hash=None, created=None, sort='DESC', limit=25):
    """
    Scan claims by created
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/claims',
        params={'owner': owner, 'hash': hash, 'created': created if created else 1, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.CLAIM) for r in results]