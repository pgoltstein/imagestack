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

print("\nTesting scanimagestack:")
im = si_stack.XYT(filestem=args.filestem, filepath=args.filepath, extention="tif")
print("\nReading the every 50th frame from the first 2000 frames:")
a=im[:2000:50]

print("\nTesting properties:")
print("- xres: {}".format(im.xres))
print("- yres: {}".format(im.yres))
print("- resolution: {}".format(im.resolution))
print("- nframes: {}".format(im.nframes))
print("- nplanes: {}".format(im.nplanes))
print("- nchannels: {}".format(im.nchannels))
print("- current channel: {}".format(im.channel))
print("- current plane: {}".format(im.plane))

print("\nDone testing\n")
