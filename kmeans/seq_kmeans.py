import argparse
import os, sys
import numpy as np

def cmdLineParsing():
  parser = argparse.ArgumentParser()
  parser.add_argument("--f", help="input meta data file")

  args = parser.parse_args()

  if not os.path.isfile(args.f):
    sys.exit("Error: input meta data file '" + args.f + "' is unreachable!")

  return args.f, args.c

def readData():
   pass
  

def main():
    print("running")
    return None

