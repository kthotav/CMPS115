# import modules
import mysql.connector
from mysql.connector import errorcode
import csv
import json, ast
import datetime
import time

from Tkinter import *



# MySQL server login info

# establish connection




def show_entry_fields():
  config = {
    'user': 'root',
    'password': 'pwd',
    'host': 'localhost',
    'database': 'dbPV',
    'raise_on_warnings': True,
  }

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()

  date = e1.get()
  print date

  query = ("""SELECT timeStep AS TimeStep, temperature AS Temperature, vac AS Vac, pac AS Pac FROM pv WHERE var_date = '%s' """ % (date))

  cursor.execute(query)
  rows = cursor.fetchall()

  c = csv.writer(open("data.csv","w"))
  c.writerow([i[0] for i in cursor.description])
  for row in rows:
      c.writerow(row)


  cursor.close()
  cnx.close()



master = Tk()
Label(master, text="Enter Date").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )

# date = str(raw_input("Enter date: "))
# query = ("""SELECT timeStep AS TimeStep, temperature AS Temperature, vac AS Vac, pac AS Pac FROM pv WHERE var_date = '%s' """ % (date))
#
# cursor.execute(query)
# rows = cursor.fetchall()
#
# c = csv.writer(open("data.csv","w"))
# c.writerow([i[0] for i in cursor.description])
# for row in rows:
#     c.writerow(row)
#
#
# cursor.close()
# cnx.close()
