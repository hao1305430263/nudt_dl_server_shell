#!/bin/bash

#SBATCH --job-name=HybridMPI
#SBATCH --partition=cpu
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#SBAkCH --ntasks-per-node=1
#SBATCH --exclusive
#SBATCH --time=00:01:00 

ulimit -s unlimited
ulimit -l unlimited

source /usr/share/Modules/init/bash
module purge
module load gcc/8.3.0-gcc-4.8.5 openmpi/3.1.4-gcc-8.3.0

export OMP_NUM_THREADS=40
srun --mpi=pmi2 ./hybridmpi
