config = {
    'publicKey': None,
    'privateKey': None,
    'account': None,
    'secret': None,
    'interface': 'https://interface.xetareality.com',
    'network': 'https://mainnet.xetareality.com',
    'registry': 'https://registry.xetareality.com',
    'xeta': '11111111111111111111111111111xeta',
    'factory': '11111111111111111111111111factory',
    'xusd': '11111111111111111111111111111xusd',
    'sponsored': '1111111111111111111111111sponsored',
    'consumed': '11111111111111111111111111consumed',
    'zero': '11111111111111111111111111111zero',
    'burn': '11111111111111111111111111111burn',
}

def init(network=None, interface=None, registry=None):
    """
    Set endpoints
    """
    global config

    if network: config['network'] = network
    if interface: config['interface'] = interface
    if registry: config['registry'] = registry