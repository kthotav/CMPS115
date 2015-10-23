import threading
import sys
import os

def main():
   global x
   """
   if (x == 6):
      print("Program Exited\n")
      sys.exit()
   """
   os.system('Parser.py')
   threading.Timer(30, main).start()
   print("Ran program " + str(x) + " Times\n") 
   x += 1 

x = 1 
main()
