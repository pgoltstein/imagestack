# imagestack

Contains functions to handle complete image stacks (consisting of multiple tiff blocks (ScanImage), or (in the future) binary files).

for now only works for XYT ScanImage stacks or multilevel XYT ScanImage stacks using fastZ.

__Installation__
```
pip install --upgrade https://github.com/pgoltstein/imagestack/archive/v0.11.tar.gz
```


__Contains__  

scanimagestack (module)
* _scanimagestack.parseheader(header)_  
    This function reads the most relevant information from the tiff header of a scanimage tiff.
* _scanimagestack.xyt(object)_  
    This class represents an entire (multi-tiff) ScanImage stack. Image channel and image plane should be set manually (defaults are 0).

    The class can load the image data using standard np.ndarray indexing:
    * data = imagestack[:] returns all the data
    * data = imagestack[1] returns the second frame (zero based slice)
    * data = imagestack[[5,8,10]] returns frames 5,8 and 10
    * data = imagestack[::2] returns every second frame.

    In addition, the class has several methods for accessing the meta data, which can be accessed as properties. For instance:
    * res = imagestack.resolution returns the [y,x] image resolution
    * nchannels = imagestack.nchannels returns number of image channels


suite2psupport (module)  
This handles the registration using suite2p. In order for this module to work, two lines of code should be added to the ```__init__.py``` file that is in the suite2p folder called registration.

```
# Add these lines to \suite2p\registration\__init__.py
from .rigid import shift_frame
from .nonrigid import transform_data
from .bidiphase import shift
```



__Requires the following python packages__
* os
* glob
* re
* numpy
* alive_progress
* ScanImageTiffReader
* argparse


__To do__
* Add more meta data properties
* Add support for manual metadata (.txt file)
* Add xyz stack
* Add support for binary stacks

---

Version 0.11 - April 9, 2020 - Pieter Goltstein
