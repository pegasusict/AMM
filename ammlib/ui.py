"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** ui.py                  user interface             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""

class UserInterface :
    def __init__(self, uiStyle) :
        self.__uiStyle = uiStyle
        if self.__uiStyle == "dialog" :
            from dialog import Dialog
            self.myDialog = new Dialog()

    def selectDir(self, rootDir, dialogtitle) :
        selectedDir = myDialog.dselect(rootDir, height=None, width=None,
                                       title=dialogtitle)
        return selectedDir

    def infoBox(self, message) :
        self.__infobox = myDialog.infobox(message, height=None, width=None)

    def ynQuestion(self, question, buttons[yes_label="yes" no_label="no"]):
        self.__ynQuestion = myDialog.yesno(question, height=None, width=None,
                                           buttons)

#        elif self.__uiStyle == "html" :
#            ### generate html interface (template)
#            self.output = "<html>" #etc etc

#           self.dialog.exitcodes = ("0 DIALOG_OK", "1 DIALOG_CANCEL",
#                                    "-1 DIALOG_ESC", "-1 DIALOG_ERROR",
#                                    "3 DIALOG_EXTRA", "2 DIALOG_HELP",
#                                    "4 DIALOG_ITEM_HELP")
