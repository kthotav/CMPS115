# File clean.py
# Cleans all the csv files in the pv_data folder

import glob, os, csv

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

def removeRows(csv_file):
    remove_from = 1
    remove_to = 12

    with open(csv_file, "r") as fp_in, open("final"+csv_file, "w+") as fp_out:
        fp_in.next()
        reader = csv.reader(fp_in)
        writer = csv.writer(fp_out)
        for row in reader:
            del row[remove_from:remove_to]
            del row[2]
            del row[2]
            del row[4]
            writer.writerow(row)


for csv_file in glob.glob("*.csv"):
    if "clean" not in csv_file:
        cleanCSVFile(csv_file)


for csv_file in glob.glob("*.csv"):
    if "clean" in csv_file:
        removeRows(csv_file)

for hgx in glob.glob("clean*.csv"):
    os.remove(hgx)
