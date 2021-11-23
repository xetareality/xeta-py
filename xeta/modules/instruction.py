from xeta.modules import transaction
from xeta.library import utils


def wrap(args, tx={}):
    """
    Wrap arguments as instruction
    Submit instruction as transaction
    Or return instruction if submit is False
    """
    instruction = utils.strip(args)
    if tx is False: return instruction
    return transaction.submit([instruction], tx)