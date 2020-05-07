#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This module holds functions that support suite 2p processed data to be integrated with image stacks

Requires suite2p

Created on Thu May 7, 2020

@author: pgoltstein
"""

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Imports
import os.path
import numpy as np
from suite2p.registration import register


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# Functions

def load_suite2p_ops( filepath ):
    """ Load the multiplane ops file
    """
    opsfile = os.path.join( filepath, "suite2p", "ops1.npy" )
    ops = np.load( opsfile, allow_pickle=True)
    print("Loaded: {}".format(opsfile))
    return ops


def shift_imagedata( imagedata, plane_no, frames, suite2p_ops ):
    """ Realignes image data to parameters in the ops dictionary
    """
    xmax = suite2p_ops[plane_no]['xoff'][frames].astype(np.int)
    ymax = suite2p_ops[plane_no]['yoff'][frames].astype(np.int)
    if suite2p_ops[plane_no]['nonrigid']:
        xmax1 = suite2p_ops[plane_no]['xoff1'][frames,:]
        ymax1 = suite2p_ops[plane_no]['yoff1'][frames,:]
    else:
        xmax1 = np.array([])
        ymax1 = np.array([])
    imagedata = imagedata.transpose(2,0,1)
    imagedata = register.apply_shifts(imagedata, suite2p_ops[plane_no], ymax, xmax, ymax1, xmax1)
    return imagedata.transpose(1,2,0)
