try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This is my python project skeleton',
    'author': 'Steven "NemesisRE" Koeberich',
    'url': 'https://nrecom.net',
    'download_url': '-',
    'author_email': 'nemesissre@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
