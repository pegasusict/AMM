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
import argparse, sys, locale, time, afops, fsop, conf, inetc, daemonizer,
       db_agent
from dialog import Dialog

def report_builder(reportType="display"):
    """reportbuilder"""
    if reportType == "display":
        ### display template
    elif reportType == "html":
        ### html template
    else reportType = "text":
        ### text template
    return


def main():
    locale.setlocale(locale.LC_ALL,'')
    d = Dialog.infobox("Please wait, initialising...")
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="enable debug mode"
                        action="store_true" default=False)
    args=parser.parse_args()
    if args.debug:
        debugSwitch = True
    ### init, load config
    prefs = parse_prefs()
    #modulelist = scan_modules()                        #???
    #dbsession = db_handler("init", sessiondata)
    ### phase 0
    basedir = prefs(basedir)
    scanned_dir = scan_dir(basedir)   ###include daemonizer functionality
    db_handler("store", scanned_dir, "flag='0'")
    ### phase 1
    filelist = db_handler("get", "flag='0'")
    newfilelist = tag_parser(filelist)
    del filelist
    dbstatus = db_handler("update", newfilelist)
    ### phase 2
    findDups()
    ### phase 3
    purge_dups()
    ### phase 4
    transcode(fileEntry, quality)
    insertTags()
    ### phase 5
    report_builder(reportType)


# standard boilerplate
if __name__ == '__main__':
    main()
