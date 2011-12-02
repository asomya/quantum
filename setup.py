#!/usr/bin/env python
import os
from distutils.core import setup
from setuptools import find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Quantum",
    packages = find_packages(),
    version = "1.0",
    description = "Layer 2 network as a service for Openstack",
    long_description = read('README'),
    url = 'http://launchpad.net/quantum',
    license = 'BSD',
    author = 'Netstack',
    author_email = 'netstack@launchpad.net',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
