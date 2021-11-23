from xeta.modules import instruction, resource
from xeta.library import models, utils
from xeta.library.config import config
import time as tm

def read(interval, token, time, args={}):
    """
    Read candle by key (interval:token) and time
    """
    if time is None: time = str(int(tm.time()) - int(tm.time()) % (60*60*24))

    return resource.read(**{**{
        'type': 'candle',
        'key': interval+':'+token,
        'sort': 'time',
        'sortValue': time,
    }, **args})

def scanIntervalTokenTime(interval, token, time=None, key=None, args={}):
    """
    Scan candles by token and interval, sort by time
    """
    return resource.scan(**{**{
        'type': 'candle',
        'index': None,
        'indexValue': None,
        'sort': 'time',
        'sortValue': time,
        'keyValue': interval+':'+token,
    }, **args})

def scanIntervalTimeTurnover(interval, time=None, turnover=None, key=None, args={}):
    """
    Scan candles by interval and time, sort by turnover
    """
    if time is None: time = str(int(tm.time()) - int(tm.time()) % (60*60*24))

    return resource.scan(**{**{
        'type': 'candle',
        'index': 'period',
        'indexValue': interval+':'+time,
        'sort': 'turnover',
        'sortValue': turnover,
        'keyValue': key,
    }, **args})

def scanIntervalTimeChange(interval, time=None, change=None, key=None, args={}):
    """
    Scan candles by interval and time, sort by change
    """
    if time is None: time = str(int(tm.time()) - int(tm.time()) % (60*60*24))

    return resource.scan(**{**{
        'type': 'candle',
        'index': 'period',
        'indexValue': interval+':'+time,
        'sort': 'change',
        'sortValue': change,
        'keyValue': key,
    }, **args})