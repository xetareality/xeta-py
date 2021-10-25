from xeta.library import models
from xeta.config import config
import time as tm
import requests


def scan(token, interval, time=None, sort='DESC', limit=100):
    """
    Scan candles by token and interval
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/candles',
        params={'token': token, 'interval': interval, 'time': time, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.CANDLE) for r in results]

def scanByTurnover(interval='1d', time=None, key=None, sort='DESC', limit=100):
    """
    Scan candles by interval and time sorted by turnover
    """
    if time is None: time = int(tm.time()) - int(tm.time()) % (60*60*24)

    r = requests.request(
        method='GET',
        url=config['interface']+'/candles',
        params={'interval': interval, 'time': time, 'key': key, 'turnover': 1, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.CANDLE) for r in results]

def scanByChange(interval='1d', time=None, key=None, sort='DESC', limit=100):
    """
    Scan candles by interval and time sorted by change
    """
    if time is None: time = int(tm.time()) - int(tm.time()) % (60*60*24)

    r = requests.request(
        method='GET',
        url=config['interface']+'/candles',
        params={'interval': interval, 'time': time, 'key': key, 'change': 1, 'sort': sort, 'limit': limit})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: results = r.json()
    except: raise Exception('request: invalid request')

    return [models.parse_values(r, models.CANDLE) for r in results]