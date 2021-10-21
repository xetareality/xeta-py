from xeta.config import config


def connect(public_key, private_key, network=None, interface=None):
    """
    Set public and private key
    Optionally set network and interface endpoints
    """
    global config

    config['public_key'] = public_key
    config['private_key'] = private_key

    if network: config['network'] = network
    if interface: config['interface'] = interface