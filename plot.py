import pandas as pd

df = pd.read_csv("benchmark.csv", dtype={'NODES' : int,
                                         'DATASET' : str})

print(df)
