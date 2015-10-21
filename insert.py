# import csv
# import MySQLdb
#
# mydb = MySQLdb.connect(host='localhost',
#     user='root',
#     passwd='root',
#     db='test1')
# cursor = mydb.cursor()
#
# csv_data = csv.reader(file('datatest.csv'))
# for row in csv_data:
#
#     cursor.execute('INSERT INTO data1(TimeStep, \
#           Temperature )' \
#           'VALUES("%s", "%s")',
#           row)
# #close the connection to the database.
# mydb.commit()
# cursor.close()
# print "Done"

import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='test1')
cnx.close()
