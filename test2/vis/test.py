# Connects to the local MySQL database

# import modules
import mysql.connector
from mysql.connector import errorcode
import csv

# MySQL server login info

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
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

#


# create database
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
        print("Creating table {}: ".format(name))
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

csv_files = ['pv_oct21.csv', 'pv_oct22.csv']
for csv_file in csv_files:
  csv_data = csv.reader(file(csv_file))
  for row in csv_data:
      cursor.execute('INSERT INTO pv(timeStep, \
            pac, temperature, vac, var_date )' 'VALUES(%s, %s, %s, %s, %s)', row)

# close connection
cnx.commit()

cursor.close()
cnx.close()
