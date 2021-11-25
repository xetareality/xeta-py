from xeta.modules import instruction, resource
from xeta.library import models, utils
from xeta.library.config import config
import json


def init(publicKey, privateKey=None):
    """
    Set public and private key
    """
    global config

    config['publicKey'] = publicKey
    config['privateKey'] = privateKey

def managed(account, secret, unsafe=None, create=None):
    """
    Connect to managed wallet
    """
    wallet = utils.request(
        method='POST',
        url=config['interface']+'/wallet',
        json=utils.strip({
            'account': account,
            'secret': secret,
            'unsafe': unsafe,
            'create': create
        }))

    init(wallet.get('publicKey'), wallet.get('privateKey'))
    return wallet

def sign(account, secret, tx):
    """
    Sign transaction with managed wallet
    Returns transaction with signature
    """
    models.validFormats(tx, models.TRANSACTION)

    return utils.request(
        method='POST',
        url=config['interface']+'/sign',
        json=utils.strip({
            'account': account,
            'secret': secret,
            'transaction': json.dumps(tx)
        }))