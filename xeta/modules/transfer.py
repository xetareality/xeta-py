from xeta.modules import transaction
from xeta.library import models, utils
from xeta.library.config import config
import json
import time


def create(to, token, amount, fromAddress=None, message=None, raw=False):
    """
    Create transfer
    """
    instruction = utils.strip({
        'function': 'transfer.create',
        'to': to,
        'token': token,
        'amount': utils.amount(amount),
        'from': fromAddress,
        'message': message,
    })

    if raw: return instruction
    return transaction.create({'instructions': [instruction]})