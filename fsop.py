#!/usr/bin/env python3 -tt
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** fsop.py                 Filesystem Operations     VER0.0.0PREALPHA **
** License: GPL v3                 Please keep my name in the credits **
************************************************************************
"""
import os

def purge_dups():
    """purge duplicate based on audio quality

    """

def verify_dir_exists(path):
    result = os.path.isdir(path)
    return result

def scan_dir(rootdir):
    """Scan recursively, store files in lists for further processing
    based on extension.

    """
    global fileList, trashList
    from pathlib import PurePath
    audioExts = [mp3, flac, m4a, aif, ogg, wma, wav, cda, mp2, ape, midi, mid,
                 mod, opus, au, aac]
    fileList = []
    trashList = []
    for root, subFolders, files in os.walk(rootdir):
        for thisfile in files:
            if PurePath(file).suffix not in audioExts:
                trashList.append(file)
            else :
                fileList.append(os.path.join(root,thisfile))
                # dirty needs fixing
    return

def verify_file_exists(path):
    result = os.path.isfile(path)
    return result

def delete_file(file_to_be_deleted):
    os.unlink(file_to_be_deleted)
    return True

###
fp = open(fname,'r')        # open for reading (must exist)
fp = open(fname,'w')        # creates new file for writing
fp = open(fname,'a')        # opens file for appending

# standard boilerplate
if __name__ == '__main__':
    main()
