#!/usr/bin/env python3 -tt
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** afops.py              audiofile operations        VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""

def tag_parser(filelist):
    for thisfile in filelist:
        """ demux tags
        * check for musicIP : set flags 2 & 5
        * check for fingerprint : set flags 2 & 4
        * else set flag 2
        """
        db_handler("update" , thisfile, tags, flags)
    return

def transcode(fileentry):
    trancodeprefs = prefs(trancode)
    if transcodeprefs == 0:
        transcodeprefs=lame_paranoid

def volume_normalizer(fileEntry):
    normalizeprefs = prefs(normalizing)
