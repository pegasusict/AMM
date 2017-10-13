"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** db_agent.py                  DB agent             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
class DBagent :
    def __init__(self):
        self.dbConnectInfo = ammConfig.get(dbConnectInfo)
        import mysql.connector as dba
        from mysql.connector import errorcode as dba_errorcode

    @classmethod
    def db_connect(self):
        if DBport != 3306:
            DBhost = DBHost + ":" + DBport
        #connect to database, display error if something goes wrong
        try:
            __myDB = dba.connect(DBuser, DBpass, DBhost, DB)
        except dba.Error as dba_error:
            if dba_error == dba_errorcode.ER_ACCESS_DENIED_ERROR:
                print("Authentication error")
            elif dba_error == dba_errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(dba_error)

    def db_create(self, table):
        """ Function doc """
        echo("blah")
