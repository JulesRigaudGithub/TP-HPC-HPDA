import numpy as np
from mpi4py import MPI

def kmeans(points, k, max_iterations, convergence_threshold, total_points):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    centroids = np.empty((k,2))
    if rank == 0: # Initialisation aléatoire des centroïdes
        centroids = points[np.random.choice(range(len(points)), k, replace=False)]
    
    comm.Bcast(centroids, root=0)

    previous_labels = None

    for iteration in range(max_iterations):
        # Attribution des points aux clusters les plus proches
        distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        
        # Mise à jour des centroïdes locaux
        local_sum_points = np.array([np.sum(points[labels == i], axis=0) for i in range(k)])
        nombre_points = np.array([len(points[labels == i]) for i in range(k)])

        global_nombre_points = np.zeros_like(nombre_points)
        global_sum_points = np.zeros_like(local_sum_points)
        comm.Allreduce(local_sum_points, global_sum_points, op=MPI.SUM)
        comm.Allreduce(nombre_points, global_nombre_points, op=MPI.SUM)

        centroids = [global_sum_points[i]/global_nombre_points[i] for i in range(k)]

        #clause de convergence
        if previous_labels is not None:
            num_changed = np.sum(labels != previous_labels)
            num_changed_global = comm.allreduce(num_changed, op=MPI.SUM)
            if num_changed_global / total_points < convergence_threshold:
                break
        
        previous_labels = np.copy(labels)
        
    return labels, centroids


# np.random.seed(0)
# points = np.random.rand(20, 2)


