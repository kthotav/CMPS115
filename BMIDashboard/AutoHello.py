import threading
import sys
import os

def main():
   global x
   if (x == 2):
      print("Program Exited\n")
      sys.exit()
   with open("test_hello.txt", "a") as myfile:
      myfile.write("hello" + str(x) + "\n")
   threading.Timer(1.5, main).start()
   print("Ran hello " + str(x) + " Times\n") 
   x += 1 

x = 1 
main()
