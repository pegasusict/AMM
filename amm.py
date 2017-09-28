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
import afops, fsop, conf, inetc, daemonizer
from dialog import Dialog
from db_agent import db_handler
### define globals
debugSwitch = False
prefs = null


def init():
    """init function

    broke down main function to increase readability"""
    global debugSwitch
    locale.setlocale(locale.LC_ALL,'')
    d = Dialog.infobox("Please wait, initialising...")
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="enable debug mode", action="store_true", default=False)
    args=parser.parse_args()
    if args.debug:
        debugSwitch = True
    ### init, load /generate config
    prefs = parse_prefs()
    dbHandle = db_handler("initialise")

def find_n_purge_dups():
    """find duplicate fingerprints in database and """

def report_builder(reportType="display", reportData):
    """reportbuilder"""
    ### determine what template to use
    if reportType == "display":
        ### display template
    elif reportType == "html":
        ### html template
    else reportType = "text":
        ### text template
    return generated_report

def main():
    init()
    stagecomplete = "init"
    ### phase 0
    ## scan source dir
    scanned_dir = fops.scan_dir(prefs['basedir'])
    ## add audiofiles to DB
    dbHandle("store", scanned_dir['audiofiles'], "flag=0")
    del scanned_dir['audiofiles']
    ## purge non-audio files
    for each fileEntry in scanned_dir['trash']:
        delete_file(fileEntry)
    del scanned_dir
    stagecomplete = '0'
    ### phase 1
    ## parse & purge tags
    filelist = dbHandle("get", "flag=0")
    newfilelist = tag_parser(filelist)
    del filelist
    afops.generate_fingerprints(newfilelist)
    ## calculate qualityIndex
    for each fileEntry in newfilelist:
        ### figure out what to get from where and how to compare codecs
    dbstatus = dbHandle("update", newfilelist, "flag=1")
    del newfilelist
    stagecomplete = '1'
    ### phase 2
    find_n_purge_dups()
    stagecomplete = '3'
    ### phase 4
    transcode(fileEntry, quality)
    insertTags(fileEntry, tags)
    stagecomplete = '4'
    ### phase 5
    report_builder(reportType, reportData)
    stagecomplete = '5'

# standard boilerplate
if __name__ == '__main__':
    main()
