from xeta.library import hashed, models, wallet, utils
from xeta.library.config import config
import json
import time


def submit(instructions, tx={}):
    """
    Create transaction
    """
    tx = utils.strip({**{
        'instructions': instructions,
        'sender': config['public_key'],
        'nonce': int(time.time())}, **tx})

    models.exclusive_fields(tx, ['signature', 'sender', 'instructions', 'nonce', 'sponsored'])
    models.valid_formats(tx, models.TRANSACTION)

    if not tx.get('signature') and not config['private_key']: return tx
    if not tx.get('signature'): tx['signature'] = wallet.sign(hashed.transaction(tx), config['private_key'])

    result = utils.request(
        method='POST',
        url=config['network']+'/transaction',
        json=tx)

    if result.get('error'): raise Exception(result['error'])
    return result

def poll(hash, interval=0.5, timeout=5):
    """
    Poll a transaction
    """
    start = time.time()
    while time.time() < start+timeout:
        result = readHash(hash)
        if result: return r.json()
        else: time.sleep(interval)

def readHash(hash, args={}):
    """
    Read transaction by hash
    """
    return resource.read(**{**{
        'type': 'transaction',
        'key': hash,
    }, **args})

def listHashes(hashes, args={}):
    """
    List transactions by hashes
    """
    return resource.list(**{**{
        'type': 'transaction',
        'keys': hashes,
    }, **args})

def scanSenderCreated(sender, created=None, hash=None, args={}):
    """
    Scan transactions by sender, sorted by created
    """
    return resource.scan(**{**{
        'type': 'transaction',
        'index': 'sender,
        'indexValue': sender,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanPeriodCreated(period, created=None, hash=None, args={}):
    """
    Scan transactions by period, sorted by created
    """
    return resource.scan(**{**{
        'type': 'transaction',
        'index': 'period,
        'indexValue': period,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})