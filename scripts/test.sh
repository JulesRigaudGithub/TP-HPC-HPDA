#!/bin/bash

mpirun -np 4 -map-by ppr:2:node:PE=4 -rank-by core python3 kmeans ../Data/META_DATA_S1.txt
