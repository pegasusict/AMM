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
    do_something_else()
"""

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

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
