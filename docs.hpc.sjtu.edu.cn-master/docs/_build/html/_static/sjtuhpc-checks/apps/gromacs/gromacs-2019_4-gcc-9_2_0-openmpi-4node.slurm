#!/bin/bash

#SBATCH -J gromacs-2019_4-gcc-9_2_0-openmpi-1node
#SBATCH -p cpu
#SBATCH -n 160
#SBATCH --ntasks-per-node=40
#SBATCH -o %j.out
#SBATCH -e %j.err

module load gromacs/2019.4-gcc-9.2.0-openmpi

ulimit -s unlimited
ulimit -l unlimited

srun --mpi=pmi2 gmx_mpi mdrun -s ./ion_channel.tpr -maxh 0.50 -resethway -noconfout -nsteps 10000
