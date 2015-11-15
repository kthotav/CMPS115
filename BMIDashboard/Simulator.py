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

def main():
   # global variables for the other modules to use as a resource.
   #
   # numOfAcq:    The number of data acquisitions that the program has completed for the current day.
   #
   # linenr:      The line number that the sensor program is currently looking at in order to simulate
   #              the mock live data.
   #
   # tsc:         stands for Timestep Counter and represents the most recent timestep that the parser has
   #              parsed thus far.
   #
   global numOfAcq
   global linenr
   global tsc

   # tup:         A tuple pair that receives the current timestamp counter and line number that the sensor
   #              program takes in and updates.
   tup = []
   tup = Sensor.mock(tsc, linenr)
   
   # If the timestamp counter >= 2 then decrement it by 1 to compensate for the offset that occurs during the
   # identification of the first timestep line, which is 
   # "2,6,Day of Simulation[],Month[],Day of Month[],DST Indicator[1=yes 0=no],Hour[],StartMinute[],EndMinute[],DayType"
   # This is because that line is not a REAL timestep value. It is mere dictionary for the timestamp attributes
   # that are going to come later on in the file.
   if tsc >= 2: tsc -= 1

   # After the sensor mocks the live data by writing to a specific file, the parser goes to the file and parses it.
   Parser.parse(tsc)
   # Increment the numOfAcq variable since data has been acquired.
   # Update the line number using the value inside tup[0] as well as the timestep counter from tup[1]
   numOfAcq += 1
   linenr = tup[0]
   tsc = tup[1]
   print("DATA HAS BEEN ACQUIRED " + str(numOfAcq) + " TIMES\n")
   # If the line number is -1, that means the sensor has finished reading and mocking all of the values within the
   # current file that it is looking at. In this case, we halt the program. Otherwise, we thread a new process to
   # execute main once again, in a recursive-like manner.
   if not (linenr == -1): threading.Timer(0, main).start() # threads in seconds
   else: return

# Initialize global variables
numOfAcq = 0
linenr = 0
tsc = 0
# Call parser createDataDict() to create the data dictionary for the database to use in order to map the
# keys (e.g. 6, 7, 10, 1998, etc) to their actual values (e.g. 1STFLOOR:STAIRS, 1STFLOOR:TRASHROOM, etc).
Parser.createDataDict("SENSOR\\MBNMS.eso")

# Call main to simulate the entire mock data acquisition pipeline.
main()
