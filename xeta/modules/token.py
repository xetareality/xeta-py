from xeta.modules import transaction
from xeta.library import models, utils
from xeta.library.config import config
import json
import time


def create(name, symbol=None, supply=None, reserve=None, description=None, links=None, meta=None, icon=None, owner=None, frozen=None, category=None, object=None, mime=None, raw=False):
    """
    Create token
    """
    instruction = utils.strip({
        'function': 'token.create',
        'name': name,
        'symbol': symbol,
        'supply': supply,
        'reserve': reserve,
        'description': description,
        'links': links,
        'meta': meta,
        'icon': icon,
        'owner': owner,
        'frozen': frozen,
        'category': category,
        'object': object,
        'mime': mime,
    })

    if supply:
        models.required_fields(instruction, ['name', 'symbol', 'supply'])
        models.exclusive_fields(instruction, ['function', 'name', 'description', 'links', 'meta', 'icon', 'symbol', 'supply', 'reserve'])
    else:
        Fields.required_fields(instruction, ['name'])
        Fields.exclusive_fields(instruction, ['function', 'name', 'description', 'links', 'meta', 'icon', 'owner', 'frozen', 'category', 'object', 'mime'])

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})

def update(token, name=None, description=None, links=None, meta=None, icon=None, frozen=None, category=None, object=None, mime=None, raw=False):
    """
    Update specified values of an token
    """
    instruction = utils.strip({
        'function': 'token.update',
        'name': name,
        'description': description,
        'links': links,
        'meta': meta,
        'icon': icon,
        'frozen': frozen,
        'category': category,
        'object': object,
        'mime': mime,
    })

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})

def mint(token, amount, raw=False):
    """
    Mint from reserve
    """
    instruction = utils.strip({
        'function': 'token.mint',
        'token': token,
        'amount': utils.amount(amount),
    })

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})

def transfer(token, to, raw=False):
    """
    Transfer from token
    """
    instruction = utils.strip({
        'function': 'token.transfer',
        'token': token,
        'to': to,
    })

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})

def withdraw(token, to, amount, raw=False):
    """
    Withdraw tokens that token holds
    """
    instruction = utils.strip({
        'function': 'token.withdraw',
        'token': token,
        'to': to,
        'amount': utils.amount(amount),
    })

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})

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

def scanBysymbol(symbol, address=None, created=None, sort='DESC', limit=25):
    """
    Scan tokens by symbol
    """
    results = utils.request(
        method='GET',
        url=config['interface']+'/tokens',
        params=utils.strip({'symbol': symbol, 'address': address, 'created': created, 'sort': sort, 'limit': limit}))

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