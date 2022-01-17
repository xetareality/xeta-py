from xeta.library.config import config
import json
import time


def requiredFields(obj, fields=[]):
    """
    Validates that required fields are present
    """
    if not fields: return
    for field in fields:
        assert obj.get(field) is not None, field+':required'

def exclusiveFields(obj, fields=[]):
    """
    Validates that obj has fields only from specified list
    """
    for k in obj.keys():
        assert k in fields, k+':invalid'

def filterFields(obj, fields=[]):
    """
    Filters out fields that are not in specified array
    """
    return {k: v for k, v in obj.items() if k in fields}

def stripFields(obj, fields=[]):
    """
    Removes fields that are specified in array
    """
    return {k: v for k, v in obj.items() if k not in fields}

def validFormats(obj, model):
    """
    Validates field formats based on model schema
    """
    for k, v in obj.items():
        assert k in obj.keys(), k+':invalid'

        t = model[k][0]
        if (t == 'string' and type(v) is str and len(v) > 0 and len(v) <= 256): continue
        elif (t == 'strings' and type(v) is list and len(v) and len(v) <= 100 and len(v) == len(set(v)) and all([type(w) is str and len(v) > 0 and len(w) <= 256 for w in v])): continue
        elif (t == 'number' and type(v) in [int, float] and v >= 0 and v <= 1e15 and v == round(v, 8)): continue
        elif (t == 'numbers' and type(v) is list and len(v) and len(v) <= 100 and len(v) == len(set(v)) and all([type(w) in [int, float] and w >= 0 and w <= 1e15 and w == round(w, 8) for w in v])): continue
        elif (t == 'hash' and type(v) is str and len(v) >= 32 and len(v) <= 44): continue
        elif (t == 'hashes' and type(v) is list and len(v) and len(v) <= 100 and len(v) == len(set(v)) and all([type(w) is str and len(w) >= 32 and len(w) <= 44 for w in v])): continue
        elif (t == 'text' and type(v) == str and len(v) <= 8192): continue
        elif (t == 'integer' and type(v) == int and v >= 0 and v <= 1e15): continue
        elif (t == 'timestamp' and type(v) == int and v >= 1e12 and v < 1e13): continue
        elif (t == 'amount' and type(v) == str and float(v) == round(float(v), 8) and float(v) >= 0 and float(v) <= 1e15): continue
        elif (t == 'boolean' and type(v) == bool): continue
        elif (t == 'object' and type(v) in [dict, list]): continue
        elif (t == 'index' and type(v) is str and len(v) == 8): continue
        else: raise Exception(k+':format')

TRANSACTION = {
    'hash': ['hash'],
    'signature': ['string'],
    'sender': ['hash'],
    'fee': ['amount'],
    'instructions': ['object'],
    'nonce': ['integer'],
    'created': ['timestamp'],
    'sponsored': ['boolean'],
    'period': ['integer'],
    'partition': ['string'],
    'outputs': ['object'],
    'error': ['string'],
    'confirmed': ['timestamp'],
    'confirmations': ['integer'],
}

TRANSFER = {
    'hash': ['hash'],
    'sender': ['hash'],
    'from': ['hash'],
    'to': ['hash'],
    'token': ['hash'],
    'amount': ['amount'],
    'created': ['timestamp'],
    'message': ['string'],
    'origin': ['hash'],
    'fromToken': ['index'],
    'toToken': ['index'],
}

BALANCE = {
    'hash': ['hash'],
    'address': ['hash'],
    'token': ['hash'],
    'amount': ['amount'],
}

ALLOWANCE = {
    'hash': ['hash'],
    'token': ['hash'],
    'address': ['hash'],
    'spender': ['hash'],
    'amount': ['amount'],
    'created': ['timestamp'],
    'origin': ['hash'],
}

TOKEN = {
    'address': ['hash'],
    'creator': ['hash'],
    'name': ['string'],
    'created': ['timestamp'],
    'origin': ['hash'],

    'description': ['string'],
    'links': ['strings'],
    'meta': ['object'],
    'preview': ['string'],

    'symbol': ['string'],
    'supply': ['amount'],
    'reserve': ['amount'],
    'whole': ['boolean'],

    'owner': ['hash'],
    'object': ['string'],
    'mime': ['string'],
    'content': ['string'],
    'frozen': ['boolean'],
    'category': ['string'],
    'ownerCategory': ['index'],
    'creatorCategory': ['index'],
}

CLAIM = {
    'hash': ['hash'],
    'creator': ['hash'],
    'created': ['timestamp'],
    'owner': ['hash'],
    'token': ['hash'],
    'tokenAmount': ['amount'],
    'xetaAmount': ['amount'],
    'expires': ['timestamp'],
    'unlocks': ['timestamp'],
    'origin': ['hash'],
    'resolved': ['timestamp'],
    'resolution': ['hash'],

    'frozen': ['boolean'],
    'category': ['string'],
    'meta': ['object'],
    'answer': ['string'],
    'number': ['number'],
    'holderCategory': ['index'],
    'issuerCategory': ['index'],

    'holder': ['index'],
    'issuer': ['index'],
    'holderToken': ['index'],
    'issuerToken': ['index'],
    'issuerHolder': ['index'],
    'issuerHolderToken': ['index'],
}

POOL = {
    'address': ['hash'],
    'creator': ['hash'],
    'token': ['hash'],
    'program': ['string'],
    'created': ['timestamp'],
    'origin': ['hash'],
    'tokenProgram': ['index'],
    'creatorProgram': ['index'],
    'activeProgram': ['string'],
    
    'name': ['string'],
    'description': ['string'],
    'mechanism': ['string'],
    'candidates': ['strings'],
    'rate': ['number'],
    'percentage': ['number'],
    'answers': ['strings'],
    'meta': ['object'],

    'expires': ['timestamp'],
    'minAmount': ['amount'],
    'maxAmount': ['amount'],
    'minTime': ['integer'],
    'maxTime': ['integer'],
    'transfersLimit': ['integer'],
    'claimsLimit': ['integer'],
    'tokenLimit': ['amount'],
    'xetaLimit': ['amount'],
    'tokenTarget': ['amount'],
    'xetaTarget': ['amount'],

    'xetaBalance': ['amount'],
    'tokenBalance': ['amount'],
    'xetaTurnover': ['amount'],
    'tokenTurnover': ['amount'],
    'transfersCount': ['integer'],
    'claimsCount': ['integer'],
    'closed': ['boolean'],
    'number': ['number'],
}

WALLET = {
    'hash': ['hash'],
    'account': ['string'],
    'secret': ['hash'],
    'publicKey': ['hash'],
    'privateKey': ['hash'],
    'created': ['timestamp'],
}

CANDLE = {
    'key': ['string'],
    'period': ['string'],
    'time': ['integer'],
    'open': ['amount'],
    'high': ['amount'],
    'low': ['amount'],
    'close': ['amount'],
    'change': ['number'],
    'volume': ['amount'],
    'turnover': ['amount'],
    'trades': ['integer'],
    'first': ['timestamp'],
    'last': ['timestamp'],
}

STATISTIC = {
    'key': ['string'],
    'time': ['integer'],
    'until': ['integer'],
    'value': ['number'],
}

OBJECT = {
    'hash': ['hash'],
    'url': ['string'],
    'mime': ['string'],
    'content': ['hash'],
    'fingerprint': ['string'],
    'cluster': ['string'],
    'processed': ['timestamp'],
    'created': ['timestamp'],
}