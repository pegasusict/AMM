#!/usr/bin/env python3 -tt
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** afops.py              audiofile operations        VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""

def tag_parser(fileList):
    """Parse tags and store in DB

    check for fingerprint, else set flag 1
    """
    for thisFile in fileList:
        db_handler("update" , thisFile, tags, flags)
    return

def generate_fingerprints(thisFileList):
    import acoustid
    for fileEntry in thisFileList:
        acoustid.fingerprint_file(fileEntry)
    return thisFileList

def store_tags(tags, thisFile):
    import eyed3

    audiofile = eyed3.load(thisFile)
    audiofile.tag.artist = u"Integrity"
    audiofile.tag.album = u"Humanity Is The Devil"
    audiofile.tag.album_artist = u"Integrity"
    audiofile.tag.title = u"Hollow"
    audiofile.tag.track_num = 2

audiofile.tag.save()

def transcode(fileEntry):
    """<<enter description>>

    """
    transcodeprefs = prefs(trancode)
    if transcodeprefs == 0:
        transcodeprefs = lame_paranoid

def volume_normalizer(fileEntry):
    prefs('normalizing')
