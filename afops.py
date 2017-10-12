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
    for thisFile in fileList:

        db_handler("update" , thisFile, tags, flags)
    return

def trim_silences(fileList):
    for _file in filelist:
        sh()

def generate_fingerprints(thisFileList):
    import acoustid
    for fileEntry in thisFileList:
        acoustid.fingerprint_file(fileEntry)
    return thisFileList

def find_n_purge_dups():
    """find duplicate fingerprints in database"""

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
