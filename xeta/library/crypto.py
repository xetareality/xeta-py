from xeta.library.config import config
import hashlib
import ed25519
import scrypt
import re

B58 = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def b58encode(v):
    """
    Encode string into base58
    """
    npad = len(v)
    v = v.lstrip(b'\0')
    npad -= len(v)

    p, acc = 1, 0
    for c in reversed(v):
        acc += p * c
        p = p << 8

    # Encode int
    result = b''
    while acc:
        acc, idx = divmod(acc, 58)
        result = B58[idx:idx+1] + result

    return (b'1'*npad+result)

def b58decode(v):
    """
    Decode base58 string
    """
    v = v.encode('ascii')
    
    origlen = len(v)
    v = v.lstrip(b'1')
    newlen = len(v)

    acc = 0
    for char in v: acc = acc * 58 + B58.index(char)

    # Decode int
    result = []
    while acc > 0:
        acc, mod = divmod(acc, 256)
        result.append(mod)

    return (b'\0' * (origlen - newlen) + bytes(reversed(result)))

def generateKeypair():
    """
    Generate ED25519 keypair
    """
    private, public = ed25519.create_keypair()
    return [b58encode(public.to_bytes()).decode(),
            b58encode(private.to_seed()).decode()]

def generatePublicKey(private):
    """
    Generates 32 byte public key from private key
    Encodes via base58
    """
    signing_key = ed25519.SigningKey(b58decode(private))
    public = signing_key.get_verifying_key().to_bytes()
    return b58encode(public).decode()

def sign(message, private):
    """
    Signs a message, such as a hash
    Returns base58 encoded signature
    """
    signature = ed25519.SigningKey(b58decode(private)).sign(b58decode(message))
    return b58encode(signature).decode()
    
def verify(message, signature, public):
    """
    Verifies a message, such as a hash
    Returns True or False depending on whether message signature is valid
    """
    verifying_key = ed25519.VerifyingKey(b58decode(public))
    try: verifying_key.verify(b58decode(signature), b58decode(message))
    except: return False
    return True

def brainwallet(account, secret):
    """
    Scrypt implementation to generate brain wallet
    Uses account value as salt combined with secret password
    """
    if len(account) < 6 or len(account) > 80 or not re.match(r'^[a-zA-Z0-9-+@_\.]*$', account): raise Exception('account:format')
    if len(secret) < 6 or len(secret) > 80 or not re.match(r'^[a-zA-Z0-9-+@_\.]*$', secret): raise Exception('secret:format')

    bytes = scrypt.hash(
        password=secret,
        salt=account,
        N=16384, r=8, p=1, buflen=32)

    return b58encode(bytes)