"""setup.py file."""

import uuid

from setuptools import setup, find_packages
from pip.req import parse_requirements

__author__ = 'Anthony Shaw <anthonyshaw@apache.org>'

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="napalm-dummy",
    version="0.1.0",
    packages=find_packages(),
    author="Anthony Shaw",
    author_email="anthonyshaw@apache.org",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/DimensionDataResearch/napalm-dummy",
    include_package_data=True,
    install_requires=reqs,
)
