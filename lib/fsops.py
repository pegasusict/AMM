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

def verify_dir_exists(path):
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
    for root, subfolders, files in os.walk(rootdir):
        for thisfile in files:
            if PurePath(file).suffix not in audioExts:
                trashList.append(file)
            else :
                fileList.append(os.path.join(root,thisfile))
                ###TODO### dirty needs fixing
        # for this_folder in subfolders:
            # scandir(this_folder)

def verify_file_exists(path):
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
