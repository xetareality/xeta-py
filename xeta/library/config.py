config = {
    'publicKey': None,
    'privateKey': None,
    'account': None,
    'secret': None,
    'dev': None,
    'interface': 'https://interface.xetareality.com',
    'network': 'https://network.xetareality.com',
    'xeta': '11111111111111111111111111111xeta',
    'factory': '11111111111111111111111111factory',
    'xusd': '11111111111111111111111111111xusd',
    'sponsored': '1111111111111111111111111sponsored',
    'consumed': '11111111111111111111111111consumed',
    'zero': '11111111111111111111111111111zero',
    'burn': '11111111111111111111111111111burn',
}

def init(network=None, interface=None, dev=None):
    """
    Set endpoints and environment mode
    """
    global config

    if network: config['network'] = network
    if interface: config['interface'] = interface
    if dev is not None: config['dev'] = dev if dev else None