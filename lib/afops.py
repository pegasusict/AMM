#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** afops.py              audiofile operations        VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
blacklist = ["Jeckell and Hide", "Frozen flame (explosive cartuning rip)"]
#class AudioFile:
#    def __init__(self, path):
#        self.__path = path
#        self.tags = []

def tag_parser(fileList):
    """Parse tags and store in DB

    check for fingerprint, set flag 2, else set flag 1
    """
    for this_file in file_list:
        ###TODO### parse & purge tags, check for MBID or acoustid fingerprint
        if fingerprint:
            flag = "2"
        else:
            flag = "1"
        db_handler("update" , thisFile, tags, flag)
    return

def trim_silences(file_list):
    """<<enter description>>

    """
    for _file in file_list:
        ###TODO### figure out the command to trim the silences
        sh()

def generate_fingerprints(this_file_list):
    """generates acoustID fingerprints and set flag 2

    """
    import acoustid
    for file_entry in this_file_list:
        new_file_list[file_entry] = acoustid.fingerprint_file(file_entry)
    return new_file_list

def find_n_purge_dups(file_list):
    """find duplicate fingerprints in database

    """
    ###TODO###
    dupfiles = dba.get("mb_id duplicates, sort desc by quality index")
    duplicatesfound = len(dupfiles)
    reportbuilder.update(duplicates_found=duplicatesfound)
    while  > 1
        for thisfile in dupfiles:
            dba.delete_row(thisfile)
            fsops.delete_file(thisfile)
            filesize = thisfile["fsize"]
            reportbuilder.update(reclaimed_space=filesize, purgedfiles)

def transcode(file_path, quality):
    """transcodes file to quality setting

    """
    transcodeprefs = prefs(transcode)
    if transcodeprefs == 0:
        transcodeprefs = "paranoid"
    shline = "lame --preset " + transcodeprefs
    sh(shline)

def store_tags(tags, thisFile):
    """retrieves tag data from database and writes it to the file

    """
    import eyed3
    ###TODO### retrieve tag data from database
    # audiofile = eyed3.load(thisFile)
    # audiofile.tag.artist = u"Integrity"
    # audiofile.tag.album = u"Humanity Is The Devil"
    # audiofile.tag.album_artist = u"Integrity"
    # audiofile.tag.title = u"Hollow"
    # audiofile.tag.track_num = 2

    audiofile.tag.save()

def volume_normalizer(fileEntry):
    """normalizes the volume to maximum without clipping

    """
    # prefs('normalizing')
    pass

def main():
    """test function for this module

    """
    pass

# standard boilerplate
if __name__ == '__main__': main()
