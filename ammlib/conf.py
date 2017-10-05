"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** conf.py                   config manager          VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
class AMMconfig :
    def __init__(self) :
        import fsops
        cfg_file = 'ammConfig.cfg'
        self.cfg = null
        if not fsops.verify_file_exists(cfg_file):
             self.cfgWizard()


    def cfgWizard(self):
        # ask for source dir
        ammConfig['source_dir'] = myUI.selectDir("/media/",
        'Please select the source directory: ')
        ammConfig['target_dir'] = myUI.selectDir("/media/",
        'Please enter the target directory: ')
        while not(fsop.verify_dir_exists(target_dir)): # needs rewrite
            must_create_dir = myUI.question(
            'The target directory does not exist. Should I create it? (y/n)')
        if must_create_dir == 'y':
            fsop.create_dir(target_dir)
        else :
            target_dir = input('Please enter a different target directory.')
    target_dir = ammConfig('target_dir')
    return result
