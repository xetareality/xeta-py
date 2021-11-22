from xeta.library import models, utils
from xeta.library.config import config


def read(type, key, sort=None, sortValue=None, fields=None, preview=None):
    """
    Read resource by key
    """
    assert type in ['transaction', 'transfer', 'balance', 'allowance', 'token', 'claim', 'pool', 'candle', 'statistic', 'lookup'], 'type:invalid'

    if type in ['token', 'pool'] keyName = 'address'
    elif type in ['statistic', 'candle']: keyName = 'key'
    else: keyName = 'hash'

    return utils.request(
        method='GET',
        url=config['interface']+'/read',
        params=utils.strip({
            'type': type,
            'key': keyName,
            'keyValue': key,
            'sort': sort,
            'sortValue': sortValue,
            'preview': preview,
        }))

def list(type, keys, sort=None, sortValues=None, fields=None, preview=None):
    """
    List resources by keys
    """
    assert type in ['transaction', 'transfer', 'balance', 'allowance', 'token', 'claim', 'pool', 'candle', 'statistic', 'lookup'], 'type:invalid'

    if type in ['token', 'pool'] keyName = 'address'
    elif type in ['statistic', 'candle']: keyName = 'key'
    else: keyName = 'hash'

    return utils.request(
        method='GET',
        url=config['interface']+'/read',
        params=utils.strip({
            'type': type,
            'key': keyName,
            'keyValues': ','.join(keys),
            'sort': sort,
            'sortValues': sortValues,
            'preview': preview,
        }))