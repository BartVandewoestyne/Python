# My solution for exercise 2.1.1

import argparse
import os
import os.path


def read_file(filename):
    return set(line.strip() for line in open(filename))


parser = argparse.ArgumentParser()

parser.add_argument("input", help="File to add to set", nargs="+")
parser.add_argument('output', help='Output file')
args = parser.parse_args()

unique_set = set()
for setfile in args.input:
    if os.path.exists(setfile):
        read_set = read_file(setfile)
        unique_set = unique_set | read_set
    else:
        print setfile, "does not exist, so skipping it."

outfile = open(args.output, 'w')
for val in unique_set:
    outfile.write(val)
outfile.close()
