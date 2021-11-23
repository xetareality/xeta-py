from xeta.modules import instruction, resource
from xeta.library import models, utils
from xeta.library.config import config
import json


def init(seed, password, unsafe=None, create=None):
    """
    Read or create credentials
    """
    return utils.request(
        method='POST',
        url=config['interface']+'/credentials',
        json=utils.strip({
            'seed': seed,
            'password': password,
            'unsafe': unsafe,
            'create': create
        }))

def sign(seed, password, tx):
    """
    Sign transaction with managed credentials
    Returns transaction with signature
    """
    models.valid_formats(tx, models.TRANSACTION)

    return utils.request(
        method='POST',
        url=config['interface']+'/sign',
        json=utils.strip({
            'seed': seed,
            'password': password,
            'transaction': json.dumps(tx)
        }))