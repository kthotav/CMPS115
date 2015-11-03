import threading
import sys
import os
import time
import subprocess
import sensor
import Parser

def main():
   global x
   global linenr
   global tsc
   tup = []
   tup = sensor.mock(tsc, linenr)
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

start_time = time.time()
main()
end_time = time.time()

print("Program Start Time: %s" % start_time)
print("PRogram End Time: %s" % end_time)
print("Program Runtime: --- %.4f seconds ---" % (end_time - start_time))
