#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** db_agent.py                  DB agent             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""

class db_agent :
    """Database agent

    will manage and interface with SQLite or MySQL DB"""
    def __init__(self):
        # my_sql = None
        # my_sql_errorcode = None
        self.dbConnectInfo = ammConfig.get(dbConnectInfo)
        import mysql.connector as my_sql
        from mysql.connector import errorcode as my_sql_errorcode

    @classmethod
    def db_connect(self):
        """connect to DB

        """
        if DBport != 3306:
            DBhost = DBHost + ":" + DBport
        #connect to database, display error if something goes wrong
        try:
            __my_db = my_sql.connect(DBuser, DBpass, DBhost, DB)
        except my_sql.Error as my_sql_error:
            if my_sql_error == my_sql_errorcode.ER_ACCESS_DENIED_ERROR:
                print("Authentication error")
            elif my_sql_error == my_sql_errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(my_sql_error)

    @classmethod
    def db_create(self, sql_struct):
        """ create DB, tables and structure """
        pass

def main():
    """just in case somebody wants to test this file by itself"""
    print("It works!!! ;-)")
    ###TODO### do something with the various methods/functions of this file

# standard boilerplate
if __name__ == '__main__':
    main()
