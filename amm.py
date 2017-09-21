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


def report_builder():

### MAIN ###
def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="enable debug mode"
                        action="store_true")
    args=parser.parse_args()
    if args.debug:
        debugSwitch = True
    #load config
    prefs = parse_prefs()
    #modulelist = scan_modules() #???
    #dbsession = db_handler("init", sessiondata)
    # phase 0
    basedir = prefs(basedir)
    scan_dir(basedir)   ###include daemonizer functionality
    # phase 1
    filelist = db_handler("get", entries flagged "0")
    newfilelist = tag_parser(filelist)
    del filelist
    dbstatus = db_handler("update", newfilelist)
    # phase 3
    purge_dups()

# standard boilerplate
if __name__ == '__main__':
    main()
