#!/usr/bin/env python3
"""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* Audiophiles Music Manager          Build 20180119          VER0.0.0PREALPHA *
* (C)2017 Mattijs Snepvangers                           pegasus.ict@gmail.com *
* lib/afops.py                       Audiofile Operations    VER0.0.0PREALPHA *
* License: MIT                             Please keep my name in the credits *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

BLACK_LIST = ["Jeckell and Hide", "Frozen flame (explosive cartuning rip)"]

def tag_parser(file_list):
    """Parse tags and store in DB

    check for fingerprint, set flag 2, else set flag 1
    """
    for this_file in file_list:
        ###TODO### parse & purge tags, check for MBID or acoustid fingerprint
        if fingerprint(this_file):
            flag = "2"
        else:
            flag = "1"
        db_handler("update" , this_file, tags, flag)
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

def find_n_purge_dups():
    """find duplicate fingerprints in database

    """
    ###TODO### find duplicate MBIDs in DB
    dupfiles = dba.get("mb_id duplicates, sort desc by quality index")
    duplicatesfound = len(dupfiles)
    reportbuilder.update(duplicates_found=duplicatesfound)
    while duplicatesfound > 1:
        for this_file in dupfiles:
            dba.delete_row(this_file)
            fsops.delete_file(this_file)
            filesize = this_file["fsize"]
            delete(dupfiles(this_file))
            duplicatesfound = len(dupfiles)
            reclaimed_space = filesize
            reportbuilder.update(reclaimed_space, purgedfiles)

def transcode(file_path, quality):
    """transcodes file to quality setting

    """
    transcodeprefs = prefs(transcode)
    if filetype(file_path) != "mp3":
        new_filepath = file_path[-3] + "mp3" ###CHECK###
        if transcodeprefs == 0: ###CHECK###
            transcodeprefs = "paranoid"
        shline = "lame --preset " + transcodeprefs + file_path + new_filepath
        sh(shline)
    else:
        raise Error(conversionError, "no need to convert mp3 to mp3"

def store_tags(tags, this_file):
    """retrieves tag data from database and writes it to the file

    """
    import eyed3
    ###TODO### retrieve tag data from database
    audiofile = eyed3.load(this_file)
    # audiofile.tag.artist = u"Integrity"
    # audiofile.tag.album = u"Humanity Is The Devil"
    # audiofile.tag.album_artist = u"Integrity"
    # audiofile.tag.title = u"Hollow"
    # audiofile.tag.track_num = 2
    audiofile.tag.save(tags, this_file)

def volume_normalizer(): # file_entry
    """normalizes the volume to maximum without clipping

    """
    # prefs('normalizing')
    pass

def main():
    """just in case somebody wants to test this file by itself"""
    print("It works!!! ;-)")
    ###TODO### do something with the various methods/functions of this file

if __name__ == '__main__':
    main()
