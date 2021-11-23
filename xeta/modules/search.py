from xeta.library import utils
from xeta.library.config import config


def query(query):
    """
    Performs a search query
    If query is valid hash, search returns resource by key (if available)
    If query is string, search returns tokens & pools matching string in name & symbol
    """
    return utils.request(
        method='GET',
        url=config['interface']+'/search',
        params={'query': query})