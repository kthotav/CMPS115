# File: dashbpard.py
# Simple GUI for the dashboard maintainer

import Tkinter, connection, tkMessageBox

mainTop = Tkinter.Tk()

def checkConnection():
   result = connection.establishConnection()
   tkMessageBox.showinfo(result)

checkButton = Tkinter.Button(mainTop, text ="Test MySQL Connection", command = checkConnection)
quitButton = Tkinter.Button(mainTop, text='Quit', command=mainTop.quit)
checkButton.pack()
quitButton.pack()

mainTop.mainloop()
