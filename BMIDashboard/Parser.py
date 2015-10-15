import glob
import os

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

def parseEsoKeys(filepath):
    data = openFile(filepath).splitlines()
    dname = "CLEAN_ESO_FILES\\"
    bname = os.path.basename(filepath)
    timesteps_base_path = dname + bname[:len(bname)-4] + "_TIMESTEPS.csv"
    hourly_base_path = dname + bname[:len(bname)-4] + "_HOURLY.csv"
    daily_base_path = dname + bname[:len(bname)-4] + "_DAILY.csv"
    timesteps_file = open(timesteps_base_path, "w+")
    hourly_file = open(hourly_base_path, "w+")
    daily_file = open(daily_base_path, "w+")
    for d in data:
        if "!TimeStep" in d: timesteps_file.write(d + "\n")
        elif "!Hourly" in d: hourly_file.write(d + "\n")
        elif "!Daily" in d: daily_file.write(d + "\n")

def main():
    print("Cleaning Raw PV Files")
    for filepath in glob.glob("RAW_PV_FILES\*.csv"):
        if "CLEAN" not in filepath: cleanPVFile(filepath)
    print("PV Files Cleaned\n")

    print("Cleaning Raw ESO Files")
    for filepath in glob.glob("RAW_ESO_FILES\*.eso"):
        if "CLEAN" not in filepath:
            cleanESOFile(filepath)
            parseEsoKeys(filepath)
    print("ESO Files Cleaned\n")

main()
