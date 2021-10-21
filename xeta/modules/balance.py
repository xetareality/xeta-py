from xeta.library import models
from xeta.config import config
import requests


def get(address, token):
    """
    Get balance by address and token
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/balance',
        params={'address': address, 'token': token})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: result = r.json()
    except: raise Exception('request: invalid request')

    return models.parse_values(result, models.BALANCE)

def scanByAddress(address, token=None, amount=None, sort='DESC', limit=25):
    """
    Scan balances by address
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/balances',
        params={'address': address, 'token': token, 'amount': amount, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.BALANCE) for r in results]

def scanByToken(token, address=None, amount=None, sort='DESC', limit=25):
    """
    Scan balances by address
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/balances',
        params={'token': token, 'address': address, 'amount': amount, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.BALANCE) for r in results]