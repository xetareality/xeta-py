from xeta.modules import transaction
from xeta.library import models, utils
from xeta.library.config import config
import json
import time


def create(name, ticker=None, supply=None, reserve=None, description=None, links=None, meta=None, icon=None, owner=None, category=None, object=None, mime=None, token=None, tokenAmount=None, xetaAmount=None, expires=None, unlocks=None, answer=None, number=None, tx={}):
    """
    Create token
    """
    assert not supply or (supply and ticker), 'validation: fungible tokens require a ticker'

    return transaction.create({**tx, **{
        'function': 'token.create',
        'message': json.dumps(utils.strip({
            'name': name,
            'ticker': ticker,
            'supply': supply,
            'reserve': reserve,
            'description': description,
            'links': links,
            'meta': meta,
            'icon': icon,
            'owner': owner,
            'category': category,
            'object': object,
            'mime': mime,
            'token': token,
            'tokenAmount': tokenAmount,
            'xetaAmount': xetaAmount,
            'expires': expires,
            'unlocks': unlocks,
            'answer': answer,
            'number': number,
        }))
    }})

def update(token, description=None, links=None, meta=None, icon=None, category=None, frozen=None, tx={}):
    """
    Update specified values of an token
    """
    return transaction.create({**tx, **{
        'token': token,
        'function': 'token.update',
        'message': json.dumps(utils.strip({
            'description': description,
            'links': links,
            'meta': meta,
            'icon': icon,
            'category': category,
            'frozen': frozen,
        }))
    }})

def mint(token, amount, tx={}):
    """
    Mint from reserve
    """
    return transaction.create({**tx, **{
        'token': token,
        'function': 'token.mint',
        'message': json.dumps({'amount': amount})
    }})

def transfer(from_address, to, token, amount, tx={}):
    """
    Transfer from token
    """
    return transaction.create({**tx, **{
        'from': from_address,
        'to': to,
        'token': token,
        'amount': amount,
        'function': 'token.transfer',
    }})

def batch(tokens, tx={}):
    """
    Batch create NFTs
    Fungible tokens cannot be created in batch due to swap pool creation
    """
    assert len(tokens) <= 20, 'input: batch exceeds maximum items'

    for t in tokens:
        models.required_fields(t, ['name'])
        models.exclusive_fields(t, ['name', 'description', 'links', 'meta', 'icon', 'owner', 'category', 'object', 'mime', 'token', 'tokenAmount', 'xetaAmount', 'expires', 'unlocks', 'answer', 'number'])
        models.valid_formats(t, models.TOKEN)

    return transaction.create({**{
        'function': 'token.batch',
        'message': json.dumps(tokens)
    }})

def get(address):
    """
    Get token by address
    """
    return models.parse_values(utils.request(
        method='GET',
        url=config['interface']+'/token',
        params={'address': address}
    ), models.TOKEN)

def batchGet(addresses):
    """
    Batch get tokens by addresses
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params={'addresses': ','.join(addresses)})

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByCreator(creator, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by creator
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'creator': creator, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByTicker(ticker, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by ticker
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'ticker': ticker, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByName(name, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by name
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'name': name, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByOwner(owner, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by owner
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'owner': owner, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByOwnerCategory(owner, category=None, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by owner and category
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'owner': owner, 'category': category, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByCreatorCategory(creator, category=None, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by creator and category
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'creator': creator, 'category': category, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByHash(hash, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by hash
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'hash': hash, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByFingerprint(fingerprint, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by fingerprint
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'fingerprint': fingerprint, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByCluster(cluster, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by cluster
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'cluster': cluster, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByClaim(creator, owner, token, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by claim
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'creator': creator, 'owner': owner, 'token': token, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByHolder(holder, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by holder
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'holder': holder, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByIssuer(cluster, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by issuer
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'issuer': issuer, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByIssuerAmount(issuer, address=None, amount=None, sort='DESC', limit=25):
    """
    Scan tokens by issuer sorted by amount
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'issuer': issuer, 'address': address, 'amount': amount, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByIssuerRandom(issuer, address=None, random=None, sort='DESC', limit=25):
    """
    Scan tokens by issuer sorted by random
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'issuer': issuer, 'address': address, 'random': random, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByIssuerAnswer(issuer, address=None, answer=None, sort='DESC', limit=25):
    """
    Scan tokens by issuer and answer
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'issuer': issuer, 'address': address, 'answer': answer, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]

def scanByIssuerNumber(issuer, address=None, number=None, sort='DESC', limit=25):
    """
    Scan tokens by issuer and number
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'issuer': issuer, 'address': address, 'number': number, 'sort': sort, 'limit': limit}))

    return [models.parse_values(r, models.TOKEN) for r in results]