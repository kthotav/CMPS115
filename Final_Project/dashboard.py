# File: dashbpard.py
# Simple GUI for the dashboard maintainer

import Tkinter, connection, tkMessageBox, createDBtable


mainTop = Tkinter.Tk()

def checkConnection():
    result = connection.establishConnection()
    tkMessageBox.showinfo(result)

def createTable():
    connection.establishConnection()
    result = createDBtable.createDBTable()
    tkMessageBox.showinfo(result)

checkButton = Tkinter.Button(mainTop, text ="Test MySQL Connection", command = checkConnection)
createButton = Tkinter.Button(mainTop, text="Create Table pv", command=createTable)

quitButton = Tkinter.Button(mainTop, text='Quit', command=mainTop.quit)

checkButton.pack()
createButton.pack()
quitButton.pack()

mainTop.mainloop()
