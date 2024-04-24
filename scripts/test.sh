#!/bin/bash

mpirun -np 2 -map-by ppr:2:node:PE=4 -rank-by core python3 kmeans ../Data/META_DATA_S1.txt
