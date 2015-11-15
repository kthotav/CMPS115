import glob
import os

# Opens a file, reads it's contents, and returns it as a single string variable.
# called "data".
def openFile(filepath):
    f = open(filepath, "r")
    data = f.read()
    return data

# Cleans the specified file located at filepath. For ESO files.
# data:         Each line of the file located at file path.
# dname:        The entire directory path of the file, exluding the actual file name.
# bname:        The basename of the directory path, which is the file name.
# newbasepath:  The new basename that we will be putting the clean files into.
# clean_file:   The file name of the clean file.
def cleanESOFile(filepath):
    data = openFile(filepath).splitlines()
    dname = "CLEAN_ESO\\"
    bname = os.path.basename(filepath)
    newbasepath = bname[:len(bname)-4] + "_FULL.csv"
    clean_file = open(dname + newbasepath, "w+") # w+ is write and read only
    for d in data:
        clean_file.write(d + "\n")

# Cleans the specified file located at filepath. For PV files.
# data:         Each line of the file located at file path.
# keys:         The key attributes for the PV files.
# values:       The data values for each of the key attributes.
# dname:        The entire directory path of the file, exluding the actual file name.
# bname:        The basename of the directory path, which is the file name.
# clean_file:   The file name of the clean file.
def cleanPVFile(filepath):
    data = openFile(filepath).replace(";", ",").splitlines()
    keys = data[4]
    values = data[6:]
    dname = "CLEAN_PV\\"
    bname = os.path.basename(filepath)
    clean_file = open(dname + bname, "w+")
    clean_file.write(keys + "\n")
    for v in values:
        clean_file.write(v + "\n")

# Parses just the ESO file keys within the data dictionary as well as the data values correlated with each key.
# Also it converts the ESO files into CSV files.
# data:         Each line of the file located at file path.
# dname:        The entire directory path of the file, exluding the actual file name.
# bname:        The basename of the directory path, which is the file name.
# ts_filepath:  The file path for the timestamp file.
# ts_file:      The time stamp file. (Contains all of the timestamp values and only those values).
# timestamps:   Reopens the time stamp file so that it can be read as a reference to indicate the latest time stamp.
# attributes:   The attributes for each data value.
# key:          The key that for each line in the data dictionary/
def parseESOKeys(filepath, tsc):
    data = openFile(filepath).splitlines()
    dname = "CLEAN_ESO\\"
    bname = os.path.basename(filepath)
    
    # Time Stamp File
    ts_filepath = "2" + bname[:len(bname)-4] + ".csv"
    ts_file = open(dname + ts_filepath, "a")
    
    # Inserts all of the time stamps into a file for reference so that it can be appeneded to the data values for
    # each attribute.
    for d in data:
        if d.startswith("2,", 0, 2):
            ts_file.write(d + "\n")
    # Close time stamp file and reopen it as read only.
    ts_file.close()
    timestamps = openFile(dname + ts_filepath).splitlines()

    # Iterate through all of the attributes within the data dictionary and create files for them if they have not
    # already been created (d1).
    for d1 in data:
        if d1 == "End of Data Dictionary":
            break
        attributes = d1.split(",")
        key = attributes[0]
        t = key + "_" + bname[:len(bname)-4] + ".csv" # Create a filename for this specific key.
        temp_file = open(dname + t, "a") # Create a file using the t variable.

        # Re-iterate through the entire file to append each of the current time stamp's data values into their
        # respective keys.
        for d2 in data:
            if d2.startswith(key + ",", 0, len(key)+1) and not d2.startswith("2,", 0, 2):
                temp_file.write(timestamps[tsc] + "," + d2 + "\n")

# Creates a data dictionary that maps each of the numerical keys to their string locations.
def createDataDict(filepath):
    data = openFile(filepath).splitlines()
    dname = "CLEAN_ESO\\"
    bname = "Data_Dictionary.csv"
    dict_file = open(dname + bname, "w")
    x = 0
    for d in data:
        if d == "End of Data Dictionary":
            break
        attributes = d.split(",")
        if len(attributes) >= 4 and x >= 6:
            val = attributes[0] + "," + attributes[2] + "," + attributes[3] + "\n"
            dict_file.write(val)
        x += 1
    dict_file.close()
    print("Dictionary has been created in directory CLEAN_ESO as 'Data_Dictionary.csv'\n")

# Runs the parsing functions above depending on what type of file it is (PV or ESO).
def parse(tsc):
    """
    print("Cleaning Raw PV Files")
    for filepath in glob.glob("RAW_PV\*.csv"):
        print(filepath)
        if "CLEAN" not in filepath: cleanPVFile(filepath)
    print("PV Files Cleaned\n")
    """

    # Iterates through all of the files in the RAW_ESO directory and calles cleanESOFile() and parseESOKeys().
    print("Cleaning Raw ESO Files")
    for filepath in glob.glob("RAW_ESO\*.eso"):
        print(filepath)
        if "CLEAN" not in filepath:
            cleanESOFile(filepath)
            parseESOKeys(filepath, tsc)
    print("ESO Files Cleaned\n")
