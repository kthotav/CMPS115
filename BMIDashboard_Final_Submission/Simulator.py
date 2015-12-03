# Simulator.py is the program that calls the mock sensor (Sensor.py) and the parser (Parser.py).
# It threads a process to run main until the sensor has finished grabbing data from the current file that it
# is looking in. It also keeps track of global variables that are essential to the sensor and parser programs
# such as timestep counter (tsc) and file line number (linenr).

import threading
import sys
import os
import time
import Sensor
import Parser
import subprocess

def main():
   global numOfAcq
   global linenr
   global tsc
   
   tup = []
   tup = Sensor.mock(tsc, linenr)

   if tsc >= 2: tsc -= 1

   Parser.parse(tsc)

   cmd = "cd DATABASE; ./bmi.sh"
   p = subprocess.call(cmd, shell=True)
   
   numOfAcq += 1
   linenr = tup[0]
   tsc = tup[1]
   
   print("DATA HAS BEEN ACQUIRED " + str(numOfAcq) + " TIMES\n")
   if not (linenr == -1): threading.Timer(0, main).start() # threads in seconds
   else: return

# Initialize global variables
numOfAcq = 0
linenr = 0
tsc = 0
Parser.createDataDict("/Users/octavio/Desktop/CMPS115/BMIDashboard/SENSOR/MBNMS_Monday.eso")
main()
