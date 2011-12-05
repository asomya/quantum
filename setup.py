#!/usr/bin/env python
# Copyright (c) 2010 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gettext
import os
import glob

from distutils.core import setup
from setuptools import find_packages

gettext.install('quantum', unicode=1)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def find_data_files(destdir, srcdir):
    package_data = []
    files = []
    for d in glob.glob('%s/*' % (srcdir, )):
        if os.path.isdir(d):
            package_data += find_data_files(
                                 os.path.join(destdir, os.path.basename(d)), d)
        else:
            files += [d]
    package_data += (destdir, files)
    return package_data

setup(
    name = "Quantum",
    packages = find_packages(exclude=['bin', 'doc', 'tools', 'etc']),
    version = "1.0",
    description = "Layer 2 network as a service for Openstack",
    long_description = read('README'),
    url = 'http://launchpad.net/quantum',
    license='Apache License (2.0)',
    author = 'Netstack',
    author_email = 'netstack@launchpad.net',
    scripts = [ 'bin/quantum',
                'bin/quantum-server',
    ],
    data_files = [
        ['/etc/quantum', ['etc/quantum.conf', 'etc/plugins.ini',
                          'etc/quantum.conf.sample', 'etc/quantum.conf.test']],
        ['/etc/init.d', ['etc/init.d/quantum-server']],
        find_data_files('/etc/quantum/plugins/cisco', 
                        'etc/quantum/plugins/cisco'),
        find_data_files('/etc/quantum/plugins/openvswitch', 
                        'etc/quantum/plugins/openvswitch'),
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
    ],
)
