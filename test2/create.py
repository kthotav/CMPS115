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

date = '2015-10-21'
query = ("""SELECT timeStep AS TimeStep, temperature AS Temperature, vac AS Vac, pac AS Pac FROM pv WHERE var_date = '%s' """ % (date))

cursor.execute(query)
rows = cursor.fetchall()

c = csv.writer(open("data.csv","w"))
c.writerow([i[0] for i in cursor.description])
for row in rows:
    c.writerow(row)


# columns = [desc[0] for desc in cursor.description]
# result = []
# for row in rows:
#     row = dict(zip(columns, row))
#     result.append(row)
#
# json_file = json.dumps(result)
# f = open('data.json', 'w')
# print >> f, json_file

# posts = [dict(Vac=row[2].encode('utf-8'), Pac=row[3].encode('utf-8'),  Temperature=row[1].encode('utf-8'), TimeStep=row[0].encode('utf-8')) for row in cursor.fetchall()]
# newposts = json.dumps(posts)
# f = open('data.json', 'w')
# print >> f, newposts
#
# for row in rows:
#   print ast.literal_eval(json.dumps(row))


cursor.close()
cnx.close()
