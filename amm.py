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
#import sys
import locale
#import time
import configargparse as argparse

import fsops
import conf
import ui
import db_agent
import afops
#import inetc
#import daemonizer

DEBUG_SWITCH = False
UI_STYLE = "dialog"
UI_LANGUAGE = "en"

def init():
    """init function

    broke down main function to increase readability"""
    global DEBUG_SWITCH
    global UI_STYLE
    global MY_UI
    locale.setlocale(locale.LC_ALL, '')
    parser = argparse.ArgumentParser(default_config_files=['/etc/AMM/*.conf',
                                                           '~/.AMM/*.conf',
                                                           './conf/*.conf'])
    parser.add_argument("--dialog", help=
                        "Use Dialog Interface (default enabled)",
                        action="store_true", default=True)
    parser.add_argument("--debug", help="enable debug mode",
                        action="store_true", default=False)
    parser.add_argument("--language",
                        help="select UI language. \
                        Valid options are \"nl\" or \"en\"(default)")
    args = parser.parse_args()
    if args.debug:
        DEBUG_SWITCH = True
    if args.dialog:
        UI_STYLE = "dialog"
    if args.language == "nl":
        UI_LANGUAGE = "nl"
    else:
        UI_LANGUAGE = "en"
    MY_UI = ui.UserInterface(uiStyle)
    MY_UI.infobox(UI_LANGUAGE['init'])
    ### init, load /generate config
    AMM_CONFIG = conf.AMMconfig()
    DB_HANDLE = db_agent.db_handler("initialise")


def mainmenu():
    # construct the menus
    echo("blah")

def report_builder(reportType, reportData):
        ### determine what template to use
    if reportType == "display":
        echo('### display template')
    elif reportType == "html":
        echo('### html template')
    else:                        # reportType = "text"
        echo('### text template')
    return result

def main():
    init()
    mainmenu()
    ### phase 0
    ## scan source dir
    scanned_dir = fsops.scan_dir(ammConfig['basedir'])
    ## add audiofiles to DB
    DB_HANDLE("store", scanned_dir['audiofiles'], "stage_completed=1")
    del scanned_dir['audiofiles']
    ## purge non-audio files
    for fileEntry in scanned_dir['trash']:
        delete_file(fileEntry)
    del scanned_dir
    #stagecomplete = '1'
    ### phase 2 -=- NEEDS TO RUN IN SEPARATE THREAD
    ## parse & purge tags
    filelist = DB_HANDLE("get", "stage_completed=1", limit=100) ### LOOP !!!
    newfilelist = tag_parser(filelist)
    del filelist
    afops.stripSilences(newfilelist)
    afops.generate_fingerprints(newfilelist)
    ## calculate qualityIndex
    for fileEntry in newfilelist:
        echo('we must do something')
        ### figure out what to get from where and how to compare codecs
    dbstatus = DB_HANDLE("update", newfilelist, "stagecompleted=2")
    del newfilelist
    #stagecomplete = '2'
    ### phase 3
    afops.find_n_purge_dups()
    #stagecomplete = '3'
    ### phase 4
    transcode(fileEntry, quality)
    insertTags(fileEntry, tags)
    #stagecomplete = '4'
    ### phase 5
    report_builder(reportType, reportData)
    #stagecomplete = '5'

# standard boilerplate
if __name__ == '__main__':
    main()
