#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='jsCatcher',
    packages=find_packages(),
    version='1.0',
    description="A python script that collect javascript link and file from url or list.",
    long_description=open('README.md').read(),
    author='Locu',
    url='https://github.com/xlocux/jsCatcher',
    install_requires=['requests', 'argparse', 'jsbeautifier', 'requests-file'],
)
