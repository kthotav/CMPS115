import threading
import os
from AutoCheck import linenr
from AutoCheck import tsc

def openFile(filepath):
    f = open(filepath, "r")
    data = f.read()
    return data

def mock():
    sensor_file = openFile("SENSOR_FILE\MBNMS CMPS115_FULL.eso").splitlines()
    raw_file = open("RAW_ESO_FILES\MBNMS CMPS115_FULL.eso", "w+")
    
    print("Starting with line %d" % linenr)
    for data in range(linenr, len(sensor_file)):
        d = sensor_file[data]
        if d.startswith("2,", 0, 2):
            if tsc == 0:
                tsc += 1
            else:
                linenr += 1
                tsc += 1
                raw_file.write(d + "\n")
                break
        raw_file.write(d + "\n")
        linenr += 1
    print("Ending with line %d\n" % linenr)

mock()
