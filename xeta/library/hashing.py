import hashlib
import base58
import json 


def hash_digest(fields):
    """
    JSON encode array of values
    Encode via sha256
    """
    return hashlib.sha256(json.dumps([str(f) if f is not None else f for f in fields], separators=(',', ':')).encode()).digest()

def hash_transaction(body):
    """
    Hash transaction body
    Fiedls: token, from, to, amount, function, message, nonce
    """
    return hash_digest([
        body.get('token'),
        body.get('from'),
        body.get('to'),
        body.get('amount'),
        body.get('function'),
        body.get('message'),
        body.get('nonce')])

def hash_allowance(body):
    """
    Hash allowance body
    Fields: address, token, spender
    """
    return hash_digest([
        body.get('address'),
        body.get('token'),
        body.get('spender')])

def hash_claim(body):
    """
    Hash claim body
    Fields: address, token, pool
    """
    return hash_digest([
        body.get('address'),
        body.get('token'),
        body.get('pool')])

def hash_pool(body):
    """
    Hash pool body
    Fields: token, program
    """
    return hash_digest([
        body.get('token'),
        body.get('program')])

def hash_token(body):
    """
    Hash token body
    Fields: name, ticker, supply
    """
    return hash_digest([
        body.get('name'),
        body.get('ticker'),
        body.get('supply')])

def hash_string(body):
    """
    Hash string
    Sha256(sha256(body))
    """
    enc = hashlib.sha256(body.encode()).digest()
    enc = hashlib.sha256(enc).digest()
    return enc # base58.b58encode(enc).decode()