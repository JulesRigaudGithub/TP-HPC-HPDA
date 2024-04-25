import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("benchmark.csv", dtype={'NODES' : int,
                                         'DATASET' : str,
                                         'ITER' : int})

# Obtenir la liste des datasets uniques
datasets = df['DATASET'].unique()

# Parcourir chaque dataset
for dataset in datasets:
    # Filtrer les données pour le dataset actuel
    dataset_data = df[df['DATASET'] == dataset]

    # Créer une nouvelle figure
    plt.figure()

    # Parcourir chaque temps et tracer la courbe correspondante
    temps_cols = ['T_READ', 'T_EXEC']
    for temps_col in temps_cols:
        plt.plot(dataset_data['NODES'], dataset_data[temps_col], label=temps_col)

    # Ajouter des étiquettes et une légende au graphique
    plt.xlabel('Nombre de nodes')
    plt.ylabel('Temps')
    plt.title(f"Temps d'exécution pour le dataset {dataset}")
    plt.legend()

    # Enregistrer le graphique au format PNG
    plt.savefig(f'temps_{dataset}.png')

    # Afficher le graphique
    plt.show()
