from xeta.library.config import config
import hashlib
import ed25519
import base58


def generateKeypair():
    """
    Generate ED25519 keypair
    """
    private, public = ed25519.create_keypair()
    return [base58.b58encode(public.to_bytes()).decode(),
            base58.b58encode(private.to_seed()).decode()]

def generatePublicKey(private):
    """
    Generates 32 byte public key from private key
    Encodes via base58
    """
    signing_key = ed25519.SigningKey(base58.b58decode(private))
    public = signing_key.get_verifying_key().to_bytes()
    return base58.b58encode(public).decode()

def sign(message, private):
    """
    Signs a message, such as a hash
    Returns base58 encoded signature
    """
    signature = ed25519.SigningKey(base58.b58decode(private)).sign(base58.b58decode(message))
    return base58.b58encode(signature).decode()
    
def verify(message, signature, public):
    """
    Verifies a message, such as a hash
    Returns True or False depending on whether message signature is valid
    """
    verifying_key = ed25519.VerifyingKey(base58.b58decode(public))
    try: verifying_key.verify(base58.b58decode(signature), base58.b58decode(message))
    except: return False
    return True