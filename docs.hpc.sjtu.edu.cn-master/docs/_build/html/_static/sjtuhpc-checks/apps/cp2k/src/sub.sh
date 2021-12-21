#!/bin/bash

#SBATCH -J py_gwc_10s
#SBATCH --partition=cpu
#SBATCH -N 1
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#SBATCH --exclusive

module load cp2k/7.1-gcc-9.2.0-openblas-openmpi

cp2k.psmp -i argon.inp -o argon.out 

