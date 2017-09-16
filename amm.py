#!/usr/bin/env python3 -tt
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** amm.py                 main script                VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
# import libs
import sys.argv as argv

def report_builder():

### MAIN ###
def main():
    args = argv
    # parse arguments
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

# standard boilerplate
if __name__ == '__main__':
    main()
