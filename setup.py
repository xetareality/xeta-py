# -*- coding: utf-8 -*-
from setuptools import setup
from pathlib import Path

setup(**{
    'name': 'xeta',
    'version': '0.9.1',
    'description': 'Official Python client for Xeta',
    'long_description': (Path(__file__).parent/'README.md').read_text(),
    'long_description_content_type': 'text/markdown',
    'author': 'Xeta Reality',
    'author_email': 'contact@xetareality.com',
    'url': 'https://github.com/xetareality/xeta-py',
    'packages': ['xeta', 'xeta.library', 'xeta.modules', 'xeta.programs'],
    'install_requires': ['requests', 'ed25519', 'base58'],
})