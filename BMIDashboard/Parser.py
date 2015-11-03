import glob
import os
import time
from AutoCheck import tsc

def openFile(filepath):
    f = open(filepath, "r")
    data = f.read()
    return data

def cleanESOFile(filepath):
    data = openFile(filepath).splitlines()
    dname = "CLEAN_ESO_FILES\\"
    bname = os.path.basename(filepath)
    newbasepath = bname[:len(bname)-4] + "_FULL.csv"
    clean_file = open(dname + newbasepath, "w+")
    for d in data: clean_file.write(d + "\n")

def cleanPVFile(filepath):
    data = openFile(filepath).replace(";", ",").splitlines()
    keys = data[4]
    values = data[6:]
    dname = "CLEAN_PV_FILES\\"
    bname = os.path.basename(filepath)
    clean_file = open(dname + bname, "w+")
    clean_file.write(keys + "\n")
    for v in values: clean_file.write(v + "\n")

def parseESOKeys(filepath):
    data = openFile(filepath).splitlines()
    dname = "CLEAN_ESO_FILES\\"
    bname = os.path.basename(filepath)
    
    ts_filepath = bname[:len(bname)-4] + "_KEY2" + ".csv"
    ts_file = open(dname + ts_filepath, "a")
    for d in data:
        if d.startswith("2,", 0, 2): ts_file.write(d + "\n")
    ts_file.close()
    timestamps = openFile(dname + ts_filepath).splitlines()
    
    for d1 in data:
        if d1 == "End of Data Dictionary": break
        key = ""
        for char in d1:
            if char == ',': break
            else: key += char
        t = bname[:len(bname)-4] + "_KEY" + key + ".csv"
        temp_file = open(dname + t, "a")
        for d2 in data:
            if d2.startswith(key + ",", 0, len(key)+1) and not d2.startswith("2,", 0, 2):
                temp_file.write(timestamps[tsc] + "," + d2 + "\n")
        tsi += 1

def main():
    print("Cleaning Raw PV Files")
    for filepath in glob.glob("RAW_PV_FILES\*.csv"):
        print(filepath)
        if "CLEAN" not in filepath: cleanPVFile(filepath)
    print("PV Files Cleaned\n")
    
    print("Cleaning Raw ESO Files")
    for filepath in glob.glob("RAW_ESO_FILES\*.eso"):
        print(filepath)
        if "CLEAN" not in filepath:
            cleanESOFile(filepath)
            parseESOKeys(filepath)
    print("ESO Files Cleaned\n")

start_time = time.time()
main()
end_time = time.time()
print("Program Start Time: %s" % start_time)
print("PRogram End Time: %s" % end_time)
print("Program Runtime: --- %.4f seconds ---" % (end_time - start_time))
