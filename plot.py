import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("benchmark.csv", dtype={'NODES' : int,
                                         'DATASET' : str,
                                         'ITER' : int})

# Pour chaque dataset, tracer les courbes
nb_HKpoints = 1
for dataset, data in df.groupby('DATASET'):
    plt.figure()  # Crée une nouvelle figure pour chaque dataset
    plt.title(f"HKPPS pour le dataset {dataset}")

    # Pour chaque temps, tracer la courbe correspondante
    for temps in ['T_READ', 'T_EXEC']:
        # Calculer la moyenne des temps pour chaque nombre de nodes
        moyennes = data.groupby('NODES')[temps].mean()
        plt.plot(moyennes.index, nb_HKpoints / moyennes.values, label=temps)

    plt.xlabel('Nombre de nodes')
    plt.ylabel('HKPPS sur 5 prises (10000 pts/s)')
    plt.legend()  # Afficher la légende
    plt.grid(True)  # Activer la grille
    plt.savefig(f'hkpps_{dataset}.png')  # Enregistrer le graphe au format PNG
    plt.close()  # Fermer la figure pour libérer la mémoire (facultatif)
    nb_HKpoints *= 10

nb_HKpoints = 1
for dataset, data in df.groupby('DATASET'):
    plt.figure()  # Crée une nouvelle figure pour chaque dataset
    plt.title(f"HKPPS pour le dataset {dataset}")

    moyennes = data.groupby('NODES')["T_WRITE"].mean()
    plt.plot(moyennes.index, nb_HKpoints / moyennes.values, label=temps)

    plt.xlabel('Nombre de nodes')
    plt.ylabel('HKPPS sur 5 prises (10000 pts/s)')
    plt.legend()  # Afficher la légende
    plt.grid(True)  # Activer la grille
    plt.savefig(f'hkpps_write_{dataset}.png')  # Enregistrer le graphe au format PNG
    plt.close()  # Fermer la figure pour libérer la mémoire (facultatif)
    nb_HKpoints *= 10