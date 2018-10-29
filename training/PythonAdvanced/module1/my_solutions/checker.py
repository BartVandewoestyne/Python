import argparse, os

parser = argparse.ArgumentParser()

# What you give as inputfile, will be given to the open function.
parser.add_argument('inputfile', type=open, help='The file to be checked')

args = parser.parse_args()

errorfound = 0

# enumerate() gebruiken om linenumber als nummer te hebben
for linenumber, line in enumerate(args.inputfile):
    line = line.rstrip(os.linesep) # get rid of the endline
    for colnumber, number in enumerate(line.split(',')):
        if not number.isdigit():
            errorfound += 1
            print('Not a number: line {}, col{}: {}'.format(lineunumber, colnumber, number))

if not errorfound:
    print('File is clean!')
else:
    print('Amount of non-numbers found = {errorfound}'.format(errorfound=errorfound))
