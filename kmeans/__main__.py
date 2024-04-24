import argparse
from mpi4py import MPI
import os, sys

from io_data import find_indexes, read_data, write_labels, write_centroids
from par_kmeans import kmeans

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
    labels_filename = f"{os.path.dirname(filename)}/Labels_{os.path.basename(filename)}"
    centroids_filename = f"{os.path.dirname(filename)}/Centroids_{os.path.basename(filename)}"

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    indexes = None
    # le process maître est le seul a décider du découpage des données d'entrée
    if rank==0:
        indexes = find_indexes(filename, size)
    
    # les informations de découpage pour la lecture concurrente sont ensuite broadcastées
    indexes = comm.bcast(indexes, root=0)

    points = read_data(filename, dim, *indexes[rank])
    labels, centroids = kmeans(points, K)

    # le process maître va retirer les fichiers de sortie si jamais il y avait
    # une version précédente, il va également écrire le fichier des centroïdes
    if rank==0 :
        if os.path.isfile(labels_filename):
            os.remove(labels_filename)

        if os.path.isfile(centroids_filename):
            os.remove(centroids_filename)
        
        write_centroids(centroids_filename, centroids)
        
    # de manière synchrone, tous les process écrivent dans le fichier
    # de sortie par ordre de rank croissant
    for i in range(size):
        if rank==i:
            write_labels(labels_filename, labels)
        comm.Barrier()
