#!/usr/bin/python3

import json
import argparse

print("/"*50)
print("libc_detective")
print("/"*50)

parser = argparse.ArgumentParser(description="Process function and offset")
parser.add_argument('--function', type=str, required=True, help='Name of the function, for example read')
parser.add_argument('--offset', type=int, required=False, help='Memory offset of the function. Gdb example: read+18 where 18 is the offset')
parser.add_argument('--leak', type=str, required=True, help='Memory offset of the leaked address: The last 3 letters in the leaked libc address')

args = parser.parse_args()

global offset
if args.offset is None:
    print("Offset not set, assuming 0")
    offset = 0





