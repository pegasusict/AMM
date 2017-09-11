#!/usr/bin/python3 -tt

### MAIN FUNCTIONS ###
from pathlib import PurePath

def scan_dir(rootdir):
    """Scan recursively, store files in lists for further processing based on extension.
    
    """
    audioExts = [mp3, lac, m4a, aif, ogg, wma, wav, cda, mp2, ape, midi, mid, opus, au]
    fileList = []
    trashList = []
    for root, subFolders, files in os.walk(rootdir):
        for thisfile in files:
            if PurePath(file).suffix not in audioExts:
                trashList.append(file)
            else :
                fileList.append(os.path.join(root,thisfile))
    return fileList

def tag_parser(filelist):
    for thisfile in filelist:
        """ demux tags
        * check for musicIP : set flags 2 & 5
        * check for fingerprint : set flags 2 & 4 
        * else set flag 2
        """
        db_handler("update" , thisfile, tags, flags)
    return

def purge_dups():
    """purge duplicate based on audio quality"""
    
def mb_query():

def cddb_query():

def get_albumart():

def get_songtext():

def transcode(fileentry):
    trancodeprefs = prefs(trancode)
    if transcodeprefs == 0:
        transcodeprefs=lame_paranoid

def volume_normalizer(fileEntry):
    normalizeprefs = prefs(normalizing)

def report_builder():

### MAIN ###
def main():
    settings = parse_ini()
    prefs = parse_prefs()
    sessiondata = prefs['session']
    modulelist = scan_modules()
    dbsession = db_handler("init", sessiondata)
# phase 1
    basedir = prefs(basedir)
    scan_dir(basedir)
# phase 2
    filelist = db_handler("get", entries flagged "0")
    newfilelist = tag_parser(filelist)
    del filelist
    dbstatus = db_handler("update", newfilelist)
# phase 3
    purge_dups()

### Boilerplate ###
if __name__ == "__main__":
    main()
