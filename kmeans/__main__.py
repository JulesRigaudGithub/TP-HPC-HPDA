import argparse
import os, sys

from io_data import find_indexes, read_data

def cmd_line_parsing():
    parser = argparse.ArgumentParser(prog="kmeans",
                                    description="Compute K-Means on the DCE cluster",
                                    epilog="Looking for any help ? Please contact G. Desjonqueres")

    parser.add_argument("filename",
                        help="input meta data file")
    
    args = parser.parse_args()

    if not os.path.isfile(args.filename):
        sys.exit("Error: input meta data file '" + args.filename + "' is unreachable!")

    return args.filename

def read_metadata(filename):
    with open(filename, 'r') as f:
        metadata = [line.split(' ')[0].strip('\n') for line in f.readlines()]

    dirname = os.path.dirname(filename)
  
    return f"{dirname}/{metadata[0]}",  int(metadata[1]), int(metadata[2])




if __name__ == "__main__":
    filename_meta = cmd_line_parsing()
    filename, N, K = read_metadata(filename_meta)
    dim = 2
    print(filename, N, K)

    indexes = find_indexes(filename, 20)
    print(len(indexes))

    array = read_data(filename, dim, *indexes[19])

    print(array)
