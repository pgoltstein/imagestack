#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This script tests the module scanimagestack.

Created on Thu Jan 30, 2020

@author: pgoltstein
"""

import si_stack
import argparse

# =============================================================================
# Arguments

parser = argparse.ArgumentParser( description = "This script tests the module scanimagestack.\n (written by Pieter Goltstein - February 2020)")
parser.add_argument('filepath', type=str, help= 'path to the tiff folder')
parser.add_argument('filestem', type=str, help= 'filestem of tiffs')
args = parser.parse_args()


# =============================================================================
# Code

im = si_stack.xyt(filestem=args.filestem, filepath=args.filepath, extention="tif")
print("Reading the every 50th frame from the first 2000 frames:")
a=im[:2000:50]
# a=im[[3,4,5]]
# a=im[3]
# a=im[-100:]
# a=im[-200:-100:2]
# a=im[::25]
