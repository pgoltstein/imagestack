# scanimagestack
Contains functions to handle complete scanImage stacks (consisting of multiple tiff blocks).

for now only works for XYT stacks or XYT stack using fastZ.

__Contains__
* _def parseheader(header)_
    This function reads the most relevant information from the tiff header of a scanimage tiff.
* _class imagestack(object)_
    This class represents an entire (multi-tiff) scanimage stack. Image channel and image plane should be set manually (defaults are 0).
    
    The class can load the image data using standard np.ndarray indexing:
    * data = imagestack[:] returns all the data
    * data = imagestack[1] returns the second frame (zero based slice)
    * data = imagestack[[5,8,10]] returns frames 5,8 and 10
    * data = imagestack[::2] returns every second frame.

    In addition, the class has several methods for accessing the meta data, which can be accessed as properties. For instance:
    * res = imagestack.resolution returns the [y,x] image resolution
    * nchannels = imagestack.nchannels returns number of image channels


__Requires the following python packages__
* os
* glob
* re
* numpy
* alive_progress
* ScanImageTiffReader
* argparse


__To do__
* Test direct Github install and update
* Add support for manual metadata (.txt file)
* Add support for binary stacks


Version 0.1 - April 3rd, 2020 - Pieter Goltstein
