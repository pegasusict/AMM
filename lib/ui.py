"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** ui.py                  user interface             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
# ToDo:
#  -replace all kwargs by their contens
#  - reread complete pythondialog documentation
#
#
########################################################################
#           self.dialog.exitcodes = ("0 DIALOG_OK", "1 DIALOG_CANCEL",
#                                    "-1 DIALOG_ESC", "-1 DIALOG_ERROR",
#                                    "3 DIALOG_EXTRA", "2 DIALOG_HELP",
#                                    "4 DIALOG_ITEM_HELP")

class UserInterface:
    def __init__(self, uiStyle="dialog"):
        self.__uiStyle = uiStyle
        if self.__uiStyle == "dialog":
            from dialog import Dialog
            self.myInterface = Dialog(dialog=self.__uiStyle, DIALOGRC=None,
                                      compat=self.__uiStyle, use_stdout=None,
                                      autowidgetsize=True,
                                      pass_args_via_file=True)

### multi line text boxes
    @classmethod
    def messageBox(self, message, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        result = myInterface.msgbox(message, kwargs)
        return result
    @classmethod
    def textBox(self, filePath):
        result = myInterface.textbox(filePath)
        return result
    @classmethod
    def scrollBox(self, message, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        result = myInterface.scrollbox(message, kwargs)
        return result
    @classmethod
    def texteditor(self, initialText, args, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        args = [None, None]
        result = myInterface.editbox_str(initialText, args, kwargs)
        return result # returns a tuple (exitcode, text)
    @classmethod
    def tailBox(self, filePath, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        myInterface.tailbox(filePath, kwargs)

### Displaying transient messages
    @classmethod
    def announce(self, message, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        result = myInterface.infobox(message, kwargs)
        return result
    @classmethod
    def countdown(self, message, timeOut, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        # timeOut is secs(int)
        result = myInterface.pause(message, timeOut, kwargs)
        return result
### progress indicators
    @classmethod
    def progressbar(self, message, percent, dialogtitle):
        if percent == '':
            percent = 0
        kwargs['dialogtitle'] = dialogtitle
        myInterface.guage_start(message, percent, kwargs)
        #ToDo: Create ProgressBarObject to enclose guage & guageupdate
        #  and to automatically call guagestop at 100%"""
    @classmethod
    def progressbarUpdate(self, percent, message, updateMessage=False):
        myInterface.guage_update(percent, message, updateMessage)
        if percent == '':
            percent = 10
    @classmethod
    def progressbarStop(self):
        result = myInterface.guage_stop()
        return result
    @classmethod
    def multiProgressbar(self, message, percent, elements, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        if percent == '':
            percent = 0
        result = myInterface.mixedguage(message, percent, elements, kwargs)
        # elements[] is a list of tuples consisting of (tag, value)
        #   possible values are:
        #   a percentage (-25 equals 25%) or
        #   Succeeded, Failed, Passed, Completed, Done, Skipped,
        #   In Progress, Checked, N/A
        # ToDo:
        #   Create an Object that automatically recalculates
        #   total_progress and resends the mixedguage command
        #   whenever one of the element values (and thereby
        #   total_progress) is changed
        return result

### lists
    @classmethod
    def buidList(self, message, items, dialogtitle):
        # items[(tag, item, status)]
        kwargs['dialogtitle'] = dialogtitle
        listheight = None
        result = myInterface.buildlist(message, listheight, items, kwargs)
        if result[0] != "DIALOG_OK":
            print"oops, something went wrong..."
        else:
            return result[1]
    @classmethod
    def checkList(self, message, choices, dialogtitle):
        # chhoices[(tag, item, status)]
        kwargs['dialogtitle'] = dialogtitle
        listheight = None
        result = myInterface.checklist(message, listheight, choices, kwargs)
        if result[0] != "DIALOG_OK":
            print"oops, something went wrong..."
        else:
            return result[1]
    @classmethod
    def menuList(self, message, choices, dialogtitle):
        # choices[(tag, item)] where tag = shortname, item = description
        kwargs['dialogtitle'] = dialogtitle
        menuheight = None
        result = myInterface.menu(message, menuheight, choices, kwargs)
        if result[0] != "DIALOG_OK":
            print"oops, something went wrong..."
        else:
            return result[1]
    @classmethod
    def radioList(self, message, choices, dialogtitle):
        # choices[(tag, item)] where tag = shortname, item = description
        kwargs['dialogtitle'] = dialogtitle
        list_height = None
        result = myInterface.menu(message, list_height, choices, kwargs)
        if result[0] != "DIALOG_OK":
            print("oops, something went wrong...")
        else:
            return result[1]
    @classmethod
    def treeView(self, message, choices, dialogtitle):
        # choices[(tag, item)] where tag = shortname, item = description
        kwargs['dialogtitle'] = dialogtitle
        menuheight = None
        result = myInterface.menu(message, menuheight, choices, kwargs)
        if result[0] != "DIALOG_OK":
            print("oops, something went wrong...")
        else:
            return result[1]

### Single-line input fields
#    @classmethod
#    def inputBox
#    @classmethod
#    def inputMenu
#    @classmethod
#    def passwordBox

### Forms
#    @classmethod
#    def form
#    @classmethod
#    def mixedForm
#    @classmethod
#    def PasswordForm

### Selecting files and directories
    @classmethod
    def selectDir(self, rootDir, title):
        selectedDir = myInterface.dselect(rootDir, title)
        if debugSwitch == True:
            debugLog += "selectDir returned %s and %s. \n" % (selectedDir[1],
                                                              selectedDir[2])
        return selectedDir

#    @classmethod
#    def selectFileDir(self, rootdir, title)
#        return result

### Date and time
#    @classmethod
#    def calendarBox
#    @classmethod
#    def timeBox

### Miscellaneous
#    @classmethod
#    def rangeBox
    @classmethod
    def ynQuestion(self, question, buttons, title):
        if buttons['yes_label'] == '':
            buttons['yes_label'] = ui_language['yes']
        if buttons['no_label'] == '':
            buttons['no_label'] = ui_language['no']
        self.__ynQuestion = myInterface.yesno(question, buttons, title)
