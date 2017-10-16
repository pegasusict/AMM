"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** db_agent.py                  DB agent             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""

class db_agent :
    def __init__(self):
        my_sql = None
        my_sql_errorcode = None
        self.dbConnectInfo = ammConfig.get(dbConnectInfo)
        import mysql.connector as my_sql
        from mysql.connector import errorcode as my_sql_errorcode

    @classmethod
    def db_connect(self):
        if DBport != 3306:
            DBhost = DBHost + ":" + DBport
        #connect to database, display error if something goes wrong
        try:
            __myDB = my_sql.connect(DBuser, DBpass, DBhost, DB)
        except my_sql.Error as my_sql_error:
            if my_sql_error == my_sql_errorcode.ER_ACCESS_DENIED_ERROR:
                print("Authentication error")
            elif my_sql_error == my_sql_errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(my_sql_error)

    @classmethod
    def db_create(self, table):
        """ Function doc """
        echo("blah")
