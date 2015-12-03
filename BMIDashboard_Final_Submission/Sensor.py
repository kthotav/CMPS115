
# Opens a file, reads it's contents, and returns it as a single string variable.
# called "data".
def openFile(filepath):
    f = open(filepath, "r")
    data = f.read()
    return data

# Mocks the simulation of live data. It takes in a timestamp counter and a line number so it knows where to
# continue within the file that it is attempting to simulate live data for.
def mock(tsc, linenr):
    # sensor_file:      The file that contains all of the data for a single data. The program will be looking
    #                   at the file in chunks that are separated by timestamp in order to simulate "live" data.
    #                   Located in the directory "SENSOR" as the file "MBNMS.eso".
    #
    # raw_file:         The file that will contain all of the raw data for the parser to use. Located in the
    #                   directory "RAW_ESO" as the file also named "MBNMS.eso". The parser will never see the
    #                   other "MBNMS.eso file that the sensor is reading from. Do not mistake them from being 
    #                   the same file.
    sensor_file = openFile("SENSOR/MBNMS_Monday.eso").splitlines()
    raw_file = open("RAW_ESO/MBNMS.eso", "w+")
    
    # Starts at the current line number until the end of the sensor_file.
    print("Starting with line %d" % linenr)
    for data in range(linenr, len(sensor_file)):
        # For every line in the sensor_file, the program checks if it's key starts with "2,".
        d = sensor_file[data]
        if d.startswith("2,", 0, 2):
            # It must be a timestamp so we check if it is the first timestamp, which is
            # "2,6,Day of Simulation[],Month[],Day of Month[],DST Indicator[1=yes 0=no],Hour[],StartMinute[],
            # EndMinute[],DayType"
            #
            # If it is, we increment the timestamp counter (tsc) and let it continue with the simulation.
            # However, if it isn't then we increment the line number (linenr) along with the tsc to record what
            # line we are on for later.
            if tsc == 0:
                tsc += 1
            else:
                linenr += 1
                tsc += 1
                raw_file.write(d + "\n")
                break
        # These lines are written to the raw_file as "raw" data for the parser to read.
        raw_file.write(d + "\n")
        linenr += 1
        # Check if line number has reached the end of the sensor file.
        if linenr >= len(sensor_file):
            linenr = -1
            break
    print("Ending with line %d\n" % linenr)
    tup = [0, 0]
    tup[0] = linenr
    tup[1] = tsc
    return tup
