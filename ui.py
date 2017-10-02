"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** ui.py                  user interface             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
### import libs
class UserInterface :
    def __init__(uiStyle, uiElement, uiMessage):
        self.__uiStyle = uiStyle
        del uiStyle
        self.__uiElement = uiElement
        del uiElement
        self.__uiMessage = uiMessage
        del uiMessage

        if self.__uiStyle == "dialog" :
            from dialog import Dialog
            self.__infobox = Dialog.infobox(uiMessage)
        elif self.__uiStyle == "html" :
            ### generate html interface (template)
            self.output = "<html>" #etc etc
