#!/bin/bash

#SBATCH --job-name=Hello_OpenMP
#SBATCH --partition=small
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#SBATCH -n 8
#SBATCH --ntasks-per-node=8

ulimit -l unlimited
ulimit -s unlimited

source /usr/share/Modules/init/bash
module purge
module load gcc

export OMP_NUM_THREADS=8
./omphello
