#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** amm.py                 main script                VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
# # # Defining variables...
DEBUG_SWITCH: bool = False
UI_STYLE: str = "dialog"
UI_LANGUAGE = "en"
PACKAGE_TITLE = "Audiophiles Music Manager"
# MY_UI: str = ""
AMM_CONFIG = dict()
db_handle: object = None

# import sys
# import time

# # # load my own code
# import lib.exceptions as exceptions
import lib.fsops as fsops
# import lib.conf as conf

import lib.db_agent as dba
import lib.afops as afops
# import lib.inetc as inetc
# import lib.daemonizer as daemonizer
import lib.reportbuilder as reportbuilder

def init():
    """init function

    broke down main function to increase readability"""
    global DEBUG_SWITCH
    global UI_STYLE
    global MY_UI
    global ui_language
    # # # init, load /generate config
    amm_config = conf.amm_config()
    db_handle = dba.db_connect()

def mainmenu():
    """menu constructor"""
    choices = {wizard, "run the configuration wizard",
               scan, "scan source directory for audiofiles"
               }
    if reportbuilder.number_of_reports > 0 :
        choices.append['reports'] = "View reports of previous runs"
    kwargs=(message, choices, title)
    MY_UI.menu_list(**kwargs)

def main():
    init()
    mainmenu()
    # # # phase 0
    # # scan source dir
    scanned_dir = fsops.scan_dir(amm_config['basedir'])
    reportsection = "scanned_src"
    reportbuilder.append_report_data(reportsection, scanned_dir)
    ## add audiofiles to DB
    db_handle.store(scanned_dir['audiofiles'], "stage_completed=1")
    del scanned_dir['audiofiles']
    # # purge non-audio files
    for file_entry in scanned_dir['trash']:
        fsops.delete_file(file_entry)
    del scanned_dir
    # stagecomplete = '1'
    # # # phase 2 -=- NEEDS TO RUN IN SEPARATE THREAD(s)
    # # parse & purge tags
    filelist = db_handle.get("stage_completed=1", limit=1000) ### LOOP !!!
    newfilelist = afops.tags_parser(filelist)
    del filelist
    afops.normalize_audio(newfilelist)
    afops.strip_silences(newfilelist)
    afops.generate_fingerprints(newfilelist)
    # # calculate qualityIndex
    for file_entry in newfilelist:
        afops.rate_quality(file_entry)
        # # # figure out what to get from where and how to compare codecs
    db_handle.update(newfilelist, "stagecompleted=2")
    del newfilelist
    # stagecomplete = '2'
    # # # phase 3
    afops.find_n_purge_dups()
    # stagecomplete = '3'
    # # # phase 4
    afops.transcode(file_entry, quality)
    afops.insert_tags(file_entry, tags)
    # stagecomplete = '4'
    # # # phase 5
    reportbuilder.append_report_data(reportSection, reportData)
    # stagecomplete = '5'

# standard boilerplate
if __name__ == '__main__': main()
