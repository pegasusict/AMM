#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** exceptions.py             Exception handler       VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""

# except IOError as error
# except ValueError as error

"""
Exception construct:

Try:
    <code>
Except <blabla>Error as error:
    print("something went wrong: ", error)
finally:
    print("goodbye cruel world!")

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

home made exception:

try:
    raise <blabla>Error
except <blabla>Error as error:
    do_something(error)
finally
    do_something_else()   """

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class ProgrammerError(Error):
    """Exception raised for errors caused by the writer of this software

    Attributes:
        expression -- expression where the mistake took place
        message -- explanation of the error
    """

    def __init__(self, expression, message="My maker has made a doo doo"):
        self.expression = expression
        self.message = message
