#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** inetc.py              internet client             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""

class deBUGger():
    """debugger...

    generates debug log"""
    def __init__(self):
        import time
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        debugfile = "debug-" + timestamp + ".log"
