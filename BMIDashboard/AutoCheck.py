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
   sensor
   Parser
   x += 1
   threading.Timer(5, main).start()
   print("Ran program " + str(x) + " Times\n")

x = 1
linenr = 0
tsc = 0
main()
