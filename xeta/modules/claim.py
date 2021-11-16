from xeta.modules import transaction
from xeta.library import models, utils
from xeta.library.config import config
import json
import time


def create(owner, token, tokenAmount, xetaAmount=None, expires=None, unlocks=None, frozen=None, category=None, meta=None, answer=None, number=None, raw=False):
    """
    Create claim
    """
    instruction = utils.strip({
        'function': 'claim.create',
        'owner': owner,
        'token': token,
        'tokenAmount': tokenAmount,
        'xetaAmount': xetaAmount,
        'expires': expires,
        'unlocks': unlocks,
        'frozen': frozen,
        'category': category,
        'meta': meta,
        'answer': answer,
        'number': number,
    })

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})

def update(tokenAmount=None, xetaAmount=None, expires=None, unlocks=None, frozen=None, category=None, meta=None, answer=None, number=None, raw=False):
    """
    Update claim
    """
    instruction = utils.strip({
        'function': 'claim.update',
        'tokenAmount': tokenAmount,
        'xetaAmount': xetaAmount,
        'expires': expires,
        'unlocks': unlocks,
        'frozen': frozen,
        'category': category,
        'meta': meta,
        'answer': answer,
        'number': number,
    })

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})

def transfer(claim, raw=False):
    """
    Transfer claim
    """
    instruction = utils.strip({
        'function': 'claim.transfer',
        'claim': claim,
        'to': to,
    })

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})

def resolve(claim, raw=False):
    """
    Resolve claim
    """
    instruction = utils.strip({
        'function': 'claim.resolve',
        'claim': claim,
    })

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})


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