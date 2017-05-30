#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


def get_version():
    regex = r"""^__version__ = '(.*)'$"""
    with open('litter_getter/__init__.py', 'r') as f:
        text = f.read()
    return re.findall(regex, text, re.MULTILINE)[0]


requirements = [
    'requests',
    'XlsxWriter',
]

test_requirements = [
    'pytest',
]

setup(
    name='litter_getter',
    version=get_version(),
    description="Retrieve literature from biomedical reference libraries such as PubMed, EPA's HERO, and imports from Endnote RIS exports",
    long_description=readme + '\n\n' + history,
    author="Andy Shapiro",
    author_email='shapiromatron@gmail.com',
    url='https://github.com/shapiromatron/litter_getter',
    packages=[
        'litter_getter',
    ],
    package_dir={'litter_getter': 'litter_getter'},
    include_package_data=True,
    install_requires=requirements,
    dependency_links=['git+git://github.com/MrTango/RISparser@bbb89c601bfd66df9907fd91933cd43a95d72a87'],
    license="MIT license",
    zip_safe=False,
    keywords='litter_getter',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
