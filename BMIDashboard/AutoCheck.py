import threading
import sys
import os

def main():
   global x
   if (x == 6):
      sys.exit()
      print("Program Exited\n")
   os.system('Parser.py')
   threading.Timer(1.5, main).start()
   print("Ran program " + str(x) + " Times\n") 
   x += 1 

x = 1 
main()
