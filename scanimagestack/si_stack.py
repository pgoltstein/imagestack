#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This module holds functions to import scanimage tiff files and gather the meta info stored in the headers. With thanks to Tobias Rose for some of the regular expressions.

Requires ScanImageTiffReader and re (regular expressions)
https://vidriotech.gitlab.io/scanimagetiffreader-python/

Created on Thu Jan 30, 2020

@author: pgoltstein
"""

# =============================================================================
# Imports

import re
from ScanImageTiffReader import ScanImageTiffReader
import argparse


# =============================================================================
# Arguments

parser = argparse.ArgumentParser( description = "This module holds functions to import scanimage tiff files and gather the meta info stored in the headers. With thanks to Tobias Rose for some of the regular expressions. It can run as a test from the command line. \n (written by Pieter Goltstein - February 2020)")
parser.add_argument('filepath', type=str, help= 'path to the tiff folder')
parser.add_argument('filestem', type=str, help= 'filestem of tiffs')
args = parser.parse_args()


# =============================================================================
# Functions

def parseheader(header):
    """ This function reads the most relevant information from the tiff header of a scanimage tiff fileself.
        Inputs
        - header: The can be obtained from ScanImageTiffReader, header (tifffile.description(0))
        Returns
        - si_info: A dictionary holding the scanimage named variables in python format (int, float, list[floats])
    """

    # Define the regular expressions needed to extract the information
    rx_dict = {
        "stackNumSlices": re.compile(r'stackNumSlices = (?P<stackNumSlices>\d+)'),
        "scanZoomFactor": re.compile(r'scanZoomFactor = (?P<scanZoomFactor>\d+.\d+)'),
        "scanFrameRate": re.compile(r'scanFrameRate = (?P<scanFrameRate>\d+.\d+)'),
        "channelsSave": re.compile(r'channelsSave = (?P<channelsSave>\d+)'),
        "fastZNumVolumes": re.compile(r'fastZNumVolumes = (?P<fastZNumVolumes>\d+)'),
        "triggerClockTimeFirst": re.compile(r'triggerClockTimeFirst = (?P<triggerClockTimeFirst>\'\d+-\d+-\d+ \d+:\d+:\d+.\d+\')'),
        "loggingFramesPerFile": re.compile(r'loggingFramesPerFile = (?P<loggingFramesPerFile>\d+)'),
        "beamPowers": re.compile(r'beamPowers = (?P<beamPowers>\d+.\d+)'),
        "loggingFileStem": re.compile(r'loggingFileStem = (?P<loggingFileStem>\'.+\')'),
        "motorPosition": re.compile(r'motorPosition = (?P<motorPosition>\[.+\])'),
        "pmtGain": re.compile(r'pmtGain = (?P<pmtGain>\[.+\])'),
        "scanLinesPerFrame": re.compile(r'scanLinesPerFrame = (?P<scanLinesPerFrame>\d+)'),
        "scanPixelsPerLine": re.compile(r'scanPixelsPerLine = (?P<scanPixelsPerLine>\d+)'),
        "stackZEndPos": re.compile(r'stackZEndPos = (?P<stackZEndPos>\d+.\d+)'),
        "stackZStartPos": re.compile(r'stackZStartPos = (?P<stackZStartPos>\d+.\d+)'),
        "stackZStepSize": re.compile(r'stackZStepSize = (?P<stackZStepSize>\d+.\d+)'),
    }

    # Now step through the dictionary and extract the information as int, float, string or a list of floats
    si_info = {}
    for key, rx in rx_dict.items():
        # Find match using reg-ex
        match = rx_dict[key].search(header)
        if match:
            # floating point numbers
            if key in ["scanZoomFactor", "scanFrameRate", "beamPowers", "stackZEndPos", "stackZStartPos", "stackZStepSize"]:
                si_info[key] = float(match.group(key))
            # strings
            elif key in ["triggerClockTimeFirst","loggingFileStem"]:
                si_info[key] = str(match.group(key)).strip('\'')
            # list of floats
            elif key in ["motorPosition","pmtGain"]:
                positions = str(match.group(key)).strip('[]')
                si_info[key] = []
                for pos in positions.split(' '):
                    si_info[key].append(float(pos))
            # otherwise integer
            else:
                si_info[key] = int(match.group(key))
        # if no reasonable match found, assign None
        else:
            si_info[key] = None

    # Return the dict
    return si_info


# =============================================================================
# Classes

class imagestack(object):
    """ This class holds the data of an entire (multi-tiff) scan image tiff stack, including methods for loading a single image, a slice, an enture image stack or just for accessing the meta data
    """
    def __init__(self, filestem=None, filepath=None):
        """ Initializes the image stack and gathers the meta data
            Inputs
            - filestem: Part of the file name that is shared among all tiffs belonging to the stack (optional, if left out all tiffs in filepath will be included)
            - filepath: Full directory path to the tiffs
        """



# =============================================================================
# Main, for testing from command line

if __name__ == '__main__':
    with ScanImageTiffReader( "/Users/pgoltstein/data/odmapping/O03/20200218-OD-L23-L4-L5/410/O03_20200218_005_001.tif" ) as tifffile:
        print("Loaded: /Users/pgoltstein/data/odmapping/O03/20200218-OD-L23-L4-L5/410/O03_20200218_005_001.tif")
        header = (tifffile.description(0))
        dimensions = (tifffile.shape())
        print("Image stack dimensions: {}".format(dimensions))
        si_info = parseheader(header)
        for k,v in si_info.items():
            print("    - {}: {}".format(k,v))
