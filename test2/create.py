# import modules
import mysql.connector
from mysql.connector import errorcode
import csv
import json, ast
import datetime
import time

# MySQL server login info

config = {
  'user': 'root',
  'password': 'pwd',
  'host': 'localhost',
  'database': 'dbPV',
  'raise_on_warnings': True,
}



# establish connection


cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

date = '2015-10-22'
query = ("SELECT timestep, temperature, vac, pac FROM pv WHERE var_date = '%s' " % (date))

cursor.execute(query)
rows = cursor.fetchall()
for row in rows:

  print ast.literal_eval(json.dumps(row))


cursor.close()
cnx.close()
