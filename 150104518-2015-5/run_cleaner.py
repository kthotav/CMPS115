import glob

def clean_csv(file):

    infile = open(file, 'r')
    outfile = open("clean_"+file, 'w')

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

for file in glob.glob("*.csv"):
    if "clean" not in file:
        clean_csv(file)
