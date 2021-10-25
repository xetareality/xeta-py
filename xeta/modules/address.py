from xeta.modules import transaction
from xeta.library import models
from xeta.config import config
import requests
import json
import time


def get(address):
    """
    Get address data (account & balance)
    """
    r = requests.request(
        method='GET',
        url=config['interface']+'/address',
        params={'address': address})

    if r.status_code == 400: raise Exception(r.text)
    elif not r.text: return

    try: result = r.json()
    except: raise Exception('request: invalid request')

    return {'balance': models.parse_values(result.get('balance'), models.BALANCE), 'account': models.parse_values(result.get('account'), models.TOKEN)}

def update(values):
    """
    Update address values
    """
    models.exclusive_fields(values, ['name', 'object', 'description', 'links', 'meta'])
    models.valid_formats(values, models.TOKEN)

    result = transaction.create({**transaction.template(), **{
        'function': 'address.update',
        'message': json.dumps(values)
    }})

    try: result['data'] = models.parse_values(result['data'], models.TOKEN)
    except: pass

    return models.parse_values(result, models.TRANSACTION)