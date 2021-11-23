from xeta.modules import instruction, resource
from xeta.library import models, utils, hashed
from xeta.library.config import config


def create(name, symbol=None, supply=None, reserve=None, description=None, links=None, meta=None, icon=None, owner=None, frozen=None, category=None, object=None, mime=None, tx={}):
    """
    Create token
    """
    token = utils.strip({
        'function': 'token.create',
        'name': name,
        'symbol': symbol,
        'supply': utils.amount(supply),
        'reserve': utils.amount(reserve),
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
        models.required_fields(token, ['name', 'symbol', 'supply'])
        models.exclusive_fields(token, ['function', 'name', 'description', 'links', 'meta', 'icon', 'symbol', 'supply', 'reserve'])
    else:
        models.required_fields(token, ['name'])
        models.exclusive_fields(token, ['function', 'name', 'description', 'links', 'meta', 'icon', 'owner', 'frozen', 'category', 'object', 'mime'])

    return instruction.wrap(token, tx)

def update(token, name=None, description=None, links=None, meta=None, icon=None, frozen=None, category=None, object=None, mime=None, tx={}):
    """
    Update specified values of an token
    """
    return instruction.wrap({
        'function': 'token.update',
        'token': token,
        'name': name,
        'description': description,
        'links': links,
        'meta': meta,
        'icon': icon,
        'frozen': frozen,
        'category': category,
        'object': object,
        'mime': mime,
    }, tx)

def mint(token, amount, tx={}):
    """
    Mint from reserve
    """
    return instruction.wrap({
        'function': 'token.mint',
        'token': token,
        'amount': utils.amount(amount),
    }, tx)

def transfer(token, to, tx={}):
    """
    Transfer from token
    """
    return instruction.wrap({
        'function': 'token.transfer',
        'token': token,
        'to': to,
    }, tx)

def read(address, args={}):
    """
    Read token by address
    """
    return resource.read(**{**{
        'type': 'token',
        'key': address,
    }, **args})

def list(addresses, args={}):
    """
    List tokens by addresses
    """
    return resource.list(**{**{
        'type': 'token',
        'keys': addresses,
    }, **args})

def scanCreatorCreated(creator, created=None, address=None, args={}):
    """
    Scan tokens by creator, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'creator',
        'indexValue': creator,
        'sort': 'created',
        'sortValue': created,
        'keyValue': address,
    }, **args})

def scanNameCreated(name, created=None, address=None, args={}):
    """
    Scan tokens by name, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'name',
        'indexValue': name,
        'sort': 'created',
        'sortValue': created,
        'keyValue': address,
    }, **args})

def scanSymbolCreated(symbol, created=None, address=None, args={}):
    """
    Scan tokens by symbol, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'symbol',
        'indexValue': symbol,
        'sort': 'created',
        'sortValue': created,
        'keyValue': address,
    }, **args})

def scanOwnerCreated(owner, created=None, address=None, args={}):
    """
    Scan tokens by owner, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'owner',
        'indexValue': owner,
        'sort': 'created',
        'sortValue': created,
        'keyValue': address,
    }, **args})

def scanOwnerCategoryCreated(owner, category, created=None, address=None, args={}):
    """
    Scan tokens by owner and category, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'ownerCategory',
        'indexValue': hashed.values([owner, category])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': address,
    }, **args})

def scanCreatorCategoryCreated(creator, category, created=None, address=None, args={}):
    """
    Scan tokens by creator and category, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'creatorCategory',
        'indexValue': hashed.values([creator, category])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': address,
    }, **args})