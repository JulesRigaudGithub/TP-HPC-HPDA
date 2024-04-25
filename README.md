# TP - HPC&HPDA

## TP5 MPI K-MEANS

Pour lancer le benchmark :
```bash
bash ./scripts/Launch-Batch
```

qui va générer 8 jobs dans la file d'attente, chacun étant constitué de trois executions du kmeans sur des datasets différents.

Pour concaténer les résultats :
```bash
bash ./scripts/Assemble-batches
```

Enfin, il suffit de tracer les courbes avec python :
```bash
python3 plot.py
```

