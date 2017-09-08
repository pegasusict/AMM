#!/usr/bin/env python3 -tt
################################################################################
## Audiophiles Music Manager                                 VER0.0.1PREALPHA ##
## (C)2017 Mattijs Snepvangers                            mattijs@ictlab.info ##
## fsop.py                     Filesystem Operations         VER0.0.1PREALPHA ##
## License: GPL v3                         Please keep my name in the credits ##
################################################################################

import os

def verify_dir_exists(path):
    result=os.path.isdir(path)
    return result

def read_src(src_dir):
    # store results in 3 lists/tuples/dicts
    # dirs, audiofiles, garbage




def verify_file_exists(path):
    result=os.path.isfile(path)
    return result

def delete_file(file_to_be_deleted):
    os.unlink(file_to_be_deleted)
    return True



fp = open(fname,'r')        # open for reading (must exist)
fp = open(fname,'w')        # creates new file for writing
fp = open(fname,'a')        # opens file for appending


