#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This script tests the module scanimagestack.

Run from command line as
>> python -m test fullpath filestem

Created on Thu Jan 30, 2020

@author: pgoltstein
"""

import sys
sys.path.append('../suite2psupport')
import si_stack
import suite2psupport

import argparse

# =============================================================================
# Arguments

parser = argparse.ArgumentParser( description = "This script tests the module scanimagestack. Run from command line as >> python -m test fullpath filestem. Written by Pieter Goltstein - February 2020")
parser.add_argument('filepath', type=str, help= 'path to the tiff folder')
parser.add_argument('filestem', type=str, help= 'filestem of tiffs')
args = parser.parse_args()


# =============================================================================
# Code

print("\nTesting scanimagestack:")
Im = si_stack.XYT(filestem=args.filestem, filepath=args.filepath, extention="tif")
print("\nReading the every 50th frame from the first 1000 frames:")
a=Im[:250:25]
print("dtype {}".format(a.dtype))
print("Shape of stack: {}".format(a.shape))

print("\nTesting properties:")
print("- xres: {}".format(Im.xres))
print("- yres: {}".format(Im.yres))
print("- resolution: {}".format(Im.resolution))
print("- nframes: {}".format(Im.nframes))
print("- nplanes: {}".format(Im.nplanes))
print("- nchannels: {}".format(Im.nchannels))
print("- zoom: {}".format(Im.zoom))
print("- zstep: {}".format(Im.zstep))
print("- FOV size: {}".format(Im.fovsize))
print("- Pixel size: {}".format(Im.pixelsize))
print("- current channel: {}".format(Im.channel))
print("- current plane: {}".format(Im.plane))

Im.imregparams = suite2psupport.load_suite2p_ops( Im.filepath )
Im.imregfunc = suite2psupport.shift_imagedata
Im.register = True

print("\nReading the every 50th frame from the first 1000 frames, now with registration:")
b=Im[:250:25]
print("dtype {}".format(b.dtype))
print("Shape of stack: {}".format(b.shape))

print("\nDone testing\n")
