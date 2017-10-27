#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** conf.py                   config manager          VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************"""

class AMMconfig :
    def __init__(self):
        import lib.fsops as fsops
        # ToDo:
        #   devise a method to utilize configArgParse to read the files
        #   and figure out how to proceed in case of missing files or
        #   arguments
        import locale
        locale.setlocale(locale.LC_ALL, '')
        import configargparse as argparse
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
        import lib.ui as ui
        MY_UI = ui.UserInterface(ui_style)
        MY_UI.announce(ui_language['init'], AMM_TITLE)


    @classmethod
    def sysinit(self, amm_config):
        if amm_config == None: # is this check valid?
            amm_config['runWizard'] = True

    @classmethod
    def cfgWizard(self):
        ### check DB connection, if not available try default settings
        kwargs = ui_language["trydb"]
        announce_title = ui_language["wait"]
        MY_UI.announce(announce_msg, announce_title)
        ### if default DB settings don't work, ask for DB info, providing
        #    default answers where applicable
        amm_config
        ### ask for source dir
        amm_config['source_dir'] = myUI.selectDir("/media/",
                                                 'Please select the source \
                                                 directory: ')
        ### create or select target directory
        kwargs['yes_label'] = ui_language["create"]
        kwargs['no_label'] = uilanguage["select"]
        must_create_dir = MY_UI.ynQuestion('Do you wish to create or select \
                                           a target directory?', **kwargs)
        ### if directory needs to be created, select dir wherein to
        #    create targetdir
        if must_create_dir == 'y':
            amm_config['base_dir'] = MY_UI.selectDir("/media/",
                                                    'Please select the \
                                                    directory wherein to \
                                                    create the target \
                                                    directory:')
            fsops.create_dir(amm_config['target_dir'])
        else:
            amm_config['target_dir'] = MY_UI.selectDir("/media/",
                                                      'Please select the \
                                                      target directory:')
        ### select output filetype & quality,
        #    default "mp3, lame preset: paranoid (where possible)"

        ### select output structure
        # default:<firstAlphaNumChar>/<artist>/(<year>) <album>/

        ### select included info (lyrics, albumart, mood)
        #    default: lyrics, albumart,

        ### whether to purge collection of live music (default: yes)


def main():
    # testfunction for this module
    pass

# standard boilerplate
if __name__ == '__main__': main()
