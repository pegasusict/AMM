"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** conf.py                   config manager          VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************"""

class AMMconfig :
    def __init__(self):
        # ToDo:
        #   devise a method to utilize configArgParse to read the files
        #   and figure out how to proceed in case of missing files or
        #   arguments
        locale.setlocale(locale.LC_ALL, '')
        parser = argparse.ArgumentParser(
              default_config_files=['/etc/AMM/*.conf', '~/.AMM/*.conf',
                                    './conf/*.conf'])
        parser.add_argument("--dialog", help=
                            "Use Dialog Interface (default enabled)",
                            action="store_true", default=True)
        parser.add_argument("--debug", help="enable debug mode",
                            action="store_true", default=False)
        parser.add_argument("--language",
                            help="select UI language. \
                            Valid options are \"nl\" or \"en\"(default)")
        args = parser.parse_args()
        if args.debug:
            debugswitch = True
        if args.dialog:
            ui_style = "dialog"
        if args.language == "nl":
            ui_language = "nl"
        else:
            ui_language = "en"
        MY_UI = ui.UserInterface(ui_style)
        MY_UI.announce(ui_language['init'], AMM_TITLE)
        ### init, load /generate config
        amm_config = conf.AMMconfig()


    @classmethod
    def sysinit(self, ammConfig):
        if ammConfig == None:
            ammConfig['runWizard'] = True

    @classmethod
    def cfgWizard(self): ## needs complete rewrite
        # ask for source dir
        ammConfig['source_dir'] = myUI.selectDir("/media/",
                                                 'Please select the source \
                                                 directory: ')
        kwargs[yes_label] = "create"
        kwargs[no_label]="select"
        must_create_dir = MY_UI.ynQuestion('Do you wish to create or select \
                                          a target directory?', kwargs)
        if must_create_dir == 'y':
            fsops.create_dir(ammConfig['target_dir'])
        ammConfig['target_dir'] = MY_UI.selectDir("/media/",
                                                 'Please select the target \
                                                 directory: ')
        while not(fsops.verify_dir_exists(ammConfig['target_dir'])):
            must_create_dir = MY_UI.ynQuestion(
            'The target directory does not exist. Should I create it? (y/n)')
        if must_create_dir == 'y':
            fsops.create_dir(ammConfig['target_dir'])
