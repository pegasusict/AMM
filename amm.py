#!/usr/bin/env python3 -tt
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** amm.py                 main script                VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
### import libs
import argparse, sys, locale, time
from ammlib import *

def init():
    """init function

    broke down main function to increase readability"""
    global debugSwitch, uiStyle
    global myUI,
    locale.setlocale(locale.LC_ALL,'')
    parser = argparse.ArgumentParser()
    parser.add_argument("--dialog", help="Use Dialog ui",
                        action="store_true", default=True)
    parser.add_argument("--debug", help="enable debug mode",
                        action="store_true", default=False)
    args=parser.parse_args()
    if args.debug:
        debugSwitch = True
    if args.dialog:
        uiStyle = "dialog"
    myUI = new UserInterface(uiStyle)
    myUI.infobox("Please wait, initializing...")
    ### init, load /generate config
    ammConfig = new AMMconfig()
    dbHandle = db_handler("initialise")
    stagecomplete = "init"

def find_n_purge_dups():
    """find duplicate fingerprints in database"""

def report_builder(reportType="display", reportData):
    """reportbuilder"""
    ### determine what template to use
    if reportType == "display" :
        ### display template
    elif reportType == "html" :
        ### html template
    else reportType = "text" :
        ### text template
    return generated_report

def main():
    init()
    ### phase 0
    ## scan source dir
    scanned_dir = fops.scan_dir(ammConfig['basedir'])
    ## add audiofiles to DB
    dbHandle("store", scanned_dir['audiofiles'], "stage_completed=1")
    del scanned_dir['audiofiles']
    ## purge non-audio files
    for each fileEntry in scanned_dir['trash']:
        delete_file(fileEntry)
    del scanned_dir
    stagecomplete = '1'
    ### phase 2 -=- NEEDS TO RUN IN SEPARATE THREAD
    ## parse & purge tags
    filelist = dbHandle("get", "stage_completed=1", limit=100) ### LOOP !!!
    newfilelist = tag_parser(filelist)
    del filelist
    afops.generate_fingerprints(newfilelist)
    ## calculate qualityIndex
    for each fileEntry in newfilelist:
        ### figure out what to get from where and how to compare codecs
    dbstatus = dbHandle("update", newfilelist, "stagecompleted=2")
    del newfilelist
    stagecomplete = '2'
    ### phase 3
    find_n_purge_dups()
    stagecomplete = '3'
    ### phase 5
    transcode(fileEntry, quality)
    insertTags(fileEntry, tags)
    stagecomplete = '5'
    ### phase 6
    report_builder(reportType, reportData)
    stagecomplete = '6'

# standard boilerplate
if __name__ == '__main__':
    main()
