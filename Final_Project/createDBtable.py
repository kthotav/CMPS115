# File: createDBtable.py
# creates databaset able called pv ONLY once


def createDBTable():
    TABLES = {}
    TABLES['pv'] = (
        "CREATE TABLE `pv` ("
        "   timeStep VARCHAR(30) NOT NULL,"
        "   pac VARCHAR(30) NOT NULL,"
        "   temperature VARCHAR(30) NOT NULL,"
        "   vac VARCHAR(30) NOT NULL,"
        "   var_date date NOT NULL"
        ") ENGINE=InnoDB"
    )

    for name, ddl in TABLES.iteritems():
        try:
            return "Creating table " + name
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                return "already exists."
            else:
                print(err.msg)
        else:
            return "OK"
