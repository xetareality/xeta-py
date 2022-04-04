from xeta.programs import auction, launch, lending, lock, loot, lottery, royalty, staking, swap, vote
from xeta.modules import instruction, resource
from xeta.library import models, utils, hashed
from xeta.library.config import config


def create(token, program, name=None, description=None, type=None, candidates=None, rate=None, percentage=None, number=None, expires=None, answers=None, meta=None, minAmount=None, maxAmount=None, minTime=None, maxTime=None, transfersLimit=None, claimsLimit=None, tokenLimit=None, xetaLimit=None, tokenTarget=None, xetaTarget=None, tx={}):
    """
    Create pool
    """
    return instruction.wrap({
        'function': 'pool.create',
        'token': token,
        'program': program,
        'name': name,
        'description': description,
        'type': type,
        'candidates': candidates,
        'rate': rate,
        'percentage': percentage,
        'number': number,
        'expires': expires,
        'answers': answers,
        'meta': meta,
        'minAmount': utils.amount(minAmount),
        'maxAmount': utils.amount(maxAmount),
        'minTime': minTime,
        'maxTime': maxTime,
        'transfersLimit': transfersLimit,
        'claimsLimit': claimsLimit,
        'tokenLimit': utils.amount(tokenLimit),
        'xetaLimit': utils.amount(xetaLimit),
        'tokenTarget': utils.amount(tokenTarget),
        'xetaTarget': utils.amount(xetaTarget),
    }, tx)

def instance(address, args={}):
    """
    Get pool by address
    Return as program instance
    """
    pool = read(address, args)
    if not pool: return
    instance = getattr(globals()[pool['program']], pool['program'].capitalize())
    return instance(pool)

def read(address, args={}):
    """
    Read pool by address
    """
    return resource.read(**{**{
        'type': 'pool',
        'key': address,
    }, **args})

def list(addresses, args={}):
    """
    List pools by addresses
    """
    return resource.list(**{**{
        'type': 'pool',
        'keys': addresses,
    }, **args})

def scanTokenProgramCreated(token, program, created=None, address=None, args={}):
    """
    Scan pools by token and program, sort by created
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'tokenProgram',
        'indexValue': hashed.values([token, program])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': address,
    }, **args})

def scanCreatorProgramCreated(creator, program, created=None, address=None, args={}):
    """
    Scan pools by creator and program, sort by created
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'creatorProgram',
        'indexValue': hashed.values([creator, program])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': address,
    }, **args})

def scanNameCreated(name, created=None, address=None, args={}):
    """
    Scan pools by name, sort by created
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'name',
        'indexValue': name,
        'sort': 'created',
        'sortValue': created,
        'keyValue': address,
    }, **args})

def scanCreatorCreated(creator, created=None, address=None, args={}):
    """
    Scan pools by creator, sort by created
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'creator',
        'indexValue': creator,
        'sort': 'created',
        'sortValue': created,
        'keyValue': address,
    }, **args})


def scanProgramCreated(program, created=None, address=None, args={}):
    """
    Scan pools by active program, sort by created
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'created',
        'sortValue': created,
        'keyValue': address,
    }, **args})

def scanProgramExpires(program, expires=None, address=None, args={}):
    """
    Scan pools by active program, sort by expires
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'expires',
        'sortValue': expires,
        'keyValue': address,
    }, **args})

def scanProgramNumber(program, number=None, address=None, args={}):
    """
    Scan pools by active program, sort by number
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'number',
        'sortValue': number,
        'keyValue': address,
    }, **args})

def scanProgramXetaBalance(program, xetaBalance=None, address=None, args={}):
    """
    Scan pools by active program, sort by xetaBalance
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'xetaBalance',
        'sortValue': xetaBalance,
        'keyValue': address,
    }, **args})

def scanProgramTokenBalance(program, tokenBalance=None, address=None, args={}):
    """
    Scan pools by active program, sort by tokenBalance
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'tokenBalance',
        'sortValue': tokenBalance,
        'keyValue': address,
    }, **args})

def scanProgramTransfersCount(program, transfersCount=None, address=None, args={}):
    """
    Scan pools by active program, sort by transfersCount
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'transfersCount',
        'sortValue': transfersCount,
        'keyValue': address,
    }, **args})

def scanProgramType(program, type=None, address=None, args={}):
    """
    Scan pools by active program, sort by type
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'type',
        'sortValue': type,
        'keyValue': address,
    }, **args})