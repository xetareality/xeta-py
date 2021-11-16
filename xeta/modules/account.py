from xeta.modules import transaction
from xeta.library import models, utils
from xeta.library.config import config
import json
import time


def get(address):
    """
    Get address data (account & balance)
    """
    result = utils.request(
        method='GET',
        url=config['interface']+'/address',
        params={'address': address})

    return {
        'pool': models.parse_values(results['pool'], models.POOL),
        'balance': models.parse_values(result['balance'], models.BALANCE),
        'account': models.parse_values(result['account'], models.TOKEN)}

def update(name, object=None, description=None, links=None, meta=None, raw=False):
    """
    Update (or create) account
    """
    instruction = utils.strip({
        'function': 'account.update',
        'name': name,
        'object': object,
        'description': description,
        'links': links,
        'meta': meta,
    })

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})