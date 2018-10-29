# My solution for exercise 2.1



import argparse
import os


def read_file(filename):
    theset = set()
    for line in filename:
        theset.add(line)
    return theset


parser = argparse.ArgumentParser()

# What you give as inputfile, will be given to the open function.
parser.add_argument('input1', type=open, help='Input file 1')
parser.add_argument('input2', type=open, help='Input file 2')
parser.add_argument('output', help='Output file')

args = parser.parse_args()

input1 = read_file(args.input1)
input2 = read_file(args.input2)

unique_set = input1 | input2

outputfile = open(args.output, 'w')
for item in unique_set:
    outputfile.write(item)
outputfile.close()
