#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** daemonizer.py              daemonizer             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
# import libs

def startDaemons() :
    """Deamonizer start

    Daemons needed:
    FSOP/AFOPS => indexer/tagParser/dupsPurger/fingerprintGenerator/transcoder
    qualityCalc
    InetC => mbClient, albumArtFetcher, lyricsFetcher

    """
    if configLoaded == True:
        ###TODO### prepare daemons to be run - qeue manager??
        return True

def main():
    """just in case somebody wants to test this file by itself"""
    print("It works!!! ;-)")
    ###TODO### do something with the various methods/functions of this file

# standard boilerplate
if __name__ == '__main__':
    main()
