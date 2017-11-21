#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** fsops.py                Filesystem Operations     VER0.0.0PREALPHA **
** License: GPL v3                 Please keep my name in the credits **
************************************************************************
"""
import os
# fileList = []
# trashList = []

def is_this_a_dir(path):
    """verify whether a directory exists

    """
    return os.path.isdir(path)

def scan_dir(rootdir):
    """Scans rootdir recursively

    store files in lists for further processing based on extension."""
    global fileList, trashList
    from pathlib import PurePath
    audioExts = [mp3, flac, m4a, aif, ogg, wma, wav, cda, mp2, ape, midi, mid,
                 mod, opus, au, aac]
    for root, files in os.walk(rootdir): ###CHECK### subfolders?
        for thisfile in files:
            if PurePath(thisfile).suffix not in audioExts:
                trashList.append(thisfile)
            else :
                fileList.append(os.path.join(root,thisfile))
                ###TODO### dirty needs fixing
        # for this_folder in subfolders:
            # scandir(this_folder)

def is_this_a_file(path):
    """verify "path" to be a file

    """
    result = os.path.isfile(path)
    return result

def delete_file(file_to_be_deleted):
    """delete file_to_be_deleted

    """
    os.unlink(file_to_be_deleted)
    return True

def main():
    """just in case somebody wants to test this file by itself"""
    print("It works!!! ;-)")
    ###TODO### do something with the various methods/functions of this file

# standard boilerplate
if __name__ == '__main__':
    main()
