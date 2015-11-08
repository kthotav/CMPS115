# File: connection.py
# Establish conection to the local database mysql

import mysql.connector
from mysql.connector import errorcode

global cnx, cursor
def establishConnection():
    # login info
    config = {
        'user': 'root',
        'password': 'pwd',
        'host': 'localhost',
        'database': 'dbPV',
        'raise_on_warnings': True,
    }

    # establish connection
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        return "Success. Connection Established!"
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return "Database does not exist"
        else:
            return err


def closeConnection():
    cnx.commit()
    cursor.close()
    cnx.close()
