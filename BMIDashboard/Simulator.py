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
   if tsc >= 2: tsc -= 1
   Parser.parse(tsc)
   x += 1
   linenr = tup[0]
   tsc = tup[1]
   print("DATA HAS BEEN ACQUIRED " + str(x) + " TIMES\n")
   if not (linenr == -1): threading.Timer(0, main).start()
   else: return

x = 0
linenr = 0
tsc = 0
main()
