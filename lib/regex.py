#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** regex.py                 RegEx module             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
# import libs
import re

email_filter = re.compile(
    """^\A(?=[a-z0-9@.!#$%&'*+/=?^_`{|}~-]{6,254}\z)
    (?=[a-z0-9.!#$%&'*+/=?^_`{|}~-]{1,64}@)
    [a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*
    @ (?:(?=[a-z0-9-]{1,63}\.)[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+
    (?=[a-z0-9-]{1,63}\z)[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\z$", IGNORECASE)""")

def main():
    """just in case somebody wants to test this file by itself"""
    print("It works!!! ;-)")
    ###TODO### do something with the various methods/functions of this file

# standard boilerplate
if __name__ == '__main__':
    main()
