import os, sys
import io
import numpy as np

def find_indexes(filename, nb_process):
    try :
        filestats = os.stat(filename)
        SIZE = filestats.st_size
        if nb_process > 1:
            SUB_SIZE = SIZE // nb_process
        else:
            SUB_SIZE = SIZE
        
        lst = []
        prev_index = 0
        with open(filename, 'rb') as f:
            for p in range(1, nb_process):
                f.seek(p*SUB_SIZE)
                while f.read(1) != b'\n':
                    continue
                index = f.tell()
                lst.append((prev_index, index))
                prev_index = index

            index = f.seek(0, io.SEEK_END)
            lst.append((prev_index, index))
        return lst

    except FileNotFoundError as e:
        print(f"Initialization error : {e}")

def read_data(filename, dim, start_index, next_index):
    try :
        lst = []
        with open(filename, 'rb') as f:
            f.seek(start_index)
            buf = f.read(next_index - start_index)
            for line in buf.split(b'\r\n'):
                line_decoded = line.decode('utf8').split('\t')

                if len(line_decoded) == dim :
                    lst.append(np.array(list(map(float, line_decoded))))

        return np.array(lst)
           
    except FileNotFoundError as e:
        print(f"Initialization error : {e}")
    except ValueError as e:
        print(f"Initialization error : {e}")

def write_labels(filename, buffer):
    try :
        with open(filename, 'a') as f:
            for cluster_assignment in buffer :
                f.write(f"{cluster_assignment}\n")
       
    except FileNotFoundError as e:
        print(f"Write error : {e}")

def write_centroids(filename, buffer):
    try :
        with open(filename, 'a') as f:
            for centroid in buffer :
                f.write(f"{centroid[0]} {centroid[1]}\n")
       
    except FileNotFoundError as e:
        print(f"Write error : {e}")