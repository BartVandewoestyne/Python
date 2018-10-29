# My solution for exercise 2.1.2

import argparse
import os
import os.path


def read_file(filename):
    return set(line.strip() for line in open(filename))


parser = argparse.ArgumentParser()

parser.add_argument('input', help="File to add to set", nargs="+")
parser.add_argument('output', help='Output file')
parser.add_argument('operation')
args = parser.parse_args()

resulting_set = set()
for setfile in args.input:
    if os.path.exists(setfile):
        read_set = read_file(setfile)
        if args.operation == 'unique':
            resulting_set.unique(read_set)
        elif args.operation == 'intersection':
            resulting_set.intersection(read_set)
        elif args.operation == 'difference':
            resulting_set.difference(read_set)
        else:
            print "unsupported operation"
    else:
        print setfile, "does not exist, so skipping it."

outfile = open(args.output, 'w')
for val in unique_set:
    outfile.write(val)
outfile.close()
