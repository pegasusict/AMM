#!/usr/bin/env python3
"""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* Audiophiles Music Manager          Build 20180119          VER0.0.0PREALPHA *
* (C)2017 Mattijs Snepvangers                           pegasus.ict@gmail.com *
* lib/daemonizer.py                  Daemonizer              VER0.0.0PREALPHA *
* License: MIT                             Please keep my name in the credits *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

# import libs

def start_daemons() :
    """Deamonizer start

    Daemons needed:
    FSOPS => indexer
    AFOPS => tagParser/dupsPurger/fingerprintGenerator/transcoder/qualityCalc
    InetC => mbClient, albumArtFetcher, lyricsFetcher

    """
    if config_loaded == True:
        ###TODO### prepare daemons to be run - qeue manager??
        return True

def main():
    """just in case somebody wants to test this file by itself"""
    print("It works!!! ;-)")
    ###TODO### do something with the various methods/functions of this file

# standard boilerplate
if __name__ == '__main__':
    main()
