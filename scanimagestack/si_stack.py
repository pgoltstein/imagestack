#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Scripts to import scanimage tiff files and meta info, with thanks to Tobias Rose for the regular expressions.

Requires ScanImageTiffReader
https://vidriotech.gitlab.io/scanimagetiffreader-python/

with ScanImageTiffReader( fullpathname ) as tifffile:
    header = (tifffile.description(0))
    dimensions = (tifffile.shape())

Created on Thu Jan 30, 2020

@author: pgoltstein
"""

from ScanImageTiffReader import ScanImageTiffReader
import re

def scanimage_parseheader(header):
    print(header)
    rx_dict = {
        "stackNumSlices": re.compile(r'stackNumSlices = (?P<stackNumSlices>\d+)'),
        "scanZoomFactor": re.compile(r'scanZoomFactor = (?P<scanZoomFactor>\d+.\d+)'),
        "scanFrameRate": re.compile(r'scanFrameRate = (?P<scanFrameRate>\d+.\d+)'),
        "channelsSave": re.compile(r'channelsSave = (?P<channelsSave>\d+)'),
        "fastZNumVolumes": re.compile(r'fastZNumVolumes = (?P<fastZNumVolumes>\d+)'),
        "triggerClockTimeFirst": re.compile(r'triggerClockTimeFirst = (?P<triggerClockTimeFirst>\'\d+-\d+-\d+ \d+:\d+:\d+.\d+\')'),
        "loggingFramesPerFile": re.compile(r'loggingFramesPerFile = (?P<loggingFramesPerFile>\d+)'),
        "beamPowers": re.compile(r'beamPowers = (?P<beamPowers>\d+.\d+)'),
        "loggingFileStem": re.compile(r'loggingFileStem = (?P<beamPowers>\'.\')'),
        "motorPosition": re.compile(r'motorPosition = (?P<motorPosition>\[.+\])'),
    }
    si_info = {}
    for key, rx in rx_dict.items():
        match = rx_dict[key].search(header)
        if match:
            if key in ["scanZoomFactor","scanFrameRate","beamPowers"]:
                si_info[key] = float(match.group(key))
            elif key in ["triggerClockTimeFirst",]:
                si_info[key] = str(match.group(key)).strip('\'')
            elif key == "motorPosition":
                positions = str(match.group(key))
                si_info[key] = []
                for pos in positions.split(' '):
                    si_info[key].append
            else:
                si_info[key] = int(match.group(key))
        else:
            si_info[key] = None
    return si_info


# Test run if called from command line
if __name__ == '__main__':
    with ScanImageTiffReader( "/Users/pgoltstein/data/odmapping/O03/20200218-OD-L23-L4-L5/410/O03_20200218_005_001.tif" ) as tifffile:
        print("Loaded: /Users/pgoltstein/data/odmapping/O03/20200218-OD-L23-L4-L5/410/O03_20200218_005_001.tif")
        header = (tifffile.description(0))
        dimensions = (tifffile.shape())
        print("Image stack dimensions: {}".format(dimensions))
        si_info = scanimage_parseheader(header)
        for k,v in si_info.items():
            print("    - {}: {}".format(k,v))
