import argparse
import os, sys

def cmdLineParsing():
    parser = argparse.ArgumentParser(prog="kmeans",
                                    description="Compute K-Means on the DCE cluster",
                                    epilog="Looking for any help ? Please contact G. Desjonqueres")

    parser.add_argument("filename",
                        help="input meta data file")
    
    args = parser.parse_args()

    if not os.path.isfile(args.filename):
        sys.exit("Error: input meta data file '" + args.filename + "' is unreachable!")

    return args.filename

def readData(filename):
    with open(filename, 'r') as f:
        metadata = [line.split(' ')[0] for line in f.readlines()]

    d = dict()
    d["data"] = metadata[0]
    d["N"] = int(metadata[1])
    d["K"] = int(metadata[2])
    return d




if __name__ == "__main__":
    print(readData(cmdLineParsing()))