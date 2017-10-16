#!/usr/bin/env python3 -tt
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** amm.py                 main script                VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
### Defining variables...
debugswitch = False
ui_style = "dialog"
ui_language = "en"
AMM_TITLE = "Audiophiles Music Manager"
MY_UI = None
ammConfig = None
db_handle = None

### import libs
#import sys
import locale
#import time
import configargparse as argparse

import lib.fsops as fsops
import lib.conf as conf
import lib.ui as ui
import lib.db_agent as dba
import lib.afops as afops
#import lib.inetc as inetc
#import lib.daemonizer as daemonizer
import lib.reportbuilder as reportbuilder


def init():
    """init function

    broke down main function to increase readability"""
    global debugswitch
    global ui_style
    global MY_UI
    global ui_language
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
        debugswitch = True
    if args.dialog:
        ui_style = "dialog"
    if args.language == "nl":
        ui_language = "nl"
    else:
        ui_language = "en"
    MY_UI = ui.UserInterface(ui_style)
    MY_UI.announce(ui_language['init'], AMM_TITLE)
    ### init, load /generate config
    amm_config = conf.AMMconfig()
    db_handle = dba.db_connect()


def mainmenu():
    """menu constructor"""
    print "work in progress"

# standard boilerplate
if __name__ == '__main__':
    init()
    mainmenu()
    ### phase 0
    ## scan source dir
    scanned_dir = fsops.scan_dir(ammConfig['basedir'])
    reportsection = "scanned_src"
    reportbuilder.append_report_data(reportsection, scanned_dir)
    ## add audiofiles to DB
    db_handle("store", scanned_dir['audiofiles'], "stage_completed=1")
    del scanned_dir['audiofiles']
    ## purge non-audio files
    for file_entry in scanned_dir['trash']:
        delete_file(file_entry)
    del scanned_dir
    #stagecomplete = '1'
    ### phase 2 -=- NEEDS TO RUN IN SEPARATE THREAD(s)
    ## parse & purge tags
    filelist = db_handle("get", "stage_completed=1", limit=1000) ### LOOP !!!
    newfilelist = tag_parser(filelist)
    del filelist
    afops.normalize_audio(newfilelist)
    afops.strip_silences(newfilelist)
    afops.generate_fingerprints(newfilelist)
    ## calculate qualityIndex
    for file_entry in newfilelist:
        print 'we must do something'
        ### figure out what to get from where and how to compare codecs
    db_handle("update", newfilelist, "stagecompleted=2")
    del newfilelist
    #stagecomplete = '2'
    ### phase 3
    afops.find_n_purge_dups()
    #stagecomplete = '3'
    ### phase 4
    transcode(file_entry, quality)
    insertTags(file_entry, tags)
    #stagecomplete = '4'
    ### phase 5
    reportbuilder.report_data(reportSection, reportData)
    #stagecomplete = '5'
