#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** test.py                     test script           VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
### Defining variables...
UI_STYLE = "dialog"
ui_language = "en"
AMM_TITLE = "Audiophiles Music Manager"
# MY_UI = None
# amm_config = dict()
# db_handle = None

# import sys
# import time

# # # load my own code
# import lib.fsops as fsops
# import lib.conf as conf
import lib.ui as ui
# import lib.debugger
# import lib.db_agent as dba
# import lib.afops as afops
# import lib.inetc as inetc
# import lib.daemonizer as daemonizer
# import lib.reportbuilder as reportbuilder

def inclusive_range(*args):
    # generator function
    numargs = len(args)
    if numargs < 1: raise TypeError('Requires at least one argument')
    if numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError('inclusive_range expected at most 3 arguments, got {}.'.format(numargs)
    i = start
    while i <= stop:
        yield i  # pass on value and continue with loop
        i += step

def main():
    print("testing...")
    MY_UI = lib.ui.UserInterface('dialog')
    kwargs['message'] = "hello"
    kwargs['title'] = "test title"
    try:
        result = MY_UI.announce(**kwargs)
    except Exception, e:
        print str(e)

# standard boilerplate
if __name__ == '__main__':
    main()
