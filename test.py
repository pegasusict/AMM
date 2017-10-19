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
debugswitch = True
ui_style = "dialog"
ui_language = "en"
AMM_TITLE = "Audiophiles Music Manager"
MY_UI = None
amm_config = None
db_handle = None

#import sys
#import time

### load my own code
#import lib.fsops as fsops
#import lib.conf as conf
import lib.ui as ui
#import lib.db_agent as dba
#import lib.afops as afops
#import lib.inetc as inetc
#import lib.daemonizer as daemonizer
#import lib.reportbuilder as reportbuilder

print("testing...")
MY_UI = lib.ui.UserInterface()
testdata['message'] = "hello"
testdata['title'] = "test title"
try:
    result = MY_UI.announce(**testdata)
except Exception, e:
    print str(e)
