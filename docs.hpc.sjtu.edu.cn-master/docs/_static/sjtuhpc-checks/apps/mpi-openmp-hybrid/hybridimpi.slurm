#!/bin/bash

#SBATCH --job-name=HybridMPI
#SBATCH --partition=cpu
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#SBATCH --ntasks-per-node=1
#SBATCH --exclusive
#SBATCH --time=00:01:00 

ulimit -s unlimited
ulimit -l unlimited

source /usr/share/Modules/init/bash
module purge; module load intel-parallel-studio/cluster.2019.4-gcc-4.8.5 

export I_MPI_DEBUG=5
export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi.so
export I_MPI_FABRICS=shm:ofi

export OMP_NUM_THREADS=40
srun ./hybridmpi
