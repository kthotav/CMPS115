import connection, glob


def show_entry_fields():
    cnx = connection.establishConnection()
    for file in glob.glob("clean*.csv")
    pv_files = open("pv_data/")
    for pv_file in pv_files:
        pv_data = pv.reader(file(pv_file))
        for row in pv_data:
           cursor.execute('INSERT INTO pv(timeStep, \
               pac, temperature, vac, var_date )' 'VALUES(%s, %s, %s, %s, %s)', row)

    cnx.commit()
    connection.closeConnection()
