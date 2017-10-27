#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** ui.py                  user interface             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#           self.dialog.exitcodes = ("0 DIALOG_OK", "1 DIALOG_CANCEL",
#                                    "-1 DIALOG_ESC", "-1 DIALOG_ERROR",
#                                    "3 DIALOG_EXTRA", "2 DIALOG_HELP",
#                                    "4 DIALOG_ITEM_HELP")
# TODO: check Lynda vid 1203 & 1204!!!!

class UserInterface:
    def __init__(self, uiStyle="dialog"):
        self.__uiStyle = uiStyle
        if self.__uiStyle == "dialog":
            from dialog import Dialog
            self.myInterface = Dialog(dialog=self.__uiStyle, DIALOGRC=None,
                                      compat=self.__uiStyle, use_stdout=None,
                                      autowidgetsize=True,
                                      pass_args_via_file=True)
        else:
            raise TypeError




# # # multi line text boxes
    @classmethod
    def message_box(self, message, title):
        result = myInterface.msgbox(message, title)
        return result
    @classmethod
    def text_box(self, filePath):
        result = myInterface.textbox(filePath)
        return result
    @classmethod
    def scroll_box(self, message, title):
        result = myInterface.scrollbox(message, title)
        return result
    @classmethod
    def text_editor(self, initialText, args, title):
        args = [None, None]
        result = myInterface.editbox_str(initialText, args, title)
        return result # returns a tuple (exitcode, text)
    @classmethod
    def tail_box(self, filePath, title):
        myInterface.tailbox(filePath, title)

# # # Displaying transient messages
    @classmethod
    def announce(self, message, title):
        result = myInterface.infobox(message, title)
        return result
    @classmethod
    def countdown(self, message, timeOut, title):
        # timeOut is secs(int)
        result = myInterface.pause(message, timeOut, title)
        return result
# # # progress indicators
    @classmethod
    def progress_bar(self, message, percent, title):
        if percent == '':
            percent = 0
        myInterface.guage_start(message, percent, title)
        # # # ToDo: Create progressBarObject to enclose guage & guageupdate
        #  and to automatically call guagestop at 100%"""
    @classmethod
    def progress_bar_update(self, percent, message, updateMessage=False):
        myInterface.guage_update(percent, message, updateMessage)
        if percent == '':
            percent = 10
    @classmethod
    def progress_bar_stop(self):
        result = myInterface.guage_stop()
        return result
    @classmethod
    def multi_progress_bar(self, message, percent, elements, title):
        if percent == '':
            percent = 0
        result = myInterface.mixedguage(message, percent, elements, title)
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

# # # lists
    @classmethod
    def buid_list(self, message, items, title):
        # items[(tag, item, status)]
        listheight = None
        result = myInterface.buildlist(message, listheight, items, title)
        if result[0] != "DIALOG_OK":
            print("oops, something went wrong...")
        else:
            return result[1]
    @classmethod
    def check_list(self, message, choices, title):
        # chhoices[(tag, item, status)]
        listheight = None
        result = myInterface.checklist(message, listheight, choices, title)
        if result[0] != "DIALOG_OK":
            print("oops, something went wrong...")
        else:
            return result[1]
    @classmethod
    def menu_list(self, message, choices, title):
        # choices[(tag, item)] where tag = shortname, item = description
        menuheight = None
        result = myInterface.menu(message, menuheight, choices, title)
        if result[0] != "DIALOG_OK":
            print("oops, something went wrong...")
        else:
            return result[1]
    @classmethod
    def radio_list(self, message, choices, title):
        # choices[(tag, item)] where tag = shortname, item = description
        list_height = None
        result = myInterface.menu(message, list_height, choices, title)
        if result[0] != "DIALOG_OK":
            print("oops, something went wrong...")
        else:
            return result[1]
    @classmethod
    def tree_view(self, message, choices, title):
        # choices[(tag, item)] where tag = shortname, item = description
        menuheight = None
        result = myInterface.menu(message, menuheight, choices, title)
        if result[0] != "DIALOG_OK":
            print("oops, something went wrong...")
        else:
            return result[1]

# # # Single-line input fields
    @classmethod
    def input_box
        pass
    @classmethod
    def input_menu
        pass
    @classmethod
    def password_box
        pass

# # # Forms
   @classmethod
    def form
        pass
    @classmethod
    def mixed_form
        pass
    @classmethod
    def password_form
        pass

# # # Selecting files and directories
    @classmethod
    def select_dir(self, rootDir, title):
        selectedDir = myInterface.dselect(rootDir, title)
        if debugSwitch == True:
            debugLog += "selectDir returned %s and %s. \n" % (selectedDir[1],
                                                              selectedDir[2])
        return selectedDir

    @classmethod
    def select_file_or_dir(self, rootdir, title)
        pass

# # # Date and time
    @classmethod
    def calendar_box
        pass
    @classmethod
    def time_box
        pass

# # # Miscellaneous
    @classmethod
    def range_box
        pass
    @classmethod
    def yn_question(self, question, buttons, title):
        if buttons['yes_label'] == '':
            buttons['yes_label'] = ui_language['yes']
        if buttons['no_label'] == '':
            buttons['no_label'] = ui_language['no']
        result = myInterface.yesno(question, buttons, title)
        return result

def main():
    # testfunction for this module
    pass

# standard boilerplate
if __name__ == '__main__': main()
