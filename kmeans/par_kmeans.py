import numpy as np
from mpi4py import MPI

def kmeans(points, k, max_iterations=1, convergence_threshold=0.05):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0: # Initialisation aléatoire des centroïdes
        centroids = points[np.random.choice(range(len(points)), k, replace=False)]

    previous_labels = None

    for iteration in range(max_iterations):
        # Attribution des points aux clusters les plus proches
        distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        
        # Mise à jour des centroïdes
        centroids = np.array([points[labels == i].mean(axis=0) for i in range(k)])

        #clause de convergence
        if previous_labels is not None:
            num_changed = np.sum(labels != previous_labels)
            if num_changed / len(points) < convergence_threshold:
                print(f"CLAUSE SEUIL!!! à {iteration}")
                break
        
        previous_labels = np.copy(labels)
          
    return labels, centroids