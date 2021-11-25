import requests


def strip(obj, min=1):
    """
    Strip None values from object
    """
    out = {k: v for k, v in obj.items() if v is not None}
    assert len(out) >= min, 'parameters:missing'
    return out

def request(**kwargs):
    """
    A request wrapper with custom error handling
    """
    r = requests.request(**kwargs)
    if r.status_code != 200: raise Exception(r.text if r.text else 'request:invalid')
    try: return r.json()
    except: return

def amount(amount):
    """
    Format amount to amount string
    Strip .0 if amount represents an integer
    """
    if amount is None: return
    amount = str(round(float(amount), 8))
    return amount if amount[-2:] != '.0' else amount[:-2]

def output(transaction, instruction=0, index=0):
    """
    Returns the resource at instruction i at index j
    """
    if len(transaction['outputs']) <= instruction: raise Exception('instruction:length')
    if len(transaction['outputs'][instruction]) <= index: raise Exception('index:length')
    return transaction['outputs'][instruction][index].split(':')[1]