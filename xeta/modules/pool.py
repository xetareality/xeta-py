from xeta.programs import auction, launch, lending, lock, loot, lottery, royalty, staking, swap, vote
from xeta.modules import instruction, resource
from xeta.library import models, utils, hashed
from xeta.library.config import config


def create(token, program, name=None, mechanism=None, candidates=None, rate=None, percentage=None, probability=None, expires=None, answers=None, meta=None, minAmount=None, maxAmount=None, minTime=None, maxTime=None, transfersLimit=None, claimsLimit=None, tokenLimit=None, xetaLimit=None, tokenTarget=None, xetaTarget=None, tx={}):
    """
    Create pool
    """
    assert program in ['auction', 'launch', 'lending', 'lock', 'loot', 'lottery', 'royalty', 'staking', 'vote'], 'program:invalid'

    return instruction.wrap({
        'function': 'pool.create',
        'token': token,
        'program': program,
        'name': name,
        'mechanism': mechanism,
        'candidates': candidates,
        'rate': rate,
        'percentage': percentage,
        'probability': probability,
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