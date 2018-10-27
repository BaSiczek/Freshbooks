import csv
import sys, getopt

def reverse_name(name):
    name = name.split(', ')
    name = name[-1::-1]
    return ' '.join(name)

def main(argv):
    input_file = argv[0]
    report = {}
    with open(input_file) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            if row[0] in report.keys():
                report[row[0]] = float(report[row[0]]) + float(row[6])
            else:
                report[row[0]] = row[6]
        for key in report:
            name = reverse_name(key)
            print(name, "   :   ", report[key])



if __name__ == "__main__":
   main(sys.argv[1:])
