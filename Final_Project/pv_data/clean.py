# File clean.py
# Cleans all the csv files in the pv_data folder

import glob


def cleanCSVFile(csv_file):
    infile = open(csv_file, 'r')
    outfile = open("clean_"+csv_file, 'w')

    data = infile.read().replace(";", ",")
    list_newdata = data.splitlines()


    keys = list_newdata[4]
    outfile.write(keys)
    outfile.write('\n')

    values = list_newdata[6:]
    for value in values:
        outfile.write(value)
        outfile.write('\n')

    infile.close()
    outfile.close()


for csv_file in glob.glob("*.csv"):
    if "clean" not in csv_file:
        cleanCSVFile(csv_file)
