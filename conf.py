#!/usr/bin/env python3 -tt
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** conf.py                   config manager          VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
import fsop

def load_conf(cfg_file='amm.cfg'):
    global amm_config
    if not fsop.verify_file_exists(cfg_file):
        result = False
    else:
        amm_config = parse_cfg_file(cfg_file)
        result = True
    return result

def get_conf():
    global amm_config
    # ask for source dir
    source_dir = input('Please enter the source directory: ')
    # if the source dir does not exist
    while not fsop.verify_dir_exists(source_dir):
        # ask again until we get a valid answer
        source_dir = input('Please enter a valid path: ')
    amm_config['source_dir'] = source_dir
    target_dir = input('Please enter the target directory: ')
    while not(fsop.verify_dir_exists(target_dir)): # needs rewrite
        must_create_dir = input(
            'The target directory does not exist. Should I create it? (y/n)')
        if must_create_dir == 'y':
            fsop.create_dir(target_dir)
        else :
            target_dir = input('Please enter a different target directory.')
    amm_config('target_dir') = target_dir
    return result

def __main__():
    if not load_conf():
        if not get_conf():
            exit('fatal config error')

