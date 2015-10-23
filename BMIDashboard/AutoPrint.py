import threading
import sys
import os

def main():
   global x
   if (x == 6):
      print("Program Exited\n")
      sys.exit()
   with open("test.txt", "a") as myfile:
      myfile.write("appended text\n")
   threading.Timer(1.5, main).start()
   print("Ran program " + str(x) + " Times\n") 
   x += 1 

x = 1
os.system('AutoHello.py')
main()

