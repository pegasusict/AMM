#!/usr/bin/env python3 -tt
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** ui.py                  user interface             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
### import libs

def user_interface(uiStyle, uiElement, uiMessage):
    if uiStyle == "dialog" :
        from dialog import Dialog
        infobox = Dialog.infobox(uiMessage)
    elif uiStyle == "html" :
        ### generate html interface (template)
