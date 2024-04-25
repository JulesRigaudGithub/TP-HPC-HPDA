import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("benchmark.csv", dtype={'NODES' : int,
                                         'DATASET' : str})

# Pour chaque dataset, tracer les courbes
for dataset, data in df.groupby('DATASET'):
    plt.figure()  # Crée une nouvelle figure pour chaque dataset
    plt.title(f"Temps d'exécution pour le dataset {dataset}")

    # Pour chaque temps, tracer la courbe correspondante
    for temps in ['T_READ', 'T_EXEC', 'T_WRITE']:
        # Calculer la moyenne des temps pour chaque nombre de nodes
        moyennes = group.groupby('NODES')[temps].mean()
        plt.plot(moyennes.index, moyennes.values, label=temps)

    plt.xlabel('Nombre de nodes')
    plt.ylabel('Temps moyen sur 5 prises (s)')
    plt.legend()  # Afficher la légende
    plt.grid(True)  # Activer la grille
    plt.savefig(f'time_{dataset}.png')  # Enregistrer le graphe au format PNG
    plt.close()  # Fermer la figure pour libérer la mémoire (facultatif)
