import threading
import sys
import os
import time
import Sensor
import Parser

def main():
   global x
   global linenr
   global tsc
   tup = []
   tup = Sensor.mock(tsc, linenr)
   if tsc == 2: tsc -= 1
   Parser.parse(tsc)
   x += 1
   linenr = tup[0]
   tsc = tup[1]
   print("Ran program " + str(x) + " Times\n")
   if not (linenr == -1): threading.Timer(1, main).start()
   else: return

x = 0
linenr = 0
tsc = 0
main()
