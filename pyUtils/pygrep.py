# Python script for basic grep like functionality using regex

import sys
import re
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="file to search through")
parser.add_argument("regex", type=str, help="pattern to match")
parser.add_argument("--out", type=str, help="file to output to (optional, requires output path)")

args = parser.parse_args()

pattern = re.compile(args.regex)

with open(args.path, 'r') as file:
    lineNum = 1
    for line in file:
        if pattern.search(line):
            if args.out:
                with open(args.out, 'a') as out_file:
                    out_file.write(f"{lineNum}: {line.strip()}\n")
            else:
                print(f"{lineNum}: {line.strip()}")
        lineNum += 1 
