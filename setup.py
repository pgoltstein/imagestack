#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup( name='scanimagestack', version='0.01', description='Contains functions to handle complete scanImage stacks (consisting of multiple tiff blocks)', url='https://github.com/pgoltstein/scanimagestack', author='Pieter Goltstein', author_email='xpieter@mac.com', license='GNU GENERAL PUBLIC LICENSE Version 3', packages=['scanimagestack'], install_requires=['re','ScanImageTiffReader'], zip_safe=False )
