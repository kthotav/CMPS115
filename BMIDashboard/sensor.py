import threading
import os

def openFile(filepath):
    f = open(filepath, "r")
    data = f.read()
    return data

def main():
    global x
    global timestamp_counter
    
    sensor_file = openFile("SENSOR_FILE\MBNMS CMPS115_FULL.eso").splitlines()
    raw_file = open("RAW_ESO_FILES\MBNMS CMPS115_FULL.eso", "w+")
    
    print("Starting with line %d" % x)
    for data in range(x, len(sensor_file)):
        d = sensor_file[data]
        if d.startswith("2,", 0, 2):
            if timestamp_counter == 0:
                timestamp_counter += 1
            else:
                x += 1
                timestamp_counter += 1
                raw_file.write(d + "\n")
                break
        raw_file.write(d + "\n")
        x += 1
    print("Ending with line %d" % x)
    
    threading.Timer(30, main).start()
    
x = 0
timestamp_counter = 0
main()
