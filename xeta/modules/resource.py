from xeta.library import utils
from xeta.library.config import config


def read(type, key, sort=None, sortValue=None, fields=None, preview=None):
    """
    Read resource by key
    """
    assert type in ['allowance', 'balance', 'candle', 'claim', 'object', 'pool', 'statistic', 'token', 'transaction', 'transfer', 'wallet'], 'type:invalid'

    return utils.request(
        method='GET',
        url=config['interface']+'/read',
        params=utils.strip({
            'type': type,
            'keyValue': key,
            'sort': sort,
            'sortValue': sortValue,
            'preview': preview,
        }))

def list(type, keys, sort=None, sortValues=None, fields=None, preview=None):
    """
    List resources by keys
    """
    assert type in ['allowance', 'balance', 'candle', 'claim', 'object', 'pool', 'statistic', 'token', 'transaction', 'transfer', 'wallet'], 'type:invalid'

    return utils.request(
        method='GET',
        url=config['interface']+'/list',
        params=utils.strip({
            'type': type,
            'keyValues': ','.join(keys),
            'sort': sort,
            'sortValues': sortValues,
            'preview': preview,
        }))

def scan(type, index, indexValue, sort=None, sortValue=None, keyValue=None, operator=None, asc=False, limit=None, preview=None):
    """
    Scan resources by index
    Candles and statistics support scanning without index (by key, sorted by time)
    """
    assert type in ['allowance', 'balance', 'candle', 'claim', 'object', 'pool', 'statistic', 'token', 'transaction', 'transfer', 'wallet'], 'type:invalid'

    if type in ['candle', 'statistic']: limit = min(limit, 1000) if limit else 200
    else: limit = min(limit, 25) if limit else 25

    return utils.request(
        method='GET',
        url=config['interface']+'/scan',
        params=utils.strip({
            'type': type,
            'keyValue': keyValue,
            'index': index,
            'indexValue': indexValue,
            'sort': sort,
            'sortValue': sortValue,
            'operator': operator,
            'asc': asc,
            'limit': limit,
            'preview': preview,
        }))