#!/usr/bin/env python3
"""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* Audiophiles Music Manager          Build 20180119          VER0.0.0PREALPHA *
* (C)2017 Mattijs Snepvangers                           pegasus.ict@gmail.com *
* amm.py                             Main script             VER0.0.0PREALPHA *
* License: MIT                             Please keep my name in the credits *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
# # # Defining variables...
debug_switch = False # NOT A CONSTANT
ui_style = "dialog" # NOT A CONSTANT
ui_language = "en" # NOT A CONSTANT
PACKAGE_TITLE = "Audiophiles Music Manager"
my_ui = "" # NOT A CONSTANT
amm_config = dict() # NOT A CONSTANT
db_handle = None # NOT A CONSTANT

# import sys
# import time

# # # load my own code
# import lib.exceptions as exceptions
import lib.fsops as fsops
import lib.conf as conf

import lib.db_agent as db_handle
import lib.afops as afops
# import lib.inetc as inetc
# import lib.daemonizer as daemonizer
import lib.reportbuilder as reportbuilder

def init():
    """init function

    broke down main function to increase readability"""
    global debug_switch # NOT A CONSTANT
    global ui_style # NOT A CONSTANT
    global my_ui # NOT A CONSTANT
    global ui_language # NOT A CONSTANT

    # # # init, load /generate config
    amm_config = conf.AMMconfig()
    db_handle = dba.DB_agent()

def mainmenu():
    """menu constructor"""
    choices = {wizard, "run the configuration wizard",
               scan, "scan source directory for audiofiles"
               }
    # if reportbuilder.number_of_reports > 0 :
    #     choices.append['reports'] = "View reports of previous runs"
    kwargs=(message, choices, title)
    chosenpath = my_ui.menu_list(**kwargs)
    return chosenpath

def __main__():
    init()
    chosenpath = mainmenu()
    if chosenpath == "wizard":
        # run configuration wizard
        conf.cfg_wizard()
    elif chosenpath == "scan":
        # # # phase 0
        # # scan source dir
        fsops.scan_dir(amm_config['basedir'])
        reportsection = "scanned_src"
        reportbuilder.append_report_data(reportsection, file_list, trashlist)
        ## add audiofiles to DB
        db_handle(store, scanned_dir['audiofiles'], "stage_completed=1")
        del scanned_dir['audiofiles']
        # # purge non-audio files
        for file_entry in scanned_dir['trash']:
            fsops.delete_file(file_entry)
        del scanned_dir
        # stagecomplete = '1'
    else :
        #illegal option
        raise Error(SystemError, "The programmer made a booboo!")

    # # # phase 2 -=- NEEDS TO RUN IN SEPARATE THREAD(s)
    # # parse & purge tags
    file_list = db_handle.get("stage_completed=1")
    newfile_list = afops.tags_parser(file_list)
    del file_list
    afops.normalize_audio(newfile_list)
    afops.strip_silences(newfile_list)
    afops.generate_fingerprints(newfile_list)
    # # calculate qualityIndex
    for file_entry in newfile_list:
        afops.rate_quality(file_entry)
        # # # figure out what to get from where and how to compare codecs
    db_handle.update(newfile_list, "stagecompleted=2")
    del newfile_list
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
if __name__ == '__main__':
    __main__()
