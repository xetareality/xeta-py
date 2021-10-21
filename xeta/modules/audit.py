from xeta.config import config
import requests


def balance(address, token, limit=1):
    """
    Request an token balance audit
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/audit',
        params={'address': address, 'token': token, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: return r.json()
    except: raise Exception('request: invalid request')

def xeta(address, limit=1):
    """
    Request a xeta balanace audit
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/audit',
        params={'address': address, 'token': config['xeta_address'], 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: return r.json()
    except: raise Exception('request: invalid request')

def transaction(signature):
    """
    Request a transaction audit
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/audit',
        params={'signature': signature})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: return r.json()
    except: raise Exception('request: invalid request')