try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='awinpub',
    version='0.1b',
    author='Doug Bromley',
    author_email='doug@tintophat.com',
    packages=['stash' ],
    scripts=[ 'bin/stash' ],
    url='http://pypi.python.org/pypi/pystash/',
    license='LICENSE.txt',
    description='Affiliate Window Publisher tools',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests>=2.2.0"
    ],
)