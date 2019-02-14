try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Creating an ORM.',
    'author': 'Murphian',
    'url': 'XXXXXXXXXX',
    'download_url': 'XXXXXXXXXXXXX',
    'author_email': 'murphianx@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['orm'],
    'scripts': [],
    'name': 'orm'
}

setup(**config)