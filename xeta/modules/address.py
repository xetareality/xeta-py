from xeta.library import utils
from xeta.library.config import config


def read(address):
    """
    Read address data (balance, profile, pool, token)
    """
    return utils.request(
        method='GET',
        url=config['interface']+'/profile',
        params={
            'address': address,
            'dev': config['dev'],
            'identity': config['identity'],
        })