"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** conf.py                   config manager          VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************"""

class AMMconfig :
    def __init__(self):
        # blah
        echo(1)

    """devise a method to utilize configArgParse to read the files and
        figure out how to proceed in case of missing files/arguments"""

    def cfgWizard(self):
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
        else :
            target_dir = input('Please enter a different target directory.')
