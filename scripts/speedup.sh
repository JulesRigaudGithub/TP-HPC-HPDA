#!/bin/bash

# Nom du fichier CSV de sortie
output_file="./scripts/speedup.csv"

# Supprimer le fichier CSV s'il existe déjà
> $output_file

# Boucle sur les valeurs de X de 1 à 16
for X in {1..8}; do
    # Calculer la valeur de Y en fonction de X
    Y=$((16 * X))

    # Charger le module py-mpi4py avec la version spécifiée
    module load py-mpi4py/3.1.4/gcc-12.3.0-openmpi

    # Soumettre le travail Slurm avec les paramètres spécifiés et rediriger la sortie vers un fichier temporaire
    #sbatch_output=$(sbatch -N $X -n $Y --exclusive -p cpu_tp --qos=8nodespu )
    mpirun -np $Y -map-by ppr:16:node:PE=16 -rank-by core python3 kmeans ../Data/META_DATA_S1.txt >> $output_file

done
