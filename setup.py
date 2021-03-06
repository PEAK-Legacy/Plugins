#!/usr/bin/env python
"""Distutils setup file"""
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup

# Metadata
PACKAGE_NAME = "Plugins"
PACKAGE_VERSION = "0.5a1"
PACKAGES = ['peak', 'peak.util']
def get_description():
    # Get our long description from the documentation
    f = file('README.txt')
    lines = []
    for line in f:
        if not line.strip():
            break     # skip to first blank line
    for line in f:
        if line.startswith('.. contents::'):
            break     # read to table of contents
        lines.append(line)
    f.close()
    return ''.join(lines)

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description="Easily add hooks and plugins to your applications",
    long_description = open('README.txt').read(), # get_description(),
    install_requires=[
        'setuptools>=0.6c', 'Contextual>=0.7a1dev,==dev', 'DecoratorTools>=1.5'],
    author="Phillip J. Eby",
    author_email="peak@eby-sarna.com",
    license="PSF or ZPL",
    url="http://pypi.python.org/pypi/Plugins",
    download_url = "svn://svn.eby-sarna.com/svnroot/Plugins#egg=Plugins-dev",
    test_suite = 'peak.util.plugins',
    packages = PACKAGES,
    namespace_packages = PACKAGES,
)

