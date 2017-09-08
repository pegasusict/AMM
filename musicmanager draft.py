#!/usr/bin/python3 -tt
"""
***************************************************************************************************
***************************************************************************************************
** Music Manager V0.0.0e pre-Alpha                                  (c) 2013 Mattijs Snepvangers **
** http://www.pegsprojects.net/                                                                  **
** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **
** A Suite that can REALLY manage ALL aspects of a digital Music Collection                      **
** of ANY size                                                                                   **
** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **
** REQUIREMENTS:                                                                                 **
**   Python >=2.7.3                                                                              **
**   Lame codec >= 0.98                                                                          **
**   MySQL Server >= 5.0.3 (preferably on the same machine via socket due to the sheer volume)   **
** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **
** Python Modules:                                                                               **
**   Eyed3                                                                                       **
**   Musicdns                                                                                    **
**   libpimp                                                                                     **
**   mysqlclient                                                                                 **
** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **
** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **
** WORKS: ---                                                                                    **
** Milestone 1: purge non-audiofiles, Unduplicate, Identify, Transcode, Organise                 **
** Milestone 2: Fix Artistnames, Fix Albumtitles, Normalize                                      **
** Milestone 3: Albumart, Lyrics, feat artists, Composer, writer, original                       **
** Future Milestones: Acoustic Optimisation, GUI, web interface,                                 **
**                    Atonome searching & downloading of missing songs                           **
***************************************************************************************************
***************************************************************************************************
"""
import sys, re, os, shutil, mysql, musicbrainz, audiotools

### PREP functions #############################################################
def parseini():
def parseprefs():
def dbhandler():

### MAIN FUNCTIONS #############################################################
def scandir(rootdir):
  audioExts = [mp3,lac,m4a,aif,ogg,wma,wav,cda,mp2,ape,midi,mid,opus]
  fileList = []
  trashList = []
  for root, subFolders, files in os.walk(rootdir):
    for thisfile in files:
      if file[-3:] not in audioExts : """find better option to isolate extension"""
        trashList.append(file)
      else :
        fileList.append(os.path.join(root,thisfile))
  return fileList
def tagparser(filelist):
  for thisfile in filelist:
    # demux tags
    # check for musicIP : set flags 2 & 5
    # check for fingerprint : set flags 2 & 4 else set flag 2
    dbhandler("update" , thisfile, tags, flags)
  return

def purgedups():

def MBquery():

def cddbquery():

def getalbumart():

def getsongtext():

def transcode(fileentry):
  trancodeprefs = prefs(trancode)
  if transcodeprefs == 0:
    transcodeprefs=lame_paranoid

def volumenormalizer(fileEntry):
  normalizeprefs = prefs(normalizing)

def rebuildCollection(): # reorganize dirstructure, move & rename files

def addMissingSongs(): # To my own library

def findMissingSongs(): # online

def NASagent(): # find missing songs on BT, order NAS to download to special dir

def reportbuilder():

### MAIN #######################################################################
def main():
  settings = parseini()
  prefs = parseprefs()
  sessiondata = prefs['session']
  modulelist = scanmodules()
  dbsession = dbhandler("init", sessiondata)
# phase 1
  basedir = prefs(basedir)
  scandir(basedir)
# phase 2
  filelist = dbhandler("get", entries flagged "0")
  newfilelist = tagparser(filelist)
  del filelist
  dbstatus = dbhandler("update", newfilelist)
# phase 3
  purgedups()

### Boilerplate ################################################################
if __name__ == "__main__":
  main()
