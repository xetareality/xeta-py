from xeta.config import config
import json
import time


def parse_values(obj, model):
    """
    Parse values into native datatypes
    """
    out = {}
    for k, v in obj.items():
        if k == 'data': out[k] = v
        if k not in model.keys(): continue

        if (model[k][0] == 'string'): out[k] = v
        elif (model[k][0] == 'strings'): out[k] = v
        elif (model[k][0] == 'hash'): out[k] = v
        elif (model[k][0] == 'hashes'): out[k] = v
        elif (model[k][0] == 'timestamp'): out[k] = int(v)
        elif (model[k][0] == 'integer'): out[k] = int(v)
        elif (model[k][0] == 'number'): out[k] = float(v)
        elif (model[k][0] == 'boolean'): out[k] = v == 'true'
        elif (model[k][0] == 'text'): out[k] = v
        else: out[k] = v

        # Attempt parsing as json
        if model[k][0] in ['string', 'text']:
            try: out[k] = json.loads(v)
            except: pass
    return out

def required_fields(obj, fields=[]):
    """
    Validates that required fields are present
    """
    if not fields: return
    for field in fields:
        assert obj.get(field) is not None, 'input: '+field+' is required'

def exclusive_fields(obj, fields=[]):
    """
    Validates that obj has fields only from specified list
    """
    for k in obj.keys():
        assert k in fields, 'input: attribute '+k+' is not allowed'

def filter_fields(obj, fields=[]):
    """
    Filters out fields that are not in specified array
    """
    return {k: v for k, v in obj.items() if k in fields}

def strip_fields(obj, fields=[]):
    """
    Removes fields that are specified in array
    """
    return {k: v for k, v in obj.items() if k not in fields}

def valid_formats(obj, model):
    """
    Validates field formats based on model schema
    """
    extended = obj.get('function', '') in ['pool.create', 'token.create', 'token.update', 'transaction.batch', 'token.batch', 'allowance.batch']

    for k, v in obj.items():
        assert k in obj.keys(), 'input: object contains invalid attribute'

        if (model[k][0] == 'string' and type(v) is str and ((extended and len(v) <= 8192) or len(v) <= 256)): continue
        elif (model[k][0] == 'strings' and type(v) is list and len(v) and len(v) <= 100 and len(v) == len(set(v)) and all([type(s) is str and len(s) <= 256 for s in v])): continue
        elif (model[k][0] == 'hash' and type(v) is str and len(v) >= 32 and len(v) <= 44): continue
        elif (model[k][0] == 'hashes' and type(v) is list and len(v) and len(v) < 100 and len(v) == len(set(v)) and all([type(s) is str and len(s) >= 32 and len(s) <= 44 for s in v])): continue
        elif (model[k][0] == 'timestamp' and type(v) == int and v >= 1e12 and v < 1e13): continue
        elif (model[k][0] == 'integer' and type(v) == int and v >= 0 and v <= 1e15): continue
        elif (model[k][0] == 'number' and type(v) in [int, float] and v >= 0 and v <= 1e15): continue
        elif (model[k][0] == 'boolean' and type(v) == bool): continue
        elif (model[k][0] == 'text' and type(v) == str and len(v) <= 8192): continue
        else: raise Exception('input: incorrect format for '+k)

TRANSACTION = {
    'signature': ['string'],
    'from': ['hash'],
    'to': ['hash'],
    'sender': ['hash'],
    'token': ['hash'],
    'amount': ['number'],
    'fee': ['number'],
    'nonce': ['integer'],
    'created': ['timestamp'],
    'message': ['string'],
    'function': ['string'],
    'delegate': ['boolean'],
    'error': ['string'],
    'input': ['string'],
    'outputs': ['strings'],
    'confirmed': ['timestamp'],
    'confirmations': ['integer'],
    'fromBalance': ['number'],
    'toBalance': ['number'],
    'payerBalance': ['number'],
}

BALANCE ={
    'address': ['hash'],
    'token': ['hash'],
    'amount': ['number'],
}

ALLOWANCE = {
    'hash': ['hash'],
    'token': ['hash'],
    'address': ['hash'],
    'spender': ['hash'],
    'amount': ['number'],
    'created': ['timestamp'],
}

CLAIM = {
    'hash': ['hash'],
    'address': ['hash'],
    'token': ['hash'],
    'owner': ['hash'],
    'amount': ['number'],
    'created': ['timestamp'],
    'expires': ['timestamp'],
    'unlocks': ['timestamp'],
    'answer': ['hash'],
    'number': ['number'],
    'random': ['number'],
    'frozen': ['boolean'],
}

TOKEN = {
    'address': ['hash'],
    'creator': ['hash'],
    'name': ['string'],
    'ticker': ['string'],
    'supply': ['integer'],
    'created': ['timestamp'],
    'reserve': ['integer'],
    'description': ['string'],
    'links': ['strings'],
    'object': ['string'],
    'meta': ['text'],
    'icon': ['string'],
    'mime': ['string'],
    'hash': ['string'],
    'fingerprint': ['string'],
    'cluster': ['string'],
}

POOL = {
    'address': ['hash'],
    'creator': ['hash'],
    'token': ['hash'],
    'program': ['string'],
    'created': ['timestamp'],
    'name': ['string'],
    'mechanism': ['string'],
    'candidates': ['hashes'],
    'rate': ['number'],
    'percentage': ['number'],
    'probability': ['number'],
    'expires': ['timestamp'],
    'minAmount': ['number'],
    'maxAmount': ['number'],
    'minTime': ['integer'],
    'maxTime': ['integer'],
    'transfersLimit': ['integer'],
    'claimsLimit': ['integer'],
    'tokenLimit': ['number'],
    'xetaLimit': ['number'],
    'tokenTarget': ['number'],
    'xetaTarget': ['number'],
    'xetaBalance': ['number'],
    'tokenBalance': ['number'],
    'xetaTurnover': ['number'],
    'tokenTurnover': ['number'],
    'transfersCount': ['integer'],
    'claimsCount': ['integer'],
    'answers': ['hashes'],
    'closed': ['boolean'],
    'leader': ['hash'],
}

CANDLE = {
    'key': ['string'],
    'time': ['integer'],
    'open': ['number'],
    'high': ['number'],
    'low': ['number'],
    'close': ['number'],
    'volume': ['number'],
    'turnover': ['number'],
    'trades': ['integer'],
    'first': ['timestamp'],
    'last': ['timestamp'],
}