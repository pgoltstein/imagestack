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
from suite2p.registration import rigid, nonrigid


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

    # Get parameters
    xmax = suite2p_ops[plane_no]['xoff'][frames].astype(np.int)
    ymax = suite2p_ops[plane_no]['yoff'][frames].astype(np.int)
    if suite2p_ops[plane_no]['nonrigid']:
        nblocks = suite2p_ops[plane_no]['nblocks']
        xblock = suite2p_ops[plane_no]['xblock']
        yblock = suite2p_ops[plane_no]['yblock']
        xmax1 = suite2p_ops[plane_no]['xoff1'][frames,:]
        ymax1 = suite2p_ops[plane_no]['yoff1'][frames,:]

    # for suite2p, data : int16 or float32, 3D array (size [nimg x Ly x Lx])
    imagedata = imagedata.transpose(2,0,1)

    # old suite2p
    # imagedata = register.apply_shifts(imagedata, suite2p_ops[plane_no], ymax, xmax, ymax1, xmax1)

    # New suite2p -> rigid registration step
    for frame_no, (dy, dx) in enumerate(zip(ymax, xmax)):
        imagedata[frame_no,:,:] = rigid.shift_frame( frame=imagedata[frame_no,:,:], dy=dy, dx=dx )

    # New suite2p -> non-rigid registration step
    if suite2p_ops[plane_no]['nonrigid']:
        imagedata = nonrigid.transform_data(
            data=imagedata,
            nblocks=nblocks,
            xblock=xblock,
            yblock=yblock,
            ymax1=ymax1,
            xmax1=xmax1,
        )

    return imagedata.transpose(1,2,0)
