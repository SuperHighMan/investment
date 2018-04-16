from setuptools import setup, find_packages
import codecs
import os
import investment

long_desc = """
investment
================

* Module Crawling
* Module Analysis
* Module Persistence
* Module Visualization

Installation
-----------------
python setup.py
"""

def read_install_requires():
    with open('requirements.txt', 'r') as f:
        res = f.readline()
    res = list(map(lambda s: s.replace('\n', ','), res))
    return res

setup(
    name='investment',
    version=investment.__version__,
    description='A utility for Crawling Market Data and for Data Analysis',
    long_description = long_desc,
    #install_requires=read_install_requires(),
    author=investment.__author__,
    url='https://github.com/SuperHighMan/investment.git',
    platforms='python 3.6',
    packages=find_packages(),
)